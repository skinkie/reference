from dataclasses import dataclass, field
from typing import Optional, Union

from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .journey_layover_structure import JourneyLayoverStructure
from .journey_pattern_ref import JourneyPatternRef
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class JourneyPatternLayoverStructure(JourneyLayoverStructure):
    journey_pattern_ref: Optional[Union[ServiceJourneyPatternRef, ServicePatternRef, DeadRunJourneyPatternRef, JourneyPatternRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
