from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .country_ref_structure import CountryRefStructure
from .extensions_1 import Extensions1
from .natural_language_string_structure import NaturalLanguageStringStructure
from .situation_source_type_enumeration import SituationSourceTypeEnumeration
from .source_type_enum import SourceTypeEnum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationSourceStructure:
    country: Optional[CountryRefStructure] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source_type: SituationSourceTypeEnumeration = field(
        metadata={
            "name": "SourceType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    web: Optional[str] = field(
        default=None,
        metadata={
            "name": "Web",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    other: Optional[str] = field(
        default=None,
        metadata={
            "name": "Other",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source_method: Optional[SourceTypeEnum] = field(
        default=None,
        metadata={
            "name": "SourceMethod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    agent_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentReference",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source_role: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceRole",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    time_of_communication: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeOfCommunication",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    external_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceFile",
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
