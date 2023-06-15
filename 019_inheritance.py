class Animal:
    def __init__(self, name="unknown", weight=0):
        self.__name = name
        self.__weight = weight
        
    @property
    def name(self, name):
        self.__name = name
        
        def make_noise(self):
            return "Grrrr"
        
        def __str__(self):
            return "{} is a {} and says {}".format(self.__name, type(self).__weight, self.make_noise())

        def __gt_(self, animal2):
            if self.__weight > animal2.__weight:
                return True
            else: return False
        
        ''' other magic methods 
            __eq__ : equal
            __ne__ : not equal
            __lt__ : less than
            __le__ : less than or equal
            __gt__ : greater than
            __ge__ : greater than or equal
            __add__ : add
            __sub__ : subtract
            __mul__ : multiply
            __div__ : divide
            __floordiv__ : floor division
            __mod__ : modulo
            __pow__ : power
            __lshift__ : left shift
            __rshift__ : right shift
            __and__ : and
            __xor__ : xor
            __or__ : or
        '''
        
# create a class that will inherit from Animal
class Dog(Animal):
    def __init__(self, name="unknown", owner="unknown", weight=0):
        # initialize
        Animal.__init__(self, name, weight)
        self.__owner = owner
        
    def __str__(self):
        # call super, call Animal version of the function
        return super().__str__() + " and is owned by" + self.__owner

animal = Animal("Fido", 100)
print(animal)
dog = Dog("Fido", "John", 100)
print(dog)
