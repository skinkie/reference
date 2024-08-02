from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class LinkContentEnumeration(Enum):
    TIMETABLE = "timetable"
    RELATED_SITE = "relatedSite"
    DETAILS = "details"
    ADVICE = "advice"
    OTHER = "other"
