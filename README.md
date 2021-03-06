# DeepLearning

## 1.介绍
### 1.1在本实例中，如果想将代码直接运行需注意以下几点：
* Python版本3.X（本人使用的是Python 3.6）
* numpy版本：1.16.0
* scipy版本：0.19.1
* tensorflow版本：1.12.0
* tensorboard版本：1.12.2
* pytorch版本：0.4.0
* torchvision版本：0.2.1
### 1.2 项目说明
* data：
    * **mlp_regression_train**:用于多层感知机拟合的数据集（训练数据）
    * **mlp_regression_test**:用于多层感知机拟合的数据集（测试数据）
    * **mnist_train**:mnist数据集的抽样数据,数据量为：6000（训练数据）
    * **mnist_test**:mnist数据集的抽样数据，数据量为：1000（测试数据）
* pt：使用pytorch动态图构建神经网络
* tf：使用tensorflow静态图构建神经网络
* tf_eager：使用tensorflow动态图(eager)构建神经网络
### 1.3 项目注意

* 在数据拟合的过程中，使用relu激活函数，不能拟合小于0的值，因此推荐使用Leaky ReLU等激活器
* 在数据多分类的过程中，注意使用数据归一化（标准化），有利于加快训练的速度，促进模型的收敛