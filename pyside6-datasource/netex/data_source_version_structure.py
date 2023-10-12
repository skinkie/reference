from dataclasses import dataclass, field
from typing import Optional
from netex.external_object_ref_structure import ExternalObjectRefStructure
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DataSourceVersionStructure(TypeOfValueVersionStructure):
    """
    Type for DATA SOURCE.

    :ivar email: Contact email for data queries.
    :ivar data_licence_code: Data Licence identifier.  +v1.2.2
    :ivar data_licence_url: URL fto Data Licence +v1.2.2
    """
    class Meta:
        name = "DataSource_VersionStructure"

    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_licence_code: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DataLicenceCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_licence_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataLicenceUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
