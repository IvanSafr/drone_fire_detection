import cv2, math

def degreesToRadians(degrees):
  return degrees * math.pi / 180;


def calculate_gps_coordinate(initial_latitude, initial_longitude, direction, m):
    # конвертируем градусы в радианы
    lat_rad = math.radians(initial_latitude)
    lon_rad = math.radians(initial_longitude)

    radius = 6378.1 * 1000 # радиус Земли в километрах * метры

    # определяем направление
    if direction.lower() == 0:
        lat_rad += m / (radius)
    elif direction.lower() == 1:
        lat_rad -= m / (radius)
    elif direction.lower() == 2:
        lon_rad += m / (radius * math.cos(lat_rad))
    elif direction.lower() == 3:
        lon_rad -= m / (radius * math.cos(lat_rad))
    else:
        print("Некорректное направление!")
        return

    # конвертируем обратно в градусы
    end_val =(math.degrees(lat_rad), math.degrees(lon_rad))

    return end_val


def cordinate_write(x, y, h):
    f = 1
    dis_s = 1
    n, m = 3840, 2160

    # Удаление от дрона до очага возгарания
    pos_charge = math.sqrt(
        # Гейская формула, выведенная под чаем и тотальным недосыпом
        ((n/2-x)**2 + (m/2-y)**2)*dis_s*h/f*m*n
    )

    return pos_charge
