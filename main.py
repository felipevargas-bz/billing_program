
class Product:

    def __init__(self, name, price):

        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("<Error> You must enter correct values")
        self._name = name
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        try:
            self._price = int(price)
        except:
            raise ValueError("<Error> You must enter correct values")

p_list = []
