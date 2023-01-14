""" Defines classes for Sofka Space Station Challenge"""

def get_values(ship):
    """ Recives ship, an instance of SpaceShip class.
        returns list with atributes of the instance"""
    values = [ship.name, ship.type, ship.country, ship.year, ship.active,
                ship.weight, ship.trust, ship.fuel, ship.function,
                ship.load_weight, ship.height, ship.power, ship.speed,
                ship.capacity, ship.orbit_height]
    return values

class SpaceShip:
    """A class to model basic atributes of all space ships"""
    def __init__(self, name:str):
        self.name = name
        self.weight = 0
        self.trust = 0
        self.country = ''
        self.fuel = ''
        self.year = 0
        self.active = ''
        self.type = ''
        self.function = '' # Specific purpouse

        # Shuttle Variables
        self.load_weight = 0
        self.height = 0
        self.power = 0

        # Not Tripulated Variables
        self.speed = 0

        # Tripulated Variables
        self.capacity = 0 # Number of tripulants 
        self.orbit_height = 0
    
    def __repr__(self) -> str:
        return f"{self.type}('{self.name}')"


class Shuttle(SpaceShip):
    """A class to model space shuttles"""
    def __init__(self, name: str):
        super().__init__(name)
        self.type = 'Shuttle'
        self.load_weight = 0
        self.height = 0
        self.power = 0
    
class NotTripulated(SpaceShip):
    """A class to model not tripulated ships e.g. satelites, probes"""
    def __init__(self, name: str):
        super().__init__(name)
        self.type = 'Not Tripulated'
        self.speed = 0

class Tripulated(SpaceShip):
    """A class to model tripulated ships"""
    def __init__(self, name: str):
        super().__init__(name)
        self.type = 'Tripulated'
        self.capacity = 0 # Number of tripulants 
        self.orbit_height = 0