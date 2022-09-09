from entity.PlantEntity import PlantEntity

class PlantDTO:

    def __init__(self):

        self.id = None
        self.plant = None
        self.image = None
        self.humidity = None
        self.brightness = None
        self.warmth = None
        self.substrates = None

    @staticmethod
    def createFromEntity(entity: PlantEntity):
        plantDTO = PlantDTO()
        plantDTO.id = entity.id
        plantDTO.plant = entity.plant
        plantDTO.image = entity.image
        plantDTO.humidity = entity.humidity
        plantDTO.brightness = entity.brightness
        plantDTO.warmth = entity.warmth
        plantDTO.substrates = entity.substrates

    def __repr__(self):
        return str(self.__dict__)