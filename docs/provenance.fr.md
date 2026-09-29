# Provenance, modifications et données

Cette édition provient du dépôt [Dyslexia-Focused-Study-Toolkit-Reading-Experiment](https://github.com/TimTrinche/Dyslexia-Focused-Study-Toolkit-Reading-Experiment), commit `a142ff991a45c49f77413beaa6052a2551d7b3ae`. Le programme historique porte la mention v5e. Cette publication conserve son protocole et explicite les limites de ses mesures.

## Modifications pour la publication

- Placement des textes et JSON dans `materials/`, conformément au plan, et résolution des chemins depuis le dossier du plan.
- Validation des identifiants avant leur emploi dans un chemin de fichier.
- Neutralisation des cellules CSV commençant par des caractères de formule, tout en conservant les nombres signés. Les réponses textuelles capturées sont également conservées dans un JSONL avant cette neutralisation.
- Désactivation par défaut des capteurs auxiliaires et de l'audio ; confirmation avant le démarrage OpenFace.
- Suppression des espaces superflus dans les en-têtes CSV OpenFace avant leur lecture.
- Création des dossiers de session avec des permissions restrictives lorsque le système les prend en charge.

## Données locales

Les sessions, enregistrements audio, caractéristiques faciales, réponses et journaux ne sont pas publiés. `.gitignore` empêche leur ajout accidentel dans les emplacements habituels mais ne remplace pas une vérification des fichiers avant commit. Un dossier existant peut conserver ses permissions antérieures. Le disque, les sauvegardes et les accès du poste doivent être protégés selon le protocole de l'équipe.

Utiliser des pseudonymes et conserver toute table de correspondance séparément. Déterminer les capteurs utiles, l'information des participants, la durée de conservation et les personnes ayant accès aux données avant de commencer. La fenêtre de confirmation du logiciel ne remplace pas ce travail.

## Dépendances et citation

OpenFace, ses modèles, Python et les bibliothèques conservent leurs propres licences. Les polices ne sont pas redistribuées. `CITATION.cff` identifie ce logiciel ; il ne fournit pas de DOI inventé ni de validation scientifique. La [documentation PLI](https://pragmalearninginstitute.com/outils/documentation) et [RUMBA.RD](https://pragmalearninginstitute.com/rumba-rd) présentent le contexte des outils.
