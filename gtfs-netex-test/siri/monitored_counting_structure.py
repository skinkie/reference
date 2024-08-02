from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union

from .counted_feature_unit_enumeration import CountedFeatureUnitEnumeration
from .counting_trend_enumeration import CountingTrendEnumeration
from .counting_type_enumeration import CountingTypeEnumeration
from .extensions_1 import Extensions1
from .natural_language_string_structure import NaturalLanguageStringStructure
from .type_of_value_structure import TypeOfValueStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MonitoredCountingStructure:
    counting_type: CountingTypeEnumeration = field(
        metadata={
            "name": "CountingType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    counted_feature_unit: Optional[CountedFeatureUnitEnumeration] = field(
        default=None,
        metadata={
            "name": "CountedFeatureUnit",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    type_of_counted_feature: Optional[TypeOfValueStructure] = field(
        default=None,
        metadata={
            "name": "TypeOfCountedFeature",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    count_or_percentage: Optional[Union[int, Decimal]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Count",
                    "type": int,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Percentage",
                    "type": Decimal,
                    "namespace": "http://www.siri.org.uk/siri",
                    "min_inclusive": Decimal("0"),
                },
            ),
        },
    )
    trend: Optional[CountingTrendEnumeration] = field(
        default=None,
        metadata={
            "name": "Trend",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accuracy: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Accuracy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_inclusive": Decimal("0"),
        },
    )
    description: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    counted_items_id_list: Optional["MonitoredCountingStructure.CountedItemsIdList"] = field(
        default=None,
        metadata={
            "name": "CountedItemsIdList",
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
    class CountedItemsIdList:
        item_id: List[str] = field(
            default_factory=list,
            metadata={
                "name": "ItemId",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
