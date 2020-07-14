from player import *
default_refresh = lambda x : None

class Section:
    def __init__(self, name, instrument, size, refresh=default_refresh):
        self.name = name

