from dataclasses import dataclass
from .publication_delivery_structure import PublicationDeliveryStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PublicationDelivery(PublicationDeliveryStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
