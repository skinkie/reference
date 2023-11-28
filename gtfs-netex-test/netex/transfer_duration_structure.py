from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransferDurationStructure:
    """
    Type for TRANSFER DURATION.

    :ivar default_duration: Default time needed for a traveller to make
        a TRANSFER.
    :ivar frequent_traveller_duration: Time for a traveller familiar
        with the journey to make transfer.
    :ivar occasional_traveller_duration: Time for an Occasional
        Traveller to make a TRANSFER.
    :ivar mobility_restricted_traveller_duration: Time for a Mobility
        Restricted traveller to make a TRANSFER.
    """
    default_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DefaultDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequent_traveller_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FrequentTravellerDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    occasional_traveller_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "OccasionalTravellerDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mobility_restricted_traveller_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MobilityRestrictedTravellerDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
