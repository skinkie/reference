from dataclasses import dataclass, field
from typing import Optional
from netex.codespace_ref_structure import CodespaceRefStructure
from netex.data_source_ref_structure import DataSourceRefStructure
from netex.locale_structure import LocaleStructure
from netex.responsibility_set_ref_structure import ResponsibilitySetRefStructure
from netex.system_of_units import SystemOfUnits

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VersionFrameDefaultsStructure:
    """
    Type for frame defaults.

    :ivar default_codespace_ref: Default CODESPACE to assume for an
        identifiers that do not have an explicit CODESPACE specified..
    :ivar default_data_source_ref: Default DATA SOURCE. Assume this
        value as the DATA SOURCE for content if not specified on
        individual elements.
    :ivar default_responsibility_set_ref: Default RESPONSIBILITY SET.
        Assume this value as the DATA SOURCE for content if not
        specified on individual elements.
    :ivar default_locale: Default LOCAL for frame elements. Assume this
        value for     timezone and language of elements if not specified
        on individual elements.
    :ivar default_location_system: Default spatial coordinate system
        (srsName).  E.g.  WGS84 Value to use for   location elements
        using coordinates if not specified on individual elements.
    :ivar default_system_of_units: Units of measurement for all
        dimension values in Frame. Default System  is Si Metres.
    :ivar default_currency: Default Currency type to use.
    """
    default_codespace_ref: Optional[CodespaceRefStructure] = field(
        default=None,
        metadata={
            "name": "DefaultCodespaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_data_source_ref: Optional[DataSourceRefStructure] = field(
        default=None,
        metadata={
            "name": "DefaultDataSourceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_responsibility_set_ref: Optional[ResponsibilitySetRefStructure] = field(
        default=None,
        metadata={
            "name": "DefaultResponsibilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_locale: Optional[LocaleStructure] = field(
        default=None,
        metadata={
            "name": "DefaultLocale",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_location_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLocationSystem",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_system_of_units: Optional[SystemOfUnits] = field(
        default=None,
        metadata={
            "name": "DefaultSystemOfUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultCurrency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        }
    )
