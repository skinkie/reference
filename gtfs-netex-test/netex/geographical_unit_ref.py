from dataclasses import dataclass

from .geographical_unit_ref_structure import GeographicalUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GeographicalUnitRef(GeographicalUnitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
