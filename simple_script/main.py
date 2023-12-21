import mlx.core as mx
a = mx.array([1, 2., 3, 4])
print(a)
print(a.shape)



a = mx.random.normal((10,))
b = mx.random.normal((10,))

print(a)
print(b)
c = mx.add(a, b, stream=mx.cpu)
print(c)
d = mx.add(a, c, stream=mx.gpu)
print(d)