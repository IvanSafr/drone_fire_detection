import cv2
import numpy as np
import imutils

# img = np.zeros((photo.shape[0], photo.shape[1]), dtype='uint8')
#
# circle = cv2.circle(img.copy(), (500, 300), 100, (255, 255, 255), -1)
#
# sq = cv2.rectangle(img.copy(), (25, 25), (350, 380), 255, 3)
#hsv = cv2.cvtColor(photo, cv2.COLOR_BGR2HSV )


def fire_detect(img_name):
    IS_FIRE = False

    img = cv2.imread(img_name)
    img = cv2.resize(img, (900, 900))

    # hsv_min_smoke = np.array((90, 0, 49), np.uint8)
    # hsv_max_smoke = np.array((172, 153, 180), np.uint8)

    # Параметры поиска огня
    hsv_min_fire = np.array((0, 123, 205), np.uint8)
    hsv_max_fire = np.array((88, 255, 255), np.uint8)

    fire = cv2.inRange(img, hsv_min_fire, hsv_max_fire)


    # smoke = cv2.inRange(img, hsv_min_smoke, hsv_max_smoke)
    # mask = cv2.bitwise_or(fire, smoke)
    # img_f = cv2.bitwise_and(img, img, mask=mask)

    kernal = np.ones((5, 5), np.uint8)
    fire_pr = cv2.dilate(fire, kernal, iterations=3)


    # Переводим в массив точек
    img3 = fire_pr.astype(np.uint8)

    # ищем контуры
    cnts = cv2.findContours(img3.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    if len(cnts) > 0:
        IS_FIRE = True

        print("[INFO] {} the source of the fire detected".format(len(cnts)))

        # Рисуем клятые квадратики
        for j in cnts:
            rect = cv2.boundingRect(j)
            x, y, w, h = rect
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

    # Любимый ретурнчик
    return img, fire, IS_FIRE
  
