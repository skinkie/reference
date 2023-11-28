from dataclasses import dataclass
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClassificationDescriptorVersionStructure(TypeOfValueVersionStructure):
    """
    Type for a Descriptor for a POINT OF INTEREST CLASSIFICATION.
    """
    class Meta:
        name = "ClassificationDescriptor_VersionStructure"
