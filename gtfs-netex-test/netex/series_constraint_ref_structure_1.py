from dataclasses import dataclass
from netex.series_constraint_ref_structure_2 import SeriesConstraintRefStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SeriesConstraintRefStructure1(SeriesConstraintRefStructure2):
    """
    Type for Reference to a SERIES CONSTRAINT.
    """
    class Meta:
        name = "SeriesConstraintRefStructure"
