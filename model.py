import random

class Model(object):
    def __init__(self):
        self._nmax=100 #numero massimo della ricerca
        self._Mmax=6 #numero massimo di tentativi
        self._Mrim=None
        self._segreto=None


    @property
    def Segreto(self):
        return self._segreto
    @property
    def Nmax(self):
        return self._nmax

    @property
    def Mmax(self):
        return self._Mmax

    @property
    def Mrim(self):
        return self._Mrim

    def inizializza(self):
        self._segreto=random.randint(1,self._nmax)
        print(self._segreto)
        self._Mrim=self._Mmax

    def indovina(self,tentativo):
        if self.Mrim==0:
            return (self.Mrim,None) #restituisco le vite rimaste e il risultato del tentativo
        else:
            self._Mrim=self._Mrim-1
        if (tentativo==self._segreto):
            return (self.Mrim,0)
        elif tentativo>self._segreto:
            return (self.Mrim,-1)  #segreto piu piccolo
        else:
            return (self.Mrim,1)
