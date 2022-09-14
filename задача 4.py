class Car:
    def __init__(self,maxprice):
        self.__maxprice=maxprice
        print(self.__maxprice)
    def new_maxprice(self,maxprice):
        self.__maxprice=maxprice
    def print(self):
        print(self.__maxprice)

mob=Car(1000)
mob.new_maxprice(1500)
mob.print()
