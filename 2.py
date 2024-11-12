def fun(x):
    # 计算多项式 f(x) = x^3 - 4x^2 + 6x - 2
    return x**3 - 4*x**2 + 6*x - 2

# 测试输入
x = float(input('请输入x的值：'))
print('多项式计算结果为：', fun(x))
