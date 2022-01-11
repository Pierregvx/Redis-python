import redis
import sys
import random
r = redis.Redis(host='localhost', port=6379, db=0)
liste = []
choice = {}

#STEP 1
def exec_menu(choix):
    ch = choix.lower()
    if ch == '':
        choice['main_menu']()
    else:
        try:
            choice[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            choice['menu']()
    return

def inputs():
    
    user=input("Username : ")
    pwd=input("Password : ")
    age=input("Age : ")
    loc = input("location : ")
    sex = input('gender : ')
    email=input("E-mail adress : ")
    postal = input("postal : ")
    return ["Username",user,"Password",pwd,"Age",age,"Location",loc,"Gender",sex,"E-mail",email,"Postal",postal]   

def signIn():
    i = inputs()
    liste = []
    liste.append(i)
    #=>ajouter l'individu
    ind="Individu"
    iden=random.randint(1,15343048)
    res=ind+":"+str(iden)
    delimiteur = ' '
    s = delimiteur.join(i)
    #print(res,s)
    print("Le numéro d'identification est :",res)
    r.set(res, s)
    print(r.get("0"))

def exit():
    sys.exit()

def menurinc():
    print("1 : sign in ")
    print("2 : register ")
    print("3 : leave")
    choix = input(">> ")
    exec_menu(choix)


#STEP 2
#Utilisation de sadd pour avoir des liens
#Faut utiliser 3 set 
def register():
    code=input("Quel est votre numéro  d'identification : ")
    while r.get(code)==None:
        print("Mauvais identifiant",code)
        code=input("Quel est votre numéro  d'identification : ")
    print("Bienvenue : ",r.get(code))
    choix=input("Voulez ajouter à un ami : (1 oui 2 non)")
    if choix==1 or choix=='1':
        ami=input("Quel est le numéro  d'identification de votre ami : ")
        while r.get(ami)==None:
            print("Mauvais identifiant",ami)
            ami=input("Quel est le numéro  d'identification de votre ami : ")
        r.sadd(code,ami)
    else:
        print("Au revoir !")

choice = {
    'menu':menurinc,
    '1':signIn,
    '2':register,
    "3":exit
}


if __name__ =="__main__":
    menurinc()

