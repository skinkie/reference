from netexio.serializer import Serializer
from typing import T

import pickle

from netexio.xmlserializer import MyXmlSerializer

class MyPickleSerializer(Serializer):
    xmlserializer: MyXmlSerializer = MyXmlSerializer()
    sql_type = 'BINARY'

    def marshall(self, obj, clazz: T):
        if not getattr(obj, '__module__', None) == 'netex':
            obj = self.xmlserializer.unmarshall(obj, clazz)

        return pickle.dumps(obj, pickle.HIGHEST_PROTOCOL)

    def unmarshall(self, obj, clazz: T) -> T:
        return pickle.loads(obj)