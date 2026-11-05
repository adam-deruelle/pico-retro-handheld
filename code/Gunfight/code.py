######################################
# IMPORTATION DES DIFFERENTS MODULES #
######################################

# Modules Natifs
import time
import random
# Modules du dossier 'lib'
import Ressources_gunfight
import Gestion_controles

############################
# DEFINITION DES FONCTIONS #
############################

#Fonction lancer animation tir et de touche de l'autre joueur
def tirer(joueur):
    animation_courrante_tir = 5
    if joueur == "J1" :
        animation_courrante_touche = 14
        while animation_courrante_tir < 8:
            Gunfight.sheriff[0] = animation_courrante_tir
            animation_courrante_tir +=1
            time.sleep(0.05)

        while animation_courrante_touche > 9 :
            Gunfight.bandit[0] = animation_courrante_touche
            animation_courrante_touche -= 1
            time.sleep(0.05)
    elif joueur == "J2" :
        animation_courrante_touche = 10
        while animation_courrante_tir < 8:
            Gunfight.bandit[0] = animation_courrante_tir
            animation_courrante_tir +=1
            time.sleep(0.05)

        while animation_courrante_touche < 15 :
            Gunfight.sheriff[0] = animation_courrante_touche
            animation_courrante_touche += 1
            time.sleep(0.05)
    else :
        animation_courrante_touche_j1 = 10
        animation_courrante_touche_j2 = 14
        while animation_courrante_tir < 8:
            Gunfight.bandit[0] = animation_courrante_tir
            Gunfight.sheriff[0] = animation_courrante_tir
            animation_courrante_tir +=1
            time.sleep(0.05)
        while animation_courrante_touche_j1 < 15 and animation_courrante_touche_j2 > 9 :
            Gunfight.sheriff[0] = animation_courrante_touche_j1
            animation_courrante_touche_j1 += 1
            Gunfight.bandit[0] = animation_courrante_touche_j2
            animation_courrante_touche_j2 -= 1
            time.sleep(0.05)
    time.sleep(0.75)

    Gunfight.bandit[0] = 0
    Gunfight.sheriff[0] = 0



######################################
#  INSTANCIATION DES OBJETS UTILES   #
######################################

# Création d'un objet 'Tutoriel' contenant les éléments graphiques
Gunfight = Ressources_gunfight.gunfight()

# Création d'un objet donnant accès aux contrôles (joystick et boutons)
Controles = Gestion_controles.controles()


#############################################
# AJOUT DES ELEMENTS GRAPHIQUES SUR L'ECRAN #
#############################################

# Ajoute une image de fond au groupe principal
Gunfight.groupe_principal.append(Gunfight.ecran_titre)

# Autres éléments
Gunfight.groupe_principal.append(Gunfight.bouton_start)
Gunfight.bouton_start.x = 29
Gunfight.bouton_start.y = 110
# les impacts de balles
Gunfight.groupe_principal.append(Gunfight.tir1)
Gunfight.groupe_principal.append(Gunfight.tir2)
Gunfight.groupe_principal.append(Gunfight.tir3)
Gunfight.groupe_principal.append(Gunfight.tir4)
Gunfight.groupe_principal.append(Gunfight.tir5)
# on les cache
Gunfight.tir1.hidden = True
Gunfight.tir2.hidden = True
Gunfight.tir3.hidden = True
Gunfight.tir4.hidden = True
Gunfight.tir5.hidden = True
# Affiche le groupe principal sur l'écran
Gunfight.ecran.root_group = Gunfight.groupe_principal

# joue le bruitage de l'écran titre
time.sleep(1)
Gunfight.audio_pwm1.play(Gunfight.bruitage_ecran_titre)

#############################
# BOUCLE D'ATTENTE DE TITRE #
#############################

while Controles.bouton_start.value == Controles.relache:
    Gunfight.bouton_start.hidden = False
    time.sleep(0.5)
    Gunfight.bouton_start.hidden = True
    time.sleep(0.5)

Gunfight.audio_pwm1.stop()
Gunfight.audio_pwm2.play(Gunfight.bruitage_start)

#Impacts des balles
Gunfight.tir1.hidden = False
time.sleep(0.5)
Gunfight.tir2.hidden = False
time.sleep(0.7)
Gunfight.tir3.hidden = False
time.sleep(1)
Gunfight.tir4.hidden = False
time.sleep(0.3)
Gunfight.tir5.hidden = False
time.sleep(1)

time.sleep(1)

########################
# AFFICHAGE DES REGLES #
########################
# Libération de la RAM
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.ecran_titre))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.bouton_start))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.tir1))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.tir2))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.tir3))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.tir4))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.tir5))

# Ajout de l'image de l'astronaute
Gunfight.groupe_principal.append(Gunfight.cowboy)
Gunfight.cowboy.y = Gunfight.hauteur_ecran - 96
Gunfight.cowboy.x = 90

# Ajoute des labels au groupe principal pour l'affichage des règles
Gunfight.groupe_principal.append(Gunfight.label1_regles)
Gunfight.label1_regles.y = 10
Gunfight.label1_regles.x = 5
Gunfight.groupe_principal.append(Gunfight.label2_regles)
Gunfight.label2_regles.y = 20
Gunfight.label2_regles.x = 5
Gunfight.groupe_principal.append(Gunfight.label3_regles)
Gunfight.label3_regles.y = 35
Gunfight.label3_regles.x = 5
Gunfight.label3_regles.text = "Tirer sur l'adver-\nsaire des que la\ncloche rententit\n J1 : droite\n J2 : start"

# Ajoute le bouton de 'start'
Gunfight.groupe_principal.append(Gunfight.bouton_start)
time.sleep(1)


###############################
# BOUCLE D'ATTENTE DES REGLES #
###############################

while Controles.bouton_start.value == Controles.relache :
    Gunfight.bouton_start.hidden = False
    time.sleep(0.5)
    Gunfight.bouton_start.hidden = True
    time.sleep(0.5)
time.sleep(1)


###############################
# AFFICHAGE DE L'ECRAN DE JEU #
###############################

# Libération de la RAM
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.cowboy))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.label1_regles))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.label2_regles))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.label3_regles))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.bouton_start))

# Ajout de l'image de fond du jeu
Gunfight.groupe_principal.append(Gunfight.ecran_jeu)

# Ajout des éléments graphiques du jeu
Gunfight.groupe_principal.append(Gunfight.label_score_J1)
Gunfight.label_score_J1.y = 15
Gunfight.label_score_J1.x = 40

Gunfight.groupe_principal.append(Gunfight.label_score_J2)
Gunfight.label_score_J2.y = 15
Gunfight.label_score_J2.x = Gunfight.largeur_ecran - 50

Gunfight.groupe_principal.append(Gunfight.cartouches)
Gunfight.cartouches.y = 10
Gunfight.cartouches.x = 60

Gunfight.groupe_principal.append(Gunfight.cloche)
Gunfight.cloche.y = 30
Gunfight.cloche.x = 70

Gunfight.groupe_principal.append(Gunfight.sheriff)
Gunfight.sheriff.y = 50
Gunfight.sheriff.x = -10

Gunfight.groupe_principal.append(Gunfight.bandit)
Gunfight.bandit.y = 50
Gunfight.bandit.x = 110

Gunfight.groupe_principal.append(Gunfight.label_avertissement)
Gunfight.label_avertissement.x = 10
Gunfight.label_avertissement.y = 110
Gunfight.label_avertissement.hidden = True

# Variables du jeu
fin_de_partie = False
score_J1 = 0
score_J2 = 0
Gunfight.cartouches[0] = 0
manche = 1
compteur_ralentissement_animation = 0

#################
# BOUCLE DE JEU #
#################
while not fin_de_partie :
    Gunfight.cloche[0] = 0
    duree_cloche = random.randint(2,15)
    while duree_cloche > 0 :
        compteur_ralentissement_animation += 1
        if compteur_ralentissement_animation >= 10 :
            compteur_ralentissement_animation = 0
            Gunfight.sheriff[0] = (Gunfight.sheriff[0] + 1) % 4
            Gunfight.bandit[0] = (Gunfight.bandit[0] + 1) % 4
        if Controles.bouton_haut.value == Controles.appuye or Controles.bouton_bas.value == Controles.appuye :
            Gunfight.label_avertissement.hidden = False
            duree_cloche = random.randint(2,15)
            time.sleep(1)
            Gunfight.label_avertissement.hidden = True
        time.sleep(0.025)
        duree_cloche -= 0.03
    Gunfight.cloche[0] = 1
    Gunfight.audio_pwm2.play(Gunfight.bruitage_cloche)
    time.sleep(1)
    Controles.LED_test.value = True
    Gunfight.label_avertissement.hidden = True
    tir_fait = False
    while not tir_fait :
        tir_J1 = Controles.bouton_haut.value == Controles.appuye
        tir_J2 = Controles.bouton_bas.value == Controles.appuye

        if tir_J1 or tir_J2 :
            Gunfight.audio_pwm2.play(Gunfight.bruitage_tir)
            time.sleep(1)
            tir_fait = True
            Controles.LED_test.value = False
        if tir_J1 and not tir_J2:
            score_J1 += 1
            tirer("J1")
        if not tir_J1 and tir_J2 :
            score_J2 += 1
            tirer("J2")
        if tir_J1 and tir_J2 :
            score_J1 += 1
            score_J2 += 1
            tirer("les deux")

        Gunfight.label_score_J1.text = str(score_J1)
        Gunfight.label_score_J2.text = str(score_J2)

        compteur_ralentissement_animation += 1
        if compteur_ralentissement_animation >= 10 :
            compteur_ralentissement_animation = 0
            Gunfight.sheriff[0] = (Gunfight.sheriff[0] + 1) % 4
            Gunfight.bandit[0] = (Gunfight.bandit[0] + 1) % 4
        time.sleep(0.025)

    if manche < 8 :
        Gunfight.cartouches[0] += 1
    else :
        fin_de_partie = True
    manche += 1
    time.sleep(0.05)

###############################
# AFFICHAGE DE L'ECRAN DE FIN #
###############################

# Libération de la RAM
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.ecran_jeu))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.label_score_J1))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.label_score_J2))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.cartouches))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.cloche))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.sheriff))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.bandit))
Gunfight.groupe_principal.pop(Gunfight.groupe_principal.index(Gunfight.label_avertissement))

# Ajout de l'image de fond de l'ecran fin
Gunfight.groupe_principal.append(Gunfight.ecran_fin)

# Ajout des éléments graphiques de la scene de fin en fonction du gagnant
if int(Gunfight.label_score_J1.text) > int(Gunfight.label_score_J2.text) :
    Gunfight.groupe_principal.append(Gunfight.portrait_J1)
    Gunfight.portrait_J1.x = 10
    Gunfight.portrait_J1.y = 30
    Gunfight.label_score_final.text = Gunfight.label_score_J1.text
    Gunfight.groupe_principal.append(Gunfight.label_score_final)
    Gunfight.label_score_final.x = 35
    Gunfight.label_score_final.y = 110

elif int(Gunfight.label_score_J1.text) < int(Gunfight.label_score_J2.text) :
    Gunfight.groupe_principal.append(Gunfight.portrait_J2)
    Gunfight.portrait_J2.x = 10
    Gunfight.portrait_J2.y = 30
    Gunfight.label_score_final.text = Gunfight.label_score_J2.text
    Gunfight.groupe_principal.append(Gunfight.label_score_final)
    Gunfight.label_score_final.x = 35
    Gunfight.label_score_final.y = 110
else :
    Gunfight.label_score_final.text = "Egalite"
    Gunfight.groupe_principal.append(Gunfight.label_score_final)
    Gunfight.label_score_final.x = 15
    Gunfight.label_score_final.y = 80

###########################
# BOUCLE D'ATTENTE FINALE #
###########################

while True:
    if Controles.bouton_reset.value == Controles.appuye :
        supervisor.reload()
    pass
