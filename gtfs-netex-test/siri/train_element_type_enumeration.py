from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TrainElementTypeEnumeration(Enum):
    BUFFET_CAR = "buffetCar"
    CARRIAGE = "carriage"
    ENGINE = "engine"
    CAR_TRANSPORTER = "carTransporter"
    SLEEPER_CARRIAGE = "sleeperCarriage"
    LUGGAGE_VAN = "luggageVan"
    RESTAURANT_CARRIAGE = "restaurantCarriage"
    OTHER = "other"
