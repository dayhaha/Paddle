================
手写字符识别教程
================


MNIST数据
==========

数据下载
---------

我们首先下载 `MNIST <http://yann.lecun.com/exdb/mnist/>`_ 数据库，
该数据库是手写字符识别常用的数据库。在 ``demo/mnist`` 目录中执行
一下命令，进行下载：

    .. code-block::  bash

           ./data/get_mnist_data.sh

数据说明
--------

- 解压缩


  将下载下来的数据进行gzip解压，可以在文件夹 ``demo/mnist/data/raw_data`` 中得到以下四个文件:

  .. code-block::  text

      t10k-images-idx3-ubyte      测试数据图片，10,000条数据
      t10k-labels-idx1-ubyte      测试数据标签，10,000条数据
      train-images-idx3-ubyte     训练数据图片，60,000条数据
      train-labels-idx1-ubyte     训练数据标签，60,000条数据

- 数据格式

  MNIST的每条数据可以分为两部分：一张手写字符图片和对应的标签。标签对应着0~9是个数字，而图片
  则是28X28的像素矩阵，我们随机选取训练集中的10张图片进行绘制，并给出标签集中对应的标签：

  .. code-block::  python

      pass

  .. image::    src/mnist_image.jpg
      :align:   center


  .. code-block::  python

      label: [6, 6, 6, 3, 7, 3, 0, 7, 7, 9]
  


Softmax回归
===========



多层感知器
==========


卷积神经网络
============

