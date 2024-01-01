from dataclasses import dataclass
from .medium_application_instance_versioned_child_structure import (
    MediumApplicationInstanceVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MediumApplicationInstance(
    MediumApplicationInstanceVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
