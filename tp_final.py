from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, nb_document:int, titre:str,annePublication:int):
        self.nb_document= nb_document
        self.titre= titre
        self.anneePublication=annePublication
        nb_document=0

    @abstractmethod
    def afficherInfos(self):
        pass
    def afficherNbDocument(self):

        nb_document+= 1
        print(f"nombre de documents : {nb_document}")

    class Genre ():
        def __init__(self,categorie):
            self.categorie=categorie

class Empruntable (ABC):
    def __init__(self):
        self.estEmprunte = False
    @abstractmethod
    def emprunter(self):
        pass
    @abstractmethod
    def rendre(self):
        pass

class Livre (Document,Empruntable):
    def __init__(self,annePublication, titre,auteur:str, nb_pages:int,genre:str):
            self.anneePublication=annePublication
            self.titre=titre
            self.auteur=auteur
            self.nb_pages=nb_pages
            self.genre=genre
    def afficherInfos (self):
        print(f"titre :{self.titre}, auteur : {self.auteur}, année de publication : {self.anneePublication}, nombre de pages : {self.nb_pages}")

    @classmethod
    def construc(self, titre, auteur,genre,nb_pages,annePublication):
            self.titre=titre
            self.auteur=auteur
            self.genre =genre
            self.nb_pages = 100
            self.annePublication=0

    def emprunter(self):
         return super().emprunter()
    def rendre(self):
         return super().rendre()
    
class Consultable (ABC):
    def __init__(self, auteur, nb_pages, genre):
        super().__init__(auteur, nb_pages, genre)
    @abstractmethod
    def consulter(self):
     pass

class Magazine (Document,Consultable):
    def __init__(self, nb_document, titre, annePublication,numero:int):
        super().__init__(nb_document, titre, annePublication)
        self.numero=numero
    def afficherInfos (self):
        print(f"titre :{self.titre}, année de publication : {self.anneePublication}")
    def consulter(self):
        print(f"consulter {self.titre}")


livre1= Livre(1800,"le rouge et le noir","stendal",300,"roman")
livre2= Livre(1980,"harry potter", " jk rowling",485,"roman")
livre3= Livre(1920,"le seigneur des anneaux", " tolkien",688,"fantasy")

magazine1= Magazine(1,"jv magazine",2021,25)
magazine2= Magazine(1,"paris match",2025,12)
magazine3= Magazine(1,"chasse et pêche",2014,40)

ma_liste_livre =[livre1,livre2,livre3]
ma_liste_magazine = [magazine1,magazine2,magazine3]

for livre in ma_liste_livre:
    livre.afficherInfos()

for magazine in ma_liste_magazine:
    magazine.afficherInfos()

magazine1.consulter()
