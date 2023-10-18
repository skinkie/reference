import inspect
import sys
import os

os.listdir("netex")

# members = inspect.getmembers(netex)
# class_list = [x[1] for x in members]

# print(class_list)
# with open(sys.argv[1]) as f:
all_files = ['.' + x.split('.py')[0]+' ' for x in os.listdir('netex') if x.endswith('.py')]

f = open(sys.argv[1], 'r')
all_lines = f.readlines()

all_classes = []

keep_printing = False
for l in all_lines:
    l = l.split('\n')[0]
    if keep_printing:
        print(l)
        if l.endswith(')'):
            keep_printing = False
        else:
            all_classes.append(l.split(' ')[-1])

    else:
        done = False
        for f in all_files:
            if f in l and done == False:
                print(l)
                if l.endswith('('):
                    keep_printing = True
                else:
                    all_classes.append(l.split(' ')[-1])
                done = True

print("__all__ = [")
for c in all_classes:
    print("   \"" + c + "\",")
print("]")