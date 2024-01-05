import cv2, math

def cordinate_write(x, y, h):
    f = 1
    dis_s = 1
    n, m = 3840, 2160

    # Удаление от дрона до очага возгарания
    pos_charge = math.sqrt(
        # Гейская формула, выведенная под чам и тотальным недосыпом
        ((n/2-x)**2 + (m/2-y)**2)*dis_s*h/f*m*n
    )

    return pos_charge