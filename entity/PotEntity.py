from config.DBConfig import base
from sqlalchemy import Column, String, Integer

class PotEntity(base):

    __tablename__ = "pots"

    id = Column("ID", Integer, primary_key=True)
    potName = Column("Place", String)
    plant = Column("Plant", String)
    status = Column("Status", String)
    humidity = Column("Humidity", String)
    brightness = Column("Brightness", String)

    def __repr__(self):
        return f"Pot ID: {self.id}\n" \
               f"Pot name: {self.potName}\n" \
               f"Plant: {self.plant}\n" \
               f"Status: {self.status}\n" \
               f"Humidity: {self.humidity}\n" \
               f"Brightness: {self.brightness}\n"