# 📒 Mon carnet de bord

**Nom : QUINQUET** 

**Prénom : Alinoé** 

**Adresse de mon site :** https://patronnino.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

> _Ma réponse :_ Sur PythonAnywhere

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Parce que le site est en ligne et disponible depuis n'importe quel appareil

Observations :
- 🧩 Défi : sans le guillemet de fin, Python ne peut plus lire le fichier et le site ne fonctionne plus. L'Error log indique `SyntaxError: unterminated string literal`, avec le numéro de la ligne fautive.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ le nom du domaine est "www.google.com". Le chemin est "/maps"

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ Le serveur m'envoie ce message pour me dire que cette route n'existe pas

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ Le site ne démarre plus du tout, donc toutes les pages affichent une erreur et non uniquement la route concernée. L'Error log indique `AssertionError: View function mapping is overwriting an existing endpoint function: loisirs`, ce qui veut dire que Flask refuse deux fonctions avec le même nom car il ne saurait plus laquelle utiliser.

Observations :
- `/blabla` renvoie une erreur 404, `/Presentation` aussi car les chemins sont sensibles aux majuscules, et `/presentation/` aussi car le `/` de fin en fait un autre chemin que `/presentation`.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur envoie uniquement du texte avec des balises, c'est ce qu'on voit avec Ctrl + U, alors que le navigateur interprète ces balises afin d'afficher une page mise en forme avec des titres, des listes et des images.

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ `<h1>` sert à faire le titre principal, `<p>` un paragraphe, `<ul>` une liste à puces et `<li>` chaque élément à l'intérieur de cette liste.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ Le serveur envoie seulement l'adresse de l'image dans la balise `<img>`, c'est donc le navigateur qui va la chercher lui-même sur le serveur de Wikimédia et non sur PythonAnywhere.

Observations :
- Sans le `</strong>`, le navigateur n'affiche aucune erreur : il se débrouille avec ce qu'il reçoit et le reste du texte passe simplement en gras.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Chacun peut travailler sur sa partie sans toucher à celle de l'autre : le développeur s'occupe du code Python et le graphiste du HTML, ce qui évite notamment de casser le site en modifiant simplement la présentation.

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Ils sont remplacés par le serveur, avant l'envoi de la page. On le vérifie avec Ctrl + U : dans le code source reçu par le navigateur, il n'y a plus de `{{ prenom }}` mais directement "Alinoé".

Observations :
- 🧩 Défi : `loisirs` est envoyé depuis Python et la boucle `{% for %}` crée un `<li>` par loisir, ajouter un loisir dans la liste suffit donc à mettre à jour la page.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ Le HTML décrit la structure de la page (titres, listes, liens) alors que le CSS décrit son apparence (couleurs, polices, marges), on peut donc changer tout l'aspect d'un site sans toucher à son contenu.

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ Trois fichiers : le HTML de la page, `style.css` et l'image du logo Python, qui vient d'un autre serveur. Le navigateur tente aussi de récupérer `favicon.ico`, ce qui fait une quatrième requête mais elle répond 404.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Le navigateur garde le fichier CSS en mémoire (le cache) afin de ne pas le retélécharger à chaque page, il peut donc continuer à utiliser l'ancienne version. Ctrl + F5 l'oblige à redemander le fichier au serveur.

Observations :
- `/static/style.css` affiche directement le texte du CSS, sans mise en forme.
- 🧩 Défi : `templates/base.html` contient le `<head>` et le menu, `accueil.html` et `presentation.html` le reprennent avec `{% extends "base.html" %}` et ne remplissent que leurs blocs.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP signifie HyperText Transfer Protocol. C'est le navigateur qui envoie la requête et le serveur qui envoie la réponse.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ Quatre requêtes : `presentation` (le document HTML), `style.css`, `Python-logo-notext.svg` (l'image, sur le serveur de Wikimédia) et `favicon.ico`.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ `200` veut dire que tout s'est bien passé et que le serveur renvoie bien ce qui est demandé. Le `404` de la favicon veut dire que le fichier n'existe pas : le navigateur cherche tout seul la petite icône de l'onglet et mon site n'en a pas.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ Ces modifications sont faites uniquement sur la copie de la page dans mon navigateur et non sur le serveur. Rien n'est envoyé au serveur, les autres visiteurs reçoivent donc toujours la page d'origine, et moi aussi dès que je recharge.

Observations :
- `favicon.ico` répond 404 car mon site n'a pas d'icône.
- Une fois le CSS en cache, `style.css` répond `304` : le fichier n'a pas changé donc le serveur ne le renvoie pas.
- 🧩 Défi : `Content-Type` vaut `text/html; charset=utf-8` pour `presentation` et `text/css; charset=utf-8` pour `style.css`. Cette information dit au navigateur comment traiter ce qu'il reçoit.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Le nom du paramètre est `search_query` et sa valeur est `chat`.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ `int()` ne peut pas transformer le texte "bonjour" en nombre, Python lève donc une `ValueError` et le serveur répond une erreur 500. Il faudrait vérifier la valeur avant de faire le calcul, par exemple avec un `try` / `except`, afin de renvoyer un message d'erreur à la place.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ Un visiteur peut injecter du HTML ou un script qui sera exécuté par le navigateur de la personne qui ouvre la page, par exemple si on lui envoie un lien piégé, ce qui peut notamment servir à voler des données. C'est le serveur de confiance qui l'affiche, donc le navigateur ne se méfie pas.

Observations :
- `/calcul` sans paramètres affiche `0 + 0 = 0` grâce à la valeur par défaut `0`. `/calcul?a=bonjour&b=4` renvoie une erreur 500 et l'Error log indique `ValueError: invalid literal for int() with base 10: 'bonjour'`.
- 🧩 Défi 1 : avec le template, `/bonjour/<button>Cliquez-moi` n'affiche plus de bouton mais le texte, et le code source contient `&lt;button&gt;`. Les caractères spéciaux sont remplacés automatiquement, le navigateur ne les interprète donc plus comme du HTML.
- 🧩 Défi 2 : `op` accepte `plus`, `moins`, `fois` et `divise`, par exemple `/calcul?a=6&b=3&op=fois` affiche `6 x 3 = 18`.

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ En GET, les données sont visibles dans l'URL (`/salut?prenom=Tom&ville=Lyon&couleur=teal`). En POST, l'URL reste `/salut` et les données passent dans le corps de la requête.

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ Pour une recherche je choisirais GET, car on peut copier l'URL, la partager ou la mettre en favori. Pour une connexion je choisirais POST, afin que le mot de passe n'apparaisse pas dans l'URL, donc ni dans l'historique ni dans les journaux du serveur.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ Non, on les voit en clair dans l'onglet Réseau (Charge utile). POST les retire de l'URL mais ne les chiffre pas, c'est le HTTPS qui protège les données pendant le trajet et non la méthode.

Observations :
- En POST, F5 fait demander au navigateur de confirmer le renvoi du formulaire, car recharger enverrait une deuxième fois les mêmes données.
- 🧩 Défi : la couleur choisie est envoyée avec le formulaire et appliquée à la réponse dans `templates/salut.html`. La réponse a un fond blanc, sinon le rouge `tomato` serait invisible sur le fond de mon site.

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ Une erreur `4xx` est une erreur du client : la demande n'est pas bonne (page qui n'existe pas, accès interdit). Une erreur `5xx` est une erreur du serveur : la demande peut être correcte mais le serveur plante, à cause d'un bug ou d'une panne.

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ Le serveur répond `302` avec un en-tête `Location` qui donne la nouvelle adresse, et c'est le navigateur qui fait tout seul la deuxième requête vers cette adresse. On le voit sur `/home` : une ligne `302` puis une ligne `200` sur `/`.

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ Quand un site change d'adresse, l'ancienne URL redirige vers la nouvelle afin de ne pas perdre les visiteurs et les liens existants. C'est aussi le cas quand un site renvoie de `http://` vers `https://`.

Observations :
- `/home` déclenche deux requêtes : `302` avec `Location: /`, puis `200` sur `/`. `/nimportequoi` affiche ma page mais le code reste `404`.
- Sans le `, 404`, le code devient `200` : pour un moteur de recherche, la page d'erreur ressemble alors à une vraie page qui existe et il peut la référencer.
- 🧩 Défi : `/secret` affiche maintenant `templates/403.html`. Le code `418` signifie "I'm a teapot" (je suis une théière) : c'est une blague du 1er avril 1998 (RFC 2324).

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ Mon adresse IP, mon navigateur et mon système d'exploitation (avec le `User-Agent`) et mes langues préférées (avec `Accept-Language`).

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ Wikipédia peut s'en servir afin de proposer directement la version de la page dans la langue du visiteur, sans qu'il ait besoin de la choisir.

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ La requête `GET /nimportequoi` a reçu un code 404. [à vérifier dans l'Access log sur PythonAnywhere]

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ La navigation anonyme porte mal son nom : elle évite surtout de garder l'historique sur mon ordinateur. Le serveur reçoit toujours mon adresse IP, mon navigateur et mes langues, et il note ma visite dans ses journaux, je ne suis donc pas anonyme pour lui.

Observations :
- Entre le téléphone et l'ordinateur, le `User-Agent` change, et l'adresse IP aussi si le téléphone est en 4G. Sur le même Wi-Fi, on a normalement la même adresse IP publique.

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ Une page HTML contient des balises que le navigateur met en forme, elle est destinée à des humains. Une réponse JSON contient des données brutes sans mise en forme (`Content-Type: application/json`), elle est destinée à des programmes.

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ Sur le serveur, c'est le Python de `flask_app.py` : les routes `/horloge` et `/api/heure`, qui calcule l'heure. Dans le navigateur, c'est le JavaScript de la balise `<script>` de `horloge.html`, qui appelle `/api/heure` toutes les secondes et met à jour le texte sans recharger la page.

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ YouTube : l'application envoie notamment ma recherche au serveur, qui lui répond avec des données sur les vidéos (titres, chaînes, miniatures, nombre de vues), et c'est l'application qui les met en forme.

Observations :
- `/api/heure` ne contient aucune balise HTML et son `Content-Type` est `application/json`.
- Sur `/horloge`, une nouvelle requête vers `/api/heure` part toutes les secondes, et la page entière n'est pas rechargée : `horloge` n'apparaît qu'une seule fois dans l'onglet Réseau.

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ Le navigateur envoie une requête HTTP au serveur qui correspond au nom de domaine, en donnant le chemin de la page et ses en-têtes. Le serveur cherche la route correspondante, exécute le code, remplit le template et renvoie un code de statut avec le HTML. Le navigateur interprète ce HTML, fait d'autres requêtes pour le CSS et les images, puis affiche la page.
