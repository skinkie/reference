from dataclasses import dataclass

from .medium_application_instance_versioned_child_structure import MediumApplicationInstanceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MediumApplicationInstance(MediumApplicationInstanceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
