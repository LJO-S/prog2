#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib_py(n):
        if n <= 1:
                return n
        else:
                return (fib_py(n-1) + fib_py(n-2))

def main():
	time_c = []
	time_py = []

	n_list = [ii for ii in range(30, 46)]

	for n in n_list:
		f = Integer(n)
		start1 = pc()
		f.fib()
		end1 = pc()
		time_c += [end1-start1]

		start2 = pc()
		fib_py(n)
		end2 = pc()
		time_py += [end2-start2]
		print('Loop klar')

	plt.plot(n_list, time_c, 'bo')
	plt.plot(n_list, time_py, 'ro')
	plt.show()


if __name__ == '__main__':
        main()
