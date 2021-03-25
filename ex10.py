# class inheritance
class Mother:
    def __init__(self, dna='mother'):
        self.dna = dna
    
    def dna_test(self):
        return self.dna

m = Mother('mother-alone')
print(m.dna_test())

class Son(Mother):
    def __init__(self, dna='Son'):
        super().__init__(dna)

s = Son()
print(s.dna_test())    

    