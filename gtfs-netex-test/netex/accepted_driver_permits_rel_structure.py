from dataclasses import dataclass, field
from typing import List, Optional

from .containment_aggregation_structure import ContainmentAggregationStructure
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .type_of_driver_permit_ref import TypeOfDriverPermitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AcceptedDriverPermitsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "acceptedDriverPermits_RelStructure"

    accepted_driver_permit: List["AcceptedDriverPermit"] = field(
        default_factory=list,
        metadata={
            "name": "AcceptedDriverPermit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class AcceptedDriverPermitVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "AcceptedDriverPermit_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_driver_permit_ref: Optional[TypeOfDriverPermitRef] = field(
        default=None,
        metadata={
            "name": "TypeOfDriverPermitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accepted_driver_permits: Optional[AcceptedDriverPermitsRelStructure] = field(
        default=None,
        metadata={
            "name": "acceptedDriverPermits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class AcceptedDriverPermit(AcceptedDriverPermitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
