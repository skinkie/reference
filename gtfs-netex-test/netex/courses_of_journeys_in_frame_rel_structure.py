from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.course_of_journeys import CourseOfJourneys

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CoursesOfJourneysInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of COURSE OF JOURNEYs.
    """
    class Meta:
        name = "coursesOfJourneysInFrame_RelStructure"

    course_of_journeys: List[CourseOfJourneys] = field(
        default_factory=list,
        metadata={
            "name": "CourseOfJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
