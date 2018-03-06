import numpy as np
import sys
import subprocess
from scipy.interpolate.interpolate_wrapper import block
from fractions import gcd

class Trace:

    def __init__(self,bk):
        self.traces = []
        self.G = {}
        # self.node_id = {}
        self.node_set = set()
        self.idMap = {}
        self.blocksize= bk
        
    def get_request(self):
        # r = []
        # for T in self.traces :
        #
        #     node_name = int(T['name'])
        #     size = T['size']
        #
        #     for i in range(int(size / self.page_size)) :
        #         r.append(self.get_node_id(node_name))
        #         node_name += self.page_size


        return self.traces

    # def get_node_name(self, node_id):
    #     return node_name[node_id]
    #
    # def get_node_id(self, node_name) :
    #     self.__map_node(node_name)
    #     return self.node_id[node_name]
    
    def getId(self, node):
        if node not in self.idMap :
            i = len(self.idMap)
            self.idMap[node] = i
        return self.idMap[node]
    
    def read(self, file_name) :
        f = open(file_name, 'r')
        # self.traces.clear()

        del self.traces[:]
        
        offsets = []
        sizes = []
        
        
        if file_name.endswith('.blkparse') :
            for line in f :
                try :
                    row = line.split(' ')
                    offsets.append(int[row[3]])
                    sizes.append(int[row[4]])
                except :
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    print(exc_type, exc_value, exc_traceback)

        elif file_name.endswith('.spc') :
            for line in f :
                try :
                    row = line.split(',')
                    offsets.append(int(row[1]))
                    sizes.append(int(row[2]))
                except :
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    print(exc_type, exc_value, exc_traceback)
            # print("=====================")
        elif file_name.endswith('.txt') :
            for line in f :
                x = int(line)
                self.traces.append(x)
                self.node_set.add(x)
                offsets.append(x)
                sizes.append(1)
        
        for off, sz  in zip(offsets, sizes) :
            numreq = sz / self.blocksize
            for i in range(0, numreq) :
                name = off + self.blocksize * i
                self.traces.append(name)
                self.node_set.add(name)
        
        
        
            
    def number_of_request(self):
        return len(self.traces)

    def unique_pages(self):
        return len(self.node_set)

    # def get_access_graph(self) :
        return self.__create_access_graph()

if __name__ == "__main__" :

    t = Trace()

    t.read('/home/giuseppe/cache_database/Financial1.spc')
