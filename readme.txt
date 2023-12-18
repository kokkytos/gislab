cd στο gislab root dir και ενεργοποίηση του virtualenv:

conda activate gislab


Αλλαγές περιεχομένου στο ./content

Αν θέλω να αλλάξω την αυτοαρίθμηση στις λίστες των διπλωματικών:
M-x org-mode
Κλικ στην λίστα και C-c C-c

Compile με pelican -r content --ignore-cache --debug
Upload στον server τα περιεχόμενα του ./output

Για να δω τοπικά τα περιεχόμενα του ./output στο http://localhost:8000/:

cd output
python -m SimpleHTTPServer

