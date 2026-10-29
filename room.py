class Room:
    """
    This class will represent the indeviduall rooms that we will have to traverse during the game that are located
    beneath the D-building.
    
    Attributes:
        room_id (int): The unique ID fort the room.
        exits (dict): A dictionary mapping the cardinal directions ("N", "E", "S", "W") for the neighbouring Room objects, 
    """
    def __init__(self, room_id):
        """
        Initialize a new room with a unique ID.
        We will also declare that there will be exits and hazards that exists, however we will make the standard states
        for these to be empty so that we later can randomise them. 
        """
        pass