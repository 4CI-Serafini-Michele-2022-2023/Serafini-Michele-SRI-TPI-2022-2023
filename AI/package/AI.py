from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier
from icecream import ic

giocatori = read_csv('../flussi/giocatori.csv')
inp = giocatori.drop(columns=['videogame'])
out = giocatori['videogame']
modello = DecisionTreeClassifier()
modello.fit(inp.values, out.values)
età=int(input("Inserisci l'età della persona"))
genere=int(input("Dammi il genere"))
previsione = modello.predict([[genere,età]])
ic(previsione)