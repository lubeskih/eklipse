# eklipse/server/models/models.py

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, DateTime, func, Boolean

BASE = declarative_base()


class SolarEclipse(BASE):
    __tablename__ = "solar-eclipses-data"

    id = Column(Integer, primary_key=True)
    date_created = Column(DateTime(timezone=False), server_default=func.now())
    date_modified = Column(DateTime(timezone=False), onupdate=func.now())

    date = Column(String(30))
    time = Column(String(30))
    saros = Column(String(30))
    geoArea = Column(String(30))
    location = Column(String(30))
    magnitude = Column(String(30))
    pathWidthKM = Column(String(30))
    pathWidthMI = Column(String(30))
    centralDuration = Column(String(30))
    solarEclipseType = Column(String(30))

    def serialize(self):
        # Used for serializing SQL objects to JSON format
        return {
            "date": self.date,
            "time": self.time,
            "saros": self.saros,
            "geoArea": self.geoArea,
            "location": self.location,
            "magnitude": self.magnitude,
            "pathWidthKM": self.pathWidthKM,
            "pathWidthMI": self.pathWidthMI,
            "centralDuration": self.centralDuration,
            "solarEclipseType": self.solarEclipseType,
        }
