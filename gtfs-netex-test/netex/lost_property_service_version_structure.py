from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.customer_service_version_structure import CustomerServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LostPropertyServiceVersionStructure(CustomerServiceVersionStructure):
    """
    Type for a LOST PROPERTY SERVICE.

    :ivar property_kept_for_duration: Period for which lost property is
        kept - after this time it may be disposed of. +V1.1
    """
    class Meta:
        name = "LostPropertyService_VersionStructure"

    property_kept_for_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PropertyKeptForDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
