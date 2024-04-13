from Automate import *
from partie_2 import *

#Test union d'automates
"""
automate = Automate.Automate([])
automate_2 = Automate.Automate([])
automate.charger("union1")
automate.to_png("automate1_union")
automate_2.charger("union2")
automate_2.to_png("automate2_union")

automate_final = Automate.Automate([])
automate_final = union_automates(automate, automate_2)
automate_final.to_png("test_union")
"""

#Test de concaténation d'automates
"""
automate = Automate.Automate([])
automate_2 = Automate.Automate([])
automate.charger("concat1")
automate.to_png("automate1_concat")
automate_2.charger("concat2")
automate_2.to_png("automate2_concat")

automate_final = Automate.Automate([])
automate_final = concat_automates(automate, automate_2)
automate_final.to_png("test_concat")
"""

#Test de répétition d'automate
"""
automate_3 = Automate.Automate([])
automate_3.charger("repet")

automate_final = repet_automate(automate_3)
automate_final.to_png("test_repet")
"""

# Test de la méthode completer()
"""
automate = Automate.Automate([])
automate.charger("concat1")
automate.to_png("automate_avant_completion")

automate.completer()
automate.to_png("automate_apres_completion")
"""

# Test de la méthode est_deterministe()
"""
# Automate déterministe
automate_det = Automate.Automate([])
automate_det.charger("concat1")
assert automate_det.est_deterministe()

# Automate non déterministe
automate_non_det = Automate.Automate([])
automate_non_det.charger("union1")
assert not automate_non_det.est_deterministe()
"""

# Test de la méthode determiniser()
"""
# Automate non déterministe
automate_non_det = Automate.Automate([])
automate_non_det.charger("union1")
automate_non_det.to_png("automate_non_deterministe")

# Déterminisation de l'automate
automate_non_det.determiniser()
automate_non_det.to_png("automate_determinise")
"""

# Test de la méthode accepte_mot()
"""
# Automate acceptant les mots en a*b
automate = Automate.Automate([])
automate.charger("concat1")

assert automate.accepte_mot('b')
assert automate.accepte_mot('ab')
assert not automate.accepte_mot('aab')
assert not automate.accepte_mot('ba')
assert automate.accepte_mot('abb')
"""

# Test accepter mot avec le mail
test = Automate.Automate([])
test.charger("test_mail")
print("Est-il déterministe ? :", "oui" if test.est_deterministe() else "non")

print(test.accepte_mot("steven.guillemet@lacatholille.fr"))
print(test.accepte_mot("charles.iacopino@lacatholille.fr"))
print(test.accepte_mot("lucien.mousin@lacatholille.fr"))

print(test.accepte_mot("trucmuche@lacatholille.fr"))