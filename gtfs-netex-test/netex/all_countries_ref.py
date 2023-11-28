from dataclasses import dataclass
from netex.all_countries_ref_structure import AllCountriesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllCountriesRef(AllCountriesRefStructure):
    """Reference to a country ISO 3166-1 Note that GB is used for UK .

    May be qualified with a 3166-2 subdivision e.g. gb +m ENG, GB + SCT, GB See www.iso.org/iso/country_codes/iso_3166_code_lists.htm.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
