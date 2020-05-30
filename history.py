
a.sekilBilgisi()
a.sekilAlani()
a.sekilCevresi()
print("---------------")
b.sekilBilgisi()
b.sekilAlani()
b.sekilCevresi()
%clear
from abc import MLK, abstractmethod

class Sekil(MLK):
    @abstractmethod
    def sekilAlani(self):pass
    @abstractmethod
    def sekilCevresi(self):pass
    @abstractmethod
    def sekilBilgisi(self):pass      

class Altigen(Sekil):
    def __init__(self):pass
    def sekilAlani(self):
        print("AltÄ±gen SÄ±nÄ±fÄ±")
    def sekilCevresi(self):
        print("AltÄ±gen SÄ±nÄ±fÄ±")
    def sekilBilgisi(self):
        print("AltÄ±gene Ait Metod Ã‡aÄŸÄ±rÄ±ldÄ±. AltÄ±genin Kenar UzunluÄŸu = 5") 


class Kare(Sekil):
    
    
    
    def __init__(self):   
        self.__kenarUzunluk=5
    def getKenarBilgi(self):
        return self.__kenarUzunluk
    def sekilAlani(self):
        alan= self.__kenarUzunluk * self.__kenarUzunluk
        print("Karenin AlanÄ±",alan)
    def sekilCevresi(self):
        cevre= self.__kenarUzunluk * 4
        print("Karenin Ã‡evresi",cevre)
    def sekilBilgisi(self):    
        print("Karenin Kenar UzunluÄŸu =",self.__kenarUzunluk)





class Daire(Sekil):
    def __init__(self):
        self.__yariCap=5
        self.pi=3.14
    def getYariCap(self):
        return self.__yariCap
    def sekilAlani(self):
        alan = self.__yariCap**2 * self.pi 
        print("Karenin AlanÄ±",alan)
    def sekilCevresi(self):
        cevre= 2*self.pi*self.__yariCap
        print("Karenin Ã‡evresi",cevre)
    def sekilBilgisi(self):    
        print("Dairenin YarÄ± Ã‡apÄ± =",self.__yariCap)

c = Altigen()
c.sekilBilgisi()


a = Kare()
b = Daire()

a.sekilBilgisi()
a.sekilAlani()
a.sekilCevresi()
print("---------------")
b.sekilBilgisi()
b.sekilAlani()
b.sekilCevresi()
runfile('C:/Users/PC/Desktop/vizeler 2.sÄ±nÄ±f/VÄ°ZELERÄ°MMMMMMM/PythonProgramlama - SinavDosyasi/Melike TUNCER-1806001012/untitled1.py', wdir='C:/Users/PC/Desktop/vizeler 2.sÄ±nÄ±f/VÄ°ZELERÄ°MMMMMMM/PythonProgramlama - SinavDosyasi/Melike TUNCER-1806001012')

## ---(Thu May  7 16:39:45 2020)---
runfile('C:/Users/PC/Desktop/vizeler 2.sÄ±nÄ±f/VÄ°ZELERÄ°MMMMMMM/PythonProgramlama - SinavDosyasi/Melike TUNCER-1806001012/untitled0.py', wdir='C:/Users/PC/Desktop/vizeler 2.sÄ±nÄ±f/VÄ°ZELERÄ°MMMMMMM/PythonProgramlama - SinavDosyasi/Melike TUNCER-1806001012')

## ---(Fri May 15 21:09:38 2020)---
runfile('C:/Users/PC/.spyder-py3/temp.py', wdir='C:/Users/PC/.spyder-py3')

## ---(Fri May 22 14:03:36 2020)---
runfile('C:/Users/PC/.spyder-py3/temp.py', wdir='C:/Users/PC/.spyder-py3')
runfile('C:/Users/PC/.spyder-py3/temp.py', wdir='C:/Users/PC/.spyder-py3')

## ---(Fri May 22 14:27:45 2020)---
runfile('C:/Users/PC/.spyder-py3/temp.py', wdir='C:/Users/PC/.spyder-py3')
runfile('C:/Users/PC/.spyder-py3/temp.py', wdir='C:/Users/PC/.spyder-py3')
runfile('C:/Users/PC/.spyder-py3/temp.py', wdir='C:/Users/PC/.spyder-py3')

## ---(Fri May 22 18:32:15 2020)---
runfile('C:/Users/PC/.spyder-py3/temp.py', wdir='C:/Users/PC/.spyder-py3')

## ---(Thu May 28 15:26:42 2020)---
runfile('C:/Users/PC/.spyder-py3/temp.py', wdir='C:/Users/PC/.spyder-py3')

## ---(Sat May 30 22:47:24 2020)---
runfile('C:/Users/PC/.spyder-py3/temp.py', wdir='C:/Users/PC/.spyder-py3')