from dataclasses import dataclass
from .standard_fare_table_version_structure import (
    StandardFareTableVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StandardFareTable(StandardFareTableVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
