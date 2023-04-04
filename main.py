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
