
import numpy as np
from processing import processImg
import tensorflow as tf

label_names = ['cat', 'dog']
model_path = "./my_model.h5"
cat_image_path = "microsoft-catsvsdogs-dataset/PetImages/Cat/10001.jpg"
dog_image_path = "microsoft-catsvsdogs-dataset/PetImages/Dog/1002.jpg"
model = tf.keras.models.load_model('./my_model.h5')

#model = XceptionModel(model_path)

transformed_image = processImg(dog_image_path)
predictions = model.predict(transformed_image)
predicted_class_index = np.argmax(predictions)
predicted_class_label = label_names[predicted_class_index]

print(f"The predicted class is: {predicted_class_label}")
