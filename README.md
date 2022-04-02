# ProjetRsxBadianeDiop
Notre projet a pour but de mettre en place un dispositif permettant d'analyser un packet ,mettre en évidence la compréhension de l'encapsulation des données et l'utilisation des bibliothèques adéquates.

* Pour notre environnement technique nous avons eu à utiliser:
    * Un logiciel de virtualisation du nom de VMWARE pour deux machines ubuntu 20.04 () 
       * Sur la premiere machine qui est la machine Serveur on a installé un serveur de base de donnees mysql , on a aussi installé un iredmail.On a aussi installé                 bind9 et isc-dhcp-server pour les services dhcp et dns.On a aussi fixé l'adresse ip de la machine et configure les services DHCP et DNS.
       * Sur la deuxième machine qui est la machine cliente on a installé un serveur de base donnees et la machine serveur attribut à la machine cliente une adresse ip             par dhcp.

* Pour les scripts nous avons :
	* Des scripts .sh pour les dépendances mysql et iredmail:
		* INSTALL_MYSQL_DEPENPENCIES.SH :on démarre avec <code>./INSTALL_DEPENPENCIES.SH </code>
		* INSTALL_IREMAIL_DEPENPENCES.SH :on démarre ce fichier bash avec <code>bash iredmail.sh</code>
	* Des scripts python dont trois server.py ,client.py et database.py 

#### Mise en place du serveur
Pour la mise en place du serveur nous avons lesfonctions suivantes :
  * Inscription ::Fonction qui permet au serveur de recupérer les informations d'inscription d'un client.
  * Connexion::Fonction qui permet au serveur de recupérer les informations de connexion d'un client.
  * OpenServer::Fonction qui permet au serveur d'initialiser une connexion en attente d'un client et d'interagir avec celui ci
		en lui offrant les possibilités de s'inscrire, de se connecter ou de se déconnecter.

#### Mise en place du client
Pour la mise en place du client qui permet au client de créer un compte ou de se connecter.

#### Creation de la base de données 
* Notre base de données nommé <code>projetrsx</code>
* Nous avons une table du nom de <code>user</code> dans cette base de données
    * La table aura les colonnes suivantes:
        * <code>nom</code>
        * <code>prenom</code>
        * <code>mail</code>
        * <code>password</code>
