from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlPeriod

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MonthValidityOffsetVersionedStructure(DataManagedObjectStructure):
    class Meta:
        name = "MonthValidityOffset_VersionedStructure"

    month: XmlPeriod = field(
        metadata={
            "name": "Month",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_offset: int = field(
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
