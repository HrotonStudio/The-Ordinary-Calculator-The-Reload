#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <immintrin.h>
#include <stdlib.h>
#include <string.h>

// 多精度整数结构
typedef struct {
    uint64_t* data;
    size_t size;
    size_t capacity;
} BigInt;

BigInt bigint_create() {
    BigInt num;
    num.capacity = 4;
    num.data = (uint64_t*)_mm_malloc(num.capacity * sizeof(uint64_t), 64);
    memset(num.data, 0, num.capacity * sizeof(uint64_t));
    num.size = 1;
    return num;
}

void bigint_expand(BigInt* num, size_t new_capacity) {
    if (new_capacity > num->capacity) {
        uint64_t* new_data = (uint64_t*)_mm_malloc(new_capacity * sizeof(uint64_t), 64);
        memcpy(new_data, num->data, num->size * sizeof(uint64_t));
        memset(new_data + num->size, 0, (new_capacity - num->size) * sizeof(uint64_t));
        _mm_free(num->data);
        num->data = new_data;
        num->capacity = new_capacity;
    }
}

// 修正后的AVX2指令
void avx2_multiply(const uint64_t* a, const uint64_t* b, uint64_t* result) {
    __m256i va = _mm256_load_si256((__m256i const*)a);
    __m256i vb = _mm256_load_si256((__m256i const*)b);
    __m256i product = _mm256_mul_epu32(va, vb);
    _mm256_store_si256((__m256i*)result, product);
}

void process_carries(BigInt* num) {
    uint64_t carry = 0;
    for (size_t i = 0; i < num->size; ++i) {
        uint64_t val = num->data[i] + carry;
        num->data[i] = val & 0xFFFFFFFFFFFFFFFFULL;
        carry = val >> 63; // 修正位移量
    }
    if (carry > 0) {
        bigint_expand(num, num->size + 1);
        num->data[num->size] = carry;
        num->size++;
    }
}

// 修正后的Python接口
static PyObject* py_power(PyObject* self, PyObject* args) {
    unsigned long base, exp;
    if (!PyArg_ParseTuple(args, "kk", &base, &exp)) {
        PyErr_SetString(PyExc_TypeError, "Requires two unsigned integers");
        return NULL;
    }

    BigInt result = fast_power(base, exp);
    PyObject* py_result = PyLong_FromUnsignedLongLong(result.data[0]);
    for (size_t i = 1; i < result.size; ++i) {
        PyObject* chunk = PyLong_FromUnsignedLongLong(result.data[i]);
        PyObject* shifted = PyNumber_Lshift(chunk, PyLong_FromLong(64 * i));
        PyObject* temp = PyNumber_Add(py_result, shifted);
        Py_DECREF(py_result);
        Py_DECREF(shifted);
        py_result = temp;
    }
    _mm_free(result.data);
    return py_result;
}