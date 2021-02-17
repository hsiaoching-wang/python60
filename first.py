import numpy as np
a = np.arange(1,21,1)
print(a)
for i, data  in enumerate(a):
	if data % 2 == 0:
		print(data,  end=' ')
print(end='\n')
for i, data in enumerate(a):
	if data % 3 == 0:
		print(data, end=' ') 