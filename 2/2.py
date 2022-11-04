import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

N = 2048
K = (3 * N) / 4

def start(fi=0):
	x = []
	skz1_x = []
	skz2_x = []
	fur = []
	mas_M = []

	for M in range(int(K), 2 * N, 15):
		print('M: ', M)

		buf1 = 0
		buf2 = 0

		sum_sin = 0
		sum_cos = 0

		for n in range(0, M):
			x.append(math.sin(2 * math.pi * n / N + fi))

			buf1 += x[-1] ** 2
			buf2 += x[-1]

			sum_sin += x[-1] * math.sin(2 * math.pi * n / M)
			sum_cos += x[-1] * math.cos(2 * math.pi * n / M)
			
		skz1_x.append(math.sqrt((1 / (M + 1)) * buf1))
		skz2_x.append(math.sqrt(((1 / (M + 1)) * buf1) - (((1 / (M + 1)) * buf2) ** 2)))

		sum_sin *= 2 / M
		sum_cos *= 2 / M
		fur.append(math.sqrt(sum_sin ** 2 + sum_cos ** 2))

	res_skz1 = []
	res_skz2 = []
	res_fur = []
	mas_M.append(M)
	for i in range(len(fur)):
		res_skz1.append(0.707 - skz1_x[i])
		res_skz2.append(0.707 - skz2_x[i])
		res_fur.append(1 - fur[i])

	print("Result length: ", len(x))
	return res_skz1, res_skz2, res_fur


res_skz1, res_skz2, res_fur = start()
figure, axis = plt.subplots(2, 1)

figure.canvas.manager.set_window_title('ЦОС')

axis[0].plot(list(range(0, len(res_skz1))), res_skz1, color='r', label='СКЗ А')
axis[0].plot(list(range(0, len(res_skz2))), res_skz2, color='g', label='СКЗ Б')
axis[0].plot(list(range(0, len(res_fur))), res_fur, color='b', label='Амплитуда')
axis[0].set_title("Без начальной фазы")
axis[0].legend()

res_skz1, res_skz2, res_fur = start(math.pi / 3)

axis[1].plot(list(range(0, len(res_skz1))), res_skz1, color='r', label='СКЗ А')
axis[1].plot(list(range(0, len(res_skz2))), res_skz2, color='g', label='СКЗ Б')
axis[1].plot(list(range(0, len(res_fur))), res_fur, color='b', label='Амплитуда')
axis[1].set_title("С начальной фазой")
axis[1].legend()
plt.show()

'''
df = pd.DataFrame(x)
df.to_excel(excel_writer = "C:/Users/Gematogesh/Desktop/results.xlsx")
print("Exported!")
'''