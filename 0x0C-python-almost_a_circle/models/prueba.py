#!/usr/bin/python3
class riot:
    def __init__(self, hour):
        self.hour = hour
    maria = 92
    Ruan = 73
    Philips = 63
    def hour(self, value):
        self.__hour = value
    def kguar(self, **kwargs):
        for a in kwargs:
            print (a, kwargs[a])


   # def argu(self, *args):
    #    Philips = args[1]
     #   self.hour = args[3]
      #  return args

Bouth = riot(79)
print(Bouth.__name__)
#print(Bouth.hour)
#Bouth.kguar(a=1, b=2, c=3)
#Bouth.hour = 97
#print(Bouth.hour)
#print(Bouth.argu(2, 3))
#print(Bouth.Philips)
#print(Bouth.hour)



#print(Bouth.__dict__)

#Zone = riot(input("Put the holly hour: "))
#print(Zone._riot__hour)
#Zone._riot__hour = 32
#print(Zone._riot__hour)
#Zone.Twi()
#print(Zone._riot__hour)




#Zone.Twi()
#riot.Twi()
#print("Interio de Class: \n: ", riot.__dict__)
#print("Interior de Object: \n", Zone.__dict__)
#print(Zone._riot__hour)
