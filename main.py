#Classes are simply blueprints for objects, responsible for defining which fields (variables) and methods (functions) the objects are going to have.
class GameObject: #Values below are not needed since it's initialized in the init function
    name = "" #Fields of a Class. Properties
    appearance = "" 
    feel = ""
    smell = ""

#Special Function to use to setup the inital values of the Class GameObject
    def __init__(self, name, appearance, feel, smell): #Initializer | Function needs self parameters
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    def look(self):#Self is the object that is calling the function
        return f"You look at the {self.name}. {self.apperance}\n"

    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"

    def sniff(self):
        return f"You sniff the {self.name}. {self.smell}\n"

game_object = GameObject("Knife", "Some appearance", "Some Feel", "Some Smell")#Instance of the Class GameObject

print(game_object.name)

print(game_object.sniff())

class Room:
    escape_code = 0
    

