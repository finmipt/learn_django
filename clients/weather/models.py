class Weather:
    def __init__(self, temperature, wind_speed ,  pressure=None):
        self.temperature = temperature
        self.pressure = pressure
        self.wind_speed = wind_speed