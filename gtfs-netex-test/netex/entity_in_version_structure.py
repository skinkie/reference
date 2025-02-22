from dataclasses import dataclass, field
from typing import Any, ForwardRef, Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlTime

from .availability_condition_ref import AvailabilityConditionRef
from .branding_ref import BrandingRef
from .containment_aggregation_structure import ContainmentAggregationStructure
from .day_of_week_enumeration import DayOfWeekEnumeration
from .day_type_ref import DayTypeRef
from .entity_structure import EntityStructure
from .extensions_2 import Extensions2
from .fare_day_type_ref import FareDayTypeRef
from .key_list import KeyList
from .modification_enumeration import ModificationEnumeration
from .multilingual_string import MultilingualString
from .operating_day_ref import OperatingDayRef
from .private_code import PrivateCode
from .private_codes import PrivateCodes
from .properties_of_day_rel_structure import PropertiesOfDayRelStructure
from .relative_operator_enumeration import RelativeOperatorEnumeration
from .service_calendar_ref import ServiceCalendarRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .status_enumeration import StatusEnumeration
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .time_of_day_enumeration import TimeOfDayEnumeration
from .timeband_ref import TimebandRef
from .validity_condition_ref import ValidityConditionRef
from .validity_condition_ref_structure import ValidityConditionRefStructure
from .validity_rule_parameter_ref import ValidityRuleParameterRef
from .validity_trigger_ref import ValidityTriggerRef
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class EntityInVersionStructure(EntityStructure):
    validity_conditions_or_valid_between: list[Union["ValidityConditionsRelStructure", "ValidBetween"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "validityConditions",
                    "type": ForwardRef("ValidityConditionsRelStructure"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidBetween",
                    "type": ForwardRef("ValidBetween"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    alternative_texts: Optional["AlternativeTextsRelStructure"] = field(
        default=None,
        metadata={
            "name": "alternativeTexts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    data_source_ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataSourceRef",
            "type": "Attribute",
        },
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    changed: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    status_attribute: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "name": "status",
            "type": "Attribute",
        },
    )
    derived_from_version_ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "derivedFromVersionRef",
            "type": "Attribute",
        },
    )
    compatible_with_version_frame_version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "compatibleWithVersionFrameVersionRef",
            "type": "Attribute",
        },
    )
    derived_from_object_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "derivedFromObjectRef",
            "type": "Attribute",
        },
    )


@dataclass(slots=True, kw_only=True)
class DataManagedObjectStructure(EntityInVersionStructure):
    key_list: Optional[KeyList] = field(
        default=None,
        metadata={
            "name": "keyList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_codes: Optional[PrivateCodes] = field(
        default=None,
        metadata={
            "name": "privateCodes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    branding_ref: Optional[BrandingRef] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    responsibility_set_ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "responsibilitySetRef",
            "type": "Attribute",
        },
    )


@dataclass(slots=True, kw_only=True)
class VersionedChildStructure(EntityInVersionStructure):
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(slots=True, kw_only=True)
class AlternativeTextVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "AlternativeText_VersionedChildStructure"

    data_managed_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DataManagedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    text: MultilingualString = field(
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeName",
            "type": "Attribute",
        },
    )
    use_for_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "useForLanguage",
            "type": "Attribute",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True, kw_only=True)
class OperatingDayVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "OperatingDay_VersionStructure"

    calendar_date: XmlDate = field(
        metadata={
            "name": "CalendarDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    service_calendar_ref: Optional[ServiceCalendarRef] = field(
        default=None,
        metadata={
            "name": "ServiceCalendarRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    earliest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_length: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DayLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(slots=True, kw_only=True)
class TimebandVersionedChildStructure(DataManagedObjectStructure):
    class Meta:
        name = "Timeband_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_time_or_start_event: Optional[Union[XmlTime, TimeOfDayEnumeration]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StartTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartEvent",
                    "type": TimeOfDayEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    end_time_or_end_event_or_day_offset_or_duration: list[Union[XmlTime, TimeOfDayEnumeration, int, XmlDuration]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EndTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndEvent",
                    "type": TimeOfDayEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Duration",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        },
    )


@dataclass(slots=True, kw_only=True)
class ValidityConditionVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "ValidityCondition_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    conditioned_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ConditionedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    with_condition_ref: Optional[ValidityConditionRefStructure] = field(
        default=None,
        metadata={
            "name": "WithConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(slots=True, kw_only=True)
class AlternativeText(AlternativeTextVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    extensions: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    validity_conditions_or_valid_between: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(slots=True, kw_only=True)
class OperatingDay(OperatingDayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ValidBetweenVersionStructure(ValidityConditionVersionStructure):
    class Meta:
        name = "ValidBetween_VersionStructure"

    from_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FromDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(slots=True, kw_only=True)
class ValidityCondition(ValidityConditionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(slots=True, kw_only=True)
class ValidityRuleParameterVersionStructure(ValidityConditionVersionStructure):
    class Meta:
        name = "ValidityRuleParameter_VersionStructure"

    rule_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "RuleObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    attribute_name_or_comparison_operator_or_attribute_value_or_method_or_is_valid: list[Union[str, RelativeOperatorEnumeration, "ValidityRuleParameterVersionStructure.AttributeValue", "ValidityRuleParameterVersionStructure.Method", bool]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AttributeName",
                    "type": str,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComparisonOperator",
                    "type": RelativeOperatorEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AttributeValue",
                    "type": ForwardRef("ValidityRuleParameterVersionStructure.AttributeValue"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Method",
                    "type": ForwardRef("ValidityRuleParameterVersionStructure.Method"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "isValid",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 3,
        },
    )

    @dataclass(slots=True, kw_only=True)
    class AttributeValue:
        content: object = field(
            metadata={
                "type": "Wildcard",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )

    @dataclass(slots=True, kw_only=True)
    class Method:
        content: object = field(
            metadata={
                "type": "Wildcard",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )


@dataclass(slots=True, kw_only=True)
class ValidityTriggerVersionStructure(ValidityConditionVersionStructure):
    class Meta:
        name = "ValidityTrigger_VersionStructure"

    trigger_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TriggerObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(slots=True, kw_only=True)
class TimebandsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timebands_RelStructure"

    timeband_ref_or_timeband: list[Union[TimebandRef, TimebandVersionedChildStructure]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimebandRef",
                    "type": TimebandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Timeband",
                    "type": TimebandVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass(slots=True, kw_only=True)
class DayTypeVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "DayType_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    earliest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_length: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DayLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    properties: Optional[PropertiesOfDayRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timebands: Optional[TimebandsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(slots=True, kw_only=True)
class ValidBetween(ValidBetweenVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    description: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    conditioned_object_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    with_condition_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    key_list: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    private_codes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    extensions: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    branding_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    validity_conditions_or_valid_between: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(slots=True, kw_only=True)
class ValidDuringVersionStructure(ValidBetweenVersionStructure):
    class Meta:
        name = "ValidDuring_VersionStructure"

    fare_day_type_ref_or_day_type_ref_or_days_of_week_or_days: Optional[Union[FareDayTypeRef, DayTypeRef, list[DayOfWeekEnumeration], str]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DaysOfWeek",
                    "type": list[DayOfWeekEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "Days",
                    "type": str,
                    "namespace": "http://www.netex.org.uk/netex",
                    "min_length": 7,
                    "max_length": 7,
                    "pattern": r"([Y | N])*",
                },
            ),
        },
    )
    timebands: Optional[TimebandsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(slots=True, kw_only=True)
class ValidityRuleParameter(ValidityRuleParameterVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(slots=True, kw_only=True)
class ValidityTrigger(ValidityTriggerVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(slots=True, kw_only=True)
class AlternativeTextsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "alternativeTexts_RelStructure"

    alternative_text: list[AlternativeText] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )


@dataclass(slots=True, kw_only=True)
class OperatingDaysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "operatingDays_RelStructure"

    operating_day_ref_or_operating_day: list[Union[OperatingDayRef, OperatingDay]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OperatingDayRef",
                    "type": OperatingDayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDay",
                    "type": OperatingDay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass(slots=True, kw_only=True)
class DayType(DayTypeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareDayTypeVersionedStructure(DayTypeVersionStructure):
    class Meta:
        name = "FareDayType_VersionedStructure"


@dataclass(slots=True, kw_only=True)
class OrganisationDayTypeVersionStructure(DayTypeVersionStructure):
    class Meta:
        name = "OrganisationDayType_VersionStructure"

    is_service_day: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsServiceDay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    serviced_organisation_ref: Optional[ServicedOrganisationRef] = field(
        default=None,
        metadata={
            "name": "ServicedOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(slots=True, kw_only=True)
class SimpleAvailabilityCondition(ValidDuringVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ValidDuring(ValidDuringVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    key_list: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    private_codes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    extensions: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    branding_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    validity_conditions_or_valid_between: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(slots=True, kw_only=True)
class FareDayType(FareDayTypeVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OrganisationDayType(OrganisationDayTypeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DayTypesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dayTypes_RelStructure"

    day_type_ref_or_day_type: list[Union[FareDayTypeRef, DayTypeRef, FareDayType, OrganisationDayType, DayType]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDayType",
                    "type": FareDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationDayType",
                    "type": OrganisationDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayType",
                    "type": DayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass(slots=True, kw_only=True)
class AvailabilityConditionVersionStructure(ValidBetweenVersionStructure):
    class Meta:
        name = "AvailabilityCondition_VersionStructure"

    is_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_types: Optional[DayTypesRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    valid_day_bits: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidDayBits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timebands: Optional[TimebandsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operating_days: Optional[OperatingDaysRelStructure] = field(
        default=None,
        metadata={
            "name": "operatingDays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(slots=True, kw_only=True)
class AvailabilityCondition(AvailabilityConditionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(slots=True, kw_only=True)
class ValidityConditionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "validityConditions_RelStructure"

    choice: list[Union[AvailabilityConditionRef, ValidityRuleParameterRef, ValidityTriggerRef, ValidityConditionRef, ValidBetween, SimpleAvailabilityCondition, ValidDuring, AvailabilityCondition, ValidityRuleParameter, ValidityTrigger, ValidityCondition]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AvailabilityConditionRef",
                    "type": AvailabilityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityRuleParameterRef",
                    "type": ValidityRuleParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityTriggerRef",
                    "type": ValidityTriggerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityConditionRef",
                    "type": ValidityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidBetween",
                    "type": ValidBetween,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SimpleAvailabilityCondition",
                    "type": SimpleAvailabilityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidDuring",
                    "type": ValidDuring,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AvailabilityCondition",
                    "type": AvailabilityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityRuleParameter",
                    "type": ValidityRuleParameter,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityTrigger",
                    "type": ValidityTrigger,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityCondition",
                    "type": ValidityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
