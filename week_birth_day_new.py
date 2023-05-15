import datetime

# для зручності перетворемо на словник
list_to_great = {
    0: {"day": "Monday", "users": []},
    1: {"day": "Tuesday", "users": []},
    2: {"day": "Wednesday", "users": []},
    3: {"day": "Thursday", "users": []},
    4: {"day": "Friday", "users": []}
}


user_list = [{"name": "Oleksandr Pripa", "birthday": datetime.datetime(1979, 1, 3)},
             {"name": "Anastasia Pripa",
                 "birthday": datetime.datetime(2005, 3, 18)},
             {"name": "Anna Pripa", "birthday": datetime.datetime(2007, 8, 6)},
             {"name": "Yurii Pripa",
                 "birthday": datetime.datetime(2009, 5, 6)},
             {"name": "Nikita Pripa",
                 "birthday": datetime.datetime(2014, 11, 30)},
             {"name": "Evgenia", "birthday": datetime.datetime(1959, 5, 11)},
             {"name": "Natalia", "birthday": datetime.datetime(1981, 9, 11)},
             {"name": "Vasilii", "birthday": datetime.datetime(1958, 2, 23)},
             {"name": "Lyudmila", "birthday": datetime.datetime(1955, 5, 7)},
             {"name": "Yurko", "birthday": datetime.datetime(2010, 5, 9)}
             ]


def get_birthdays_per_week(user):

    # ПОТОЧНА ДАТА ЗГІДНО ЗАДАЧІ
    # datetime.date.today()

    # Тестова дата для мого словника
    date = datetime.datetime(year=2023, month=12, day=28)

    for u_bd in user:
        # як на мене краще вироховувати розбіжність між датами
        birthday: datetime.datetime = u_bd['birthday'].replace(year=date.year)
        days = (birthday-date).days

        # далі ми перевіримо на входженя у необхідний інтервал
        # якщо входить
        
        # ми вирахуємо на який день тиждня припадає
        weekday = birthday.weekday()
        # додаємо до словника, також потрібно врахувати суботу та неділю та додати до понеділка
        if weekday in [5, 6]:
            weekday = 0
        list_to_great[weekday]['users'].append(u_bd['name'])

    # відображення
    # застосуємо рoзпоковку значень словника
    # значеня ключа ми можемо не враховувати
    for _, value in list_to_great.items():
        print(value['day'], value['users'])


get_birthdays_per_week(user_list)
