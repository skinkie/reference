from dataclasses import dataclass, field
from typing import Optional
from netex.equipment_version_structure import EquipmentVersionStructure
from netex.type_of_service_feature_refs_rel_structure import TypeOfServiceFeatureRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LocalServiceVersionStructure(EquipmentVersionStructure):
    """
    Type for a LOCAL SERVICE.

    :ivar types_of_service_feature: Classification of FEATUREs.
    """
    class Meta:
        name = "LocalService_VersionStructure"

    types_of_service_feature: Optional[TypeOfServiceFeatureRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfServiceFeature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
