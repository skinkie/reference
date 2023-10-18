from mro_attributes import unembed, list_attributes
from netex.alternative_texts_rel_structure import AlternativeTextsRelStructure

import netex
import inspect
members = inspect.getmembers(netex)
class_list = {x[0]:x[1] for x in members}

output = list_attributes(AlternativeTextsRelStructure, class_list, set([]))

# output = list_attributes(netex.DataSource, class_list)



print(output)