from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class PredictabilityEnumeration(Enum):
    PLANNED = "planned"
    UNPLANNED = "unplanned"
    ALL = "all"
