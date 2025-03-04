from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_retail_device import TypeOfRetailDevice
from .type_of_retail_device_ref import TypeOfRetailDeviceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypesOfRetailDeviceRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfRetailDevice_RelStructure"

    type_of_retail_device_ref_or_type_of_retail_device: list[Union[TypeOfRetailDeviceRef, TypeOfRetailDevice]] = field(
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
        },
    )
