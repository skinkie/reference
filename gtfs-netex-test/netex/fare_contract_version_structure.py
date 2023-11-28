from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.customer_account_ref import CustomerAccountRef
from netex.customer_ref import CustomerRef
from netex.fare_contract_entries_rel_structure import FareContractEntriesRelStructure
from netex.multilingual_string import MultilingualString
from netex.type_of_fare_contract_ref import TypeOfFareContractRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareContractVersionStructure(DataManagedObjectStructure):
    """
    Type for FARE CONTRACT.

    :ivar name: Name of FARE CONTRACT.
    :ivar description: Description of FARE CONTRACT.
    :ivar start_date: Start Date of FARE CONTRACT.
    :ivar end_date: End Date of FARE CONTRACT.
    :ivar status: Status of FARE CONTRACT.
    :ivar customer_ref:
    :ivar customer_account_ref:
    :ivar type_of_fare_contract_ref:
    :ivar fare_contract_entries: Events in CONTRACT.
    """
    class Meta:
        name = "FareContract_VersionStructure"

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
    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_account_ref: Optional[CustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_contract_ref: Optional[TypeOfFareContractRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract_entries: Optional[FareContractEntriesRelStructure] = field(
        default=None,
        metadata={
            "name": "fareContractEntries",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
