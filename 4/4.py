import math
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
			buf += (-1)**(random.random()) * B2 * math.sin(2 * math.pi * i / N)

		x.append(B1 * math.sin(2 * math.pi * i / N) + buf)
	return x


def dft(x):
	""" Discrete Fourier transform. Returns spectrums of A and fi.

	Args:
		x (list): signal

	Returns:
		Re: spectrum of A
		Im: spectrum of fi
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


def main():
	""" Main."""

	x = create_signal()
	plt.plot(range(len(x)), x)
	plt.grid()
	plt.show()


if __name__ == "__main__":
	main()
