#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint
import random

from pulp import *
import duckdb


with duckdb.connect("/tmp/test2.duckdb") as con:
  con.executemany("""
DROP TABLE IF EXISTS points;
CREATE TABLE points (id integer, name text);
INSERT INTO points VALUES (1, 'Ta');
INSERT INTO points VALUES (2, 'Tb');
INSERT INTO points VALUES (3, 'Tc');
INSERT INTO points VALUES (4, 'Td');

INSERT INTO points VALUES (0, 'Depot');

DROP TABLE IF EXISTS journeys;
CREATE TABLE journeys (id integer, departure integer, arrival integer, origin integer, destination integer);
INSERT INTO journeys VALUES (1, 7*3600 + 10*60, 7*3600 + 30*60, 1, 2);
INSERT INTO journeys VALUES (2, 7*3600 + 20*60, 7*3600 + 40*60, 3, 4);
INSERT INTO journeys VALUES (3, 7*3600 + 40*60, 8*3600 +  5*60, 2, 1);
INSERT INTO journeys VALUES (4, 8*3600 +  0*60, 8*3600 + 30*60, 4, 3);
INSERT INTO journeys VALUES (5, 8*3600 + 35*60, 9*3600 +  5*60, 3, 4);

DROP TABLE IF EXISTS deadheads;
CREATE TABLE deadheads (origin integer, destination integer, duration integer);
INSERT INTO deadheads VALUES (0, 1, 25);
INSERT INTO deadheads VALUES (0, 2, 25);
INSERT INTO deadheads VALUES (0, 3, 25);
INSERT INTO deadheads VALUES (0, 4, 25);
INSERT INTO deadheads VALUES (1, 0, 25);
INSERT INTO deadheads VALUES (2, 0, 25);
INSERT INTO deadheads VALUES (3, 0, 25);
INSERT INTO deadheads VALUES (4, 0, 25);


INSERT INTO deadheads VALUES (1, 1,  0);
INSERT INTO deadheads VALUES (1, 2, 15);
INSERT INTO deadheads VALUES (1, 3, 20);
INSERT INTO deadheads VALUES (1, 4, 20);
INSERT INTO deadheads VALUES (2, 1, 15);
INSERT INTO deadheads VALUES (2, 2,  0);
INSERT INTO deadheads VALUES (2, 3, 25);
INSERT INTO deadheads VALUES (2, 4, 10);
INSERT INTO deadheads VALUES (3, 1, 20);
INSERT INTO deadheads VALUES (3, 2, 25);
INSERT INTO deadheads VALUES (3, 3,  0);
INSERT INTO deadheads VALUES (3, 4, 15);
INSERT INTO deadheads VALUES (4, 1, 20);
INSERT INTO deadheads VALUES (4, 2, 10);
INSERT INTO deadheads VALUES (4, 3, 15);
INSERT INTO deadheads VALUES (4, 4,  0);

DROP TABLE IF EXISTS compatible_trips;
CREATE TABLE compatible_trips AS SELECT current.id AS current, onward.id AS onward, duration as deadhead_cost FROM journeys AS current, journeys AS onward, deadheads WHERE current.destination = deadheads.origin AND onward.origin = deadheads.destination AND (current.arrival + duration) <= onward.departure;
""")


problem = LpProblem('driver_scheduling', LpMinimize)
a = []
variables = []
costs = []

variables_for_destination = {}
variables_for_origin = {}

with duckdb.connect('/tmp/test2.duckdb') as con:
  con.execute("""SELECT current.id AS current, onward.id AS onward, duration as deadhead_cost FROM journeys AS current, journeys AS onward, deadheads WHERE current.destination = deadheads.origin AND onward.origin = deadheads.destination AND (current.arrival + duration) <= onward.departure;""")
  for row in con.fetchall():
    var_name = 'x,{},{}'.format(row[0], row[1])
    a.append(var_name)
    x = LpVariable(var_name, 0, 1, LpBinary)
    variables.append(x)
    costs.append((row[2] > 0) * 1)

    destination = variables_for_destination.get(row[1], [])
    destination.append(x)
    variables_for_destination[row[1]] = destination
    origin = variables_for_origin.get(row[0], [])
    origin.append(x)
    variables_for_origin[row[0]] = origin

  con.execute("""SELECT id FROM journeys;""")
  for row in con.fetchall():
    var_name = 'x,{},{}'.format('d', row[0])
    a.append(var_name)
    x = LpVariable(var_name, 0, 1, LpBinary)
    variables.append(x)
    costs.append(25)

    destination = variables_for_destination.get(row[0], [])
    destination.append(x)
    variables_for_destination[row[0]] = destination

    var_name = 'x,{},{}'.format(row[0], 'd')
    a.append(var_name)
    x = LpVariable(var_name, 0, 1, LpBinary)
    variables.append(x)
    costs.append(0)

    origin = variables_for_origin.get(row[0], [])
    origin.append(x)
    variables_for_origin[row[0]] = origin

problem += lpDot(costs, variables)
for k, xs in variables_for_destination.items():
  problem += pulp.LpConstraint(lpSum(xs), 0, "d{}".format(k), 1)
for k, xs in variables_for_origin.items():
  problem += pulp.LpConstraint(lpSum(xs), 0, "o{}".format(k), 1)

# Pulp gives a very nice string representation of the problem when printed.
print(problem)

solver = HiGHS_CMD(path="/opt/highs/bin/highs", keepFiles=True)
status = problem.solve(solver)
print(LpStatus[status])

# We have a solution, now look at the values of xs to determine which duties
# to use. Sum the cost for each used duty.
solution = []
total_cost = 0
for i, x in enumerate(variables):
  if x.value():
    solution.append(a[i])
    total_cost += costs[i]

pprint(solution)
solution = [x.split(',') for x in solution]
graphs = []
last_element = []

while len(solution) > 0:
  y = solution.pop(0)
  _x, t, s = y
  if t == 'd':
    graphs.append([''.join(y)])
    last_element.append(s)
  else:
    try:
      i = last_element.index(t)
      graphs[i].append(''.join(y))
      last_element[i] = s
    except ValueError:
      solution.append(y)
      pass

pprint(graphs)