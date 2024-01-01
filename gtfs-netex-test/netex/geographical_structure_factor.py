from dataclasses import dataclass
from .geographical_structure_factor_version_structure import (
    GeographicalStructureFactorVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalStructureFactor(GeographicalStructureFactorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
