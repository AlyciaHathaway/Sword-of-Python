---
title: Numpy库
---
### 创建数组
```
a = np.array([[1, 2, 4], [3, 6, 9]])
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)
```

### 特殊数组
```
b = np.zeros((2, 3))
print(b)
c = np.ones((2, 3))
print(c)
d = np.empty((3, 2))
print(d)
```

### 序列数组
```
e = np.arange(1, 20, 5)
print(e)
f = np.linspace(0, 9, 10)
print(f)
```

### 数组索引
```
print(a[0])
print(a[:, 1])
print(a[0, 2])
```

### 数组运算
```
print(a + b)
print(a - b)
print(a * b)
print(a ** 2)
# print(a / b)
# 对应的点乘元素乘积后，求和
# print(np.dot(a, b))
print(a >= 2)
print(a.max())
print(a.min())
print(a.sum())
```

### 数组拷贝
**浅拷贝**
```
g = a
print(g)
# g[1, 2] = 9
# print(a, g)
```

**深拷贝**
```
h = a.copy()
print(h)
h[1, 2] = 10
print(a, h)
```

### 矩阵
```
A = np.matrix([[1, 2], [3, 4]])
print(A)
print(type(A))
```
**矩阵运算**
**转置**
`print(A.T)`
**乘法**
```
B = np.matrix([[3], [5]])
print(B)
print(A * B)
```
**逆矩阵(行和列要相等)**
```
# (矩阵和逆矩阵相乘 = 1个单位矩阵，也就是说如果C是A的逆矩阵，A * C = C * A)
# (默认,任意两个矩阵相乘是不等于它们相反位置的乘积的，A * C ≠ C * A)
print(A.I)
```
**解线性方程组**
`print(np.linalg.solve(A, B))`
