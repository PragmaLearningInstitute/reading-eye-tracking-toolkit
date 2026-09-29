# Comprendre et adapter le protocole de lecture

Le protocole livré est une séquence d'exemple, utile pour vérifier l'installation et les formats. Son plan figure dans `plan.csv` : A est étiqueté `plain`, B `formatted`. L'ordre du fichier est l'ordre de présentation ; aucune randomisation ni affectation de groupe n'est effectuée automatiquement.

## Déroulement effectif

1. Saisie d'un code participant et d'une catégorie de groupe.
2. Démarrage confirmé d'une seule session OpenFace et de la journalisation.
3. Deux blocs de calibration de cinq points, tous deux avant le premier texte.
4. Lecture du texte A ; Entrée marque la fin de lecture.
5. Pause, questions à choix pour les six premières questions, puis réponses ouvertes suivant le matériel, et échelle subjective.
6. Lecture et questionnaires des essais suivants dans l'ordre du plan.
7. Arrêt de la collecte et calcul des résumés disponibles.

Les choix `dys`, `control`, `autre` sont de simples étiquettes enregistrées par l'opérateur. Le logiciel ne détermine aucun diagnostic ni aucune admissibilité. Les réponses ouvertes peuvent être accompagnées d'audio si cette option a été activée.

## Matériel expérimental

Chaque ligne du plan contient `trial_id`, `condition`, `text_path`, `qcm_path`, `likert_path`. Les fichiers texte d'exemple utilisent du texte brut ou des balises `<strong>` pour l'emphase. Ils ne sont pas des pages HTML générales. Les JSON présents dans `materials/` donnent le format exact des questions attendu par le code.

Conserver une copie du plan et du matériel correspondant à chaque session. Si l'objectif est de comparer la typographie seule, contrôler les différences de contenu, longueur, difficulté, police et géométrie. Le plan A/B fourni ne suffit pas à séparer effet de texte, effet d'ordre et effet du formatage.

## Calibration et synchronisation

Les points affichés fournissent des associations entre angles estimés et positions d'écran. Le rapport ajuste une transformation affine et rapporte son adéquation sur les points utilisés. Cette adéquation n'est pas une précision validée sur de nouveaux points et ne remplace pas une validation indépendante.

Les marqueurs sont alignés sur une estimation du démarrage d'OpenFace. Ce mécanisme est logiciel : il n'offre pas une synchronisation matérielle à la milliseconde. Vérifier les délais et pertes de trames pour toute analyse fine des événements.

## Avant une étude

Définir la question principale, le contrebalancement, les critères d'exclusion, le traitement des données manquantes et l'analyse statistique avant la collecte. Réaliser une répétition complète. Conserver les paramètres de police et les dimensions de zone de texte, car une modification de mise en page change les zones d'intérêt.

Le [guide RUMBA.RD](https://github.com/PragmaLearningInstitute/rumba-rd/blob/main/docs/evaluation.fr.md) explique la reproductibilité du formatage. La [documentation PLI](https://pragmalearninginstitute.com/outils/documentation) relie ces outils ; elle ne remplace pas la définition d'un protocole de recherche propre à l'étude.
