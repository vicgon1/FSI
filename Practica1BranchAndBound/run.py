# Search methods

import search


ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.rya_graph_search(ab).path())
print(search.ryasub_graph_search(ab).path())

print("---------------------------------------------")

ob = search.GPSProblem('O', 'B'
                       , search.romania)

print(search.rya_graph_search(ob).path())
print(search.ryasub_graph_search(ob).path())

print("---------------------------------------------")

no = search.GPSProblem('N', 'O'
                       , search.romania)

print(search.rya_graph_search(no).path())
print(search.ryasub_graph_search(no).path())

print("---------------------------------------------")