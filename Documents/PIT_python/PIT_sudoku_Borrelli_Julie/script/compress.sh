#!/bin/bash
#Compresse l'espace de travail à l'exception de sudoku_db.txt

cd ../..
tar zcvf PIT_sudoku_Borrelli_Julie.tar.gz --exclude='sudoku_db.txt' PIT_sudoku_Borrelli_Julie/

