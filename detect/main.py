# Логика обработки наличия пожара
from detector import fire_detect
import cv2

for i in range(0, 10):
    file_name = "img/f"+ str(i) +".jpg"

    img, fire_img, is_fire = fire_detect(file_name)

    cv2.imshow("result", img)
    cv2.imshow("pt", fire_img)

    if is_fire==True:
        print("огонь найден")

    cv2.waitKey(0)