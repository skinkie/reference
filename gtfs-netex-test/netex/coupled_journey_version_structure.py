from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.multilingual_string import MultilingualString
from netex.train_block_ref import TrainBlockRef
from netex.vehicle_journey_refs_rel_structure import VehicleJourneyRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CoupledJourneyVersionStructure(DataManagedObjectStructure):
    """
    Type for COUPLED JOURNEY.

    :ivar name: Name of COUPLED JOURNEY.
    :ivar description: Description of COUPLED JOURNEY.
    :ivar train_block_ref:
    :ivar journeys: VEHICLE JOURNEYs making up the COUPLED JOURNEY.
    """
    class Meta:
        name = "CoupledJourney_VersionStructure"

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
    train_block_ref: Optional[TrainBlockRef] = field(
        default=None,
        metadata={
            "name": "TrainBlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journeys: Optional[VehicleJourneyRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
