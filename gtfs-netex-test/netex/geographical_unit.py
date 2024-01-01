from dataclasses import dataclass
from .geographical_unit_version_structure import (
    GeographicalUnitVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalUnit(GeographicalUnitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
