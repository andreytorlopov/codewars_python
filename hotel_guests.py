# массив содержит время прихода и ухода гостей
# необходимо найти максимальное количество гостей в отеле

# Пример:
# Входные данные:

from datetime import datetime

arr = [("08:00", "10:30"),
       ("09:15", "11:00"),
       ("10:00", "12:00"),
       ("14:00", "16:30"),
       ("15:00", "17:00")]

# Выходные данные:
# В отеле максимум 3 гостя, в промежуток с 10:00 до 11:00

parsed_arr = [(datetime.strptime(start, "%H:%M").time(), datetime.strptime(end, "%H:%M").time()) for start, end in arr]
# print(parsed_arr)
