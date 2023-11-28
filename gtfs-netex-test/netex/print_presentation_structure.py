from dataclasses import dataclass, field
from typing import Optional
from netex.font_size_enumeration import FontSizeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PrintPresentationStructure:
    """
    Types describing common presentation properties for Print.

    :ivar colour: Default colour value for printed  graphics associated
        with ENTITY - e.g. of a LINE, e.g. CMYK.
    :ivar colour_name: Name of default colour value for printed graphics
        associated with entity., eg Pentone name
    :ivar colour_system: Name of colour system used for printed
        ColourName and TextColourName: for example, - RAL,
        https://en.wikipedia.org/wiki/RAL_colour_standard; - DIN 6164
        http://www.dtpstudio.de/atlas/farbsysteme/DIN%206164_bs00_3.htm;
        - Pantone (be aware that Pantone is proprietary), etc.
    :ivar background_colour: Default RGB background colour value for
        printed text and graphics associated with ENTITY - e.g. of a
        LINE.
    :ivar background_colour_name: Name of the backgropund colour value
        (in ColourSystem) for printed text and graphics associated with
        entity.
    :ivar text_colour: Default colour value for printed text associated
        with entity. CMYK.
    :ivar text_colour_name: Name of default colour value for printed
        text associated with entity,  in specified ColourSystem.
    :ivar text_font: Identifier of font for printed text.
    :ivar text_font_name: Name of font for printed text.
    :ivar text_language: Default language for printed text.
    :ivar font_size: Default language for printed text +v1.1.
    """
    colour: Optional[str] = field(
        default=None,
        metadata={
            "name": "Colour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    colour_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColourName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    colour_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColourSystem",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    background_colour: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "BackgroundColour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 6,
            "format": "base16",
        }
    )
    background_colour_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "BackgroundColourName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    text_colour: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextColour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    text_colour_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextColourName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    text_font: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextFont",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    text_font_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextFontName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    text_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextLanguage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    font_size: Optional[FontSizeEnumeration] = field(
        default=None,
        metadata={
            "name": "FontSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
