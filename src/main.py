from Automate import *
from partie_2 import *

#Test union d'automates
"""
automate = Automate([])
automate_2 = Automate([])
automate.charger("union1")
automate.to_png("automate1_union")
automate_2.charger("union2")
automate_2.to_png("automate2_union")

automate_final = union_automates(automate, automate_2)
automate_final.to_png("test_union")
"""

#Test de concaténation d'automates
"""
automate = Automate([])
automate_2 = Automate([])
automate.charger("concat1")
automate.to_png("automate1_concat")
automate_2.charger("concat2")
automate_2.to_png("automate2_concat")

automate_final = concat_automates(automate, automate_2)
automate_final.to_png("test_concat")
"""

#Test de répétition d'automate
"""
automate_3 = Automate([])
automate_3.charger("repet")

automate_final = repet_automate(automate_3)
automate_final.to_png("test_repet")
"""

test = Automate.Automate([])
test.charger("test_gros")
test.to_png("test_gros")