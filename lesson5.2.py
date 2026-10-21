# Переменные для хранения одной задачи
task_id = 0
title = ""
description = ""
status = "нет задачи"

while True:
    print("\n--- МЕНЕДЖЕР ЗАДАЧ ---")
    print("1. Создать задачу (Create)")
    print("2. Посмотреть задачу (Read)")
    print("3. Изменить статус (Update)")
    print("4. Удалить задачу (Delete)")
    print("5. Выйти")

    choice = input("\nВыберите пункт меню: ")

    # 1. CREATE
    if choice == "1":
        task_id = 1
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        status = "новая"
        print("Задача успешно создана!")

    # 2. READ 
    elif choice == "2":
        if task_id == 0:
            print("\nСписок задач пуст.")
        else:
            print("\n--- ВАША ЗАДАЧА ---")
            print("ID:", task_id)
            print("Название:", title)
            print("Описание:", description)
            print("Статус:", status)

    # 3. UPDATE 
    elif choice == "3":
        if task_id == 0:
            print("\nНет задач для изменения.")
        else:
            print("\nТекущий статус:", status)
            print("Выберите новый статус:")
            print("1. В процессе")
            print("2. Выполнена")

            try:
                status_choice = float(input("Введите номер статуса: "))

                if status_choice == 1:
                    status = "в процессе"
                    print("Статус изменен на 'в процессе'.")
                elif status_choice == 2:
                    status = "выполнена"
                    print("Статус изменен на 'выполнена'.")
                else:
                    print("Такого варианта нет.")
            except:
                print("Ошибка! Нужно ввести число.")

    # 4. DELETE 
    elif choice == "4":
        if task_id == 0:
            print("\nУдалять нечего.")
        else:
            task_id = 0
            title = ""
            description = ""
            status = "нет задачи"
            print("Задача удалена!")

    # 5. ВЫХОД
    elif choice == "5":
        print("До свидания!")
        break

    else:
        print("Неверный выбор, попробуйте снова.")