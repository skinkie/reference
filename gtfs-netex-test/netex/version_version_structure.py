from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.multilingual_string import MultilingualString
from netex.type_of_version_ref import TypeOfVersionRef
from netex.version_ref_structure import VersionRefStructure
from netex.version_status_enumeration import VersionStatusEnumeration
from netex.version_type_enumeration import VersionTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VersionVersionStructure(DataManagedObjectStructure):
    """
    Type for a VERSION.

    :ivar start_date: Date of start of VERSION currency.
    :ivar end_date: Date of end of VERSION currency. Date is INCLUSIVE.
    :ivar status: Status of VERSION.
    :ivar description:
    :ivar version_type: Version type: Point or Baseline.
    :ivar type_of_version_ref:
    :ivar derived_from_version_ref: Reference to VERSION from which this
        VERSION was derived.
    """
    class Meta:
        name = "Version_VersionStructure"

    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    status: Optional[VersionStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    version_type: Optional[VersionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "VersionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_version_ref: Optional[TypeOfVersionRef] = field(
        default=None,
        metadata={
            "name": "TypeOfVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    derived_from_version_ref: Optional[VersionRefStructure] = field(
        default=None,
        metadata={
            "name": "DerivedFromVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
