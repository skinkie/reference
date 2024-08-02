from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .cause import Cause
from .comment import Comment
from .confidentiality_value_enum import ConfidentialityValueEnum
from .extension_type import ExtensionType
from .group_of_locations import GroupOfLocations
from .impact import Impact
from .management import Management
from .probability_of_occurrence_enum import ProbabilityOfOccurrenceEnum
from .source import Source
from .url_link import UrlLink
from .validity import Validity

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class SituationRecord:
    situation_record_creation_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    situation_record_creation_time: XmlDateTime = field(
        metadata={
            "name": "situationRecordCreationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    situation_record_observation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordObservationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    situation_record_version: int = field(
        metadata={
            "name": "situationRecordVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    situation_record_version_time: XmlDateTime = field(
        metadata={
            "name": "situationRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    situation_record_first_supplier_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordFirstSupplierVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    confidentiality_override: Optional[ConfidentialityValueEnum] = field(
        default=None,
        metadata={
            "name": "confidentialityOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    probability_of_occurrence: ProbabilityOfOccurrenceEnum = field(
        metadata={
            "name": "probabilityOfOccurrence",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    validity: Validity = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    impact: Optional[Impact] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    cause: Optional[Cause] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    general_public_comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "name": "generalPublicComment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    non_general_public_comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "name": "nonGeneralPublicComment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    url_link: List[UrlLink] = field(
        default_factory=list,
        metadata={
            "name": "urlLink",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    group_of_locations: GroupOfLocations = field(
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    management: Optional[Management] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    situation_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
