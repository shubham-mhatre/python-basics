
class Father:
    def gardening(self):
        print("i enjoy gardening")

    def skills(self):
        print("programming, playing football")

class Mother:
    def cooking(self):
        print("i love cooking")

    def skills(self):
        print("art, singing")

class Child(Father,Mother):
    def sport(self):
        print("i love sports")

    def skills(self):
        print("sports, Math")
        #Father.skills(self) #can call parent class method like this in child class

c=Child()
c.sport()
c.cooking() #calling father class method by child object
c.gardening() #calling mother class method by child object

#as method as same name in all three class
c.skills()
Father.skills(c) #using child object calling skills method of father
Mother.skills(c) #using child object calling skills method of mother