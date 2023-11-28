from dataclasses import dataclass, field
from typing import Optional
from netex.info_links_rel_structure import InfoLinksRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PresentationStructure:
    """
    Types describing common presentation properties for Display.

    :ivar colour: Default RGB colour value for graphics associated with
        ENTITY - e.g. for a LINE.
    :ivar colour_name: Name of default colour value for graphics
        associated with ENTITY.
    :ivar colour_system: Name of colour system used for ColourName and
        TextColourName: for example, - RAL,
        https://en.wikipedia.org/wiki/RAL_colour_standard; - DIN 6164
        http://www.dtpstudio.de/atlas/farbsysteme/DIN%206164_bs00_3.htm;
        - Pantone (be aware that Pantone is proprietary), etc.
    :ivar background_colour: Default RGB background colour value for
        text and graphics associated with ENTITY - e.g. of a LINE.
    :ivar background_colour_name: Name of the background colour (in
        ColourSystem) for text and graphics associated with entity.
    :ivar text_colour: Default colour value for text associated with
        ENTITY.
    :ivar text_colour_name: Name of default colour value (in
        ColourSystem) for text associated with ENTITY.
    :ivar text_font: Identifier of font for text.
    :ivar text_font_name: Name of font for text.
    :ivar text_language: Default language for text.
    :ivar info_links: Hyperlinks associated with presentation.
    """
    colour: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Colour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 6,
            "format": "base16",
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
    text_colour: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TextColour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 6,
            "format": "base16",
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
    info_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "infoLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
