from typing import T
from utils import get_object_name, get_boring_classes, get_interesting_classes
import netex
netex.set_all = frozenset(netex.__all__) # This is the true performance step

class Serializer:
    sql_type = 'TEXT'

    def __init__(self):

        self.name_object = {}
        for clazz in get_boring_classes():
            self.name_object[get_object_name(clazz)] = clazz

        self.clean_element_names, self.interesting_element_names, self.interesting_classes = get_interesting_classes()
        for i in range(0, len(self.interesting_element_names)):
            # TODO: Validate duplicates, below will only make sure we overwrite with first order members
            self.name_object[self.interesting_element_names[i]] = self.interesting_classes[i]

    def marshall(self, xml, clazz: T):
        pass

    def unmarshall(self, obj, clazz: T) -> T:
        pass