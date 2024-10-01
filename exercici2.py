class Person:
    def __init__(self, firstname, lastname):
        print("Constructor Super Classe - Person")
        self.firstname = firstname
        self.lastname = lastname
        self.abilities = []
    
    def add_ability(self, ability):
        #Ens referim amb self per a accedir al metode ability, abilities és una llista array buida de la classe Person, i el metode append agregar un element al final de la llista
        self.abilities.append(ability) #agrega una habilitat al array abilities
    
    #Com el metode info ha de mostrar la informació de la persona.
    def info(self):
        #retornarem amb string el nom i el cognom del atribut.
        return f"{self.firstname} {self.lastname}"

#La classe Candidate hereda tots els atributs i metodes de la classe Person  
class Candidate(Person):
    #Constructor de la classe Candidate
    def __init__(self, firstname, lastname, gender):
        Person.__init__(self, firstname, lastname) #Cridem al constructor Person i passara els atributs firstname, lastname i hem de ficar self al no ficar super
        #Agreguem un nou atribut
        self.gender = gender
        
    def info(self):
        #pronoun és per a referirse al Candidat com masculi o femeni
        pronoun = "Ell" if self.gender == "male" else "Ella"
        return f"{pronoun} és {self.firstname} {self.lastname}"
    
# Test Input
c1 = Candidate('Manel', 'Cantells', 'male')
c1.add_ability('JavaScript')
c1.add_ability('Python')

c2 = Candidate('Maria', 'Gironés', 'female')
c2.add_ability('PHP')

# Test Output
#Mostrem la informació del candidat
print(c1.info())
print(c1.abilities)
print(c2.info())
print(c2.abilities)
        
        
        
        