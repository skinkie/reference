from typing import List

from lxml import etree
from tests.fixtures.books.fixtures import books
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import LxmlTreeSerializer

serializer = LxmlTreeSerializer()
result = serializer.render(books)

open("/tmp/test.xml", "wb").write(etree.tostring(result, pretty_print=True))

parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse("/tmp/test.xml", parser)
tree.write("/tmp/test2.xml", pretty_print=True)


context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
xml_parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

books_list: List[BookForm] = []
for book_xml in tree.finditer(".//{urn:books}book"):
    book: books.BookForm = xml_parser.parse(book_xml, books.BookForm)
    books_list.append(book)

lxml_serializer = LxmlTreeSerializer(context)

element = tree.find(".//{urn:books}book")
element.getparent().append(element, lxml_serializer.render(service_frame))
