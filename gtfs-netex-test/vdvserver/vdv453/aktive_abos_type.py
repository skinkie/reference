from dataclasses import dataclass, field
from typing import List, Union
from .abo_andtype import AboAndtype
from .abo_asbref_type import AboAsbrefType
from .abo_asbtype import AboAsbtype
from .abo_ausref_type import AboAusrefType
from .abo_austype import AboAustype
from .abo_azbref_type import AboAzbrefType
from .abo_azbtype import AboAzbtype
from .abo_vistype import AboVistype


@dataclass(kw_only=True)
class AktiveAbosType:
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
            ),
        },
    )
