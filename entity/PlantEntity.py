from config.DBConfig import base
from sqlalchemy import Column, Integer, String, BLOB

class PlantEntity(base):

    __tablename__ = "plants"

    id = Column("ID", Integer, primary_key=True)
    plant = Column("Plant", String, nullable=False)
    image = Column("Image", BLOB, nullable=False)
    humidity = Column("Humidity", String, nullable=False)
    brightness = Column("Brightness", String, nullable=False)
    warmth = Column("Warmth", String, nullable=False)
    substrates = Column("Substrates", String, nullable=False)

    def __repr__(self):
        return f"Plant ID: {self.id}\n" \
               f"Plant name: {self.plant}\n" \
               f"Plant Image: {self.image}\n" \
               f"Humidity: {self.humidity}\n" \
               f"Brightness: {self.brightness}\n" \
               f"Warmth: {self.warmth}\n" \
               f"Substrates: {self.substrates}\n"