from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MonthValidityOffsetVersionedStructure(DataManagedObjectStructure):
    """
    Type for MONTH VALIDITY OFFSET.

    :ivar month: Month for which offset applies.
    :ivar name: Name of MONTH VALIDITY OFFSET.
    :ivar day_offset: Number of days relative to start of month.
    """
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
        }
    )
    day_offset: int = field(
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
