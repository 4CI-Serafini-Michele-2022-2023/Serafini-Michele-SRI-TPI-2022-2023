from pandas import read_csv
from sklearn import DecisionTreeClassifier

giocatori = read_csv('../flussi/giocatori.csv')
inp = giocatori.drop(columns=['videogame'])
out = giocatori['videogame']
modello = DecisionTreeClassifier()
modello.fit(inp.values, out.values)
età=input("Inserisci l'età della persona")
previsione = modello.predict([[0,età]])
print(previsione)