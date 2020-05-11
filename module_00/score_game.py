import numpy as np


def predict_number_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1,101)  # Предполагаемое число
        if number == predict: 
            return(count)   # Выход из цикла, если угадали


def predict_number_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, 
       больше оно или меньше нужного. Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count += 1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count)   # Выход из цикла, если угадали


def score_game(predict_func):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []   # Список для сохранения числа попыток угадывания

    np.random.seed(1)   # Фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1))
    
    for number in random_array:
        count_ls.append(predict_func(number))   # Угадывание числа и сохранение количества попыток угадывания
    score = int(np.mean(count_ls)) 
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)


score_game(predict_number_v2)