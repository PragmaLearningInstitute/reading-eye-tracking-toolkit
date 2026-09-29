# Validation de l'édition publique

Vérifications effectuées le 28 septembre 2026 sur la copie de publication. Les sources de production n'ont pas été modifiées.

## Vérifié

- Trois tests : neutralisation des formules dans les cellules CSV, conservation des mesures numériques signées, refus des identifiants utilisables comme chemins.
- Analyse syntaxique du programme Python et validité des JSON de matériel.
- Correspondance des chemins de `plan.csv` avec les fichiers livrés.
- Examen du filtrage OpenFace, des calculs de proxy, de la calibration et des frontières de collecte ; les limites sont décrites dans les guides.
- Exclusion des sessions, voix, caractéristiques faciales, journaux et fichiers de dépendances générés.

## Limites

Aucune collecte avec caméra ou microphone réel n'a été réalisée pendant la préparation. La chaîne OpenFace, la synchronisation, la calibration et le rendu plein écran demandent une répétition complète sur le matériel de l'étude. L'audit de sécurité est partiel. Les métriques ne sont pas validées contre un oculomètre de référence, ne donnent pas un diagnostic et ne démontrent pas un effet causal du formatage.
