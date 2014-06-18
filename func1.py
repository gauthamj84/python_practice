def fib(n):
	a, b = 0, 1
	while a < n:
		print b
		a, b = b, a+b

fib(200)
f = fib
f(10)