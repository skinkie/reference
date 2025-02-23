from netexio.serializer import Serializer
from typing import T
import lz4.frame
import cloudpickle

from netexio.xmlserializer import MyXmlSerializer

class MyPickleSerializer(Serializer):
    xmlserializer: MyXmlSerializer = MyXmlSerializer()
    sql_type = 'BINARY'

    def __init__(self, compression: bool = True):
        Serializer.__init__(self)
        self.compression = compression

    def marshall(self, obj, clazz: T):
        if not getattr(obj, '__module__', None).startswith('netex.'): # TODO: can we just get the parent?
            obj = self.xmlserializer.unmarshall(obj, clazz)

        if self.compression:
            return lz4.frame.compress(cloudpickle.dumps(obj))
        else:
            return cloudpickle.dumps(obj)

    def unmarshall(self, obj, clazz: T) -> T:
        if self.compression:
            return cloudpickle.loads(lz4.frame.decompress(obj))
        else:
            return cloudpickle.loads(obj)