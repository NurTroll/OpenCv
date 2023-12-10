import cv2
import numpy as np
from datetime import datetime

def open_file():
    while True:
        filename = input('Введите путь и имя файла: ')
        try:
            image = cv2.imread(filename)
            if image is None:
                raise FileNotFoundError('Фвйл не найден')
        except FileNotFoundError as error:
            print(error)
        else:
            return image


def resize_image(image):
    wide = 250
    f = float(wide) / image.shape[1]
    new_size = (wide, int(image.shape[0] * f))
    res = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
    return res


def crop_image(image):
    crop = image[120:350, 10:130]
    return crop


def rotate_image(image):
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    prepObj = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated = cv2.warpAffine(image, prepObj, (w, h))
    return rotated


def flip_image(image):
    flipped = cv2.flip(image, 1)
    return flipped


def blur_image(image):
    blurred_img = cv2.GaussianBlur(image, ksize=(11, 11), sigmaX=0, sigmaY=0)
    return blurred_img

def sharpen_image(image):
    matrix = [
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]
    sharp_filter = np.array(matrix)
    # параметр ddepth отвечает за «глубину» картинки
    sharpen_img = cv2.filter2D(image, ddepth=-1, kernel=sharp_filter)
    return sharpen_img


def show_image(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)
def save_file(image):
    path = input('Введите путь к файлу: ')
    file_name = input('Введите имя файла: ')
    # Получите текущую дату и время
    date = datetime.now()
    # Форматируйте дату и время в желаемый формат
    timestamp = date.strftime("%d.%m-%H.%M")
    cv2.imwrite(f'{path}{file_name}-{timestamp}.jpg', image)



print('Откройте первый файл')
image1 = open_file()

while True:
    print('1. Загрузить изображения\n2. Показать изображениеn\n3. Изменить изображение\n4. Сохранить изображения\n5. Выход')
    key_input = input('Выберите действие: ')
    if key_input == '1':
        image1 = open_file()
    if key_input == '2':
        show_image(image1)
    elif key_input == '3':
        print('1. Повернуть\n2. Обрезать\n3. Масштабировать\n4. Отзеркалить\n5. Размыть\n6. Увеличить резкость')
        key_input2 = input('Выберите операцию: ')
        if key_input2 == '1':
            image1 = crop_image(image1)
        elif key_input2 == '2':
            image1 = rotate_image(image1)
        elif key_input2 == '3':
            image1 = resize_image(image1)
        elif key_input2 == '4':
            image1 = flip_image(image1)
        elif key_input2 == '5':
            image1 = blur_image(image1)
        elif key_input2 == '6':
            image1 = sharpen_image(image1)
    if key_input == '4':
        save_file(image1)
    if key_input == '5':
        break



print('Спасибо что воспользовались нашей программой')
