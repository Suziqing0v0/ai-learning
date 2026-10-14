import numpy as np

rng42a = np.random.default_rng(42)
print("种子42第一次：", rng42a.random(5))
rng42b = np.random.default_rng(42)
print("种子42第二次：", rng42b.random(5))
rng7 = np.random.default_rng(7)
print("种子7：", rng7.random(5))
print("种子7摇色子：", rng7.integers(1, 7, 10))
