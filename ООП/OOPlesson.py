print("========== ЗАДАНИЕ 1 и 2: Машина ==========")

class Car:
    def __init__(self, mark, engine_volume):
        self.mark = mark
        self.engine_volume = engine_volume
        self.mileage = 0

    def fuel_consumption(self):
        if self.engine_volume <= 1.8:
            return f"{self.mark} - экономичный расход"
        elif self.engine_volume < 3.0:
            return f"{self.mark} - средний расход"
        else:
            return f"{self.mark} - высокий расход"

    def drive(self, distance):
        self.mileage += distance
        print(f"Машина {self.mark} проехала {distance} км. Текущий пробег: {self.mileage} км.")

    def __str__(self):
        return f"Марка: {self.mark}, Объем двигателя: {self.engine_volume}, Пробег: {self.mileage} км."


car1 = Car("BMW", 2.5)

print(car1.fuel_consumption())
print(car1)

car1.drive(100)
car1.drive(50)

print(car1)


print("\n========== ЗАДАНИЕ 3: Телефон ==========")

class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery_level = 100

    def play_game(self, hours):
        self.battery_level -= hours * 15

        if self.battery_level <= 0:
            self.battery_level = 0
            print("Телефон разряжен!")
        else:
            print(f"Вы играли {hours} ч. Заряд батареи: {self.battery_level}%")

    def charge(self):
        self.battery_level = 100
        print("Телефон полностью заряжен!")


phone = Smartphone("Samsung", "S24")

phone.play_game(3)
phone.charge()


print("\n========== ЗАДАНИЕ 4: Водитель крутой ==========")

class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def start_trip(self, km):
        print(f"Водитель {self.name} заводит {self.car.mark} и отправляется в путь!")
        self.car.drive(km)


driver = Driver("Игорь", car1)

driver.start_trip(200)

print(car1)