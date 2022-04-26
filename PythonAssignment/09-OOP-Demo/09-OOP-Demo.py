class Car:
    def __init__(self, name=""):
        self.name = name
    
    @property
    def model(self):
        print("Getting value...")
        return self._name
    
    @model.setter
    def model(self, value):
        print("Setting model name...")
        self._name = value


c = Car("Toyota")
print(c.name)