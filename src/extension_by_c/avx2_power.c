#include <Python.h>
#include <numpy/arrayobject.h>
#include <immintrin.h>

static PyObject *avx2_power(PyObject *self, PyObject *args) {
    PyArrayObject *base_array;
    PyObject *exponent_obj;
    int is_scalar = 0;
    double scalar_exponent;
    
    // 解析输入参数
    if (!PyArg_ParseTuple(args, "O!O", &PyArray_Type, &base_array, &exponent_obj)) {
        return NULL;
    }

    // 检查base数组类型和维度
    if (PyArray_NDIM(base_array) != 1 || PyArray_TYPE(base_array) != NPY_DOUBLE) {
        PyErr_SetString(PyExc_ValueError, "Base must be 1D double array");
        return NULL;
    }

    npy_intp size = PyArray_SIZE(base_array);
    double *base = (double *)PyArray_DATA(base_array);
    double *exponent = NULL;
    PyArrayObject *exponent_array = NULL;

    // 判断指数类型（标量或数组）
    if (PyArray_Check(exponent_obj)) {
        exponent_array = (PyArrayObject *)exponent_obj;
        if (PyArray_NDIM(exponent_array) != 1 || PyArray_TYPE(exponent_array) != NPY_DOUBLE) {
            PyErr_SetString(PyExc_ValueError, "Exponent must be 1D double array");
            return NULL;
        }
        if (PyArray_SIZE(exponent_array) != size) {
            PyErr_SetString(PyExc_ValueError, "Array size mismatch");
            return NULL;
        }
        exponent = (double *)PyArray_DATA(exponent_array);
    } else if (PyNumber_Check(exponent_obj)) {
        scalar_exponent = PyFloat_AsDouble(exponent_obj);
        if (PyErr_Occurred()) return NULL;
        is_scalar = 1;
    } else {
        PyErr_SetString(PyExc_TypeError, "Exponent must be array or scalar");
        return NULL;
    }

    // 创建输出数组
    PyArrayObject *result_array = (PyArrayObject *)PyArray_NewLikeArray(base_array, NPY_KEEPORDER, NULL, 0);
    if (!result_array) return NULL;
    double *result = (double *)PyArray_DATA(result_array);

    // AVX2向量化处理
    int i;
    if (is_scalar) {
        __m256d exp_vec = _mm256_set1_pd(scalar_exponent);
        for (i = 0; i < size - 3; i += 4) {
            __m256d base_vec = _mm256_loadu_pd(&base[i]);
            __m256d res_vec = _mm256_pow_pd(base_vec, exp_vec);
            _mm256_storeu_pd(&result[i], res_vec);
        }
    } else {
        for (i = 0; i < size - 3; i += 4) {
            __m256d base_vec = _mm256_loadu_pd(&base[i]);
            __m256d exp_vec = _mm256_loadu_pd(&exponent[i]);
            __m256d res_vec = _mm256_pow_pd(base_vec, exp_vec);
            _mm256_storeu_pd(&result[i], res_vec);
        }
    }

    // 处理剩余元素
    for (; i < size; i++) {
        result[i] = pow(base[i], is_scalar ? scalar_exponent : exponent[i]);
    }

    return (PyObject *)result_array;
}

static PyMethodDef methods[] = {
    {"power", avx2_power, METH_VARARGS, "AVX2 accelerated power function"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "avx2_power",
    "AVX2 accelerated power function",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_avx2_power(void) {
    import_array();
    return PyModule_Create(&module);
}