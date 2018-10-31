import tensorflow as tf 
from tensorflow.examples.tutorials.mnist import input_data
#from tensorflow.model import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
n_nodes_hl1 = 500
n_nodes_hl3 = 500
n_nodes_hl2 = 500

n_classes = 10
batch_size = 100

x = tf.placeholder('float',[None, 784])
y = tf.placeholder('float') #There was an error here

def neural_network_model(data) :

# (input_data * weights + biases)
