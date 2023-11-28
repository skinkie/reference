from dataclasses import dataclass, field
from typing import Optional
from netex.additional_driver_type_enumeration import AdditionalDriverTypeEnumeration
from netex.driver_type_fee_basis_enumeration import DriverTypeFeeBasisEnumeration
from netex.rental_option_version_structure import RentalOptionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AdditionalDriverOptionVersionStructure(RentalOptionVersionStructure):
    """
    Type for ADDITIONAL DRIVER OPTION.

    :ivar additional_driver: Additional driver options.
    :ivar driver_fee_basis: Additional driver options.
    :ivar number_ofdrivers: Maximimum Number of drivers allwoed.
    """
    class Meta:
        name = "AdditionalDriverOption_VersionStructure"

    additional_driver: Optional[AdditionalDriverTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "AdditionalDriver",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_fee_basis: Optional[DriverTypeFeeBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "DriverFeeBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_ofdrivers: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOFDrivers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
