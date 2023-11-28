from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.journey_headways_rel_structure import JourneyHeadwaysRelStructure
from netex.journey_layovers_rel_structure import JourneyLayoversRelStructure
from netex.journey_run_times_rel_structure import JourneyRunTimesRelStructure
from netex.journey_wait_times_rel_structure import JourneyWaitTimesRelStructure
from netex.multilingual_string import MultilingualString
from netex.presentation_structure import PresentationStructure
from netex.private_code import PrivateCode
from netex.type_of_time_demand_type_ref import TypeOfTimeDemandTypeRef
from netex.vehicle_type_preferences_rel_structure import VehicleTypePreferencesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeDemandTypeVersionStructure(DataManagedObjectStructure):
    """
    Type for TIME DEMAND TYPE.

    :ivar name: Name of TIME DEMAND TYPE.
    :ivar description: Description of TIME DEMAND TYPE.
    :ivar private_code:
    :ivar type_of_time_demand_type_ref:
    :ivar presentation: The presentation colours to use for this demand
        type.
    :ivar run_times: RUN TIMEs for TIME DEMAND TYPE.
    :ivar wait_times: WAIT TIMEs for TIME DEMAND TYPE.
    :ivar layovers: LAYOVERs for TIME DEMAND TYPE.
    :ivar headways: HEADWAYs for TIME DEMAND TYPE.
    :ivar vehicle_preferences: VWHICLE PREFERENCEs for TIME DEMAND TYPE.
    """
    class Meta:
        name = "TimeDemandType_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_time_demand_type_ref: Optional[TypeOfTimeDemandTypeRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    run_times: Optional[JourneyRunTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wait_times: Optional[JourneyWaitTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "waitTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    layovers: Optional[JourneyLayoversRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    headways: Optional[JourneyHeadwaysRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_preferences: Optional[VehicleTypePreferencesRelStructure] = field(
        default=None,
        metadata={
            "name": "vehiclePreferences",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
