#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
from numba import njit

@njit
def fib_py(n):
        if n <= 1:
                return n
        else:
                return (fib_py(n-1) + fib_py(n-2))

def main():
	n = 47
	f = Integer(n)
	start1 = pc()
	f.fib()
	end1 = pc()
	print('C++ time: ', end1-start1)

	start2 = pc()
	fib_py(n)
	end2 = pc()
	print('Numba time: ', end2-start2)


if __name__ == '__main__':
        main()
