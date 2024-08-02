from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .entry_qualifier_structure import EntryQualifierStructure
from .organisation_ref_structure import OrganisationRefStructure
from .parameterised_action_structure import ParameterisedActionStructure
from .participant_ref_structure import ParticipantRefStructure
from .perspective_enumeration import PerspectiveEnumeration
from .situation_version import SituationVersion
from .textual_content_structure import TextualContentStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PassengerInformationActionStructure(ParameterisedActionStructure):
    action_ref: EntryQualifierStructure = field(
        metadata={
            "name": "ActionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    recorded_at_time: XmlDateTime = field(
        metadata={
            "name": "RecordedAtTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    version: Optional[SituationVersion] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "SourceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    owner_ref: Optional[OrganisationRefStructure] = field(
        default=None,
        metadata={
            "name": "OwnerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    perspective: List[PerspectiveEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Perspective",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    action_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActionPriority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    textual_content: List[TextualContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "TextualContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
