from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DataObjectServicePermissionStructure:
    value: float = field(
        metadata={
            "required": True,
        }
    )
