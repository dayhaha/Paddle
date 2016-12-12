MovieLens数据集评分回归模型
=========================

这里我们在MovieLens数据集描述一种**余弦相似度回归**任务。
该示例将展示paddle如何进行词向量嵌入，处理相似度回归，针对文本
的单词级别的卷积神经网络，以及paddle如何处理多种类型的输入。
需要注意的是，该模型网络只是用于进行demo展示paddle如何工作，而
没有进行结构的微调。


**我们非常欢迎您用PADDLEPADDLE构建更好的示例，如果您有好的建议来
让这个示例变得更好，希望能让我们知晓。**

数据准备
```````
下载并解压数据集
''''''''''''''
这里我们使用 `movielens 1m 数据集 <ml_dataset.html>`_。
要下载和解压数据集，只需要简单的运行下面的命令即可。

.. code-block:: bash

	cd demo/recommendation/data
	./ml_data.sh

:code:`demo/recommendation/data/ml-1m`的目录结构为:

.. code-block:: text

	+--ml-1m
		+--- movies.dat 	# 电影特征
		+--- ratings.dat 	# 评分
		+--- users.dat 		# 用户特征
		+--- README 		# 数据集描述

字段配置文件
''''''''''
**字段配置文件**用来具体说明数据集的字段和文件格式，
例如，说明每个特征文件具体字段是**什么**类型。

ml-1m的字段配置文件在目录:code:`demo/recommendation/data/config.json`中。
其具体说明了字段类型和文件名称:
1) 用户文件中有四种类型的字段\: 编号，性别，年龄和职业；
2) 文件名称为"users.dat"，文件的分隔符为"::"。

.. include:: ../../../demo/recommendation/data/config.json
   :code: json
   :literal:

准备数据
```````
你需要安装python的第三方库。
**强烈推荐使用VIRTUALENV来创造一个干净的python环境。**

.. code-block:: bash

	pip install -r requirements.txt
































