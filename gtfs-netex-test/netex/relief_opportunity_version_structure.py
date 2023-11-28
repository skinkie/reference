from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.block_ref import BlockRef
from netex.multilingual_string import MultilingualString
from netex.train_block_ref import TrainBlockRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ReliefOpportunityVersionStructure(DataManagedObjectStructure):
    """
    Type for RELIEF OPPORTUNITY.

    :ivar name: Name of RELIEF OPPORTUNITY.
    :ivar description: Description of RELIEF OPPORTUNITY.
    :ivar time: Time at which RELIEF OPPORTUNITY occurs.
    :ivar day_offset: Day offset of time from current OPERATING DAY.
    :ivar train_block_ref_or_block_ref:
    """
    class Meta:
        name = "ReliefOpportunity_VersionStructure"

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
    time: XmlTime = field(
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_block_ref_or_block_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainBlockRef",
                    "type": TrainBlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockRef",
                    "type": BlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
