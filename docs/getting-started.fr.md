# Installer le toolkit et préparer une première session

Ce toolkit associe un protocole de lecture, des questionnaires et les estimations de regard d'OpenFace. Il rend la collecte et le calcul inspectables. Pour le contexte de la mise en forme, consulter [RUMBA.RD sur le site de Pragma Learning Institute](https://pragmalearninginstitute.com/rumba-rd).

## Installer les composants

1. Installer Python 3.11 ou ultérieur avec Tk. Exécuter `python3 -m tkinter` : une petite fenêtre doit apparaître.
2. Créer un environnement virtuel et installer `requirements.txt`, comme dans le [README](../README.md).
3. Installer OpenFace depuis son [dépôt officiel](https://github.com/TadasBaltrusaitis/OpenFace). Le toolkit attend `build/bin/FeatureExtraction` sous `OPENFACE_ROOT`. Les étapes de compilation et les modèles dépendent du système ; suivre les instructions de la version choisie.
4. Vérifier la caméra dans votre environnement, puis fermer les logiciels susceptibles de l'occuper. Lancer `python experiment_runner.py` depuis la racine du dépôt.

Pillow sert à l'estimation facultative de luminance de l'écran, OpenCV à celle d'une caméra ambiante et sounddevice à l'enregistrement facultatif du microphone. L'installation de sounddevice peut nécessiter PortAudio. L'exécutable OpenFace réalise la collecte principale ; installer OpenCV seul ne le remplace pas.

## Répétition avec des données fictives

Choisir un identifiant tel que `DEMO-01`, sans nom réel. Le code accepte au maximum 64 caractères parmi lettres ASCII, chiffres, tirets et tirets bas, avec un premier caractère alphanumérique. Les chemins et formules ne sont pas acceptés comme identifiants.

Cliquer sur **Lancer OpenFace**, lire la confirmation de collecte, puis démarrer la calibration. Les deux blocs de cinq points précèdent la première lecture. Pendant la lecture, Entrée signale la fin. Les étapes suivantes comprennent une pause, les questions et l'échelle subjective. Échap demande l'arrêt de l'expérience.

Vérifier les fichiers créés avant d'organiser une session réelle : marqueurs de début/fin, présence du CSV OpenFace, rapport de police, géométrie et réponses. Une interface qui s'affiche ne prouve pas que le suivi du regard est exploitable.

## Configuration

| Variable | Usage |
| --- | --- |
| `OPENFACE_ROOT` | Dossier contenant `build/bin/FeatureExtraction` |
| `OPENFACE_DEVICE` | Caméra OpenFace, index `0` par défaut |
| `DATA_ROOT` | Dossier local des sessions, `./data` par défaut |
| `PLAN_CSV` | Plan des essais ; les chemins relatifs sont résolus depuis le dossier du plan |
| `FONT_FAMILY`, `SEMIBOLD_FAMILY` | Police de lecture et variante de demi-gras |
| `BASE_FONT_SIZE` | Taille, `24` par défaut |
| `TEXT_W_PCT`, `TEXT_H_PCT` | Fraction de la fenêtre réservée au texte, `0.70` chacune |
| `ENABLE_AUDIO` | `1` autorise l'enregistrement audio par les contrôles prévus |
| `ENABLE_SCREEN_LUMINANCE` | `1` active la mesure à partir d'une capture d'écran |
| `ENABLE_AMBIENT_CAMERA` | `1` active une caméra d'estimation de luminance ambiante |
| `AMBIENT_CAMERA_INDEX` | Index de cette caméra ; éviter le périphérique déjà utilisé par OpenFace |
| `TELEMETRY_HZ` | Fréquence demandée, `1.0` par défaut |

Les options auxiliaires restent désactivées par défaut. Une capture de luminance ne constitue pas une mesure photométrique calibrée. Ne pas activer deux lecteurs concurrents du même périphérique caméra. Définir explicitement un autre index si une caméra ambiante est réellement nécessaire.

## Résoudre les problèmes

| Symptôme | Vérification |
| --- | --- |
| OpenFace introuvable | Confirmer le chemin exact de `FeatureExtraction` et son droit d'exécution |
| Caméra indisponible | Autorisations du système, index, application concurrente |
| Tk manquant | Utiliser une distribution Python avec Tk compatible |
| Gras absent ou différent | Examiner `font_report.txt` et les polices effectivement installées |
| Aucun essai chargé | Vérifier les colonnes de `plan.csv` et les chemins relatifs |
| Résultats vides | Examiner les colonnes OpenFace, `success`, `confidence` et les marqueurs |
| Audio absent | Vérifier `ENABLE_AUDIO=1`, sounddevice, PortAudio et le périphérique sélectionné |

Une validation matérielle complète doit être refaite sur chaque poste. La publication ne certifie pas une compatibilité universelle avec toutes les versions d'OpenFace ou tous les systèmes.
