import math
import mmh3
from bitarray import bitarray

class Bloom_Filter(object):
    def __init__(self, m , k):
        self.hash_num = k  #num of hash functions to use
        self.bit_num = m   #num of bits to use
        self.bFilter = bitarray(self.bit_num) #bit array of the given size
        self.bFilter.setall(0)    #initialize bits to 0

    def add(self, key):
        for seed in range(self.hash_num):
            item = mmh3.hash(key, seed) % self.bit_num
            self.bFilter[item] = True

    def probablyContains(self, key):
        for seed in range(self.hash_num):
            item = mmh3.hash(key, seed) % self.bit_num
            if self.bFilter[item] == True:
                return True
            else:
                return False

    def save(self, filename):
        array_to_01 = self.bFilter.to01()
        with open(filename + '.bin', "wb") as file:
            file.write(array_to_01.encode('ascii'))

    def restore(self, filename):
        with open(filename + '.bin', "rb") as file:
            array_values = file.read()
            self.bFilter = bitarray(array_values)
