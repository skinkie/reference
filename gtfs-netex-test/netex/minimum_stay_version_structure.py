from dataclasses import dataclass, field
from typing import List, Optional
from netex.day_of_week_enumeration import DayOfWeekEnumeration
from netex.minimum_stay_type_enumeration import MinimumStayTypeEnumeration
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MinimumStayVersionStructure(UsageParameterVersionStructure):
    """
    Type for MINIMUM STAY.

    :ivar minimum_stay_type: Nature of minimum stay  requirement.
    :ivar requires_nights_away: Days of Week that must be away.
    :ivar minimum_number_of_nights_away: Minimum number of nighst away
        that must be spent.
    :ivar maximum_number_of_nights_away: Minimum number of nighst that
        can be spent away on trip.
    """
    class Meta:
        name = "MinimumStay_VersionStructure"

    minimum_stay_type: Optional[MinimumStayTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "MinimumStayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requires_nights_away: List[DayOfWeekEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RequiresNightsAway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    minimum_number_of_nights_away: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfNightsAway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_nights_away: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfNightsAway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
