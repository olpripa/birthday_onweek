# Алгоритм програми
# 1 - на основі вхідного списку user_list
#   формую список list_bd - із словника з (name, та tuple(місяць народження, день народження,
#   який день тижня наступне день народження від поточної дати))
# 2 -

import datetime


list_to_great = [{1: "Monday", "users": []},
                 {2: "Tuesday", "users": []},
                 {3: "Wednesday", "users": []},
                 {4: "Thursday", "users": []},
                 {5: "Friday", "users": []}
                 ]


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


# допоміжна функція, повертає tuple (month, day, weekday)
def date_day(date):
    return date.month, date.day, date.isoweekday()


def get_birthdays_per_week(user):
    list_date = []
    list_bd = []

    # ПОТОЧНА ДАТА ЗГІДНО ЗАДАЧІ
    # datetime.date.today()

    # Тестова дата для мого словника
    date = datetime.datetime(year=2023, month=12, day=28)

    # формуємо список дат на тиждень вперед із поточної
    for i in range(1, 7):
        list_date.append(date + datetime.timedelta(days=i))
    # перетворю список дат на тиждень вперед в список кортежів необхідного формату
    date_on_week = list(map(date_day, list_date))
    # print(date_on_week)

    # Формуємо список коли наступне день народження від поточної дати в необхідному форматі згідно алгоритму
    for u_bd in user:
        m = u_bd.get("birthday").month
        d = u_bd.get("birthday").day
        if datetime.datetime(year=date.year, month=m, day=d) >= date:
            bd_future = datetime.datetime(year=date.year, month=m, day=d)
            # print(bd_future)
        else:
            bd_future = datetime.datetime(year=date.year+1, month=m, day=d)
            # print(bd_future)
        bd = (m, d, bd_future.isoweekday())
        # print(bd)
        list_bd.append({"name": u_bd.get("name"), "bd": bd})

    for d in list_bd:
        if d.get('bd') in date_on_week:
            if d.get('bd')[2] > 5:
                d_add = list_to_great[0].get("users")
                d_add.append(d.get("name"))
            else:
                d_add = list_to_great[d.get('bd')[2]].get("users")
                d_add.append(d.get("name"))
    # формуємо та виводимо список по дням у відповідному форматі
    i = 1
    for el in list_to_great:
        if len(el.get("users")) > 0:
            str_out = el.get(i) + ': ' + ", ".join(el.get('users'))
            print(str_out)
        i += 1


get_birthdays_per_week(user_list)
