class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width
        
    # create a getter
    @property
    def height(self):
        print("Retrieving the height")
        return self.__height
    
    # create a setter
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for the height")
            
    @property
    def width(self):
        print("Retrieving the width")
        return self.__width
    
    # create a setter
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for the width")
    
    def get_area(self):
        return int(self.__width) * int(self.__height)
    
square = Square()
square.height = "10"
square.width = "10"
print("Square Area: ", square.get_area())







