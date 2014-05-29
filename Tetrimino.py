#!/usr/bin/env python

import numpy

class Tetramino(object):
    def __init__(self,name,rots):
        self.name = name
        self.ParseRots(rots)
    def ParseRots(self,rots):
        rotations = [[] for _ in xrange(4)]
        for line in rots.split('\n'):
            for rot,pat in zip(rotations,line.split()):
                rot.append(map(int,pat))
        self.rotations = [numpy.array(rot,dtype=numpy.int8) for rot in self.rotations]

tet_I = Tetramino(name='I',
                  rots = """0000 0010 0000 0100
                            1111 0010 0000 0100
                            0000 0010 1111 0100
                            0000 0010 0000 0100""")
tet_J = Tetramino(name='J',
                  rots = """200 022 000 020
                            222 020 222 020
                            000 020 002 220""")
tet_L = Tetramino(name='L',
                  rots = """003 030 000 330
                            333 030 333 030
                            000 033 300 030""")
tet_O = Tetramino(name='O',
                  rots = """44 44 44 44
                            44 44 44 44""")
tet_S = Tetramino(name='S',
                  rots = """055 050 000 500
                            550 055 055 550
                            000 005 550 050""")
tet_T = Tetramino(name='T',
                  rots = """060 060 000 060
                            666 066 666 660
                            000 060 060 060""")
tet_Z = Tetramino(name='Z',
                  rots = """770 007 000 070
                            077 077 770 770
                            000 070 077 700""")

colors = {1:(0,255,255),
          2:(255,0,0),
          3:(255,165,0),
          4:(255,255,0),
          5:(0,255,0),
          6:(128,0,128),
          7:(255,0,0)}
