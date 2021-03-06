# -*- coding: utf-8 -*-
# 利用多层感知机多分类，测试数据mnist的csv版本，抽样版本(eager模式，即tensorflow动态图机制)
# 输入层具有28*28个神经元，输出层有10个神经元
# 使用tensorflow高级API进行多分类任务
import tensorflow as tf
import tensorflow.contrib.eager as tfe
import numpy as np
# 启动tensorflow的动态图机制
tfe.enable_eager_execution()
'''--------加载数据start--------'''
# 加载训练数据及测试数据
trainData = np.loadtxt('../data/mnist_train.csv',delimiter=",")
testData = np.loadtxt('../data/mnist_test.csv',delimiter=",")
# 提取训练数据的x 及 y
# 将x_train数据标准化，可以大大加快网络的训练速度
x_train = trainData[:, 1:]/255
y_train = trainData[:, 0]
# 将y_train标签进行one-hot编码
# y_train.astype(np.int)：进行类型转换，转换为int型
y_train_one_hot = tf.one_hot(y_train.astype(np.int), 10).numpy()
# 提取测试数据的x,y
x_test = testData[:, 1:]/255
y_test = testData[:, 0]
# 将训练数据封装到dataSet中
# shuffle意味着打乱训练数据集中的顺序
# repeat意味着训练数据无限重复
# batch意味着每次在dataSet中提取64条数据
ds = tf.data.Dataset.from_tensor_slices({
    "x": x_train,
    'y': y_train_one_hot
}).shuffle(buffer_size=123).repeat().batch(64)
'''--------加载数据end--------'''

'''--------模型start--------'''
class MLPModel(object):
    def __init__(self):
        '''模型结构为784->32->64->32->10'''
        # 定义第一层全连接层的结构，仅需要定义输出单元，输入单元不需要设置
        self.layer1 = tf.layers.Dense(units=32, activation=tf.nn.relu)
        # 定义第二层全连接层的结构，仅需要定义输出单元，输入单元不需要设置
        self.layer2 = tf.layers.Dense(units=64, activation=tf.nn.relu)
        # 定义第三层全连接层的结构，仅需要定义输出单元，输入单元不需要设置
        self.layer3 = tf.layers.Dense(units=32, activation=tf.nn.relu)
        # 定义最后一层全连接层的结构，仅需要定义输出单元，输入单元不需要设置
        self.out_layer = tf.layers.Dense(units=10)
    def forward(self, inputs):
        '''模型结构为784->32->64->32->10'''
        # 计算第一层输出（具有激活函数）
        layer1_out = self.layer1(inputs)
        # 计算第二层输出（具有激活函数）
        layer2_out = self.layer2(layer1_out)
        # 计算第三层输出（具有激活函数）
        layer3_out = self.layer3(layer2_out)
        # 计算输出层的输出（没有写激活函数）
        out_layer = self.out_layer(layer2_out)
        return out_layer
'''--------模型end--------'''

'''--------定义loss函数 start--------'''
def loss_fn(forward, inputs, ys):
    # ys与out_layer都是one-hot类型的向量
    # 使用交叉熵定义损失函数
    return tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits_v2(labels=ys, logits=forward(inputs)))
'''--------定义loss函数 end--------'''

'''--------定义优化器与梯度函数 start--------'''
model = MLPModel()
# 0.00001 为学习率，即learning_rate
optimizer = tf.train.AdamOptimizer(0.01)
# tfe.implicit_gradients相当于一个python修饰器，可以计算变量的梯度
grad_fn = tfe.implicit_gradients(loss_fn)
'''--------定义优化器与梯度函数 end--------'''

'''--------训练start--------'''

for index, batchData in enumerate(tfe.Iterator(ds)):
    # 计算梯度，grad是当前的梯度数组,本代码对应着8个变量
    grad = grad_fn(model.forward, tf.cast(batchData['x'], dtype=tf.float32), batchData['y'])
    # 优化权重，反向传播
    optimizer.apply_gradients(grad)
    if index % 50 == 0:
        y_pre = model.forward(tf.cast(x_test, dtype=tf.float32))
        # 测试正确率
        correct_prediction = np.equal(np.argmax(y_pre.numpy(), 1), y_test)
        accuracy = np.mean(correct_prediction.astype(np.float))
        print(accuracy)
'''--------训练end--------'''
