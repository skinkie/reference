from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.derived_view_structure import DerivedViewStructure
from netex.multilingual_string import MultilingualString
from netex.operator_ref import OperatorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperatorDerivedViewStructure(DerivedViewStructure):
    """
    Type for an OPERATOR VIEW.

    :ivar operator_ref:
    :ivar name: The name of the ORGANISATION.
    :ivar short_name: A short name of the ORGANISATION.
    :ivar legal_name: The legal name of the ORGANISATION, if different
        from Name.
    :ivar trading_name: The Trading name of the ORGANISATION given to
        the Public - If different from Name or Legal Name.
    :ivar alternative_names: Alternativie names for ORGANISATION.
    """
    class Meta:
        name = "Operator_DerivedViewStructure"

    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
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
    legal_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "LegalName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    trading_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "TradingName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
