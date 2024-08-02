from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .cause import Cause
from .comment import Comment
from .extension_type import ExtensionType
from .group_of_locations import GroupOfLocations
from .impact import Impact
from .management import Management
from .probability_of_occurrence_enum import ProbabilityOfOccurrenceEnum
from .source import Source
from .validity import Validity

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class OptionalTrafficElementStructure:
    situation_record_creation_reference: str = field(
        metadata={
            "name": "situationRecordCreationReference",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
            "max_length": 1024,
        }
    )
    situation_record_creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_observation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordObservationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "situationRecordVersion",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordVersionTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_first_supplier_version_time: XmlDateTime = field(
        metadata={
            "name": "situationRecordFirstSupplierVersionTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    probability_of_occurrence: Optional[ProbabilityOfOccurrenceEnum] = field(
        default=None,
        metadata={
            "name": "probabilityOfOccurrence",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    impact: Optional[Impact] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    cause: Optional[Cause] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_public_comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "name": "generalPublicComment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    non_general_public_comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "name": "nonGeneralPublicComment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    group_of_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    management: Optional[Management] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationRecordExtension",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    traffic_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficElementExtension",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
