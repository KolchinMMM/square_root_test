import math


def get_square_roots(a, b, c):
	if a == 0:
		if b == 0:
			return tuple()
		return (-c/b, )
	elif b == 0:
		if c > 0:
			return ()
		elif c == 0:
			return (0, )
		sqrt = math.sqrt(-c)
		return -sqrt, sqrt
	elif c == 0:
		return 0, -b/a
	else:
		d = b**2 - 4*a*c
		if d<0:
			return ()
		elif d == 0:
			return (-b/(2*a), )
		squared = math.sqrt(d)
		return (-b - squared)/(2*a), (-b + squared)/(2*a)


def main():
	print(get_square_roots(1, 0, 3))

if __name__ == "__main__":
	main()