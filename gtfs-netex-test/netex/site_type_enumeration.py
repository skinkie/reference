from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SiteTypeEnumeration(Enum):
    SCHOOL = "school"
    UNIVERSITY = "university"
    WORKS = "works"
    OFFICE = "office"
    MILITARY_BASE = "militaryBase"
    RETAIL = "retail"
    TRANSPORT = "transport"
    SPORTS = "sports"
    GOVERNMENT = "government"
    CULTURAL_ATTRACTION = "culturalAttraction"
    OTHER = "other"
