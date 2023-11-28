from dataclasses import dataclass, field
from typing import Optional
from netex.access_equipment_version_structure import AccessEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class QueueingEquipmentVersionStructure(AccessEquipmentVersionStructure):
    """
    Type for a QUEUEING EQUIPMENT.

    :ivar number_of_servers: Number of queue server points.
    :ivar railed_queue: Whether queueing are is controlled by cattle
        bars.
    :ivar ticketed_queue: Whether queue is controlled by numbered
        tickets.
    :ivar disabled_priority: Whether there is priority access for
        disabled (no-queue).+v1.1
    :ivar queuing_seated_possible: Whether queuing may be done
        seated.+v1.1
    """
    class Meta:
        name = "QueueingEquipment_VersionStructure"

    number_of_servers: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfServers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railed_queue: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RailedQueue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketed_queue: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TicketedQueue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    disabled_priority: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisabledPriority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    queuing_seated_possible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "QueuingSeatedPossible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
