# Commandes de travail (terminal)

À lancer dans un terminal ordinaire de l'ordinateur, une ligne après l'autre. Les lignes qui commencent par `#` sont des commentaires.

## 1. Se placer dans le dépôt

```bash
cd ~/Documents/github/UR_Business_Plan
```

## 2. Vérifier l'état du dépôt

```bash
git branch --show-current        # attendu : claude/business-plan-github-integration-011CUS76HRN8WURZ7PbpNU9M
git status --short               # liste des fichiers modifiés, ajoutés (??) ou effacés (D)
ls .git/index.lock 2>/dev/null && echo "Verrou git présent : si aucune commande git ne tourne, faire rm .git/index.lock"
```

## 3. Outils Python (une seule fois par ordinateur)

```bash
python3 -c "import yaml, markdown; print('Outils Python OK')"
# En cas d'erreur « No module named ... » :
sudo apt install python3-yaml python3-markdown python3-openpyxl
```

## 4. Régénérer le HTML de l'annexe 2

À faire après toute correction de la source (`ANNEX-02-Technical-Evidence.md`, `annexe-02-preuves/`, registres). On ne modifie jamais le HTML à la main.

```bash
python3 nouveau-business-plan/annexes/annexe-02-html/generer_html.py
```

## 5. Contrôle des sources

```bash
# Documents du nouveau plan : doit afficher « Erreurs : 0 »
python3 working-folder/controle-sources/verifier_sources.py --sans-parametres

# Contrôle complet, paramètres du modèle compris (erreurs héritées tant qu'ils ne sont pas re-sourcés)
python3 working-folder/controle-sources/verifier_sources.py

# Nouvel échantillon de trois chiffres à vérifier à la main (remplace l'échantillon précédent)
python3 working-folder/controle-sources/verifier_sources.py nouveau-business-plan/annexes/ANNEX-02-Technical-Evidence.md --sans-parametres --echantillon 3
```

## 6. Modèle financier (facultatif)

```bash
python3 working-folder/run.py
```

## 7. Ouvrir pour relire

```bash
xdg-open nouveau-business-plan/annexes/annexe-02-html/index.html     # l'annexe 2 (version de référence)
xdg-open working-folder/out/controle-sources.html                    # rapport du contrôle
xdg-open working-folder/out/echantillon-a-verifier.md                # échantillon de trois chiffres
xdg-open working-folder/out/rapport.html                             # rapport du modèle
```

## 8. Mettre à jour GitHub

```bash
git add -A
git status --short               # vérifier : pas de fichier inattendu
git commit -m "Message court qui dit ce qui a changé"
git push
```

Le `git push` envoie la branche de travail. Le site du modèle (ur.tapiscrm.xyz) n'est redéployé que lors d'une fusion dans `main`.

## 9. Contre-vérification par Codex

1. Application ChatGPT, projet Codex « vérification Urban Rig » : ouvrir une **nouvelle** conversation, en mode local (pas de worktree).
2. Coller le contenu de ce fichier :

```bash
cat nouveau-business-plan/annexes/notes-recherche-annexe-02/message-codex-contre-verification.md
```

3. Quand Codex a fini : refaire l'étape 8 pour envoyer son rapport (`working-folder/controle-sources/verifications/`) sur GitHub.
