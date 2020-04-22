
import os.path
#Exercici2
def comptarParaules(contingut):
  #TODO Heu de retornar el nombre de paraules que té un text
  comptador = 0
  for i in contingut:
    if(i == " "):
      comptador = comptador + 1
     #Com podeu detectar una paraula, que el separa les paraules?
  return comptador

def comptarFrases(contingut):
  #TODO Heu de retornar el nombre de frases. 
  comptador = 0
  for f in contingut:
    if(f=="." or f ==";" or f == ":"):
      comptador = comptador + 1
  #Com es separen les frases?
  return comptador
def mitjanaParaulesPerFrase(contingut):
  mitjana = comptarParaules(contingut)/comptarFrases(contingut)
  return mitjana

#Exercici 3
def numeroParulesComplexes(contingut):
  #TODO Heu de retornar el nombre de paraules complexes que té el text
  complexos = 0
  for z in text:
    if(len(z)>5):
      complexos = complexos + 1 

  #Són aquelles que tenen méés de cinc lletres
  return complexos

def percetantgeParaulesComplexes(contingut):
  percentatge =100*((numeroParulesComplexes(contingut))/(comptarParaules(contingut))
  return percentatge

#TODO Fer-ho al final de tot el 5.
#Exericic 5 llegir configuració

#Exercici 1

print("Gràcies!")
resposta = ""
#TODO heu de completar el codi perquè la variable text tingui el contingut del fitxer
while(resposta!="És fitxer"):
  nomFitxer = input("Entra el nom de l'arxiu que vols analitzar")
  if (os.path.isfile("noticies/"+nomFitxer)):
    resposta ="És fitxer"
  else:
    resposta = "No és fitxer"
    print("No és fitxer")
text = open("noticies/"+nomFitxer,"r")
contingut= text.read()

#Per provar exercici 2 i 3 podeu posar-vos print aquíí per comprovar si es compta béé paraules, si compta frases, si es fa la mitja i si es detecten les complexes.

#Exercici 4
#càlcul de la fórmula
print(comptarParaules(contingut))
print(comptarFrases(contingut))
IndexBoira = 0.4 * (mitjanaParaulesPerFrase(contingut))(percetantgeParaulesComplexes(contingut))

#TODO  Pinteu index per pantalla 
print(IndexBoira)
#TODO Classifiqueu exercici segons índex
# Digueu com és el text seguint la taula https://en.wikipedia.org/wiki/Gunning_fog_inde
#TODO
#Heu de tancar el fitxer


