from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TrainElementTypeEnumeration(Enum):
    """
    Allowed values for TYPE OF TRAIIN ELEMENT.
    """
    BUFFET_CAR = "buffetCar"
    CARRIAGE = "carriage"
    ENGINE = "engine"
    CAR_TRANSPORTER = "carTransporter"
    SLEEPER_CARRIAGE = "sleeperCarriage"
    LUGGAGE_VAN = "luggageVan"
    RESTAURANT_CARRIAGE = "restaurantCarriage"
    OTHER = "other"
