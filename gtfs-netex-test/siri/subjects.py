from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .subject_type_of_works_enum import SubjectTypeOfWorksEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class Subjects:
    subject_type_of_works: SubjectTypeOfWorksEnum = field(
        metadata={
            "name": "subjectTypeOfWorks",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    number_of_subjects: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfSubjects",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    subjects_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "subjectsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
