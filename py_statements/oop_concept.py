class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    # extending classes
class JackRussell(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
    
# main entry point
if __name__ == "__main__":
    miles = JackRussell("Miles", 4, "chiwawa")
    print (miles.speak())