from dataclasses import dataclass, field
from typing import Optional
from netex.step_limit_unit_enumeration import StepLimitUnitEnumeration
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StepLimitVersionStructure(UsageParameterVersionStructure):
    """
    Type for STEP LIMIT.

    :ivar restricted: Whether restricted to a number of stops.
    :ivar adjustment_units: Units in which steps atre counted.
    :ivar minimum_number_of_steps: Minimum number of steps allowed.
    :ivar maximum_number_of_steps: Miaxmum number of steps allowed.
    :ivar maximum_number_of_trips: Miaxmum number of Overall trips
        allowed.
    """
    class Meta:
        name = "StepLimit_VersionStructure"

    restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Restricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    adjustment_units: Optional[StepLimitUnitEnumeration] = field(
        default=None,
        metadata={
            "name": "AdjustmentUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_number_of_steps: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_steps: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_trips: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfTrips",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
