from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from netex.output_detail_enumeration import OutputDetailEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NetworkFrameRequestPolicyStructure:
    """Parameters that affect the request processing.

    Mostly act to reduce the number of stops returned.

    :ivar maximum_number_of_elements: Maximum number of objects to
        include in response. If absent, include all instances.
    :ivar include_deleted: Whether to include  in response. elements
        flagged as deleted. By default this will be false.
    :ivar urgency: Allows requestor to indicate a relative urgency of
        request. A longer period can be specified for non urgent
        requests, e.g. to get  historic data. If not specified assume
        best possible response desired, preferably immediate.
    :ivar must_have_by: Allows requestor to indicate that if data cannot
        be supplied by a given time it will not be useful. Can be used
        to prioritize data on systems working at full load.
    :ivar language: Preferred language for text elements in response.
    :ivar request_detail: Level of detail to return. Default is all. All
        = Return all data and geometry, but not Xref NoGeometry = Return
        all, omitting geometry. XRef - Return Xcross Reference data ,
        e.g. links for zones.
    """
    maximum_number_of_elements: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    include_deleted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeDeleted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    urgency: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Urgency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    must_have_by: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "MustHaveBy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    request_detail: List[OutputDetailEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RequestDetail",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
