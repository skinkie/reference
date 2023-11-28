from dataclasses import dataclass, field
from netex.flexible_mode_of_operation_value_structure import FlexibleModeOfOperationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleOperation(FlexibleModeOfOperationValueStructure):
    """Passenger transport operation linked to a fixed network/schedule but
    offering flexibility, in order for instance, to optimise the service or to
    satisfy passenger demand.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
