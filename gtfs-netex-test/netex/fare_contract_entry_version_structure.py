from dataclasses import dataclass, field
from typing import Optional
from netex.fare_contract_ref import FareContractRef
from netex.log_entry_version_structure import LogEntryVersionStructure
from netex.type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareContractEntryVersionStructure(LogEntryVersionStructure):
    """
    Type for FARE CONTRACT ENTRY.

    :ivar is_valid: Whether FARE CONTRACT ENTRY is valid.
    :ivar type_of_fare_contract_entry_ref: A classifiication of FARE
        CONTRACT ENTRYs.
    :ivar fare_contract_ref:
    """
    class Meta:
        name = "FareContractEntry_VersionStructure"

    is_valid: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsValid",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_contract_entry_ref: Optional[TypeOfFareContractEntryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareContractEntryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract_ref: Optional[FareContractRef] = field(
        default=None,
        metadata={
            "name": "FareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
