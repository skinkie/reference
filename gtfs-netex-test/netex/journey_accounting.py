from dataclasses import dataclass, field
from netex.journey_accounting_version_structure import JourneyAccountingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyAccounting(JourneyAccountingVersionStructure):
    """
    Parameters characterizing VEHICLE JOURNEYs or SPECIAL SERVICEs used for
    accounting purposes in particular in contracts between ORGANISATIONs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
