from __future__ import print_function, unicode_literals, absolute_import, division

import numpy as np
import matplotlib.pyplot as plt
from csbdeep.utils import Path, download_and_extract_zip_file, plot_some, normalize, normalize_mi_ma
from csbdeep.io import load_training_data, save_tiff_imagej_compatible

#(X_train, Y_train), (X_val,Y_val), axes = load_training_data('data_label.npz', validation_split=0.1, verbose=True)
data = np.load('data_label.npz')
#training images (180)
print('Images number :', len(data['X']))

x = data['Y'][2,...,0]

print('x len :', len(data['X'][0]))
print('image size =', x.shape)

# To see npz content :
"""
lst = data.files
for item in lst:
    print("item : ", item)
    print("data: ", data[item])

"""

# To download :
import matplotlib.pyplot as plt
for i in range(5, 10):
    img = normalize(data['X'][i], 0, 100, clip=True)
    plt.imshow(np.squeeze(img))
    plt.savefig("X/img" + str(i) + ".png")

    img = normalize(data['Y'][i], 0, 100, clip=True)
    plt.imshow(np.squeeze(img))
    plt.savefig("Y/img" + str(i) + ".png")
plt.show()


# To show patch pairs X / Y
fig=plt.figure(figsize=(8, 4))
plt.axis('off')
h = 2
w = 5
for i in range(1, w):
    plt.subplot(h, w, i)
    img = np.squeeze(normalize(data['X'][i][0][5], 0, 100, clip=True))
    plt.axis('off')
    plt.imshow(img)

    plt.subplot(h, w, w + i)
    img = np.squeeze(normalize(data['Y'][i][0][5], 0, 100, clip=True))
    plt.axis('off')
    plt.imshow(img)
plt.show()
