


# **Kwargs: Waxaa Loo soo gaabiyay keyword arguments
# waa keyword iyo qiimihisa
# calamada (**) waxay cadaynayaa function-kaas inuu qaadanayo keyword arguments
# isla socdo wuxuuna usoo celinaya qaab dictionary ahaan

# tusaale

def keyword_args(**kwargs): # function-kaan waxan ubaas gareeyay kwargs
    print(kwargs)

keyword_args(name='Mohamed',age=20,address='hodan') #name: keyword,mohamed: argument

#output: {'name': 'mohamed', 'age': 20, 'address': 'hodan'}

# qaab dictionary ayuu usoo daabici doonaa

# si aad ugu bixisid dictionary una so aqrisid sida caadig ah
# waxaad ubaahantahay loop inaad isticmaasho

# using loop
def key_args(**kwargs):
    for data in kwargs:
        print(f'{data}: {kwargs[data]}')
key_args(name='ali',age=20)

# output:
# name : mohamed
# age : 20

