from dataclasses import dataclass
from .medium_application_instance_ref_structure import (
    MediumApplicationInstanceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MediumApplicationInstanceRef(MediumApplicationInstanceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
