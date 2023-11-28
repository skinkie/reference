from dataclasses import dataclass
from netex.interchange_ref_structure import InterchangeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourneyInterchangeRefStructure(InterchangeRefStructure):
    """
    Type for a reference to a SERVICE JOURNEY INTERCHANGE.
    """
