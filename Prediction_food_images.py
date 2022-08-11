from keras import utils
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import os
from keras.models import load_model
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


#creating a list of all the foods, in the argument i put the path to the folder that has all folders for food
def create_foodlist(path):
    list_ = list()
    for root, dirs, files in os.walk(path, topdown=False):
      for name in dirs:
        list_.append(name)
    return list_

#loading the model i trained and finetuned
my_model = load_model('model_trained.h5', compile = False)
food_list = create_foodlist("F:/건강관리를 위한 음식 이미지/Validation/[원천]음식001_Val")

#function to help in predicting classes of new images loaded from my computer(for now)
def predict_class(model, images, show = True):
  for img in images:
    img = utils.load_img(img, grayscale=False, color_mode='rgb', target_size=(299, 299))

    img = utils.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.

    pred = model.predict(img)
    index = np.argmax(pred)    #Returns the indices of the maximum values along an axis, In case of multiple occurrences of the maximum values, the indices corresponding to the first occurrence are returned.
    food_list.sort()
    pred_value = food_list[index]
    if show:
        plt.imshow(img[0])
        plt.axis('off')
        plt.title(pred_value)
        plt.show()

#add the images you want to predict into a list (these are in the WD)
images = []
#당근케이크
#images.append('A020157XX_10157.jpg')
#김치볶음밥
#images.append('B010407XX_11015.jpg')
#감자튀김
#images.append('B120303XX_00937.jpg')
#카프레제샐러드
#images.append('B140761XX_01243.jpg')

#Training 에 있던 사진으로....
#까르보나라
#images.append('B030702XX_31674.jpg')
#가지구이(맨첫번째)
#images.append('B080302XX_00001.jpg')

#
#훈제연어
#images.append('A270331XX_31180.jpg')
#티라미수
#images.append('A020144XX_05251.jpg')
#파전
#images.append('B090358XX_10053.jpg')
#감자볶음 (인터넷에서 이미지 가져옴, 트레이닝 갯수 적었던 항목)
#images.append('01b7eea72762a593a34298308fb6b8441.jpg')
#모둠회 (인터넷, 562개)
#images.append('img.jpg')
#라따뚜이
#images.append('2464F53B587AB99A0B.jfif')
#프레즐
#images.append('A020146XX_00109.jpg')
#양배추샐러드
#images.append('B140741XX_01119.jpg')
#시저샐러드
images.append('B140737XX_00187.jpg')

print("PREDICTIONS BASED ON PICTURES UPLOADED")
predict_class(my_model, images, True)

