# def summa(a,b):
#      return f'{a}+{b}+{a+b}'

# result = summa(a=1, b=2)
# print(result)




# def result_temperature_kg(*args):
#     return f'Ср значение температуры в Кыргызстане на сегодня {sum(args)/len(args)}'

# result = result_temperature_kg(float(input('Введите температуру ИК: ')),
#                                   (float(input('Введите температуру Чуй: ')),
#                                    (float(input('Введите температуру Ош: ')),
#                                     )))

# print(result)



univer=[]
technikum=[]
army=[]
married=[]

abiturients = [
        {'name' :'Igor', 'ОРТ':110, 'gender': 'male'},
        {'name' :'Aelita', 'ОРТ':120, 'gender': 'female'},
        {'name' :'Igor', 'ОРТ':110, 'gender': 'male'},
        {'name' :'Akylai', 'ОРТ':40, 'gender': 'female'},
        {'name' :'Ivan', 'ОРТ':50, 'gender': 'male'},
        {'name' :'Ainazik', 'ОРТ':30, 'gender': 'female'},
        {'name' :'Ruslan', 'ОРТ':70, 'gender': 'male'},
        {'name' :'Igor', 'ОРТ':110, 'gender': 'male'},
        {'name' :'Abbas', 'ОРТ':80, 'gender': 'male'},
]

def all_abit(lst):
    for i in lst :
        for k,v in i.items():
            print(f'{k}-{v}')
all_abit(lst=abiturients)