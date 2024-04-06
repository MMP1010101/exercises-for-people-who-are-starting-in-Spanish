import os

def modoNormal():

    import random
    import time
    import os 
    
    def printTime(text):
        i = 0
        while True:
            print(text[i], end="")
            time.sleep(0.15)
            i = i + 1
            if i == len(text):
                break

    os.system("cls") and os.system("clear")

    printTime("log dice:")
    var = random.randint(1,10)
    var2n1 = random.randint(1,10)
    var2n2 = random.randint(1,10)
    var3n1 = random.randint(1,10)
    var3n2 = random.randint(1,10)
    var3n3 = random.randint(1,10)

    user2 = 0
    user3 = 0

    atemps = 100000000
    baner = """

                                                                                 
                                                                                 
  ______   ______   ______   ______   ______   ______   ______   ______   ______ 
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/ 
                                                                                 
                                                                                 
.___ _______    _____________________________ ____________________               
|   |\      \  /  _____/\______   \_   _____//   _____/\_   _____/               
|   |/   |   \/   \  ___ |       _/|    __)_ \_____  \  |    __)_                
|   /    |    \    \_\  \|    |   \|        \/        \ |        \               
|___\____|__  /\______  /|____|_  /_______  /_______  //_______  /               
            \/        \/        \/        \/        \/         \/                
___________.____                                                                 
\_   _____/|    |                                                                
 |    __)_ |    |                                                                
 |        \|    |___                                                             
/_______  /|_______ \                                                            
        \/         \/                                                            
 _______   ____ ___  _____  _____________________ ________                       
 \      \ |    |   \/     \ \_   _____/\______   \\_____  \                      
 /   |   \|    |   /  \ /  \ |    __)_  |       _/ /   |   \                     
/    |    \    |  /    Y    \|        \ |    |   \/    |    \                    
\____|__  /______/\____|__  /_______  / |____|_  /\_______  /                    
        \/                \/        \/         \/         \/                     
                                                                                 
                                                                                 
  ______   ______   ______   ______   ______   ______   ______   ______   ______ 
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/ 
                                                                                 
                                                                                 

    """
    user = int(input(baner))
    while atemps != 0 and user != var:
        printTime("console: as fallado! intentalo de nuevo")
        print(var)
        time.sleep(1)
        os.system("cls") and os.system("clear")
        user = int(input(baner))
        atemps = atemps - 1

    printTime("has ganado unos 3 intentos mas")
    atemps += 3
    time.sleep(1)

    os.system("cls") and os.system("clear")

    user = int(input(baner))
    while atemps != 0 and user != var2n1 and user2 != var2n2:
        time.sleep(1)
        os.system("cls") and os.system("clear")
        print(var2n1)
        print(var2n2)
        user = int(input("Ingresa tu numero aqui: "))
        os.system("cls") and os.system("clear")
        user2 = int(input("\nIngresa tu segundo numero aqui: "))
        printTime("console: as fallado! intentalo de nuevo")
        atemps = atemps - 1

    printTime("has ganado unos 3 intentos mas")
    atemps += 1
    time.sleep(1)
    
    os.system("cls") and os.system("clear")

    user = int(input(baner))
    while atemps != 0 and user != var3n1 and user2 != var3n2 and user3 != var3n3:
        printTime("console: as fallado! intentalo de nuevo")
        time.sleep(1)
        os.system("cls") and os.system("clear")
        print(var3n1)
        print(var3n2)
        print(var3n3)
        user = int(input("Ingresa tu numero aqui: "))
        os.system("cls") and os.system("clear")
        user2 = int(input("Ingresa tu segundo numero aqui: "))
        os.system("cls") and os.system("clear")
        user3 = int(input("\nIngresa tu tercer numero aqui: "))

        atemps = atemps - 1
        if  user != var3n1 and user2 != var3n2 and user3 != var3n3:
            print("""


 __      __.___ _______  _____________________ 
/  \    /  \   |\      \ \_   _____/\______   
\   \/\/   /   |/   |   \ |    __)_  |       _/
 \        /|   /    |    \|        \ |    |   
  \__/\  / |___\____|__  /_______  / |____|_  /
       \/              \/        \/         \/ 

""")
            
print("""

  ________    _____      _____  ___________  
 /  _____/   /  _  \    /     \ \_   _____/  
/   \  ___  /  /_\  \  /  \ /  \ |    __)_   
\    \_\  \/    |    \/    Y    \|        \  
 \______  /\____|__  /\____|__  /_______  /  
        \/         \/         \/        \/   
    ____________   _________________________ 
    \_____  \   \ /   /\_   _____/\______   
     /   |   \   Y   /  |    __)_  |       _/
    /    |    \     /   |        \ |    |   
    \_______  /\___/   /_______  / |____|_  /
            \/                 \/         \/ 
                                            

""")
            
        


    

    
os.system("cls") and os.system("clear")

if __name__ == "__main__":
    modoNormal()