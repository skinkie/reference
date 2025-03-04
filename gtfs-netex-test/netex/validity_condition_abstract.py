from dataclasses import dataclass

from .entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ValidityConditionAbstract(DataManagedObjectStructure):
    class Meta:
        name = "ValidityCondition_"
        namespace = "http://www.netex.org.uk/netex"
