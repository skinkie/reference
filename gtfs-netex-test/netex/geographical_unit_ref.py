from dataclasses import dataclass
from .geographical_unit_ref_structure import GeographicalUnitRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalUnitRef(GeographicalUnitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
