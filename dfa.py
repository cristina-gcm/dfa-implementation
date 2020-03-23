def checkWord(w, dfa, end):
    s = 0
    for c in w:
        if c == "#": # "#"=lambda
            continue
        if c in dfa[s]:
            s = dfa[s][c]
        else:
            print("Automatul nu accepta cuvantul dat.", s, c)
            return
    if s in end:
        print("Automaul accepta cuvantul dat.")


f = open("date.txt", 'r')
nr=int(f.readline())  #nr de tranzitii
start=int(f.readline()) #starea initiala
end=list() #lista cu starile finale
x=f.readline()
x=x.split()
for e in x:
    end.append(int(e)) #crearea unei liste cu starile finale
dfa={}
for i in range(0, nr):
    x = f.readline()
    x = x.split()
    if int(x[0]) in dfa:
        dfa[int(x[0])][x[2]] = int(x[1])
    else:
        dfa[int(x[0])] = {}
        dfa[int(x[0])][x[2]] = int(x[1])
#print(dfa)

w = input("Cuvantul introdus in automat este: ")
checkWord(w, dfa, end)
