from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SelfDriveSubmodeEnumeration(Enum):
    """Values for SelfDrive MODEs of TRANSPORT: TPEG pti_table_12.

    :cvar UNKNOWN:
    :cvar UNDEFINED:
    :cvar HIRE_SCOOTER: Rental scooter (Small wheeled  low platform
        vehicles, - includes push scooters, electric scooters,
        skateboards,  Sedgeways, etc). +v1.2.2
    :cvar HIRE_CYCLE: Rental cycle  (Bicycle, tandem, tricycle, pedal or
        electric ; use SimpleVehicleType / VehicleCategory  to specify
        exact model. Includes pedal cycles, electric bikes, hybrids,
        etc). +v1.2.2
    :cvar HIRE_MOTORBIKE: Rental motorcycle (moped, velo, motorbike,
        quadbike, etc  ; use SimpleVehicleType / VehicleCategory  to
        specify exact model.
    :cvar HIRE_CAR: Rental car - Includes all sizes (Small, mini,
        medium, large, etc)
    :cvar HIRE_VAN: Rental van - Includes all categories of small to
        large minivan, minibus and transporter.
    :cvar OWN_SCOOTER: Own scooter (Small wheeled  low platform
        vehicles, - includes push scooters, electric scooters,
        skateboards,  Sedgeways, etc). +v1.2.2
    :cvar OWN_CYCLE: Own cycle (Bicycle, tandem, tricile, pedal or
        electric ; use SimpleVehicleType / VehicleCategory to specify
        exact model. Includes push scooters, electric scooters,
        skateboards,  Sedgeways, etc). +v1.2.2
    :cvar OWN_MOTORBIKE: Own motorcycle (moped, velo, motorbike,
        quadbike, etc  ; use SimpleVehicleType / VehicleCategory  to
        specify exact model.  +v1.2.2
    :cvar OWN_CAR: OWn car. Includes all sizes (Small, mini, medium,
        large, etc) +v1.2.2
    :cvar OWN_VAN: Own van - Includes all categories of small to large
        minivan, minibus and transporter.+v1.2.2
    :cvar ALL_HIRE_VEHICLES:
    :cvar ALL_VEHICLES:
    """
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    HIRE_SCOOTER = "hireScooter"
    HIRE_CYCLE = "hireCycle"
    HIRE_MOTORBIKE = "hireMotorbike"
    HIRE_CAR = "hireCar"
    HIRE_VAN = "hireVan"
    OWN_SCOOTER = "ownScooter"
    OWN_CYCLE = "ownCycle"
    OWN_MOTORBIKE = "ownMotorbike"
    OWN_CAR = "ownCar"
    OWN_VAN = "ownVan"
    ALL_HIRE_VEHICLES = "allHireVehicles"
    ALL_VEHICLES = "allVehicles"
