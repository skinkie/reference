from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from netex.call_versioned_child_structure import CallVersionedChildStructure
from netex.driver_ref import DriverRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DatedCallVersionedChildStructure(CallVersionedChildStructure):
    """
    Data type for DATED CALL.

    :ivar driver_ref:
    :ivar arrival_date: Date of  departure.
    :ivar departure_date: Date of departure.
    """
    class Meta:
        name = "DatedCall_VersionedChildStructure"

    driver_ref: Optional[DriverRef] = field(
        default=None,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    arrival_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ArrivalDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departure_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
