from dataclasses import dataclass, field
from typing import List, Union
from xsdata.models.datatype import XmlDateTime
from .abo_andtype import AboAndtype
from .abo_asbref_type import AboAsbrefType
from .abo_asbtype import AboAsbtype
from .abo_ausref_type import AboAusrefType
from .abo_austype import AboAustype
from .abo_azbref_type import AboAzbrefType
from .abo_azbtype import AboAzbtype
from .abo_vistype import AboVistype


@dataclass(kw_only=True)
class AboAnfrageType:
    choice: List[
        Union[
            AboAsbrefType,
            AboAsbtype,
            AboAzbrefType,
            AboAzbtype,
            AboVistype,
            AboAndtype,
            AboAusrefType,
            AboAustype,
            int,
            bool,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AboASBRef",
                    "type": AboAsbrefType,
                    "namespace": "",
                },
                {
                    "name": "AboASB",
                    "type": AboAsbtype,
                    "namespace": "",
                },
                {
                    "name": "AboAZBRef",
                    "type": AboAzbrefType,
                    "namespace": "",
                },
                {
                    "name": "AboAZB",
                    "type": AboAzbtype,
                    "namespace": "",
                },
                {
                    "name": "AboVIS",
                    "type": AboVistype,
                    "namespace": "",
                },
                {
                    "name": "AboAND",
                    "type": AboAndtype,
                    "namespace": "",
                },
                {
                    "name": "AboAUSRef",
                    "type": AboAusrefType,
                    "namespace": "",
                },
                {
                    "name": "AboAUS",
                    "type": AboAustype,
                    "namespace": "",
                },
                {
                    "name": "AboLoeschen",
                    "type": int,
                    "namespace": "",
                },
                {
                    "name": "AboLoeschenAlle",
                    "type": bool,
                    "namespace": "",
                },
            ),
        },
    )
    sender: str = field(
        metadata={
            "name": "Sender",
            "type": "Attribute",
            "required": True,
        }
    )
    zst: XmlDateTime = field(
        metadata={
            "name": "Zst",
            "type": "Attribute",
            "required": True,
        }
    )
