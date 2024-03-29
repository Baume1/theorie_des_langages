import graphviz
import os
os.environ["PATH"] += os.pathsep + '../bin'

class Automate:
    #---------------------------Manipulation de données---------------------------------
    def __init__(self, alphabet):
        self.alphabet = set(alphabet)
        self.etats = set()
        self.etats_init = set()
        self.etats_term = set()
        self.transitions = []
        
    def __str__(self):
        print("Alphabet : ", self.alphabet)
        print("Etats : ", self.etats)
        print("Etats initiaux : ", self.etats_init)
        print("Etats terminaux : ", self.etats_term)
        print("Transitions :")
        for transition in self.transitions:
            print("\t", transition[0], "--(" + self.str_symboles(transition[1]) + ")-->", transition[2])

    def ajouter_alphabet(self, liste):
        for element in liste:
            self.alphabet.add(element)

    def ajouter_etat(self, id, est_initial=False, est_terminal=False):
        """
        Ajoute un état à l'automate. 
        L'état est identifié par un identifiant unique. 
        L'état peut être initial et/ou terminal.
        """
        self.etats.add(id)
        if(est_initial):
            self.etats_init.add(id)
        if(est_terminal):
            self.etats_term.add(id)

    def ajouter_transition(self, source, symbole, destination):
        """
        Ajoute une transition à l'automate. 
        La transition est définie par un état source, un symbole de l'alphabet et un état destination. 
        Cette méthode peut lever une exception si la transition est invalide (état source ou destination non existante, symbole
        non présent dans l'alphabet)
        """
        for transition in range(len(self.transitions)):
            if(self.transitions[transition][0] == source and self.transitions[transition][2] == destination):
                self.transitions[transition][1] += tuple(symbole)
                return
        self.transitions.append([source, tuple(symbole), destination])

    def symbole_transition(self, source, destination):
        for transition in range(len(self.transitions)):
            if(self.transitions[transition][0] == source and self.transitions[transition][2] == destination):
                return self.transitions[transition][1]
        return None

    def destination_transition(self, source, symbole):
        for transition in range(len(self.transitions)):
            if(self.transitions[transition][0] == source and symbole in self.transitions[transition][1]):
                return self.transitions[transition][2]
        return None
    
    #----------------------------Récupérer les infos en string------------------------------
    
    def str_symboles(self, liste_symboles):
        """
        Retourne une chaîne de caractères représentant les symboles de la liste donnée.
        
        Args:
            liste_symboles (list): Liste des symboles à convertir en chaîne.
            
        Returns:
            str: Chaîne de caractères représentant les symboles séparés par des virgules.
        """
        symboles = ''
        if(len(liste_symboles) > 1):
            for symbole in range(len(liste_symboles) -1):
                symboles += liste_symboles[symbole] + ","
            symboles += liste_symboles[symbole + 1]
        else:
            symboles += liste_symboles[0]
        return symboles
    
    def str_alphabet(self):
        """
        Retourne une chaîne de caractères représentant l'alphabet.
        
        Returns:
            str: Chaîne de caractères représentant les lettres de l'alphabet séparées par des espaces.
        """
        str_finale = ""
        for lettre in self.alphabet:
            str_finale += lettre + " "
        return str_finale
    
    def str_etats(self):
        """
        Retourne une chaîne de caractères représentant les états.
        
        Returns:
            str: Chaîne de caractères représentant les états séparés par des espaces.
        """
        str_finale = ""
        for etat in self.etats:
            str_finale += etat + " "
        return str_finale
    
    def str_etats_init(self):
        """
        Retourne une chaîne de caractères représentant les états initiaux.
        
        Returns:
            str: Chaîne de caractères représentant les états initiaux séparés par des espaces.
        """
        str_finale = ""
        for etat in self.etats_init:
            str_finale += etat + " "
        return str_finale
    
    def str_etats_term(self):
        """
        Retourne une chaîne de caractères représentant les états terminaux.
        
        Returns:
            str: Chaîne de caractères représentant les états terminaux séparés par des espaces.
        """
        str_finale = ""
        for etat in self.etats_term:
            str_finale += etat + " "
        return str_finale
    
    def str_transitions(self):
        """
        Retourne une chaîne de caractères représentant les transitions.
        
        Returns:
            str: Chaîne de caractères représentant les transitions au format "état_initial label état_final" séparées par des sauts de ligne.
        """
        str_finale = ""
        for transition in self.transitions:
            for label in transition[1]:
                print(transition[0] + " " + label + " " + transition[2] + ' \n')
                str_finale += transition[0] + " " + label + " " + transition[2] + ' \n'
        return str_finale

    
    #-----------------------------Affichage avec graphViz------------------------------------------

    def to_dot(self):
        """
        #Retourne la description du graphe au format dot
        """
        dot = graphviz.Digraph()
        dot.attr(rankdir="LR")
        for cpt in range(1, len(self.etats_init) + 1):
            dot.node("__" + str(cpt) + "__", shape="point")
        
        pt_init = 1
        for etat in self.etats:
            dot.node(etat, shape="circle" if etat not in self.etats_term else "doublecircle")
            if(etat in self.etats_init):
                dot.edge("__" + str(pt_init) + "__", etat)
                pt_init += 1
        
        for transition in self.transitions:
            dot.edge(transition[0], transition[2], label=self.str_symboles(transition[1]))

        return dot
    
    def to_png(self, filename):
        """
        Génère l'image dans le fichier filename
        """
        dot = self.to_dot()
        dot.render(filename="../images/"+filename, format="png")

    #---------------------------------Sauvegarde et chargement-----------------------------------
    
    def sauvegarder(self, filename):
        """
        Sauvegarde l'automate dans un fichier .txt
        """
        fichier = open(filename+".txt", "w")
        fichier.write(self.str_alphabet() + '\n')
        fichier.write(self.str_etats() + '\n')
        fichier.write(self.str_etats_init() + '\n')
        fichier.write(self.str_etats_term() + '\n')
        fichier.write(self.str_transitions())
        fichier.close()

    def charger(self, filename):
        """
        Charge les informations d'un automate à partir d'un fichier texte.

        Args:
            filename (str): Nom du fichier texte contenant les informations de l'automate, sans l'extension '.txt'.

        Le fichier texte doit respecter le format suivant :
        Ligne 1 : Alphabet de l'automate, séparé par des espaces.
        Ligne 2 : Liste des états de l'automate, séparés par des espaces.
        Ligne 3 : Liste des états initiaux de l'automate, séparés par des espaces.
        Ligne 4 : Liste des états terminaux de l'automate, séparés par des espaces.
        Lignes suivantes : Transitions de l'automate, chacune sur une ligne séparée, au format 'état_initial symbole état_final'.

        Après avoir lu le fichier, les attributs suivants de l'objet automate sont mis à jour :
            - self.alphabet (set) : Ensemble des symboles de l'alphabet.
            - self.etats (set) : Ensemble des états de l'automate.
            - self.etats_init (set) : Ensemble des états initiaux de l'automate.
            - self.etats_term (set) : Ensemble des états terminaux de l'automate.
            - self.transitions (list) : Liste des transitions de l'automate, ajoutées à l'aide de la méthode self.ajouter_transition().
        """
        fichier = open("../"+filename+".txt", "r")

        #Récupérer l'alphabet à la ligne 1
        ligne = fichier.readline().split(" ")
        ligne.remove('\n') if '\n' in ligne else ''
        self.alphabet=(set(ligne))

        #Récupérer la liste des états à la ligne 2
        ligne = fichier.readline().split(" ")
        ligne.remove('\n') if '\n' in ligne else ''
        self.etats=(set(ligne))

        #Récupérer la liste des états initiaux à la ligne 3
        ligne = fichier.readline().split(" ")
        ligne.remove('\n') if '\n' in ligne else ''
        self.etats_init=(set(ligne))

        #Récupérer la liste des états terminaux à la ligne 4
        ligne = fichier.readline().split(" ")
        ligne.remove('\n')
        self.etats_term=(set(ligne))

        #Récupérer la liste des transitions sur le reste des lignes
        while(ligne[0] != ''):
            ligne = fichier.readline().split(" ")
            self.ajouter_transition(ligne[0], ligne[1], ligne[2]) if ligne[0] != '' else ''
        
        fichier.close()

    #-----------------------------Finaliser l'automate-----------------------------------------
    def completer(self):
        self.ajouter_etat("puit")

        for etat in self.etats:
            for symbole in self.alphabet:
                for transition in self.transitions:
                    if (transition[0] == etat and symbole not in transition[1]):
                        self.ajouter_transition(etat, symbole, "puit")
