from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .abstract_situation_element_structure import AbstractSituationElementStructure
from .references_structure import ReferencesStructure
from .situation_source_structure import SituationSourceStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationElementStructure(AbstractSituationElementStructure):
    references: Optional[ReferencesStructure] = field(
        default=None,
        metadata={
            "name": "References",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source: SituationSourceStructure = field(
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    versioned_at_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VersionedAtTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
