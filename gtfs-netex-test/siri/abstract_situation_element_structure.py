from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .country_ref_structure import CountryRefStructure
from .participant_ref_structure import ParticipantRefStructure
from .situation_number import SituationNumber
from .situation_version import SituationVersion

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractSituationElementStructure:
    creation_time: XmlDateTime = field(
        metadata={
            "name": "CreationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    country_ref: Optional[CountryRefStructure] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    participant_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_number: SituationNumber = field(
        metadata={
            "name": "SituationNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    update_country_ref: Optional[CountryRefStructure] = field(
        default=None,
        metadata={
            "name": "UpdateCountryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    update_participant_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "UpdateParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: Optional[SituationVersion] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
