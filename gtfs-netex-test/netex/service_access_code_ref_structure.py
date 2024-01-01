from dataclasses import dataclass
from .travel_document_ref_structure import TravelDocumentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceAccessCodeRefStructure(TravelDocumentRefStructure):
    value: RestrictedVar
