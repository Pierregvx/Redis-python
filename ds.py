import redis
import sys
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
    loc = input("location:")
    sex = input('gender :')
    email=input("E-mail adress: ")
    postal = input("postal :")
    return [user,pwd,age,loc,sex,email,postal]   
def signIn():
    a = inputs()
    liste = []
    liste.append(a)
    #=>ajouter l'individu
    #r.set(i[0][0], i[0].split())
def exit():
    sys.exit()
def menurinc():
    print("1 : sign in ")
    print("2 : leave")
    choix = input(">>")
    exec_menu(choix)

choice = {
    'menu':menurinc,
    '1':signIn,
    "2":exit
}

if __name__ =="__main__":
    menurinc()