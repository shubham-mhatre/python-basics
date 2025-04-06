
class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg

    def handle_exception(self):
        print("user defined/custom exception ",self.msg)

try:
    raise Accident("crash between two cars")
except Accident as e:
    e.handle_exception()