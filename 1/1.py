import math

import pandas as pd


'''
A - амплитуда - высота - длина вектора
f - частота - сколько раз в один период мы берем значение дискретизации
fi - фаза - начальный угол вектора в нулевой момент времени
'''


def export(id, mas):
	df = pd.DataFrame(mas)
	name = str(id) + ".xlsx"
	df.T.to_excel(excel_writer = name)


def make_garmonic_noise(a, f, fi):
	N = 2048
	res_mas = []

	for n in range(0, N - 1):
		x = a * math.sin((2 * math.pi * f * n)/N + fi)
		res_mas.append(x)

	return res_mas


def make_poligarmonic_noise(a, f, fi):
	N = 2048
	res_mas = []

	for n in range(0, N - 1):
		sum = 0
		for j in range(0, 4):
			sum += a[j] * math.sin((2 * math.pi * f[j] * n) / N + fi[j])
		res_mas.append(sum)

	return res_mas


res_mas = []
mas = make_garmonic_noise(8, 4, math.pi / 6)
res_mas.append(mas)
mas = make_garmonic_noise(8, 4, math.pi / 3)
res_mas.append(mas)
mas = make_garmonic_noise(8, 4, 2 * math.pi / 3)
res_mas.append(mas)
mas = make_garmonic_noise(8, 4, math.pi / 4)
res_mas.append(mas)
mas = make_garmonic_noise(8, 4, 0)
res_mas.append(mas)
export("1a", res_mas)

res_mas = []
mas = make_garmonic_noise(4, 8, 0)
res_mas.append(mas)
mas = make_garmonic_noise(4, 1, 0)
res_mas.append(mas)
mas = make_garmonic_noise(4, 5, 0)
res_mas.append(mas)
mas = make_garmonic_noise(4, 4, 0)
res_mas.append(mas)
mas = make_garmonic_noise(4, 9, 0)
res_mas.append(mas)
export("1b", res_mas)

res_mas = []
mas = make_garmonic_noise(8, 2, 0)
res_mas.append(mas)
mas = make_garmonic_noise(3, 2, 0)
res_mas.append(mas)
mas = make_garmonic_noise(2, 2, 0)
res_mas.append(mas)
mas = make_garmonic_noise(1, 2, 0)
res_mas.append(mas)
mas = make_garmonic_noise(4, 2, 0)
res_mas.append(mas)
export("1c", res_mas)

aj = [3, 3, 3, 3, 3]
fj = [1, 2, 3, 4, 5]
fij = [math.pi / 4, 3 * math.pi / 4, 2 * math.pi / 3, math.pi / 2, math.pi / 3]
res_mas = make_poligarmonic_noise(aj, fj, fij)
export(2, res_mas)


print("Экспортировано!")