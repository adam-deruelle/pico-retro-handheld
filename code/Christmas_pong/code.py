######################################
# IMPORTATION DES DIFFERENTS MODULES #
######################################
# Modules Natifs
import time
import random
import supervisor
# Modules du dossier 'lib'
import Ressources_pong
import Gestion_controles

######################################
#  INSTANCIATION DES OBJETS UTILES   #
######################################
Pong = Ressources_pong.pong()
Controles = Gestion_controles.controles()

#################################
# AFFICHAGE DE L'ECRAN DE TITRE #
#################################
Pong.groupe_principal.append(Pong.ecran_titre_christmas)
Pong.groupe_principal.append(Pong.guirlande)
Pong.groupe_principal.append(Pong.bouton_start)

Pong.ecran.root_group = Pong.groupe_principal
time.sleep(0.5)
Pong.audio_pwm2.play(Pong.bruitage_intro)

#############################
# BOUCLE D'ATTENTE DE TITRE #
#############################
while Controles.bouton_start.value == Controles.relache :
    Pong.bouton_start.hidden = False
    time.sleep(0.5)
    Pong.bouton_start.hidden = True
    time.sleep(0.5)

###################################
# AFFICHAGE DE L'ECRAN DES REGLES #
###################################
# Libération de la RAM
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.ecran_titre_christmas))
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.bouton_start))
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.guirlande))


# Ajout de l'image de l'image de fond
Pong.groupe_principal.append(Pong.ecran_regles_christmas)

# Ajoute des labels au groupe principal pour l'affichage des règles
Pong.groupe_principal.append(Pong.label1_regles)
Pong.groupe_principal.append(Pong.label2_regles)
Pong.groupe_principal.append(Pong.label3_regles)
Pong.label3_regles.text = "Chaque joueur doit \nrenvoyer la balle\navec sa raquette.\nDeplacements haut \net bas uniquement"

# Ajoute le bouton de 'start'
Pong.groupe_principal.append(Pong.bouton_start)
time.sleep(1)

###############################
# BOUCLE D'ATTENTE DES REGLES #
###############################
while Controles.bouton_start.value == Controles.relache :
    Pong.bouton_start.hidden = False
    time.sleep(0.5)
    Pong.bouton_start.hidden = True
    time.sleep(0.5)
Pong.audio_pwm2.stop()
###############################
# AFFICHAGE DE L'ECRAN DE JEU #
###############################
# Libération de la RAM
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.ecran_regles_christmas))
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.label1_regles))
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.label2_regles))
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.label3_regles))
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.bouton_start))

# Ajout de l'image de fond du jeu
Pong.groupe_principal.append(Pong.ecran_jeu_christmas)

# Ajout des éléments graphiques du jeu
Pong.groupe_principal.append(Pong.score_g)
Pong.score_g.hidden = True

Pong.groupe_principal.append(Pong.score_d)
Pong.score_d.hidden = True

Pong.groupe_principal.append(Pong.raquette_d_christmas)
Pong.raquette_d_christmas.x = 150

Pong.groupe_principal.append(Pong.raquette_g_christmas)
Pong.raquette_g_christmas.x = 5

Pong.groupe_principal.append(Pong.balle_christmas)

####################
# VARIABLES DU JEU #
####################
fin_de_partie = False
sens_deplacement_balle_x = 1
sens_deplacement_balle_y = 1
joueur_marque = ""

# Initialisation des timers
timer_score = 0.0

###################
###################
## BOUCLE DE JEU ##
###################
###################
while not fin_de_partie :

    # Deplacement raquette droite
    if Controles.joystick_horizontal.value > 60000 and Pong.raquette_d_christmas.y > 9 : #( Pong.hauteur_ecran-10 - Pong.hauteur_raquette_christmas):
        Pong.raquette_d_christmas.y = Pong.raquette_d_christmas.y -1

    elif Controles.joystick_horizontal.value < 15000 and Pong.raquette_d_christmas.y < ( Pong.hauteur_ecran-12 - Pong.hauteur_raquette_christmas):
        Pong.raquette_d_christmas.y = Pong.raquette_d_christmas.y + 1

    # Deplacement raquette gauche
    if Controles.bouton_haut.value == Controles.appuye and Pong.raquette_g_christmas.y > 9 : #( Pong.hauteur_ecran-10 - Pong.hauteur_raquette_christmas):
        Pong.raquette_g_christmas.y = Pong.raquette_g_christmas.y -1

    elif Controles.bouton_bas.value == Controles.appuye and Pong.raquette_g_christmas.y < ( Pong.hauteur_ecran-12 - Pong.hauteur_raquette_christmas):
        Pong.raquette_g_christmas.y = Pong.raquette_g_christmas.y + 1

    #Deplacer la balle
    Pong.balle_christmas.x = Pong.balle_christmas.x + sens_deplacement_balle_x
    Pong.balle_christmas.y = Pong.balle_christmas.y + sens_deplacement_balle_y

    #Balle touche le bord gauche
    if (Pong.balle_christmas.x < 0) :
        #Retient qui a marqué
        joueur_marque = "J2"
        #Arret de la balle
        sens_deplacement_balle_x = 0
        sens_deplacement_balle_y = 0
        #Jouer le son
        Pong.audio_pwm2.play(Pong.bruitage_rebond_murs)
        #Augmenter le score
        Pong.score_d[0] += 1
        #Montrer les scores
        Pong.score_g.hidden = False
        Pong.score_d.hidden = False
        #Cache la balle
        Pong.balle_christmas.hidden = True
        #Position balle avant lancement
        Pong.balle_christmas.x = 90
        Pong.balle_christmas.y = 20
    #Attente du lancement pour le joueur 2
    if Controles.bouton_start.value == Controles.appuye and joueur_marque == "J2":
        #Montrer la balle
        Pong.balle_christmas.hidden = False
        #Sens vers le joueur qui a marqué
        sens_deplacement_balle_x = 1
        #Choisir aléatoirement la direction haut ou bas
        sens_deplacement_balle_y = random.choice([-1,1])

    #Balle touche le bord droit
    elif (Pong.balle_christmas.x > (Pong.largeur_ecran - Pong.diametre_balle_christmas)) :
        #Retient qui a marqué
        joueur_marque = "J1"
        #Arret de la balle
        sens_deplacement_balle_x = 0
        sens_deplacement_balle_y = 0
        #Jouer le son
        Pong.audio_pwm2.play(Pong.bruitage_rebond_murs)
        #Augmenter le score
        Pong.score_g[0] += 1
        #Montrer le score
        Pong.score_g.hidden = False
        Pong.score_d.hidden = False
        #Cacher la balle
        Pong.balle_christmas.hidden = True
        #La positioner pour repartir
        Pong.balle_christmas.x = 90
        Pong.balle_christmas.y = 20
    #Attente le lancement
    if Controles.bouton_droite.value == Controles.appuye and joueur_marque == "J1":
        #Montrer la balle
        Pong.balle_christmas.hidden = False
        #Sens vers le joueur qui a marqué
        sens_deplacement_balle_x = -1
        #Choisir aléatoirement la direction haut ou bas
        sens_deplacement_balle_y = random.choice([-1,1])

    if (Pong.balle_christmas.y < 8) or (Pong.balle_christmas.y > (Pong.hauteur_ecran-10 - Pong.diametre_balle_christmas)) :
        sens_deplacement_balle_y = -sens_deplacement_balle_y
        Pong.audio_pwm2.play(Pong.bruitage_rebond_murs)


    #Collison
    if (Pong.collision(Pong.raquette_g_christmas, Pong.balle_christmas) or
    Pong.collision(Pong.raquette_d_christmas, Pong.balle_christmas)):
        sens_deplacement_balle_x = -sens_deplacement_balle_x
        Pong.audio_pwm2.play(Pong.bruitage_rebond_raquette)

    #Si score afficher lancer timer_score
    if Pong.score_d.hidden == False or Pong.score_g.hidden == False :
        timer_score += 0.005
    #Si le timer arrive a 1s, on cache les scores
    if timer_score > 1 :
        Pong.score_g.hidden = True
        Pong.score_d.hidden = True
        #Reset du timer
        timer_score = 0.0
    #Premier joueur a 6 points gagne
    if Pong.score_d[0] > 5 or Pong.score_g[0] > 5:
        fin_de_partie = True
    time.sleep(0.009)

###############################
# AFFICHAGE DE L'ECRAN DE FIN #
###############################
# Libération de la RAM
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.ecran_jeu_christmas))
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.score_g))
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.score_d))
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.raquette_g_christmas))
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.raquette_d_christmas))
Pong.groupe_principal.pop(Pong.groupe_principal.index(Pong.balle_christmas))

# Ajout de l'image de fond de fin
Pong.groupe_principal.append(Pong.ecran_fin_christmas)

# Ajoute des labels au groupe principal pour l'affichage des scores
Pong.label_score_J1.text = str(Pong.score_g[0])
Pong.label_score_J2.text = str(Pong.score_d[0])
Pong.groupe_principal.append(Pong.label_score_J1)
Pong.label_score_J1.x += 15
Pong.groupe_principal.append(Pong.label_score_J2)
Pong.groupe_principal.append(Pong.label_score_slash)
Pong.audio_pwm2.play(Pong.bruitage_game_over)
###########################
# BOUCLE D'ATTENTE FINALE #
###########################
while True :
    if Controles.bouton_reset.value != Controles.appuye :
        supervisor.reload()
