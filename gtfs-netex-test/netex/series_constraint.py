from dataclasses import dataclass

from .series_constraint_version_structure import SeriesConstraintVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeriesConstraint(SeriesConstraintVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
