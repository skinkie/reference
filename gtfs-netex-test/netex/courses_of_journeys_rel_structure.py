from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.course_of_journeys import CourseOfJourneys
from netex.course_of_journeys_ref import CourseOfJourneysRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CoursesOfJourneysRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of COURSE OF JOURNEYs.
    """
    class Meta:
        name = "coursesOfJourneys_RelStructure"

    course_of_journeys_ref_or_course_of_journeys: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CourseOfJourneysRef",
                    "type": CourseOfJourneysRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CourseOfJourneys",
                    "type": CourseOfJourneys,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
