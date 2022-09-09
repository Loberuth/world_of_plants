from entity.SensorEntity import SensorEntity

class SensorsDTO:

    def __init__(self):
        self.id = None
        self.humidity = None
        self.brightness = None
        self.warmth = None
        self.phValue = None
        self.salinity = None
        self.airTemperature = None

    @staticmethod
    def createFromEntity(entity: SensorEntity):
        sensorsDTO = SensorsDTO()
        sensorsDTO.id = entity.id
        sensorsDTO.humidity = entity.humidity
        sensorsDTO.brightness = entity.brightness
        sensorsDTO.warmth = entity.warmth
        sensorsDTO.phValue = entity.phValue
        sensorsDTO.salinity = entity.salinity
        sensorsDTO.airTemperature = entity.airTemperature