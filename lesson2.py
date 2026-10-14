#login = "admin"
#password = "12345"

#attempts = 3

#while attempts > 0:
 #   user_login = input("Введите логин: ")
   # user_password = input("Введите пароль: ")

 #   if user_login == login and user_password == password:
    #    print("Добро пожаловать!")
 #       break
  #  else:
   #     attempts -= 1
    #    print("Неверный логин или пароль")
        
      #  if attempts > 0:
     #       print("Осталось попыток:", attempts)
    #    else:
         #   print("Аккаунт заблокирован")
         
         #===================
         #решение с магазином
        # ====================
        
        
#money = 1000
#spent = 0

#while True:
#    print("\n1 — Купить хлеб")
#    print("2 — Купить молоко")
  #  print("3 — Купить шоколад")
   # print("4 — Показать остаток денег")
 #   print("0 — Выйти")

    #choice = input("Выберите действие: ")

    #if choice == "1":
     #   if money >= 50:
      #      money -= 50
         #   spent += 50
           # print("Хлеб куплен")
     #   else:
            #print("Недостаточно денег")

   # elif choice == "2":
       # if money >= 80:
          #  money -= 80
            #spent += 80
            #print("Молоко куплено")
      #  else:
          #  print("Недостаточно денег")

   # elif choice == "3":
      #  if money >= 150:
        #    money -= 150
        #    spent += 150
          #  print("Шоколад куплен")
     #   else:
         #   print("Недостаточно денег")

 #   elif choice == "4":
     #   print("Осталось денег:", money)

  #  elif choice == "0":
     #   print("Вы потратили:", spent)
      #  print("Осталось:", money)
       # break

   # else:
       # print("Неверный выбор")
       
       
       #==================
       #решение с игрой
       #==================
       
#import random

#secret = random.randint(1, 100)
#attempts = 7

#while attempts > 0:
  #  number = int(input("Угадайте число от 1 до 100: "))

    #if number < secret:
   #     print("Загаданное число больше")
  #  elif number > secret:
   #     print("Загаданное число меньше")
#    else:
   #     print("Вы победили!")
    #    break

  #  attempts -= 1
  #  print("Осталось попыток:", attempts)

#if attempts == 0:
  #  print("Вы проиграли.")
 #   print("Загаданное число:", secret)