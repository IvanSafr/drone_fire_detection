import numpy as np
import cv2


# создаем пустую функцию
def nothing(args): pass


# создаем окно для отображения результата и бегунки
cv2.namedWindow("setup")
cv2.createTrackbar("b1", "setup", 0, 255, nothing)
cv2.createTrackbar("g1", "setup", 0, 255, nothing)
cv2.createTrackbar("r1", "setup", 0, 255, nothing)
cv2.createTrackbar("b2", "setup", 255, 255, nothing)
cv2.createTrackbar("g2", "setup", 255, 255, nothing)
cv2.createTrackbar("r2", "setup", 255, 255, nothing)
cv2.createTrackbar("blur", "setup", 0, 10, nothing)

fn = "detect/img/f5.jpg"  # путь к файлу с картинкой
img = cv2.imread(fn)  # загрузка изображения

while True:
    r1 = cv2.getTrackbarPos('r1', 'setup')
    g1 = cv2.getTrackbarPos('g1', 'setup')
    b1 = cv2.getTrackbarPos('b1', 'setup')
    r2 = cv2.getTrackbarPos('r2', 'setup')
    g2 = cv2.getTrackbarPos('g2', 'setup')
    b2 = cv2.getTrackbarPos('b2', 'setup')


    # собираем значения из бегунков в множества
    min_p = (g1, b1, r1)
    max_p = (g2, b2, r2)

    img_bl = cv2.medianBlur(img, 3)  # сглаживание изображения

    img_mask = cv2.inRange(img_bl, min_p, max_p)
    img_m = cv2.bitwise_and(img, img, mask=img_mask)
    cv2.imshow('img', img_m)


    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()



# import numpy as np
# import cv2
#
# def nothing(args):pass
# cv2.namedWindow("setup")
# cv2.namedWindow("setup2")
# cv2.createTrackbar("b1", "setup", 0, 255, nothing)
# cv2.createTrackbar("g1", "setup", 0, 255, nothing)
# cv2.createTrackbar("r1", "setup", 0, 255, nothing)
# cv2.createTrackbar("b2", "setup", 255, 255, nothing)
# cv2.createTrackbar("g2", "setup", 255, 255, nothing)
# cv2.createTrackbar("r2", "setup", 255, 255, nothing)
# cv2.createTrackbar("blur", "setup2", 0, 10, nothing)
# fn = "KOT.jpg" # путь к файлу с картинкой
# img = cv2.imread(fn) # загрузка изображения
#
# while True:
#    r1 = cv2.getTrackbarPos('r1', 'setup')
#    g1 = cv2.getTrackbarPos('g1', 'setup')
#    b1 = cv2.getTrackbarPos('b1', 'setup')
#    r2 = cv2.getTrackbarPos('r2', 'setup')
#    g2 = cv2.getTrackbarPos('g2', 'setup')
#    b2 = cv2.getTrackbarPos('b2', 'setup')
#    blur = cv2.getTrackbarPos('blur', 'setup2')
#    min_p = (g1,b1,r1)
#    max_p = (g2,b2,r2)
#    img_bl = cv2.medianBlur(img, 1+blur*2) # сглаживание изображения
#    img_mask = cv2.inRange(img_bl, min_p, max_p)
#    img_m = cv2.bitwise_and(img, img, mask = img_mask)
#    cv2.imshow('img', img_m)
#    if cv2.waitKey(33) & 0xFF == ord('q'):
#       break
# cv2.destroyAllWindows()