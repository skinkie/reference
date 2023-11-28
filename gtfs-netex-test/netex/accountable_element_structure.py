from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccountableElementStructure(DataManagedObjectStructure):
    """
    Type for ACCOUNTABLE ELEMENT.

    :ivar description: Description of ACCOUNTABLE ELEMENT.
    :ivar accounting_time: How long a time shoudl be used for the the
        ACCOUNTABLE ELEMENT.
    :ivar accounting_factor: Accounting Factor to use for the the
        ACCOUNTABLE ELEMENT.
    :ivar preparation_duration: Time to prepare ACCOUNTABLE ELEMENT.
    :ivar finishing_duration: Time to complete ACCOUNTABLE ELEMENT.
    """
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accounting_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AccountingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accounting_factor: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AccountingFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    preparation_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreparationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    finishing_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FinishingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
