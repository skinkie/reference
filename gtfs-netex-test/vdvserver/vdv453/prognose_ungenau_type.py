from enum import Enum


class PrognoseUngenauType(Enum):
    FAHRZEUG_IM_STAU = "Fahrzeug im Stau"
    TECHNISCHES_PROBLEM = "technisches Problem"
    DISPOSITIVE_MA_NAHME = "dispositive Maßnahme"
    FEHLENDE_AKTUALISIERUNG = "fehlende Aktualisierung"
