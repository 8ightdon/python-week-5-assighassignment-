# Base Class
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.level = level

    def show_details(self):
        print(f"🦸 Name: {self.name}\n💥 Power: {self.power}\n⭐ Level: {self.level}")

    def attack(self):
        print(f"{self.name} attacks with {self.power}!")

# Derived Class with Polymorphism & Encapsulation
class FlyingHero(Superhero):
    def __init__(self, name, power, level, flight_speed):
        super().__init__(name, power, level)
        self.__flight_speed = flight_speed  # Encapsulated

    def fly(self):
        print(f"{self.name} is flying at {self.__flight_speed} km/h 🚀")

    # Overriding attack method (polymorphism)
    def attack(self):
        print(f"{self.name} performs an aerial strike with {self.power} 💨!")

# Test
hero1 = Superhero("Blaze", "Fire Blast", 5)
hero2 = FlyingHero("Skyhawk", "Wind Slash", 7, 300)

hero1.show_details()
hero1.attack()
print("-----")
hero2.show_details()
hero2.fly()
hero2.attack()
