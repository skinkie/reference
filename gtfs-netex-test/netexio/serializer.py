from typing import T

class Serializer:
    sql_type = 'TEXT'

    def marshall(self, xml, clazz: T):
        pass

    def unmarshall(self, obj, clazz: T) -> T:
        pass