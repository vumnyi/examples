class Temperature:

    def __init__(self, celsius):
        self._celsius = celsius
        self.cache = {}

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if self.cache is not None:
            self.cache = {}
            print('Cache cleared')
        self._celsius = value

    @property
    def kelvin(self):
        if 'kelvin' not in self.cache.keys():
            self.cache['kelvin'] = self.celsius - 273.15
            print('Cache saved')
        return self.cache['kelvin']

    @property
    def fahrenheit(self):
        if 'fahrenheit' not in self.cache.keys():
            self.cache['fahrenheit'] = self.celsius * 9 / 5 + 32
            print('Cache saved')
        return self.cache['fahrenheit']


t = Temperature(20)
print(t.kelvin)
"""
Cache saved
-253.14999999999998
"""
# when we call property kelvin second time we got cache value
print(t.kelvin)
"""
-253.14999999999998
"""
# when we set celsius we cleared cache with setter property
t.celsius = 30
"""
Cache cleared
"""
print(t.kelvin)
"""
Cache saved
-243.14999999999998
"""
