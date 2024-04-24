from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DeckNavigationPathTypeEnumeration(Enum):
    DECK_ENTRANCE_TO_DECK_SPACE = "deckEntranceToDeckSpace"
    DECK_ENTRANCE_TO_SPOT = "deckEntranceToSpot"
    SPOT_TO_DECK_SPACE = "spotToDeckSpace"
    SPOT_TO_DECK_ENTRANCE = "spotToDeckEntrance"
    SPOT_TO_SPOT = "spotToSpot"
    OTHER = "other"
