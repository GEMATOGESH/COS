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

	B1, B2 = 500, 3
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
	for i in range(length - K + 1):
		buf = 0
		for j in range(i - m, i + m + 1):
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
		x1  = 0 if (i - 6) < 0  else x[i - 6]
		x2  = 0 if (i - 5) < 0  else x[i - 6]
		x3  = 0 if (i - 4) < 0  else x[i - 6]
		x4  = 0 if (i - 3) < 0  else x[i - 6]
		x5  = 0 if (i - 2) < 0  else x[i - 6]
		x6  = 0 if (i - 1) < 0  else x[i - 6]
		x7  = 0 if (i + 1) >= N else x[i + 1]
		x8  = 0 if (i + 2) >= N else x[i + 2]
		x9  = 0 if (i + 3) >= N else x[i + 3]
		x10 = 0 if (i + 4) >= N else x[i + 4]
		x11 = 0 if (i + 5) >= N else x[i + 5]
		x12 = 0 if (i + 6) >= N else x[i + 6]
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
	Aj0, Fij0 = dft(x)
	x_arythmetic = arithmetic_mean(copy.deepcopy(x), SLIPPY_WINDOW)
	Aj1, Fij1 = dft(x_arythmetic)
	x_parabola = parabola(copy.deepcopy(x))
	Aj2, Fij2 = dft(x_parabola)
	x_median = median_averaging(copy.deepcopy(x), MEDIAN_WINDOW)
	Aj3, Fij3 = dft(x_median)

	fig, axs = plt.subplots(2, 1)
	axs[0].plot(range(len(x)), x, range(len(x_arythmetic)), x_arythmetic, range(len(x_parabola)), x_parabola, range(len(x_median)), x_median)
	axs[0].legend(["original", "arithmetic mean", "parabola", "median averaging"])
	axs[1].plot(range(len(Aj0)), Aj0, range(len(Fij0)), Fij0, range(len(Aj1)), Aj1, range(len(Fij1)), Fij1, range(len(Aj2)), Aj2, range(len(Fij2)), Fij2, range(len(Aj3)), Aj3,  range(len(Fij3)), Fij3)
	axs[1].legend(["original A", "original fi", "arithmetic A", "arithmetic fi", "parabola A", "parabola fi", "median averaging A", "median averaging fi"])
	plt.show()


if __name__ == "__main__":
	main()
