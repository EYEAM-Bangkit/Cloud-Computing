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

    labels = {0: 'arctictis binturong', 1: 'Phascolarctos cinereus', 2: 'Lemur Catta', 3: 'Eulemur sanfordi', 4: 'Tarsius tumpara', 5:'Odobenus rosmarus'}

    result = labels[classi]
    return result
