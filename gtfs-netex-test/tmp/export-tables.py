import inspect
from netex import models

clsmembers = inspect.getmembers(models, inspect.isclass)

with open('/tmp/overview.txt', 'w') as f:
    for member in clsmembers:
        if hasattr(member[1], '__dataclass_fields__'):
            f.write(member[0] + "\n")
            for attribute in sorted(list(member[1].__dataclass_fields__.keys())):
                f.write(attribute + "\n")
            f.write("\n")
