from abc import ABC, abstractmethod
import uuid

class User(ABC):
    def __init__(self, user_name, user_last_name, mail):
        self.name = user_name
        self.last_name= user_last_name
        self.mail = mail

class GenerateurMatric(ABC):
    """
    def __init__(self):
        self.Matric = self.Gen_matric()

    @staticmethod
    def Gen_matric():
        return str(uuid.uuid4())

    """
    @abstractmethod
    def Gen_matric(self):
        pass




class Apc(GenerateurMatric, User):
    def __init__(self,user_name, user_last_name, mail):
        super().__init__(user_name, user_last_name, mail)
        self.Matric = self.Gen_matric()

    def Gen_matric():
        return str(uuid.uuid4())


    
        
class Etudiant(GenerateurMatric, User):
    def __init__(self,user_name, user_last_name, mail):
        super().__init__(user_name, user_last_name, mail)
        self.Matric = self.Gen_matric()

    def Gen_matric():
        return str(uuid.uuid4())


class SecCompte(GenerateurMatric,User):
    def __init__(self,user_name, user_last_name, mail):
        User.__init__(self,user_name, user_last_name, mail)
        self.Matric = self.Gen_matric()

    def Gen_matric():
        return str(uuid.uuid4())

        

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


"""
use= User("ilunga","Vainqueur","ilunga@gmail.com")
print(use)
"""

"""
lido = SecCompte("estha", "ether", "estha@gmail.com")
print(lido.Gen_matric())
"""

lido = SecCompte("ggg","huffd","hfhhfhf")
print(lido.Gen_matric())