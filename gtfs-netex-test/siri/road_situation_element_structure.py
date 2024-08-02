from dataclasses import dataclass, field
from typing import List, Optional, Union

from .actions_structure import ActionsStructure
from .affects_scope_structure import AffectsScopeStructure
from .alert_cause import AlertCause
from .audience_enumeration import AudienceEnumeration
from .day_type import DayType
from .defaulted_text_structure import DefaultedTextStructure
from .environment_reason import EnvironmentReason
from .environment_sub_reason import EnvironmentSubReason
from .equipment_reason import EquipmentReason
from .equipment_sub_reason import EquipmentSubReason
from .extensions_1 import Extensions1
from .half_open_timestamp_output_range_structure import HalfOpenTimestampOutputRangeStructure
from .image_structure import ImageStructure
from .info_link_structure_2 import InfoLinkStructure2
from .information_status_enum import InformationStatusEnum
from .miscellaneous_reason import MiscellaneousReason
from .miscellaneous_sub_reason import MiscellaneousSubReason
from .natural_language_string_structure import NaturalLanguageStringStructure
from .personnel_reason import PersonnelReason
from .personnel_sub_reason import PersonnelSubReason
from .probability_of_occurrence_enum import ProbabilityOfOccurrenceEnum
from .pt_consequences_structure import PtConsequencesStructure
from .public_event_type_enum import PublicEventTypeEnum
from .quality_index_enumeration import QualityIndexEnumeration
from .report_type import ReportType
from .scope_type_enumeration import ScopeTypeEnumeration
from .sensitivity_enumeration import SensitivityEnumeration
from .severity import Severity
from .situation_element_structure import SituationElementStructure
from .situation_record import SituationRecord
from .undefined_reason import UndefinedReason
from .unknown_reason import UnknownReason
from .verification_status_enumeration import VerificationStatusEnumeration
from .workflow_status_enumeration import WorkflowStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RoadSituationElementStructure(SituationElementStructure):
    verification: Optional[VerificationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Verification",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress: Optional[WorkflowStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Progress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    quality_index: Optional[QualityIndexEnumeration] = field(
        default=None,
        metadata={
            "name": "QualityIndex",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reality: Optional[InformationStatusEnum] = field(
        default=None,
        metadata={
            "name": "Reality",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    likelihood: Optional[ProbabilityOfOccurrenceEnum] = field(
        default=None,
        metadata={
            "name": "Likelihood",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publication: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Publication",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_period: List[HalfOpenTimestampOutputRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    repetitions: Optional["RoadSituationElementStructure.Repetitions"] = field(
        default=None,
        metadata={
            "name": "Repetitions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publication_window: List[HalfOpenTimestampOutputRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "PublicationWindow",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    alert_cause_or_unknown_reason_or_miscellaneous_reason_or_personnel_reason_or_equipment_reason_or_environment_reason_or_undefined_reason: Optional[Union[AlertCause, UnknownReason, MiscellaneousReason, PersonnelReason, EquipmentReason, EnvironmentReason, UndefinedReason]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AlertCause",
                    "type": AlertCause,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "UnknownReason",
                    "type": UnknownReason,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "MiscellaneousReason",
                    "type": MiscellaneousReason,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "PersonnelReason",
                    "type": PersonnelReason,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "EquipmentReason",
                    "type": EquipmentReason,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "EnvironmentReason",
                    "type": EnvironmentReason,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "UndefinedReason",
                    "type": UndefinedReason,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    miscellaneous_sub_reason_or_personnel_sub_reason_or_equipment_sub_reason_or_environment_sub_reason: Optional[Union[MiscellaneousSubReason, PersonnelSubReason, EquipmentSubReason, EnvironmentSubReason]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MiscellaneousSubReason",
                    "type": MiscellaneousSubReason,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "PersonnelSubReason",
                    "type": PersonnelSubReason,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "EquipmentSubReason",
                    "type": EquipmentSubReason,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "EnvironmentSubReason",
                    "type": EnvironmentSubReason,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    public_event_reason: Optional[PublicEventTypeEnum] = field(
        default=None,
        metadata={
            "name": "PublicEventReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reason_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ReasonName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    severity: Optional[Severity] = field(
        default=None,
        metadata={
            "name": "Severity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    sensitivity: Optional[SensitivityEnumeration] = field(
        default=None,
        metadata={
            "name": "Sensitivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    audience: Optional[AudienceEnumeration] = field(
        default=None,
        metadata={
            "name": "Audience",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    scope_type: Optional[ScopeTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ScopeType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    report_type: Optional[ReportType] = field(
        default=None,
        metadata={
            "name": "ReportType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    planned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Planned",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    keywords: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keywords",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        },
    )
    secondary_reasons: Optional["RoadSituationElementStructure.SecondaryReasons"] = field(
        default=None,
        metadata={
            "name": "SecondaryReasons",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    summary: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Summary",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    detail: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Detail",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advice: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Advice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    internal: Optional[DefaultedTextStructure] = field(
        default=None,
        metadata={
            "name": "Internal",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    images: Optional["RoadSituationElementStructure.Images"] = field(
        default=None,
        metadata={
            "name": "Images",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    info_links: Optional["RoadSituationElementStructure.InfoLinks"] = field(
        default=None,
        metadata={
            "name": "InfoLinks",
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
    consequences: Optional[PtConsequencesStructure] = field(
        default=None,
        metadata={
            "name": "Consequences",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publishing_actions: Optional[ActionsStructure] = field(
        default=None,
        metadata={
            "name": "PublishingActions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record: Optional[SituationRecord] = field(
        default=None,
        metadata={
            "name": "SituationRecord",
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
    class Repetitions:
        day_type: List[DayType] = field(
            default_factory=list,
            metadata={
                "name": "DayType",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class SecondaryReasons:
        reason: List["RoadSituationElementStructure.SecondaryReasons.Reason"] = field(
            default_factory=list,
            metadata={
                "name": "Reason",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class Reason:
            alert_cause_or_unknown_reason_or_miscellaneous_reason_or_personnel_reason_or_equipment_reason_or_environment_reason_or_undefined_reason: Optional[Union[AlertCause, UnknownReason, MiscellaneousReason, PersonnelReason, EquipmentReason, EnvironmentReason, UndefinedReason]] = field(
                default=None,
                metadata={
                    "type": "Elements",
                    "choices": (
                        {
                            "name": "AlertCause",
                            "type": AlertCause,
                            "namespace": "http://www.siri.org.uk/siri",
                        },
                        {
                            "name": "UnknownReason",
                            "type": UnknownReason,
                            "namespace": "http://www.siri.org.uk/siri",
                        },
                        {
                            "name": "MiscellaneousReason",
                            "type": MiscellaneousReason,
                            "namespace": "http://www.siri.org.uk/siri",
                        },
                        {
                            "name": "PersonnelReason",
                            "type": PersonnelReason,
                            "namespace": "http://www.siri.org.uk/siri",
                        },
                        {
                            "name": "EquipmentReason",
                            "type": EquipmentReason,
                            "namespace": "http://www.siri.org.uk/siri",
                        },
                        {
                            "name": "EnvironmentReason",
                            "type": EnvironmentReason,
                            "namespace": "http://www.siri.org.uk/siri",
                        },
                        {
                            "name": "UndefinedReason",
                            "type": UndefinedReason,
                            "namespace": "http://www.siri.org.uk/siri",
                        },
                    ),
                },
            )
            miscellaneous_sub_reason_or_personnel_sub_reason_or_equipment_sub_reason_or_environment_sub_reason: Optional[Union[MiscellaneousSubReason, PersonnelSubReason, EquipmentSubReason, EnvironmentSubReason]] = field(
                default=None,
                metadata={
                    "type": "Elements",
                    "choices": (
                        {
                            "name": "MiscellaneousSubReason",
                            "type": MiscellaneousSubReason,
                            "namespace": "http://www.siri.org.uk/siri",
                        },
                        {
                            "name": "PersonnelSubReason",
                            "type": PersonnelSubReason,
                            "namespace": "http://www.siri.org.uk/siri",
                        },
                        {
                            "name": "EquipmentSubReason",
                            "type": EquipmentSubReason,
                            "namespace": "http://www.siri.org.uk/siri",
                        },
                        {
                            "name": "EnvironmentSubReason",
                            "type": EnvironmentSubReason,
                            "namespace": "http://www.siri.org.uk/siri",
                        },
                    ),
                },
            )
            public_event_reason: Optional[PublicEventTypeEnum] = field(
                default=None,
                metadata={
                    "name": "PublicEventReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            reason_name: List[NaturalLanguageStringStructure] = field(
                default_factory=list,
                metadata={
                    "name": "ReasonName",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )

    @dataclass(kw_only=True)
    class Images:
        image: List[ImageStructure] = field(
            default_factory=list,
            metadata={
                "name": "Image",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class InfoLinks:
        info_link: List[InfoLinkStructure2] = field(
            default_factory=list,
            metadata={
                "name": "InfoLink",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
