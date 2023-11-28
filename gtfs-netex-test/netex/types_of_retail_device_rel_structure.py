from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.type_of_retail_device import TypeOfRetailDevice
from netex.type_of_retail_device_ref import TypeOfRetailDeviceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypesOfRetailDeviceRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TYPE OF RETAIL DEVICEs.
    """
    class Meta:
        name = "typesOfRetailDevice_RelStructure"

    type_of_retail_device_ref_or_type_of_retail_device: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfRetailDeviceRef",
                    "type": TypeOfRetailDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfRetailDevice",
                    "type": TypeOfRetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
