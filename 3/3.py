import math
import copy
import random
import matplotlib.pyplot as plt


N = 1024


def make_some_noise(a=20, fi=0):
	x = []

	for i in range(0, N):
		x.append(a * math.cos((2 * 10 * math.pi * i)/N - fi))
	return x


def make_some_polynoise():
	x = []
	a = [1, 3, 4, 10, 11, 14, 17]
	fi = [math.pi/6, math.pi/4, math.pi/3, math.pi/2, 3 * math.pi/4, math.pi]

	id_a = random.randint(0, len(a) - 1) 
	id_fi = random.randint(0, len(fi) - 1)
	for i in range(0, N):
		buf = 0

		for j in range(1, 10):
			buf += (a[j % 7] * math.cos((2 * math.pi * j * i)/N - fi[j % 6]))
		x.append(buf)
	return x


def restore_some_noise(A, fi):
	y = []

	for i in range(0, N):
		buf = 0
		for j in range(0, N // 2 - 1):
			buf += A[j] * math.cos((2 * math.pi* j * i) / N - fi[j])
		y.append(buf)
	return y


def restore_some_polynoise(A):
	y = []

	for i in range(0, N):
		buf = 0
		for j in range(1, N // 2 - 1):
			buf += A[j] * math.cos((2 * math.pi* j * i) / N)
		buf += A[0]/2
		y.append(buf)
	return y


def restore_some_polynoise_with_water(A, fi):
	y = []

	for i in range(0, N):
		buf = 0
		for j in range(1, N // 2 - 1):
			buf += A[j] * math.cos((2 * math.pi* j * i) / N - fi[j])
		buf += A[0]/2
		y.append(buf)
	return y


def restore_any_noise_with_filter(A, fi, type_sig=0, type_fil=0, filter=[0,float("inf")]):
	for i in range(0, len(A)):
		if type_fil == 0:
			if i > filter[1]:
				A[i] = 0
		elif type_fil == 1:
			if i < filter[0]:
				A[i] = 0
		elif type_fil == 2:
			if i < filter[0] or i > filter[1]:
				A[i] = 0

	if not type_sig:
		return restore_some_noise(A, fi)
	else:
		return restore_some_polynoise_with_water(A, fi)


def dpf(x):
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


def harmonic():
	x = make_some_noise()
	rng = range(0, len(x))
	Aj, fij = dpf(x)
	restored = restore_some_noise(Aj, fij)
	return rng, x, restored, Aj, fij


def polyharmonic():
	x = make_some_polynoise()
	rng = range(0, len(x))
	Aj, fij = dpf(x)
	restored = restore_some_polynoise(Aj)
	restored_with_fi = restore_some_polynoise_with_water(Aj, fij)
	return rng, x, restored, restored_with_fi, Aj, fij


def main():
	fig, axs = plt.subplots(2, 3)

	rng, x, restored, Re, Im = harmonic()
	filtered1 = restore_any_noise_with_filter(copy.deepcopy(Re), Im, 0, 0, filter=[0, 10])
	filtered2 = restore_any_noise_with_filter(copy.deepcopy(Re), Im, 0, 1, filter=[10, 0])
	filtered3 = restore_any_noise_with_filter(copy.deepcopy(Re), Im, 0, 2, filter=[10, 10])

	axs[0, 0].plot(rng, x, 'r', rng, restored, 'k--', rng, Re, 'g')
	axs[0, 0].set_xlabel('Harmonic')
	axs[0, 0].legend(['original','restored', 'A', 'Filtered'], loc='upper center')

	axs[0, 1].plot(rng, Im, 'b--')
	axs[0, 1].set_xlabel('Harmonic fi')
	axs[0, 1].legend(['fi'], loc='upper center')

	axs[0, 2].plot(rng, filtered1, 'r', rng, filtered2, 'g', rng, filtered3, 'b--')
	axs[0, 2].set_xlabel('Harmonic filter')
	axs[0, 2].legend(['Lp', 'Hp', 'Mp'], loc='upper center')

	rng, x, restored, restored_with_fi, Re, Im = polyharmonic()
	filtered1 = restore_any_noise_with_filter(copy.deepcopy(Re), Im, 1, 0, filter=[0, 1])
	filtered2 = restore_any_noise_with_filter(copy.deepcopy(Re), Im, 1, 1, filter=[9, 0])
	filtered3 = restore_any_noise_with_filter(copy.deepcopy(Re), Im, 1, 2, filter=[4, 4])

	axs[1, 0].plot(rng, x, 'r', rng, restored_with_fi, 'k--', rng, restored, 'k', rng, Re, 'g') 
	axs[1, 0].set_xlabel('Polyharmonic')
	axs[1, 0].legend(['original','restored with fi', 'restored', 'A', 'filtered'], loc='upper center')

	axs[1, 1].plot(rng, Im, 'b--') 
	axs[1, 1].set_xlabel('Polyharmonic fi')
	axs[1, 1].legend(['fi'], loc='upper center')

	axs[1, 2].plot(rng, filtered1, 'r', rng, filtered2, 'g', rng, filtered3, 'b--')
	axs[1, 2].set_xlabel('Polyharmonic filter')
	axs[1, 2].legend(['Lp', 'Hp', 'Mp'], loc='upper center')

	plt.show()


if __name__=="__main__":
	main()
