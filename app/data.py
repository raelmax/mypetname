from models import Nome

l = []
arquivo = open('nomes_femeas')
for x in arquivo.readlines():
    l.append(x)
for a in l:
    newa = a.strip("\n").decode("utf-8", 'ignore')
    nome_ = Nome(nome=newa, tipo='femea')
    nome_.put()
