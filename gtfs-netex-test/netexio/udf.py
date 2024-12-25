from netexio.attributes import resolve_attr
from netexio.serializer import Serializer
from transformers.references import split_path

def obj_attr_cmp_udf(serializer: Serializer, serialized: bytes, clazz: str, path: str, cmp: str) -> bool:
    deserialized = serializer.unmarshall(serialized, clazz)
    split = split_path(path)
    attribute = resolve_attr(deserialized, split)
    return attribute == cmp
