# Stammbaum-Programm
Dieses Programm ermöglicht die Verwaltung von Stammbäumen für Sims aus dem Spiel Sims 4. 

## Installation 
1. Erstell eine virtuelle Umgebung: 

'''bash
conda create --name Stammbaum python=3.12
conda activate Stammbaum

### Git-Commits:
Nachdem Änderungen am Code vorgenommen wurden, kann folgendes ausgeführt werden:

'''bash
# Zeig geänderte Dateien an
git status

# Geänderte Dateien dem Index hinzufügen
git add . 

# Ein Commmit vor nehmen
git commit -m "Erste Implementierung der Stammbaum-Klassen"

# Pushen vom Commit auf ein entferntes Repository 
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git branch -M main
git push -u origin main
