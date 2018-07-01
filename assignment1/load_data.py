# coding: utf-8
import pickle as pk
import numpy as np
xs = []
ys = []
for i in range(1,6):
    f = os.path.join(r"cs231n\datasets\cifar-10-batches-py\data_batch_%d" %i)
    with open(f, "rb") as file:
        data_dict = pk.load(file, encoding = 'latin1')
        X = data_dict['data']
        Y = data_dict['labels']
        xs.append(X)
        ys.append(Y)
f = os.path.join(r"cs231n\datasets\cifar-10-batches-py\test_batch")
with open(f, 'rb') as file:
	data = pk.load(file, encoding = 'latin1')
	Xte = data['data']
	Yte = data['labels']

Xte = Xte.reshape(10000,3,32,32).transpose(0,2,3,1).astype('float')
Yte = np.array(Yte).astype('float')
Xtr = np.concatenate(xs)
Ytr = np.concatenate(ys)
Xtr = Xtr.reshape(50000,3,32,32).transpose(0,2,3,1).astype('float')
Ytr = Ytr.astype('float')


