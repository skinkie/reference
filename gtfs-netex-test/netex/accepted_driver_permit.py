from dataclasses import dataclass

from .accepted_driver_permit_version_structure import AcceptedDriverPermitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AcceptedDriverPermit(AcceptedDriverPermitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
