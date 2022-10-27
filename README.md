<p align="center">
  <img src="https://user-images.githubusercontent.com/63207451/141209252-a98cc392-8831-4fbe-af90-61cb7eee8264.png" height="100">
  <img src="https://user-images.githubusercontent.com/63207451/141208795-3b0b5e6e-e014-4215-8ed2-fdd205ddfa41.png" height="100">
  <img src="https://user-images.githubusercontent.com/63207451/145711302-b7184614-9c46-43b1-9448-0640ecfdc6de.png" height="100">
  <img src="https://user-images.githubusercontent.com/63207451/118670736-29bd2980-b7f7-11eb-8aa4-ad41fa393ed1.png" height="100">
</p>

<br/>
<h1 align="center"> No-code AI platform </h1>
<br/>

<p align="center">
  <a href="https://share.streamlit.io/antonin-lfv/online_preprocessing_for_ml/main.py"><img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"/></a>
  </p>

<br/>

<p align="center">
  La <b>No-code AI platform</b> est un site développé avec <b>Python</b> et déployé avec <b>Streamlit</b>, qui permet de faire du Machine/Deep Learning sans écrire de code. La partie analyse et Machine Learning repose sur l'utilisation d'un dataset, qui peut être soit un dataset déjà disponible sur le site (les iris, ou les penguins), soit un dataset de votre choix que vous aurez uploadé, et avec qui vous pourrez effectuer du preprocessing directement depuis la page d'upload (Attention à bien re télécharger le dataset modifié et de le re uploader). Une fois le dataset choisi, vous pouvez l'utiliser pour alimenter des algorithmes tels que des SVM, des K-Means, des KNN ou encore des réductions de dimension.
<p/>
<br>

<p align="center">
<b>La No-Code AI Platform a été ensuite créée avec Flask et déployée sur Heroku, le repo est disponible <a href="https://github.com/antonin-lfv/No-code-AI-platform">ici</a></b>
  </p>
  
  <br>  <br>  <br>  <br>
  
> Pour accéder au site, cliquez sur le bouton **"Open in streamlit"** en haut du ReadMe

<br>

## Test du site en local

Clonez le repo puis, depuis le terminal au dossier du projet :

```bash
Streamlit run main.py
```

<br/>

## Mode d'emploi

Je vais détailler ici l'utilisation de la platform, avec des exemples pour chacune des pages. Pour commencer, voici la première par laquelle vous allez arriver. Sur la gauche se trouve la barre de navigation, vous permettant de vous déplacer au travers des pages. À partir de cette page, il vous faut charger des données sur la page **Dataset**, sous peine de ne pas pouvoir utiliser les autres pages.

<p align="center">
  <img width="850" alt="Capture d’écran 2022-10-27 à 23 28 53" src="https://user-images.githubusercontent.com/63207451/198401805-e4a95b7e-51d3-4579-ac6b-27d37d76494c.png">
  </p>

Détaillons maintenant la page Dataset. Sur cette page, vous allez choisir les données à utiliser. Pour ce faire, plusieurs choix s'offre à vous. Le premier est d'utiliser l'un des dataset proposés dont le type de problème (Classification ou Régression) est donné, le second est d'utiliser votre propre dataset que vous importerai en cliquant sur **Choisir un dataset personnel**.

<p align="center">
<img width="850" alt="Capture d’écran 2022-10-27 à 23 32 16" src="https://user-images.githubusercontent.com/63207451/198402345-a71ecd6a-debc-4e21-9f00-b1d0169b30d4.png">
  </p>


Si vous choisissez un dataset personnel, vous pourrez spécifier un séparateur si besoin, et modifier le dataset (il faudra retélécharger le dataset après modification). Dans le cas ou vous choisissez un dataset parmi ceux proposer, vous ne pourrez pas les modifier (ils sont déjà nettoyés).

<p align="center">
<img width="850" alt="Capture d’écran 2022-10-27 à 23 32 16" src="https://user-images.githubusercontent.com/63207451/198404597-41d4b83e-369c-4528-b511-a59047e31ec1.png">
  </p>
  
<p align="center">
<img width="850" alt="Capture d’écran 2022-10-27 à 23 32 16" src="https://user-images.githubusercontent.com/63207451/198404609-a4e73f9d-53a1-4c05-9ca4-5d4480a77cb7.png">
  </p>

À présent, vous pouvez naviguer parmi les pages pour visualiser les données, créer des modèles, etc. La première page est celle d'**analyse des colonnes**, elle permet d'afficher les colonnes indépendemment, et d'avoir les caractéristiques mathématiques de celle-ci. Les caractéristiques dépendent du type de la colonne.

<p align="center">
<img width="850" alt="Capture d’écran 2022-10-27 à 23 32 16" src="https://user-images.githubusercontent.com/63207451/198405223-96e1acb5-c875-40a0-84bc-5733b4b79319.png">
  </p>


La page suivant, **Matrice de corrélations** permet de voir les possibles corrélations entre les features du dataset. Vous devez simplement spécifier les features à prendre en compte. Vous pouvez également renseigner une feature catégorielle pour la coloration.

<p align="center">
<img width="850" alt="Capture d’écran 2022-10-27 à 23 32 16" src="https://user-images.githubusercontent.com/63207451/198405775-12b0cf2d-a26c-4226-9ca5-8f9ae2fcde2a.png">
  </p>

La page **section graphiques** vous donne la possibilité de créer des graphiques pour suivre en détail les corrélations entre deux features. Plusieurs options de graphiques sont disponibles (Points, Courbe, Coordonnées géographiques, Histogramme), plusieurs indices statistiques peuvent être affichés ainsi que les courbes de régressions Linéaire et Polynomiale avec les équations finales pour chacune.

<p align="center">
<img width="850" alt="Capture d’écran 2022-10-27 à 23 32 16" src="https://user-images.githubusercontent.com/63207451/198406497-c46770c5-e80c-4e04-aaf7-cf4db1707b0a.png">
  </p>

Nous voila maintenant dans la section **Régressions**, dans cette page vous pourrez suivre les courbes d'apprentissage de plusieurs modèles de régressions (sélectionnés en fonction du type de données). Il y a la régression linéaire, polynomiale, Elastic Net, Ridge, Lasso, de poisson. Il vous suffit de renseigner les features et la bonne target et le tour est joué.

<p align="center">
<img width="850" alt="Capture d’écran 2022-10-27 à 23 32 16" src="https://user-images.githubusercontent.com/63207451/198407133-6888d8a1-0f27-4322-9ca1-71229e4abe7c.png">
  </p>

Attaquons nous maintenant à la partie classification, qui renferme des nouvelles pages pour chaque modèle pris en compte, KNN, K-Means, Support Vector Machine et Decision Tree.

<br>

<p align="center">
    <a href="https://antonin-lfv.github.io" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/127334786-f48498e4-7aa1-4fbd-b7b4-cd78b43972b8.png" title="Web Page" width="38" height="38"></a>
  <a href="https://github.com/antonin-lfv" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97302854-e484da80-1859-11eb-9374-5b319ca51197.png" title="GitHub" width="40" height="40"></a>
  <a href="https://www.linkedin.com/in/antonin-lefevre-565b8b141" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303444-b2c04380-185a-11eb-8cfc-864c33a64e4b.png" title="LinkedIn" width="40" height="40"></a>
  <a href="mailto:antoninlefevre45@icloud.com" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303543-cec3e500-185a-11eb-8adc-c1364e2054a9.png" title="Mail" width="40" height="40"></a>
</p>
