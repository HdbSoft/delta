# DELTA DATA PROCESSING FRAMEWORK:
# 2d graphics tools for functions and
# matrices using matplotlib

import matplotlib.pyplot as plt

def plot(data, _type, **kwargs):
	if not data:
		return 1
	else:
		if _type == 'function':
			min_, max_, n = -10, 10, 20

			data_ = []
			for i in range(min_, max_, n):
				data_.append(data(i))

			plt.plot(data_)
			plt.show()

		elif _type == 'matrix':
			plt.imshow(data)
			plt.show()
