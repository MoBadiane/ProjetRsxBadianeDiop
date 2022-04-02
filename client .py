#!/usr/bin/env python3
import json
import socket
import datetime


def openClientTunnel(host,
                     port,
                     buffer=4096):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("Connexion au serveur de MPSI/ISI")
    print(f'Connexion faite à: {datetime.datetime.now()}')
    print(f'Connexion faite via le port: {port} à l\'adresse: {host}')

    req = 0
    
    while True:

        reponse = client.recv(buffer)
        print(reponse.decode("utf-8"))
        req = input("")
        client.send(choix_str.encode("utf-8"))

        if req == "1":
            reponse = client.recv(buffer)
            print(reponse.decode("utf-8"))
            choix_str = input("")
            client.send(choix_str.encode("utf-8"))

            reponse = client.recv(buffer)
            print(reponse.decode("utf-8"))
            choix_str = input("")
            client.send(choix_str.encode("utf-8"))

            reponse = client.recv(buffer)
            print(reponse.decode("utf-8"))
            choix_str = input("")
            client.send(choix_str.encode("utf-8"))

            reponse = client.recv(buffer)
            print(reponse.decode("utf-8"))
            choix_str = input("")
            client.send(choix_str.encode("utf-8"))
        
        elif req == "2":
            reponse = client.recv(buffer)
            print(reponse.decode("utf-8"))
            choix_str = input("")
            client.send(choix_str.encode("utf-8"))

            reponse = client.recv(buffer)
            print(reponse.decode("utf-8"))
            choix_str = input("")
            client.send(choix_str.encode("utf-8"))

        elif req == "3":
            client.close()

    print("Connexion fermée")


if __name__ == '__main__':
    openClientTunnel("192.168.10.5", 50000)
