class Car:
    color = "white"

    def __init__(self,model,colour,year):
        self.model = model
        self.colour = colour
        self.year = year
    def show_info(self):
        print("model:", self.model)
        print("colour:", self.color)
        print("year:", self.year)
    def set_colour(self, newColor):
        self.colour = newColor
    def set_model(self, newmodel):
        self.model = newmodel
    def set_year(self, newyear):
        self.year = newyear

myCar = Car("lamba","red","2000")
myCar.color = "red"
myCar.show_info()

myCar2 = Car("audi","black","1980")
myCar2.color = "black"

myCar2.show_info()
