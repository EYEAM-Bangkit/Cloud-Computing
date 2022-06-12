from keras.models import load_model
from keras.preprocessing import image
from numpy import expand_dims, vstack, argmax

model = load_model("./model/model_1.h5")

# classifier code and stuffs
def classify(data):
    img = data.resize((300,300))
    x = image.img_to_array(img)
    x = expand_dims(x, axis=0)
    x = x/255
    images = vstack([x])

    classi = argmax(model.predict(images, batch_size=10), axis=-1)[0]

    labels = {0: 'arctictis binturong', 1: 'Phascolarctos cinereus', 2: 'Eulemur sanfordi', 3: 'Tarsius tumpara', 4:'Odobenus rosmarus'}
    result = labels[classi]
    return result
