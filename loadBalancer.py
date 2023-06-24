# -*- coding: utf-8 -*-
"""
Implementazione del load balancer
"""
import threading
import socket


def least_connection():
    pass

class LoadBalancer(object):
    
#     """ Socket implementation of a load balancer.
#     Flow Diagram:
#     +---------------+      +-----------------------------------------+      +---------------+
#     | client socket | <==> | client-side socket | server-side socket | <==> | server socket |
#     |   <client>    |      |          < load balancer >              |      |    <server>   |
#     +---------------+      +-----------------------------------------+      +---------------+
#     Attributes:
#         ip (str): virtual server's ip; client-side socket's ip
#         port (int): virtual server's port; client-side socket's port
#         algorithm (str): algorithm used to select a server
#         flow_table (dict): mapping of client socket obj <==> server-side socket obj
#         sockets (list): current connected and open socket obj
#     """


    #Configurazione del load balancer
    def __init__(self):
        
        #indirizzo ip e porta dei server di backend
        
        #lista dei server attivi
        
        # N.B. utilizziamo una funzione che mi richiede i server presenti in quel momento, dal momento che si possono creare e distruggere
        self.servers=[]
        
        #Dizionario che mappa i collegamenti client - server
        self.dizionario={ }
        #porta in cui si mette in ascolto il server
        self.port=8888
        


    def gestione_comunicazione_client(self,client_socket):
        """
        Funzione che gestisce la comunicazione con ciascun client:
            il server riceve i dati, li elabora, e invia una risposta
        """
        while True:
            data=client_socket.recv(4096)
            if not data:
                break
            # Elabora la richiesta del client
            risposta = " Il server di load balancer risponde"
            client_socket.send(risposta.encode())
        client_socket.close()
        


    def creazione_socket_server(self):
        host= "" #il server è in ascolto su tutte le interfacce disponibili dell'host
        port=self.port
        # Creazione della socket del server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        #10 è il backlog, ovvero il numero massimo di richieste che possono essere in attesa
        server_socket.listen(10)
        print("Server di load balancing in ascolto su {}:{}".format(host, port))

        while True:
            client_socket, client_address = server_socket.accept()
            print("Connessione accettata da {}:{}".format(client_address[0], client_address[1]))
            # Avvia un thread separato per gestire il client
            client_thread = threading.Thread(target=self.gestione_comunicazione_client, args=(client_socket,))
            client_thread.start()
        self.gestione_comunicazione_client(client_socket)
        
        
    def attiva_server():
        pass 


if __name__ =='__main__':
    load_balancer=LoadBalancer()
    load_balancer.creazione_socket_server()


    # def accetto_connessioni(self):
    #     #accettazione delle connessioni del client in entrata sulla socket
    #     pass

    # def seleziona_server(self):
    #     #seleziona uno dei server backend disponibili utilizzando l'algoritmo di bilanciamento del carico scelto (least connection)
    #     pass
    # def inoltro_richieste_al_server(self):
    #     #inoltra la richiesta del client al server backend utilizzando una nuova connessione o una connessione esistente
    #     pass

    # def gestione_risposte(self):
    #     #trasmetti la risposta al client originale che ha effettuato la richiesta
    #     #Puoi utilizzare la socket del client originale per inviare la risposta al client
    #     pass
    # def gestisci_connessioni(self):
    #     #Gestisci le connessioni in arrivo e in uscita, monitorando le connessioni attive
    #     # e chiudendo eventuali connessioni inattive o problematiche
    #     pass

    # def monitoraggio_server(self):
    #     #Implementa funzionalità di monitoraggio per monitorare le prestazioni
    #     # dei server backend e il carico sul server di load balancing
    #     pass

    # def gestione_errori(self):
    #     #implementa la gestione degli errori per affrontare scenari come errori di connessione,
    #     # timeout, errori del server backend, ecc.
    #     pass

