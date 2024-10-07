a = int(input("Введите число от 1 до 12: "))
b = input("ru or en? ")
def month(a, b):
    if b == "en":
        if a == 1:
            result = "January"
        elif a == 2:
            result = "February"
        elif a == 3:
            result = "March"
        elif a == 4:
            result = "April"
        elif a == 5:
            result = "May"
        elif a == 6:
            result = "June"
        elif a == 7:
            result = "July"
        elif a == 8:
            result = "August"
        elif a == 9:
            result = "September"
        elif a == 10:
            result = "October"
        elif a == 11:
            result = "November"
        elif a == 12:
            result = "December"
    elif b == "ru":
        if a == 1:
            result = "Январь"
        elif a == 2:
            result = "Февраль"
        elif a == 3:
            result = "Март"
        elif a == 4:
            result = "Апрель"
        elif a == 5:
            result = "Май"
        elif a == 6:
            result = "Июнь"
        elif a == 7:
            result = "Июль"
        elif a == 8:
            result = "Август"
        elif a == 9:
            result = "Сентябрь"
        elif a == 10:
            result = "Октябрь"
        elif a == 11:
            result = "Ноябрь"
        elif a == 12:
            result = "Декабрь"
    print(f'{result}')
month(a, b)