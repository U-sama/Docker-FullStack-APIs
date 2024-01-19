# import tensorflow as tf
# from keras import layers
# from keras.applications import Xception



# class XceptionModel():
#     def __init__(self, modelPath, images_size=200):
#         Working_model = Xception(weights='imagenet', include_top=False, input_shape=(images_size, images_size, 3))
#         # Freeze the layers of the base model
#         for layer in Working_model.layers:
#             layer.trainable = False
#         model = tf.keras.models.Sequential([
#             Working_model,

#             layers.Flatten(),

#             layers.Dense(256,activation='relu'),
#             layers.Dropout(0.5),
#             layers.Dense(2,activation='softmax'),
#         ])
#         model = model(modelPath)
#         return model