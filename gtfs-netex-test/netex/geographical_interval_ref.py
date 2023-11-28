from dataclasses import dataclass
from netex.geographical_interval_ref_structure import GeographicalIntervalRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalIntervalRef(GeographicalIntervalRefStructure):
    """
    Reference to a GEOGRAPHICAL INTERVAL.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
