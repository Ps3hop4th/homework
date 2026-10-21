# flags = {
#     'ru': {'red blue', 'white'},
#     'kg': {"red yellow", 'red'},
#     'ua': {"red blue", 'red', 'blue'},
#     'uk': {"yellow", "blue"},
#     'kz': {'blue yellow', 'blue'} ,
#     'jp': {'white', 'red'} ,
#     'fr': {'blue', 'white', 'red'} ,
#     'ca': {'red' , 'white'} ,
# }

# while True:
#     colors = input('Введите цвета: ').lower()
#     if colors == 'Выход' :
#         break

#     colors = colors.split()
#     for country in flags:
#         if all(color in flags[country] for color in colors) :
#             print(country)

# =============
#  задание 1
# =============

# data_tuple = ('h', 6.13, 'C', ['e', 'T'], True, 'k', 'e', '3', 'e', 1, ('g', 'x'), False)

# letters = []
# numbers = []

# for item in data_tuple:
#     if type(item) == list or type(item) == tuple:
#         for x in item:
#             if type(x) == str:
#                 letters.append(x)
#         else:
#             numbers.append(x)
#     else:
#         if type(item) == str:
#             letters.append(item)
#         else:
#             numbers.append(item)
    
#     print("letters:", letters)
#     print("numbers:", numbers)

# это страка 47 для теста гитхаба была использована