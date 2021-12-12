


# *args : waxaa loo soo gaabiyay arguments
# calamada xidigta waxay caddaynaysaa function-kaas inuu qaadanayo
# variables fara badan ama variable length

# tussale ahaan f
def arguments(*args): # function-kan waxaa ubaas gareeyay *args oo macnahedu ah variables badan ayuu qadan karaa
    print(args)

arguments('Mohamed',20,'Hodan',61518989,'JUST')

#-> output: (Mohamed,20,Hodan,61518989,JUST)
# wuxuu usoo celinaya qaab tuple ahaan  waxaad soo print gareeyn karta qeybta aad
# ubaahantahy adigoo isticmaalya index

# tusslo ahaan
def arguments(*args): # function-kan waxaa ubaas gareeyay *args oo macnahedu ah variables badan ayuu qadan karaa
    print(args[0])

arguments('Mohamed',20,'Hodan',61518989,'JUST')

# output: Mohamed
