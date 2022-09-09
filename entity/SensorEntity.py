from config.DBConfig import base
from sqlalchemy import Column, Integer, String

class SensorEntity(base):

    __tablename__ = "sensor_values"

    id = Column("ID", Integer, primary_key=True)
    humidity = Column("Humidity", String, nullable=False)
    brightness = Column("Brightness", String, nullable=False)
    warmth = Column("Warmth", String, nullable=False)
    phValue = Column("PH value", String, nullable=False)
    salinity = Column("Salinity", String, nullable=False)
    airTemperature = Column("Air temperature", String, nullable=False)

    def __repr__(self):
        return f"ID: {self.id}\n" \
               f"Humidity: {self.humidity}\n" \
               f"Brightness: {self.brightness}\n" \
               f"Warmth: {self.warmth}\n" \
               f"PH value: {self.phValue}\n" \
               f"Salinity: {self.salinity}\n" \
               f"Air temperature: {self.airTemperature}\n"