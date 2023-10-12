from mro_attributes import list_attributes
from netex.data_source import DataSource

def create_widget(name, mytype, optional, default, field):
    print(name, mytype)
def create_multiwidget(name, mytype, optional, default, field):
    print("\n" + name + "\n-----")
    for name, type_optional, default, field in mytype:
        if type_optional is not None:
            mytype, optional = type_optional
            if type(mytype) == list:
                create_multiwidget(name, mytype, optional, default, field)
            else:
                create_widget(name, mytype, optional, default, field)
        else:
            print(name, 'failed')
    print("\n")

def print_attributes(dataclazz):
    mytype = list_attributes(dataclazz)
    create_multiwidget(dataclazz.__name__, mytype, None, None, None)

    """
    for name, type_optional, default, field in list_attributes(dataclazz):
        if type_optional is not None:
            mytype, optional = type_optional
            create_multiwidget()
            if type(mytype) == list:
                create_multiwidget(name, mytype, optional, default, field)
            else:
                create_widget(name, mytype, optional, default, field)
        else:
            print(name)
    """

print_attributes(DataSource)
