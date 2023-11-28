from dataclasses import dataclass, field
from typing import Optional
from netex.derived_view_structure import DerivedViewStructure
from netex.multilingual_string import MultilingualString
from netex.notice_ref import NoticeRef
from netex.private_code import PrivateCode
from netex.publicity_channel_enumeration import PublicityChannelEnumeration
from netex.type_of_notice_ref import TypeOfNoticeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NoticeAssignmentDerivedViewStructure(DerivedViewStructure):
    """
    Type for NOTICE ASSIGNMENT View.

    :ivar name: Name of ASSIGNMENT.
    :ivar notice_ref:
    :ivar mark: Mark associated with NOTICE.
    :ivar mark_url: URL for image associated with NOTICE.
    :ivar publicity_channel: How NOTICE is to be publicised. Default is
        all.
    :ivar advertised: Whether NOTICE is advertised to public.
    :ivar text: Text content of NOTICe.
    :ivar public_code: Alternative code associated with Notice.
    :ivar short_code: Alternative short code associated with Notice.
    :ivar private_code:
    :ivar type_of_notice_ref:
    :ivar can_be_advertised: Whether NOTICE is advertised to public.
        This may be overridden on an assignment.
    :ivar order: Order of Assignment.
    """
    class Meta:
        name = "NoticeAssignment_DerivedViewStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_ref: Optional[NoticeRef] = field(
        default=None,
        metadata={
            "name": "NoticeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mark",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mark_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "MarkUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    publicity_channel: Optional[PublicityChannelEnumeration] = field(
        default=None,
        metadata={
            "name": "PublicityChannel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    advertised: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_notice_ref: Optional[TypeOfNoticeRef] = field(
        default=None,
        metadata={
            "name": "TypeOfNoticeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    can_be_advertised: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanBeAdvertised",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
