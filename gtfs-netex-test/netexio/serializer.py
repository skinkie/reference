import sys
from typing import T
import netex



class Serializer:
    sql_type = 'TEXT'

    def __init__(self):
        from netexio.dbaccess import get_interesting_classes

        self.clean_element_names, self.interesting_element_names, self.interesting_classes = get_interesting_classes()
        # TODO: Really rework get_interesting_classes, to automatically include this
        self.name_object = {}
        for x in self.interesting_element_names:
            try:
                self.name_object[x] = getattr(sys.modules['netex'], x)
            except:
                pass

    def marshall(self, xml, clazz: T):
        pass

    def unmarshall(self, obj, clazz: T) -> T:
        pass