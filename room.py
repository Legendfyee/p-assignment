class Room:
    """
    This class will represent the indeviduall rooms that we will have to traverse during the game that are located
    beneath the D-building.
    
    Attributes:
        room_id (int): The unique ID fort the room.
        exits (dict): A dictionary mapping the cardinal directions ("N", "E", "S", "W") for the neighbouring Room objects.
        hazards (str/None): The hazards that will arise in the different rooms such as "Hole", "Bats", "Wumpus" or None if the room is safe.
    """
    def __init__(self, room_id):
        """
        Initialize a new room with a unique ID.
        We will also declare that there will be exits and hazards that exists, however we will make the standard states
        for these to be empty so that we later can have the program change them.
        
        :param room_id: The unique number for the room (int)
        :return: (None) 
        """
        self.room_id = room_id
        self._exits = {}
        self.hazards = None
    def add_exit(self, direction, neighboring_room):
        """
        Connects the room to a neighboring room in a specific direction.
        
        :param direction: Cardinal directions ("N", "E", "S", "W") (str).
        
        """
        ...