from dataclasses import dataclass, field
from netex.sales_offer_package_substitution_version_structure import SalesOfferPackageSubstitutionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackageSubstitution(SalesOfferPackageSubstitutionVersionStructure):
    """
    A particular tariff, described by a combination of parameters.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
