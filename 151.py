import math, itertools
import networkx as nx
from pprint import pprint

counter = itertools.count(100)

def ne():
	return counter.next()

MINUS_M = [
		[2,  3,  4,  5],
		[    3,  4,  5],
		[        4,  5],
		[            5],
]

CORRECT = (2,3,4,5)

gr = nx.DiGraph()

INITIAL_NODE = (ne(), (5,))
PHI_START = 16

gr.add_node(INITIAL_NODE)
frontier = [ INITIAL_NODE ]


for phi in xrange(PHI_START, 2, -1):
	print 'phi:', phi
	new_frontier = [ ]
	corrects = [ ]
	for node in frontier:
		# print 'frontier node:', node
		for minus_cand in MINUS_M:
			negatives = minus_cand[1:]
			positive = minus_cand[0]
			if all(n in node[1] for n in negatives):
				new_node = list(node[1]) + [positive]
				for n in negatives:
					del new_node[new_node.index(n)]
				new_node = tuple(sorted(new_node))
				append_to_corrects = False
				if new_node == CORRECT:
					append_to_corrects = True
				new_node = (ne(), new_node)
				gr.add_node(new_node)
				evnoika = sum(1 for n in new_node[1] if n == positive)
				ola = len(new_node[1])
				prob = float(evnoika) / ola
				gr.add_edge(new_node, node, logprob = math.log(prob))
				new_frontier.append(new_node)
				if append_to_corrects:
					corrects.append(new_node)
	frontier = new_frontier

### pprint(frontier)
pprint(len(frontier))
pprint(len(corrects))

sum_prob = 0.
for sp in corrects:
	prob = math.exp( nx.shortest_path_length(gr, sp, INITIAL_NODE, weight = 'logprob') )
	# print prob
	sum_prob += prob

print sum_prob
