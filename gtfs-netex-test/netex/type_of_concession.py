from dataclasses import dataclass, field
from netex.type_of_concession_version_structure import TypeOfConcessionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfConcession(TypeOfConcessionVersionStructure):
    """
    Category of concession user.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
