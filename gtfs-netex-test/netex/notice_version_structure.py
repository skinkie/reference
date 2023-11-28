from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.delivery_variants_rel_structure import DeliveryVariantsRelStructure
from netex.multilingual_string import MultilingualString
from netex.private_code import PrivateCode
from netex.type_of_notice_ref import TypeOfNoticeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NoticeVersionStructure(DataManagedObjectStructure):
    """
    Type for NOTICE.

    :ivar name: Name of Notice. Use Text for content.
    :ivar short_name: Short Name of Notice. Use Text for content. +v1.1.
    :ivar text: Text content of NOTICe.
    :ivar public_code: Alternative code associated with Notice.
    :ivar short_code: Alternative short code associated with Notice.
    :ivar private_code:
    :ivar type_of_notice_ref:
    :ivar can_be_advertised: Whether NOTICE is advertised to public.
        This may be overridden on an assignment.
    :ivar driver_display_text: Text to show to Driver or Staff for the
        Notice.
    :ivar variants: Variations on NOTICE for different media.
    """
    class Meta:
        name = "Notice_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
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
    driver_display_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "DriverDisplayText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    variants: Optional[DeliveryVariantsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
