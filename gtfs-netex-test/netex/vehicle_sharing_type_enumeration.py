from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleSharingTypeEnumeration(Enum):
    CAR_SHARING_CLUB = "carSharingClub"
    PEER_TO_PEER_CAR_SHARING = "peerToPeerCarSharing"
    VEHICLE_SHARING = "vehicleSharing"
