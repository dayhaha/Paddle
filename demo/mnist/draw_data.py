import numpy as np
import matplotlib.pyplot as plt
import random


def read_data(path, filename):
    imgf = path + filename + "-images-idx3-ubyte"
    labelf = path + filename + "-labels-idx1-ubyte"
    f = open(imgf, "rb")
    l = open(labelf, "rb")

    f.read(16)
    l.read(8)

    # Define number of samples for train/test
    if "train" in filename:
        n = 60000
    else:
        n = 10000

    images = np.fromfile(
        f, 'ubyte', count=n * 28 * 28).reshape((n, 28 * 28)).astype('float32')
    labels = np.fromfile(l, 'ubyte', count=n).astype("int")

    return images, labels


if __name__ == "__main__":
    train_images, train_labels = read_data("./data/raw_data/", "train")
    test_images, test_labels = read_data("./data/raw_data/", "t10k")
    label_list = []
    for i in range(10):
        index = random.randint(0, len(train_images) - 1)
        label_list.append(train_labels[index])
        plt.subplot(1, 10, i + 1)
        plt.imshow(train_images[index], cmap="Greys_r")
        plt.axis('off')
    plt.show()
    print('label: %s' % (label_list, ))
