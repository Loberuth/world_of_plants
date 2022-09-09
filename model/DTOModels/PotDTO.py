from entity.PotEntity import PotEntity

class PotDTO:

    def __init__(self):
        self.id = None
        self.potName = None
        self.plant = None
        self.status = None
        self.humidity = None
        self.brightness = None

    @staticmethod
    def createFromEntity(entity: PotEntity):
        potDto = PotDTO()
        potDto.id = entity.id
        potDto.potName = entity.potName
        potDto.plant = entity.plant
        potDto.status = entity.status
        potDto.humidity = entity.humidity
        potDto.brightness = entity.brightness

