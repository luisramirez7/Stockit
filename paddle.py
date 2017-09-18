import paddle

def multilayer_perceptron(data):
    hidden1 = paddle.layer.fc(input=data, size=128, act=paddle.activation.Relu())
    hidden2 = paddle.layer.fc(input=hidden1,
                              size=64,
                              act=paddle.activation.Relu())
    predict = paddle.layer.fc(input=hidden2,
                              size=10,
                              act=paddle.activation.Softmax())
    return predict

def train(): 

	paddle.init(use_gpu=False, trainer_count=1)

	data = paddle.layer.data(
	    name='numeric', type=paddle.data_type.float_value(784))
	label = paddle.layer.data(
	    name='label', type=paddle.data_type.integer_value(10))

	predict = multilayer_perceptron(data) # uncomment for MLP

	cost = paddle.layer.classification_cost(input=predict, label=label)

	parameters = paddle.parameters.create(cost)

	optimizer = paddle.optimizer.Momentum(
	    learning_rate=0.1 / 128.0,
	    momentum=0.9,
	    regularization=paddle.optimizer.L2Regularization(rate=0.0005 * 128))

	trainer = paddle.trainer.SGD(cost=cost,
	                             parameters=parameters,
	                             update_equation=optimizer)