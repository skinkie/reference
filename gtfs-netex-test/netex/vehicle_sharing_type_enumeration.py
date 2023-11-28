from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleSharingTypeEnumeration(Enum):
    """
    Allowed values for VehicleSharingModeOfOperation.
    """
    CAR_SHARING_CLUB = "carSharingClub"
    PEER_TO_PEER_CAR_SHARING = "peerToPeerCarSharing"
    VEHICLE_SHARING = "vehicleSharing"
