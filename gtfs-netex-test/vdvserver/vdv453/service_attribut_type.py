from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ServiceAttributType:
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    wert: str = field(
        metadata={
            "name": "Wert",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
