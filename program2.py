class Animal:
    def move(self):
        print("This animal moves in its own way.")

class Dog(Animal):
    def move(self):
        print("🐶 The dog runs on four legs.")

class Bird(Animal):
    def move(self):
        print("🐦 The bird flies through the sky.")

class Fish(Animal):
    def move(self):
        print("🐟 The fish swims in water.")

# Test the polymorphism
animals = [Dog(), Bird(), Fish()]
for animal in animals:
    animal.move()
