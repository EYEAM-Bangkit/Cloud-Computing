from keras.models import load_model
from keras.preprocessing import image
from numpy import expand_dims, vstack, argmax

model = load_model("./models/model_1.h5")

# classifier code and stuffs
def classify(data):
    img = data.resize((300,300))
    x = image.img_to_array(img)
    x = expand_dims(x, axis=0)
    images = vstack([x])

    classi = argmax(model.predict(images, batch_size=10), axis=-1)[0]

    labels = {0: 'Binturong', 1: 'Koala', 2: 'Lemur', 3: 'Tarsier', 4:'Walrus'}
    result = labels[classi]
    return result
