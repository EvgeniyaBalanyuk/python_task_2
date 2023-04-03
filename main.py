if __name__ == '__main__':

# Task1
    region = input('Введите ваш регион: ')
    child = int(input('Введите сколько у вас детей: '))
    salary = input('В каком банке получаете зарплату: ')
    insurance = input('Согласие на оформление страхования в зарплатном банке: ')  # Базовая ставка - 10%

    if region == 'Дальний Восток':
        print('Ставка по ипотеке - 2%')
    if region == 'Москва' and child > 3 and salary == 'ПСБ' and insurance == 'Да':
        print('Процентная ставка: 7%')
    if region == 'Москва' and child > 3 and salary == 'ПСБ' and insurance == 'Нет':
        print('Процентная ставка: 8.5%')
    if region == 'Москва' and child < 3 and salary == 'ПСБ' and insurance == 'Да':
        print('Процентная ставка: 8%')
    if region == 'Москва' and child < 3 and salary == 'ПСБ' and insurance == 'Нет':
        print('Процентная ставка: 9.5%')
    if region == 'Москва' and child < 3 and salary == 'Сбер' and insurance == 'Нет':
        print('Процентная ставка: 10%')
    if region == 'Москва' and child > 3 and salary == 'Сбер' and insurance == 'Нет':
        print('Процентная ставка: 9%')




# Task2
    month = input('Введите месяц: ')
    day = int(input('Введите число: '))
    if (month == 'Март' and 21 <= day <= 31) or (month == 'Апрель' and 1 <= day <= 19):
        print('Овен')
    elif (month == 'Апрель' and 20 <= day <= 30) or (month == 'Май' and 1 <= day <= 20):
        print('Телец')
    elif (month == 'Май' and 21 <= day <= 31) or (month == 'Июнь' and 1 <= day <= 20):
        print('Близнецы')
    elif (month == 'Июнь' and 21 <= day <= 30) or (month == 'Июль' and 1 <= day <= 22):
        print('Рак')
    elif (month == 'Июль' and 23 <= day <= 31) or (month == 'Август' and 1 <= day <= 22):
        print('Лев')
    elif (month == 'Август' and 23 <= day <= 31) or (month == 'Сентябрь' and 1 <= day <= 22):
        print('Дева')
    elif (month == 'Сентябрь' and 23 <= day <= 30) or (month == 'Октябрь' and 1 <= day <= 22):
        print('Весы')
    elif (month == 'Октябрь' and 23 <= day <= 31) or (month == 'Ноябрь' and 1 <= day <= 21):
        print('Скорпион')
    elif (month == 'Ноябрь' and 22 <= day <= 30) or (month == 'Декабрь' and 1 <= day <= 21):
        print('Стрелец')
    elif (month == 'Декабрь' and 22 <= day <= 31) or (month == 'Январь' and 1 <= day <= 19):
        print('Козерог')
    elif (month == 'Январь' and 20 <= day <= 30) or (month == 'Февраль' and 1 <= day <= 18):
        print('Водолей')
    elif (month == 'Февраля' and 19 <= day <= 28) or (month == 'Март' and 1 <= day <= 20):
        print('Рыбы')
    else:
        print('Ввели некорректные данные')













