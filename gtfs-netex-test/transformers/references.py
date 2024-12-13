from netexio.attributes import update_attr, resolve_attr
from refs import getRef


def replace_with_reference_inplace(obj, path, klass=None):
    # TODO: Separate function
    split = []
    for p in path.split('.'):
        if p.isnumeric():
            p = int(p)
        split.append(p)

    attribute = resolve_attr(obj, split)

    # This does the assumption that the caller knows references would be allowed as type
    update_attr(obj, split, getRef(attribute, klass=klass))
