class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(make_sound(dog))  # Woof!
print(make_sound(cat))  # Meow!
