import Automate
from copy import deepcopy

#---------------------------------Traitement d'automates------------------------------------------------

def union_automates(automate_1:Automate, automate_2:Automate):
    """
    Fonction prenant deux automates en entrée et retournant leur union en créant un nouvel automate avec des 𝜖-transitions.
    Cette union implique la création d'un nouvel état initial lié aux états initiaux des deux automates d'origine, les transformant en états simples.

    Args:
        automate_1 (Automate): Premier automate à unir.
        automate_2 (Automate): Deuxième automate à unir.

    Returns:
        Automate: Nouvel automate représentant l'union des deux automates d'entrée.
    """
    #Initialiser le nouvel automate
    automate_final = Automate([])

    #Ajouter les deux alphabets
    automate_final.ajouter_alphabet(automate_1.alphabet)
    automate_final.ajouter_alphabet(automate_2.alphabet)

    #Ajouter les états (incrémenter de 1 pour le premier)
    decalage = 1
    for etat in automate_1.etats:
        automate_final.ajouter_etat(str(int(etat) + decalage), est_terminal=etat in automate_1.etats_term)
    #Ajouter les transitions en réutilisant le décalage
    for transition in automate_1.transitions:
        for symbole in transition[1]: #On itère sur le tuple s'il y a plusieurs symboles pour la "même" transition
            automate_final.ajouter_transition(str(int(transition[0]) + decalage), symbole, str(int(transition[2]) + decalage))
    
    #Faire la même chose avec le second automate en décalant de la taille de l'ancien automate pour éviter d'avoir des duplicatas
    decalage += len(automate_1.etats) #On ajoute la taille de l'ancien automate pour correctement décaler
    for etat in automate_2.etats:
        automate_final.ajouter_etat(str(int(etat) + decalage), est_terminal=etat in automate_2.etats_term)
    #Ajouter les transitions du second automate en réutilisant le décalage
    for transition in automate_2.transitions:
        for symbole in transition[1]: #On itère sur le tuple s'il y a plusieurs symboles pour la "même" transition
            automate_final.ajouter_transition(str(int(transition[0]) + decalage), symbole, str(int(transition[2]) + decalage))

    #On ajoute l'état initial
    automate_final.ajouter_etat(str(int(min(automate_final.etats)) -1), est_initial=True) #-1 pour qu'il soit pile juste avant le plus petit

    #On recommence avec le décalage mais cette fois-ci pour relier les anciens états initiaux au nouveau plus petit
    decalage = 1
    for etat_init in automate_1.etats_init:
        automate_final.ajouter_transition(min(automate_final.etats), "ε", str(int(etat_init) + decalage))
    
    #Pareil qu'avant avec l'ajout de la taile de l'ancien
    decalage += len(automate_1.etats)
    for etat_init in automate_2.etats_init:
        automate_final.ajouter_transition(min(automate_final.etats), "ε", str(int(etat_init) + decalage))

    return automate_final

def concat_automates(automate_1:Automate, automate_2:Automate):
    #Initialiser le nouvel automate
    automate_final = Automate([])

    #Ajouter les deux alphabets
    automate_final.ajouter_alphabet(automate_1.alphabet)
    automate_final.ajouter_alphabet(automate_2.alphabet)

    #Ajouter les états
    for etat in automate_1.etats:
        automate_final.ajouter_etat(etat, etat in automate_1.etats_init)
    #Ajouter les transitions en réutilisant le décalage
    for transition in automate_1.transitions:
        for symbole in transition[1]: #On itère sur le tuple s'il y a plusieurs symboles pour la "même" transition
            automate_final.ajouter_transition(transition[0], symbole, transition[2])
    
    #On initialise le décalage ici
    etat_int = int(max(automate_final.etats)) +1  #+1 pour qu'il soit pile juste après le plus grand
    #On ajoute l'état intermédiaire
    automate_final.ajouter_etat(str(etat_int))
    decalage = etat_int + 1 #Car on vient de rajouter un état

    #On ajoute les états du second automate
    for etat in automate_2.etats:
        automate_final.ajouter_etat(str(int(etat) + decalage), est_terminal=etat in automate_2.etats_term)
    #Puis on ajoute ses transitions avec le décalage
    for transition in automate_2.transitions:
        for symbole in transition[1]: #On itère sur le tuple s'il y a plusieurs symboles pour la "même" transition
            automate_final.ajouter_transition(str(int(transition[0]) + decalage), symbole, str(int(transition[2]) + decalage))
    
    #Maintenant on fait la liaison grâce à l'état intermédiaire
    for etat in automate_1.etats_term: #Des états finaux du premier automate
        automate_final.ajouter_transition(etat, "ε", str(etat_int))
        
    for etat in automate_2.etats_init: #Des états initiaux du second automate
        automate_final.ajouter_transition(str(etat_int), "ε", str(int(etat) + decalage))
    return automate_final

def repet_automate(automate:Automate):
    automate_final = deepcopy(automate) #Vu que rien n'est changé, on le copie juste (pas d'affectation sinon automate_final agit comme un pointeur)
    nouvel_etat = str(int(max(automate.etats)) + 1) #Le nouvel état est juste après l'état le plus "grand"
    automate_final.ajouter_etat(nouvel_etat, True, True) #Nouvel état terminal et initial
    
    #On relie le nouvel état vers tous les états initiaux
    for etat in automate.etats_init:
        automate_final.ajouter_transition(nouvel_etat, "ε", etat)

    #On relie tous les états terminaux vers le nouvel état
    for etat in automate.etats_term:
        automate_final.ajouter_transition(etat, "ε", nouvel_etat)
    return automate_final