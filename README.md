ytyhty
## ceci est une classe
from abc import ABC, abstractmethod
 #ceci est une class python 
class Document(ABC):
    def __init__(self, nb_document:int, titre:str,annePublication:int):
        self.nb_document= nb_document
        self.titre= titre
        self.anneePublication=annePublication
        nb_document=0
