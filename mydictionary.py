""" 
Scrivere la classe MyDictionary che implementa gli operatori di dict riportati di seguito. MyDictionary
deve avere solo una variabile di istanza e questa deve essere di tipo lista. Per rappresentare le coppie, dovete
usare la classe MyPair che ha due variabili di istanza (key e value) e i metodi getKey, getValue, setKey,
setValue .
"""
    
import collections
from multiprocessing import Value
from operator import delitem, truediv

class MyDictionary():
    
    class MyPair():
            def __init__(self,key,value):
                self.key=key
                self.value=value
            
            def getKey(self):
                return self.key
        
            def getValue(self):
                return self.value
        
            def setValue(self, newValue):
                self.value=newValue
            def __str__(self):
                return"(" + str(self.key)+","+str(self.value)+")"
        
    def __init__(self):
        self.dlist=list()
    
    
    def __setitem__(self,key,value):
        
        if isinstance(key,collections.abc.Hashable):
            raise TypeError("unashable type:", str(type(key)))
        
        for p in self.dlist:
            
            if p.getKey()==key:
                p.setValue(value)
                return
            self.dlist.append(MyDictionary.MyPair(key,value))
            return
        
    def __getitem__(self,key):
        
        if isinstance(key,collections.abc.Hashable):
                raise TypeError("unashable type:", str(type(key)))
        
        for p in self.dlist:
            
            if p.getKey()==key:
                return p.getValue()
        raise KeyError(key)
    
    def __contains__(self, key):
        
        for item in self.dlist:
            if item.getKey()==key:
                return True
            return False
        
    def __eq__(self,d):
        #oppure si poteva usare contains
        for item in self.dlist:
            flag=False
            for item2 in d.dlist:
                if item2.getKey()==item.getKey() and item.getValue()==item2.getValue():
                    flag= True
                    break
            #se flag è false vuol dire che le chiavi e il valore non combaciano e quindi false
                if not flag: return False
            #se la lunghezza delle due lunghezza sono uguali dopo aver verificato che all'interno ci sono gli stessi valori ritorna true
        if len(self.dlist)==len(d.dlist):
            return True
                            
    def delitem(self,key):
        for i,item in enumerate(self.dlist):
            
            if item.getKey()==key:
                #self.dlist=self.dlist[:i]+self.dlist[i+1:]
                self.dlist.pop(i)
                return
            raise KeyError(key)
        
        
dic=MyDictionary()
dic["a"]='r'
dic["a"]='e'
print (dic['a'])
dic["b"]='d'
print(dic['b'])