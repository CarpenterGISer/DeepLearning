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
* pt：使用pytorch动态图构建神经网络(文件夹)
    * **mlp_regression_csv**：使用pytorch动态图建造多层感知机（MLP）拟合曲线，从csv文件中读取数据，没有使用归一化层(Batch Normalization)
* tf：使用tensorflow静态图构建神经网络(文件夹)
    * **mlp_regression_csv**：使用tensorflow静态图建造多层感知机（MLP）拟合曲线，从csv文件中读取数据，没有使用归一化层(Batch Normalization)
* tf_eager：使用tensorflow动态图构建神经网络(文件夹)
    * **mlp_regression_csv**：使用tensorflow动态图建造多层感知机（MLP）拟合曲线，从csv文件中读取数据，没有使用归一化层(Batch Normalization)
### 1.2 项目注意

* 在数据拟合的过程中，使用relu激活函数，不能拟合小于0的值，因此推荐使用Leaky ReLU等激活器