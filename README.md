### 📚 [Projet d'admission EPITECH](https://github.com/djsfabio/ktr-msc-ls1)

#### Projet réalisé dans le cadre de l'admission en MSc Pro de l'école Epitech. 

## Mise en contexte

Ce projet est un gestionnaire de carte de visite. Il s'adresse aux jeunes entrepreneurs qui recherchent une solution numérique
pour stocker les informations de leurs multiples cartes de visite acquises lors de leurs différentes soirée de networking. 

## Installation
```
git clone https://github.com/djsfabio/ktr-msc-ls1.git
```
```
cd ktr-msc-ls1
```
alors
```
pipenv install
```
```
pipenv shell
```
ou
```
pip install -r requirements.txt
```
## Utilisation

```
python main.py
```

# Consigne du projet :

## Step 1 - Create the repository ✅

1. Create your github account if you don’t have one yet  
2. Createa a repository named ktr-msc-ls1  

## Step 2 - "Profile" Interface ✅

Create a "profile" interface allowing the user of your application to save his own information, in the following form :  

• Name (mandatory short text field)  
• Company name (optional short text field)  
• Email address (optional long text field)  
• Telephone number (optional phone field)  

### + Bonus 1 - Save the datas ✅
Make sure that this data is persistent.

## Step 3 - Data Protection ✅
Create a password protection system for this interface. 
### + Bonus 2 - Multi-users ✅
Create one profile per user.
### + Bonus 3 - User switch ✅
Allow your users to log out. 

## Step 4 - "Library" Interface ✅
Create a "library" interface that allow your user to add new business cards to your application with the following fields :  
• Name (optional short text field)  
• Company name (optional short text field)  
• Email address (mandatory email field)  
• Telephone number (optional phone field)  

## Final bonus - Business card exchange ❌
Allow two users of your application on two different devices to automatically exchange their profile information and add it to their business card "library".