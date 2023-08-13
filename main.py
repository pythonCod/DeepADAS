import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
tf.get_logger().setLevel('ERROR')
import numpy as nb


print("-------------")
print("GPU detected")
print("-------------")
tf.config.list_physical_devices('GPU')


tensor_0d = tf.constant(5)
tensor_2d = tf.constant([[1, 2, 3],[8,4,6],[12, 100, 178]])
tensor_3d = tf.constant([
    [[1,2,3],
    [4,5,6],
    [7,8,9]],


[[11,12,13],
 [14,15,16],
 [17,18,19]]
])


print(tensor_2d.shape) 