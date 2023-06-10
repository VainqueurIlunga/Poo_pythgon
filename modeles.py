from abc import ABC, abstractmethod
import uuid

class User(ABC):
    def __init__(self):
        pass

class APC(User):
    pass
        
class Etudiant(User):
    pass

class SecCompt(User):
    pass

class GestionInscription:
    pass

class FicheInscription:
    pass

class Document:
    pass

class Promotion:
    pass

class Faculte:
    pass

class Departement:
    pass