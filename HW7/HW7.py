# 參考 https://github.com/ccc-py/micrograd/?tab=readme-ov-file#example-usage
# 使用ChatGPT輔助

from micrograd.engine import Value

# 初始化變數 a、b、c
a = Value(2.0)
b = Value(1.0)
c = Value(3.0)

# 迭代優化的主要循環
for i in range(100000):
    # 定義目標函數 f = a^2 + b^2 + c^2
    f = a**2 + b**2 + c**2

    # 輸出目標函數值和變數值
    print('f(p) = {}, p = [{}, {}, {}]'.format(f.data, a.data, b.data, c.data))

    # 計算梯度並執行反向傳播
    f.backward()

    # 檢查梯度大小，若小於閾值則跳出迭代
    if a.grad < 0.001:
        break

    # 更新變數值，執行梯度下降
    step = 0.01
    a -= a.grad * step
    b -= b.grad * step
    c -= c.grad * step

# 輸出最終結果
print('\nf(p) = {}, p = [{}, {}, {}]'.format(f.data, a.data, b.data, c.data))