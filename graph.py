#!/usr/bin/env python

import random

class Graph(object):
    """
    Generates and stores the graph.
    Graph is assumed to be sparse.
    """
    def __init__(self,generator,initial):
        """
        @param generator: A generator that takes as input a node and yields each connected node.
        @param initial: The first node to search.  Should be usable as dictionary keys.
        """
        self.generator = generator
        self.indices = {}
        self.nodes = []
        self.unchecked = map(self.index,initial)
        while self.unchecked:
            self.CheckNode()
    def CheckNode(self):
        """
        Pops a value from self.unchecked,
          finds all associated values,
          then adds them into the graph.
        """
        index = self.unchecked.pop()
        node = self.node(index)
        newlinks = map(self.index,self.generator(node))
        self.nodes[index][1] = newlinks
        self.unchecked.extend(i for i in newlinks if i>index)
    def index(self,node):
        try:
            return self.indices[node]
        except KeyError:
            curr = len(self.indices)
            self.indices[node] = curr
            self.nodes.append([node,None])
            return curr
    def node(self,index):
        return self.nodes[index][0]
    def __len__(self):
        return len(self.nodes)
    def PageRank(self):
        """Implements a random walk to determine pagerank"""
        max_steps = int(1e6)
        reset = 0.15
        def random_jump():
            return random.randint(0,len(self)-1)
        counts = [0 for _ in self.nodes]
        current = random_jump()
        for i in xrange(max_steps):
            options = self.nodes[current][1]
            if not options or random.random()<reset:
                current = random_jump()
            else:
                current = random.choice(options)
            counts[current] += 1
        return [float(c)/max_steps for c in counts]
    def __str__(self):
        output = []
        for node,links in self.nodes:
            links = ', '.join(str(self.node(i)) for i in links)
            output.append('{} -> {}'.format(node,links))
        return '\n'.join(output)




if __name__=='__main__':
    def gen(x):
        return {
            'A':[],
            'B':['C'],
            'C':['B'],
            'D':['A','B'],
            'E':['B','D','F'],
            'F':['E','B'],
            'G':['B','E'],
            'H':['B','E'],
            'I':['B','E'],
            'J':['E'],
            'K':['E']
            }[x]
    g = Graph(gen,['A','B','C','D','E','F','G','H','I','J','K'])
    import IPython; IPython.embed()
