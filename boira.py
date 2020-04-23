
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
  for z in contingut:
    if(len(z)>5):
      complexos = complexos + 1 

  return complexos


def percetantgeParaulesComplexes(contingut):
  percentatge = 100*((numeroParulesComplexes(contingut))/(comptarParaules(contingut)))
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
IndexBoira = 0.4 * (mitjanaParaulesPerFrase(contingut))-(percetantgeParaulesComplexes(contingut))

#TODO  Pinteu index per pantalla 
print(IndexBoira)
if(round(IndexBoira) == 6):
  print("Sixth grade")
elif(round(IndexBoira) == 7):
  print("Seventh grade")
elif(round(IndexBoira) == 8):
  print("Eighth grade")
elif(round(IndexBoira) == 9 or round(IndexBoira) == 10 or round(IndexBoira) == 11 or round(IndexBoira) == 12):
  print("High school")
elif(round(IndexBoira) == 13 or round(IndexBoira) == 14 or round(IndexBoira) == 15 or round(IndexBoira) == 16 or round(IndexBoira) == 17):
  print("College")
#TODO Classifiqueu exercici segons índex
# Digueu com és el text seguint la taula https://en.wikipedia.org/wiki/Gunning_fog_inde
#TODO
#Heu de tancar el fitxer


