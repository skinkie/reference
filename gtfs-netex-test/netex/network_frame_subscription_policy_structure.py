from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NetworkFrameSubscriptionPolicyStructure:
    """
    Data type for Subscription Request for  NeTEx Data Object  Service.

    :ivar incremental_updates: Whether the producer should return the
        complete set of current data, or only provide updates to the
        last data returned, i.e. additions, modifications and deletions.
        If false each subscription response will contain the full
        information as specified in this request.
    """
    incremental_updates: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncrementalUpdates",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
