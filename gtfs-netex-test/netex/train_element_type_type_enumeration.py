from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TrainElementTypeTypeEnumeration(Enum):
    BUFFET_CAR = "buffetCar"
    CARRIAGE = "carriage"
    ENGINE = "engine"
    CAR_TRANSPORTER = "carTransporter"
    LARGE_VEHICLE_TRANSPORTER = "largeVehicleTransporter"
    SLEEPER_CARRIAGE = "sleeperCarriage"
    LUGGAGE_VAN = "luggageVan"
    RESTAURANT_CARRIAGE = "restaurantCarriage"
    OTHER = "other"
