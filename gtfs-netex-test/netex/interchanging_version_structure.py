from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.register_break_of_journey_enumeration import RegisterBreakOfJourneyEnumeration
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InterchangingVersionStructure(UsageParameterVersionStructure):
    """
    Type for INTERCHANGING.

    :ivar can_interchange: Whether an Jinterchange can be made.
    :ivar from_mode: Mode from which interchange is made.
    :ivar to_mode: Mode to which interchange is made.
    :ivar maximum_number_of_interchanges: Maximum number of  interhanges
        between SERVICE JOURNEYs that can be made in a single TRIP.
    :ivar maximum_time_to_make_atransfer: Whether fare for return trip
        is simply double the single fare.
    :ivar can_break_journey: Whether the Journey can be interrupted,
        i.e. leave stop point and return.
    :ivar cross_border: Whether interchanging crosses a border.
    :ivar register_break_of_journey: Whether the Journey can be
        interrupted, i.e. leave stop point and return. +v1.1
    """
    class Meta:
        name = "Interchanging_VersionStructure"

    can_interchange: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "FromMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "ToMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_interchanges: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfInterchanges",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_time_to_make_atransfer: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumTimeToMakeATransfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    can_break_journey: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanBreakJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cross_border: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrossBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    register_break_of_journey: Optional[RegisterBreakOfJourneyEnumeration] = field(
        default=None,
        metadata={
            "name": "RegisterBreakOfJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
