def hackH():
    print 'hi!'
def hackM():
    print 'hi!'
def hackE():
    print 'hi!'
def starter():
    dificulty=raw_input('>>')
    dif=dificulty
    if dif=='Easy':
        hackE()
    if dif=='Normal' or dif=='Medium':
        hackM()
    if dif=='Hard':
        hackH()
    else:
        starter()
starter()
