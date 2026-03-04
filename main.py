from pathlib import Path
import json

base = Path(__file__).parent
with open(base / "dati.json", "r", encoding="utf-8") as f:
    dati = json.load(f)

Lettere=dati["Lettere"]
#Lettere = [3,4,5,4,2,1,3,2,2,2,2,2,2,1,1,3,2]

lettereCopiate = Lettere
lettereCopiate.sort(reverse=True)
DimensioneBusta=dati["Dimensione"]
IndiceIniziale=0
indiceFinale=len(lettereCopiate)-1
ListaFinale=[]
ElementiAggiunti =0

while(ElementiAggiunti<len(lettereCopiate)):
    ListaFinale.append([lettereCopiate[IndiceIniziale]])
    ElementiAggiunti+=1
    while(sum(ListaFinale[IndiceIniziale])<DimensioneBusta):
        somma=sum(ListaFinale[IndiceIniziale])
        letterafinale=lettereCopiate[indiceFinale]
        if(somma+letterafinale<=DimensioneBusta):
            ListaFinale[IndiceIniziale].extend([lettereCopiate[indiceFinale]])
            indiceFinale -= 1
            ElementiAggiunti+=1
            if(indiceFinale<=IndiceIniziale):
                break
        else:
            break
    IndiceIniziale+=1

result = '-'.join(map(str, ListaFinale))
with open(base /"ListaFinale.txt", "w") as f:
  f.write(result)
