# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')


# num = input('введите число от 1 до 7: ')
#
# if int(num) > 7 or int(num) < 1:
#     raise Exception("Введите дни недели от 1 до 7")
#
#
# inn = input('Введите ИНН: ')
#
# if len(inn) < 14:
#     raise Exception('ИНН должен быть 14')
#
#
# res = request.get('http://www.codify.com/', params={'inn': inn})

# days_of_week = {
#     '1': 'Mon',
#     '2': 'Tu',
#     '3': 'We',
#     '4': 'Th',
#     '5': 'Fr',
#     '6': 'Sa',
#     '7': 'Sun'
# }
#
# print(days_of_week[num])

import datetime


class PersonAgeException(Exception):
    def __init__(self, age, message=None):
        self.age = age
        self.message = message

    def __str__(self):
        if self.message:
            return self.message
        return f'Введенный Вами возраст {self.age} не соответствует реальному возрасту.' \
               f' {self.age} не должно быть меньше 0'


def get_birth_year(age):
    age = int(age)
    if age < 0:
        raise PersonAgeException(age)
    this_year = datetime.date.today()
    birth_year = this_year.year - age
    return birth_year


if __name__ == '__main__':
    errors = dict()
    while True:
        age = input('Введите ваш возраст: ')
        try:
            birth_year = get_birth_year(age)
        except PersonAgeException as e:
            errors['error'] = e
        except ValueError:
            print('Вводите числовые значения')
        else:
            print(birth_year)
            break
        finally:
            print(errors)
