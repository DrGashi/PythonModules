from Module5.functionsAL import printoje

griting = "Pershnetje"
nejm = "Dren"

def grit():
    global griting
    griting = "Gudbaj"
    nejm = "Dren"
    mesejxh = f"{griting}, {nejm}"
    printoje(mesejxh)
grit()
printoje(griting)
printoje(nejm)