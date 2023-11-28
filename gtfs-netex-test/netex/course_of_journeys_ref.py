from dataclasses import dataclass
from netex.course_of_journeys_ref_structure import CourseOfJourneysRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CourseOfJourneysRef(CourseOfJourneysRefStructure):
    """
    Reference to a COURSE OF JOURNEYS  (Run).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
