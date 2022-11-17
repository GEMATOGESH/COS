import math
import copy
import random
import matplotlib.pyplot as plt


N = 1024
SLIPPY_WINDOW = 7
MEDIAN_WINDOW = 9


def create_signal():
	""" Creates signal.

	Returns:
		x: signal
	"""

	B1, B2 = 23, 17
	x = []

	for i in range(N):
		buf = 0
		for j in range(50, 70):
			buf += (-1)**(random.randint(0, 1)) * B2 * math.sin(2 * math.pi * i * j / N)

		x.append(B1 * math.sin(2 * math.pi * i / N) + buf)
	return x


def dft(x):
	""" Discrete Fourier transform.

	Args:
		x: signal

	Returns:
		Aj: spectrum of A
		fij: spectrum of fi
	"""

	length = len(x)
	Aj = []
	fij = []

	for i in range(0, length):
		Acj = 0
		Asj = 0
		for j in range(0, length):
			buf = 2 * math.pi * j * i / length
			Acj += x[j] * math.cos(buf)
			Asj += x[j] * math.sin(buf)

		Acj *= 2/length
		Asj *= 2/length

		Aj.append(math.sqrt(Acj**2 + Asj**2))
		fij.append(math.atan2(Asj, Acj))
	return Aj, fij


def arithmetic_mean(x, K):
	""" Arithmetic mean.

	Args:
		x: signal
		K: num of points

	Returns:
		x: updated singal
	"""

	length = len(x)
	m = int((K - 1) / 2)
	for i in range(length):
		buf = 0
		for j in range(i - m, i + m):
			if j >= N:
				print("Got ya: ", j)
				continue
			buf += x[j]
		x[i] = (1 / K) * buf
	return x


def parabola(x):
	""" Fourth degree parabola.

	Args:
		x: signal

	Returns:
		x: updated singal
	"""

	length = len(x)
	for i in range(length):
		x1  = 0 if (i - 6) < 0  else x[i-6]
		x2  = 0 if (i - 5) < 0  else x[i-6]
		x3  = 0 if (i - 4) < 0  else x[i-6]
		x4  = 0 if (i - 3) < 0  else x[i-6]
		x5  = 0 if (i - 2) < 0  else x[i-6]
		x6  = 0 if (i - 1) < 0  else x[i-6]
		x7  = 0 if (i + 1) >= N else x[i+1]
		x8  = 0 if (i + 2) >= N else x[i+2]
		x9  = 0 if (i + 3) >= N else x[i+3]
		x10 = 0 if (i + 4) >= N else x[i+4]
		x11 = 0 if (i + 5) >= N else x[i+5]
		x12 = 0 if (i + 6) >= N else x[i+6]
		x[i] = (1 / 2431) * (110 * x1 - 198 * x2 - 135 * x3 + 110 * x4 + 390 * x5 + 600 * x6 + 677 * x[i] + 600 * x7 + 390 * x8 + 110 * x9 - 135 * x10 - 198 * x11 + 110 * x12)
	return x


def median_averaging(x, K):
	""" Median averaging.

	Args:
		x: signal
		K: length of window

	Returns:
		x: updated singal
	"""

	length = len(x)
	for i in range(length):
		if (i >= K):
			window = x[(i - K):i]
			sorted = copy.deepcopy(window)
			sorted.sort()
			avg = int((K / 2) + 0.5) - 1
			x[(i - K) + avg] = sorted[avg]
	return x


def main():
	""" Main. """

	x = create_signal()
	x_arythmetic = arithmetic_mean(copy.deepcopy(x), SLIPPY_WINDOW)
	x_parabola = parabola(copy.deepcopy(x))
	x_median = median_averaging(copy.deepcopy(x), MEDIAN_WINDOW)
	plt.plot(range(len(x)), x, range(len(x_arythmetic)), x_arythmetic, range(len(x_parabola)), x_parabola, range(len(x_median)), x_median)
	plt.legend(["original", "arithmetic mean", "parabola", "median averaging"])
	plt.grid()
	plt.show()


if __name__ == "__main__":
	main()
