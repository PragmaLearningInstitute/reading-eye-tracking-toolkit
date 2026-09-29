# Lire les sorties et interpréter les métriques oculométriques

Le toolkit transforme les sorties d'OpenFace en indicateurs exploratoires. Les colonnes et unités de l'outil amont sont décrites dans la [documentation officielle OpenFace](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Output-Format). Pour les seuils et formules employés ici, la référence est `experiment_runner.py`.

## Fichiers d'une session

| Fichier | Contenu | Usage et limite |
| --- | --- | --- |
| `events.jsonl` | Événements de l'application | Trace complémentaire du déroulement |
| `markers.csv` | Phases et repères temporels | Segmenter les périodes ; synchronisation logicielle approximative |
| `of_session/*.csv` | Caractéristiques OpenFace | Données brutes de l'analyse, potentiellement sensibles |
| `qcm_*.csv`, `qcm_clicklog_*.csv` | Réponses, temps et changements de choix | Décrire le comportement sans assimiler hésitation et difficulté |
| `likert_*.csv` | Réponses subjectives | Confort déclaré, distinct d'une performance |
| `responses_raw.jsonl` | Texte capturé des réponses ouvertes avant neutralisation CSV | Source texte pour l'analyse ; conserver hors Git |
| `audio/*.wav` | Enregistrements facultatifs | Présents seulement si l'audio est utilisé |
| `font_report.txt` | Police de demi-gras retenue | Vérifier le rendu effectivement disponible |
| `layout_*.json` | Géométrie de la zone de texte | Relier le regard à la présentation |
| `telemetry.csv` | Indicateurs auxiliaires disponibles | Absence de valeur quand un capteur est désactivé ou indisponible |
| `calibration_report.json` | Ajustement affine et R² | Ajustement sur les données de calibration, pas validation indépendante |
| `gaze_norm_*.csv` | Coordonnées normalisées par essai | Lecture dans la zone de texte ; valeurs bornées à 0–1 |
| `metrics.csv` | Résumés par fichier OpenFace | Résumés de session, pas automatiquement par condition |

## Filtrage et calculs

`analyze_csv` conserve les lignes où `success == 1` et `confidence >= 0.8`. La durée rapportée va de la première à la dernière trame conservée : elle n'est pas la somme des durées effectivement observées. Les intervalles manquants restent à examiner.

Les angles horizontaux et verticaux sont lissés sur cinq échantillons. Une vitesse approximative est calculée à partir de la variation des deux angles et de l'intervalle temporel. Un seuil de 35 degrés par seconde sépare les segments candidats ; une durée minimale de 100 ms retient les fixations candidates. Ces paramètres décrivent un proxy de type I-VT, pas une validation du détecteur face à un oculomètre de référence. Le lissage par nombre de trames dépend de la cadence réellement obtenue.

`regressions_proxy` compte chaque diminution de l'angle horizontal lissé. Il ne détecte ni retour à un mot précédent ni saccade de régression linguistiquement identifiée. Le présenter comme un nombre de régressions de lecture serait trompeur.

Le taux de clignement repose sur les transitions 0→1 de `AU45_c`, si cette colonne existe, rapportées à la durée conservée. Les moyennes de pose utilisent `pose_Rx`, `pose_Ry`, `pose_Rz` lorsqu'elles sont présentes. L'absence d'une colonne n'est pas une valeur physiologique nulle.

## Comparer les conditions A et B

`metrics.csv` est calculé sur les fichiers OpenFace de la session entière. Calibration, questionnaires et pauses peuvent donc contribuer aux résumés. Pour une comparaison de lecture, il faut extraire les intervalles délimités par `reading_start` et `reading_end`, vérifier leur correspondance temporelle avec OpenFace et recalculer les mesures sur ces intervalles. Cette analyse comparative complète n'est pas automatisée par le résumé actuel.

Les fichiers `gaze_norm_*.csv` donnent une projection par essai, mais les coordonnées sont bornées à 0–1 : une valeur sur un bord ne distingue pas une fixation au bord d'un point projeté hors de la zone puis tronqué. Revenir aux angles et à la transformation non tronquée pour étudier les sorties de zone.

## Rapporter un résultat avec ses limites

Décrire la version d'OpenFace, le matériel, la cadence, les pertes, la lumière, la distance, les lunettes éventuelles, les paramètres et les exclusions. Examiner les traces avant d'interpréter les moyennes. Le R² de calibration peut sembler favorable sans assurer une précision hors des points ajustés.

Aucun fichier de cette collection ne permet seul d'établir un diagnostic de dyslexie ou un bénéfice causal de RUMBA.RD. Le toolkit permet d'inspecter un protocole et de préparer une analyse plus rigoureuse. [Pragma Learning Institute](https://pragmalearninginstitute.com/) fournit le contexte institutionnel ; les conclusions d'une étude exigent leur propre validation.
