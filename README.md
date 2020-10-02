# Kitchen Recipes App  
Purpose of this application is to create a place when users can easily 
gathering recipes from another websites and share them

## Instalation on Linux (Not tested on Windows/MacOs)
Crate virtual environment  
```bash
python3 -m venv venv
source venv/bin/activate
```
Copy repository and install requrements.txt
```git
git clone https://github.com/nero2310/KitchenRecpiesApp  
pip3 -r requirements.txt
```
Create file .env
File .env content:
```env
POSTGRES_PASSWORD=YourDatabasePassword
```
Initialize docker database and Django server
```docker
docker-compose up -d
python3 manage.py makemigrations
python3 manage.py runserver
```
