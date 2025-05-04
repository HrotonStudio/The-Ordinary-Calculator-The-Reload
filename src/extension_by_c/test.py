import avx2_power
import time, sys, numpy as np
sys.set_int_max_str_digits(2147483647)
start = time.time()
a = avx2_power.power(np.ndarray(114514), 114514)
end = time.time()
b = 114514 ** 114514
end2 = time.time()
print(f"AVX2加速结果:{a}\n原生结果:{b}\n")
print(f"AVX2加速:{end - start}\n原生:{end2 - end}\n加速比:{(end2 - end) / (end - start)}")