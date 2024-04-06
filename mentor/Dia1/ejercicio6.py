"""
Desarrolla un programa que solicite al usuario ingresar una contraseña y verifique si es 
la contraseña correcta (supón que la contraseña correcta es "python").
"""
import os
import getpass
from secret.ejercicio6 import login_password

os.system("cls")

user = input("usuario: ")
password = getpass.getpass("password: ")

if user == "elran" and password == login_password:
    os.system("cls")
    print("""

    __________.______________ ___________   _______________ _______  .___________   ________   
    \______   \   \_   _____/ \      \   \ /   /\_   _____/ \      \ |   \______ \  \_____  \  
    |    |  _/   ||    __)_  /   |   \   Y   /  |    __)_  /   |   \|   ||    |  \  /   |   \ 
    |    |   \   ||        \/    |    \     /   |        \/    |    \   ||    `   \/    |    
    |______  /___/_______  /\____|__  /\___/   /_______  /\____|__  /___/_______  /\_______  /
            \/            \/         \/                 \/         \/            \/         \/ 
    ___________.____   __________    _____    _______                                          
    \_   _____/|    |  \______   \  /  _  \   \      \                                         
    |    __)_ |    |   |       _/ /  /_\  \  /   |   \                                        
    |        \|    |___|    |   \/    |    \/    |    \                                       
    /_______  /|_______ \____|_  /\____|__  /\____|__  /                                       
            \/         \/      \/         \/         \/                                        


    """)