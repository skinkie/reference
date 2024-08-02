from dataclasses import dataclass, field
from typing import List, Optional

from .affects_scope_structure import AffectsScopeStructure
from .blocking_structure import BlockingStructure
from .boarding_structure import BoardingStructure
from .casualties_structure import CasualtiesStructure
from .condition import Condition
from .delays_structure import DelaysStructure
from .easements_structure import EasementsStructure
from .extensions_1 import Extensions1
from .half_open_timestamp_output_range_structure import HalfOpenTimestampOutputRangeStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .pt_advice_structure import PtAdviceStructure
from .severity_enumeration import SeverityEnumeration
from .suitability_structure import SuitabilityStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PtConsequenceStructure:
    period: List[HalfOpenTimestampOutputRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    condition: List[Condition] = field(
        default_factory=list,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    condition_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConditionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    severity: Optional[SeverityEnumeration] = field(
        default=None,
        metadata={
            "name": "Severity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affects: Optional[AffectsScopeStructure] = field(
        default=None,
        metadata={
            "name": "Affects",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    suitabilities: Optional["PtConsequenceStructure.Suitabilities"] = field(
        default=None,
        metadata={
            "name": "Suitabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advice: Optional[PtAdviceStructure] = field(
        default=None,
        metadata={
            "name": "Advice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    blocking: Optional[BlockingStructure] = field(
        default=None,
        metadata={
            "name": "Blocking",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    boarding: Optional[BoardingStructure] = field(
        default=None,
        metadata={
            "name": "Boarding",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delays: Optional[DelaysStructure] = field(
        default=None,
        metadata={
            "name": "Delays",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    casualties: Optional[CasualtiesStructure] = field(
        default=None,
        metadata={
            "name": "Casualties",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    easements: List[EasementsStructure] = field(
        default_factory=list,
        metadata={
            "name": "Easements",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class Suitabilities:
        suitability: List[SuitabilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
