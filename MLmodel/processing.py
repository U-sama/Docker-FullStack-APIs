from keras.preprocessing import image
import numpy as np

# Path to your single image

def processImg(image_path, images_size=200):
    # Load the image and resize it to match the target size
    img = image.load_img(image_path, target_size=(images_size, images_size))
    img_array = image.img_to_array(img)

    # Expand dimensions to match batch size (1 in this case)
    img_array = np.expand_dims(img_array, axis=0)

    # Rescale pixel values to [0, 1]
    img_array /= 255.0
    return img_array