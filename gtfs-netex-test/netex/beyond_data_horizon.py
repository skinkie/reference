from dataclasses import dataclass
from netex.beyond_data_horizon_error_structure import BeyondDataHorizonErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class BeyondDataHorizon(BeyondDataHorizonErrorStructure):
    """Error: Data period or subscription period is outside of period covered by service."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
