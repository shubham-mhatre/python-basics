class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
    def do_work(self):
        if self.occupation == "tennis player":
            print("plays tennies")
        elif self.occupation == "actor":
            print("shoots movies")

    def speaks(self):
        print(self.name,"says hi, how are you")

tom = Human("tom cruise","actor")
tom.do_work()
tom.speaks()

nadal = Human("rafa nadal","tennis player")
nadal.do_work()
nadal.speaks()