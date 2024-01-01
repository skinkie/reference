from dataclasses import dataclass
from .flexible_service_properties_ref_structure import (
    FlexibleServicePropertiesRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleServicePropertiesRef(FlexibleServicePropertiesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
