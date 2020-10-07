#-*-coding: utf8-*-
#Script permettant de jouer au sudoku et d'implanter le sudoku à la ligne n d'un fichier, pour cela, entrer en argument de ligne de commande : nom_fichier, numero_ligne

import sys
from Documents.PIT_python.PIT_sudoku_Borrelli_Julie.src.grid import SudokuGrid


def entre09 (valeurs):
	"""Vérifie que les valeurs sont comprises entre 1 et 9"""
	inter=True
	for i in valeurs:
		if not 1<=i<=9:
			inter=False
			break
	return inter


def remplissage(sudoku):
	"""Rempli une case du sudoku"""
	sudoku.__str__()
	info=[0,0,0]
	while not entre09 (info):
		info[0]=int(input("Saisir le numéro de la ligne, compris entre 1 et 9"))
		info[1]=int(input("Saisir le numéro de la colonne compris entre 1 et 9"))
		info[2]=int(input("Saisir le valeur à compléter compris entre 1 et 9"))
	if (info[0], info[1]) in sudoku.get_empty_positions():
		sudoku.write(info[0],info[1],info[2])
	else :
		chgt=input("Voulez-vous changer la valeur ? O/n")
		if chgt == 'O' or chgt =='o':
			sudoku.write(info[0],info[1],info[2])
################
#On regarde si des paramètres ont été rentrés en ligne de commande
param=True if len(sys.argv)>0 
#On crée une instance de la grille en fonction à l'aide des méthodes de classe.
if not param:
	grille=SudokuGrid.from_stdin()
else:
	grille=SudokuGrid.from_file(sys.argv[0], sys.argv[1])
#Remplissage du sudoku
while len(grille.get_empty_positions())!=0:
	remplissage(grille)
grille.__str__()
