from dataclasses import dataclass, field
from typing import List, Optional, Type
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlTime
from netex.availability_condition_ref import AvailabilityConditionRef
from netex.branding_ref import BrandingRef
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.day_of_week_enumeration import DayOfWeekEnumeration
from netex.day_type_ref import DayTypeRef
from netex.entity_structure import EntityStructure
from netex.extensions_2 import Extensions2
from netex.fare_day_type_ref import FareDayTypeRef
from netex.key_list import KeyList
from netex.modification_enumeration import ModificationEnumeration
from netex.multilingual_string import MultilingualString
from netex.operating_day_ref import OperatingDayRef
from netex.private_code import PrivateCode
from netex.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.relative_operator_enumeration import RelativeOperatorEnumeration
from netex.service_calendar_ref import ServiceCalendarRef
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.status_enumeration import StatusEnumeration
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.time_of_day_enumeration import TimeOfDayEnumeration
from netex.timeband_ref import TimebandRef
from netex.validity_condition_ref import ValidityConditionRef
from netex.validity_condition_ref_structure import ValidityConditionRefStructure
from netex.validity_rule_parameter_ref import ValidityRuleParameterRef
from netex.validity_trigger_ref import ValidityTriggerRef
from netex.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AlternativeTextsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for list of ALTERNATIVE TEXTs.

    :ivar alternative_text: ALTERNATIVE TEXT for an text attribute of
        Element.
    """
    class Meta:
        name = "alternativeTexts_RelStructure"

    alternative_text: List["AlternativeText"] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class DayTypesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of DAY TYPEs.
    """
    class Meta:
        name = "dayTypes_RelStructure"

    choice: List[object] = field(
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
                    "type": Type["FareDayType"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationDayType",
                    "type": Type["OrganisationDayType"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayType",
                    "type": Type["DayType"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class OperatingDaysRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of OPERATING DAYs.
    """
    class Meta:
        name = "operatingDays_RelStructure"

    operating_day_ref_or_operating_day: List[object] = field(
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
                    "type": Type["OperatingDay"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class TimebandsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TIMEBANDs.
    """
    class Meta:
        name = "timebands_RelStructure"

    timeband_ref_or_timeband: List[object] = field(
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
                    "type": Type["TimebandVersionedChildStructure"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityConditionsRelStructure(ContainmentAggregationStructure):
    """
    A collection of one or more VALIDITY CONDITIONs.
    """
    class Meta:
        name = "validityConditions_RelStructure"

    choice: List[object] = field(
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
                    "type": Type["ValidBetween"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SimpleAvailabilityCondition",
                    "type": Type["SimpleAvailabilityCondition"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidDuring",
                    "type": Type["ValidDuring"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AvailabilityCondition",
                    "type": Type["AvailabilityCondition"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityRuleParameter",
                    "type": Type["ValidityRuleParameter"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityTrigger",
                    "type": Type["ValidityTrigger"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityCondition",
                    "type": Type["ValidityCondition"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class EntityInVersionStructure(EntityStructure):
    """
    Type for ENTITY IN VERSION.

    :ivar validity_conditions_or_valid_between:
    :ivar alternative_texts: Additional Translations of text  elements.
    :ivar data_source_ref_attribute: Name of source of the data.
    :ivar created: Date ENTITY was first created.
    :ivar changed: Date ENTITY or version was last changed.
    :ivar modification: Nature of last modification: new, revise,
        delete, unchanged, delta. Default is "new".
    :ivar version: Version number of entity.
    :ivar status_attribute: Whether ENTITY is currently in use. Default
        is "active".
    :ivar derived_from_version_ref_attribute: Version of this object
        from which this version of ENTITY was derived.
    :ivar compatible_with_version_frame_version_ref: Version of frame
        from with which this version of ENTITY is compatible. Assumes
        Frame of the same Id as current frame.
    :ivar derived_from_object_ref: Identity of object from which this
        object of ENTITY was derived. Normally the same.
    """
    validity_conditions_or_valid_between: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "validityConditions",
                    "type": ValidityConditionsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidBetween",
                    "type": Type["ValidBetween"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    alternative_texts: Optional[AlternativeTextsRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeTexts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_source_ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataSourceRef",
            "type": "Attribute",
        }
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    changed: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    status_attribute: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "name": "status",
            "type": "Attribute",
        }
    )
    derived_from_version_ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "derivedFromVersionRef",
            "type": "Attribute",
        }
    )
    compatible_with_version_frame_version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "compatibleWithVersionFrameVersionRef",
            "type": "Attribute",
        }
    )
    derived_from_object_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "derivedFromObjectRef",
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class DataManagedObjectStructure(EntityInVersionStructure):
    """
    Abstract Type for a MANAGED OBJECT.

    :ivar key_list: A list of alternative Key values for an element.
    :ivar extensions:
    :ivar branding_ref:
    :ivar responsibility_set_ref_attribute: Reference to RESPONSIBILITY
        SET for managing the object. If absent, then responsibility is
        same as for containing context of this object.
    """
    key_list: Optional[KeyList] = field(
        default=None,
        metadata={
            "name": "keyList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    branding_ref: Optional[BrandingRef] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_set_ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "responsibilitySetRef",
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class VersionedChildStructure(EntityInVersionStructure):
    """
    Type for VERSIONED CHILD.
    """
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class AlternativeTextVersionedChildStructure(VersionedChildStructure):
    """
    Type for ALTERNATIVE TEXT.

    :ivar data_managed_object_ref: Object for  attribute for which
        ALTERNATIVE TEXTprovides an alias. May be omitted if given by
        context.
    :ivar text: Name of the entity.
    :ivar attribute_name: Name of text attribute for which this is the
        alternative tex. Must be an existing attribute name
    :ivar use_for_language: Name of language for which this is to be
        used.
    :ivar order: Order of name.
    """
    class Meta:
        name = "AlternativeText_VersionedChildStructure"

    data_managed_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DataManagedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
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
        }
    )
    use_for_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "useForLanguage",
            "type": "Attribute",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class DayTypeVersionStructure(DataManagedObjectStructure):
    """
    Type for a DAY TYPE.

    :ivar name: Name of DAY TYPE.
    :ivar short_name: Short name of DAY TYPE.
    :ivar description: Description of DAY TYPE.
    :ivar private_code:
    :ivar earliest_time: Earliest time that day starts.
    :ivar day_length: Length of day. Used to work out Latest time that
        day runs to.
    :ivar properties: Properties of the DAY TYPE.
    :ivar timebands: TIMEBANDs for the DAY TYPE.
    """
    class Meta:
        name = "DayType_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    earliest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_length: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DayLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    properties: Optional[PropertiesOfDayRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timebands: Optional[TimebandsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class OperatingDayVersionStructure(DataManagedObjectStructure):
    """
    Type for an OPERATING DAY.

    :ivar calendar_date: Actual Date of OPERATING DAY. Unique within
        SERVICE CALENDAR.
    :ivar service_calendar_ref: Reference to parent  SERVICE CALENDAR.
        If given by context, does not need to be given.
    :ivar name: Name of OPERATING DAY.
    :ivar short_name: Short name of OPERATING DAY.
    :ivar day_number: Day Number if different from Id.
    :ivar private_code:
    :ivar earliest_time: Earliest time that day starts.
    :ivar day_length: Length of day. Used to work out Latest time that
        day runs to.
    """
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
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    earliest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_length: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DayLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class TimebandVersionedChildStructure(DataManagedObjectStructure):
    """
    Type for a TIMEBAND.

    :ivar name: Name of TIMEBAND.
    :ivar start_time_or_start_event:
    :ivar choice:
    """
    class Meta:
        name = "Timeband_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_time_or_start_event: Optional[object] = field(
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
        }
    )
    choice: List[object] = field(
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
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityConditionVersionStructure(DataManagedObjectStructure):
    """
    Types for a VALIDITY CONDITION.

    :ivar name: Name of VALIDITY CONDITION.
    :ivar description: Description of VALIDITY CONDITION.
    :ivar conditioned_object_ref: Entity to which condition specifically
        attaches.
    :ivar with_condition_ref: CONDITION with which this rule is
        logically ANDed.
    """
    class Meta:
        name = "ValidityCondition_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    conditioned_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ConditionedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    with_condition_ref: Optional[ValidityConditionRefStructure] = field(
        default=None,
        metadata={
            "name": "WithConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class AlternativeText(AlternativeTextVersionedChildStructure):
    """Alternative Text.

    +v1.1
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar
    extensions: RestrictedVar


@dataclass(unsafe_hash=True, kw_only=True)
class DayType(DayTypeVersionStructure):
    """A type of day characterized by one or more properties which affect public
    transport operation.

    For example: weekday in school holidays.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareDayTypeVersionedStructure(DayTypeVersionStructure):
    """
    Type for FARE DAY TYPE.
    """
    class Meta:
        name = "FareDayType_VersionedStructure"


@dataclass(unsafe_hash=True, kw_only=True)
class OperatingDay(OperatingDayVersionStructure):
    """A day of public transport operation in a specific calendar.

    An OPERATING DAY may last more than 24 hours.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrganisationDayTypeVersionStructure(DayTypeVersionStructure):
    """Type for an ORGANISATION.

    DAY TYPE.
    """
    class Meta:
        name = "OrganisationDayType_VersionStructure"

    is_service_day: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsServiceDay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    serviced_organisation_ref: Optional[ServicedOrganisationRef] = field(
        default=None,
        metadata={
            "name": "ServicedOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class ValidBetweenVersionStructure(ValidityConditionVersionStructure):
    """
    Type for a Simple VALIDITY CONDITION.

    :ivar from_date: Start date of AVAILABILITY CONDITION.
    :ivar to_date: End of AVAILABILITY CONDITION. Date is INCLUSIVE.
    """
    class Meta:
        name = "ValidBetween_VersionStructure"

    from_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FromDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityCondition(ValidityConditionVersionStructure):
    """Condition used in order to characterise a given VERSION of a VERSION FRAME.

    A VALIDITY CONDITION consists of a parameter (e.g. date, triggering
    event, etc) and its type of application (e.g. for, from, until,
    etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityRuleParameterVersionStructure(ValidityConditionVersionStructure):
    """
    Type for a VALIDITY PARAMETER.

    :ivar rule_object_ref: Entity on which Rules based - Trigger value
        is taken from it.
    :ivar choice:
    """
    class Meta:
        name = "ValidityRuleParameter_VersionStructure"

    rule_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "RuleObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
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
                    "type": object,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Method",
                    "type": object,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "isValid",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 3,
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityTriggerVersionStructure(ValidityConditionVersionStructure):
    """
    Type for a VALIDITY TRIGGER.

    :ivar trigger_object_ref: Entity on which Trigger is based - Trigger
        value is taken from it.
    :ivar private_code:
    """
    class Meta:
        name = "ValidityTrigger_VersionStructure"

    trigger_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "TriggerObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class AvailabilityConditionVersionStructure(ValidBetweenVersionStructure):
    """
    Type for an AVAILABILITY CONDITION.

    :ivar is_available: Whether condition makes resource available or
        not available. Default is available.
    :ivar day_types: DAY TYPEs for AVAILABILITY CONDITION.
    :ivar valid_day_bits: For UIC style encoding of day types String of
        bits, one for each day in period: whether valid or not valid on
        the day.  Normally there will be a bit for every day between
        start and end date.  If bit is missing, assume available.
    :ivar timebands: TIME BANDs for AVAILABILITY CONDITION.
    :ivar operating_days: OPERATING DAYs for AVAILABILITY CONDITION.
    """
    class Meta:
        name = "AvailabilityCondition_VersionStructure"

    is_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_types: Optional[DayTypesRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    valid_day_bits: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidDayBits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timebands: Optional[TimebandsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_days: Optional[OperatingDaysRelStructure] = field(
        default=None,
        metadata={
            "name": "operatingDays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class FareDayType(FareDayTypeVersionedStructure):
    """
    A type of day used in the fare collection domain, characterized by one or more
    properties which affect the definition of access rights and prices in the fare
    system.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrganisationDayType(OrganisationDayTypeVersionStructure):
    """
    DAY TYPE defined as being available on days when ORGANISATION is open and
    requires service.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidBetween(ValidBetweenVersionStructure):
    """OPTIMISATION.

    Simple version of a VALIDITY CONDITION. Comprises a simple period.
    NO UNIQUENESS CONSTRAINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar
    key_list: RestrictedVar
    extensions: RestrictedVar
    branding_ref: RestrictedVar
    name: RestrictedVar
    description: RestrictedVar
    conditioned_object_ref: RestrictedVar
    with_condition_ref: RestrictedVar


@dataclass(unsafe_hash=True, kw_only=True)
class ValidDuringVersionStructure(ValidBetweenVersionStructure):
    """
    Type for a  SIMPLE TIMEBAND AVAILABILITY CONDITION.

    :ivar choice:
    :ivar timebands: TIME BANDs for AVAILABILITY CONDITION.
    """
    class Meta:
        name = "ValidDuring_VersionStructure"

    choice: Optional[object] = field(
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
                    "type": List[DayOfWeekEnumeration],
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
        }
    )
    timebands: Optional[TimebandsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityRuleParameter(ValidityRuleParameterVersionStructure):
    """A user defined VALIDITY CONDITION used by a rule for selecting versions.

    E.g. river level &gt; 1,5 m and bad weather.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityTrigger(ValidityTriggerVersionStructure):
    """External event defining a VALIDITY CONDITION.

    E.g. exceptional flow of a river, bad weather, Road closure for
    works.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar


@dataclass(unsafe_hash=True, kw_only=True)
class AvailabilityCondition(AvailabilityConditionVersionStructure):
    """
    VALIDITY CONDITION stated in terms of DAY TYPES and  PROPERTIES OF DAYs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar


@dataclass(unsafe_hash=True, kw_only=True)
class SimpleAvailabilityCondition(ValidDuringVersionStructure):
    """Simple version of an  AVAILABILITY CONDITION used in order to characterise a
    given VERSION of a VERSION FRAME.

    Comprises a simple period and DAY TYPE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidDuring(ValidDuringVersionStructure):
    """OPTIMISATION: Sversion  of an AVAILABILITY CONDITION    Comprises a simple period and DAY TYPE."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar
    key_list: RestrictedVar
    extensions: RestrictedVar
    branding_ref: RestrictedVar
