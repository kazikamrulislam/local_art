#Get into the file 
`cd local_art`
#setup virtiul environment
`python -m venv .venv`
#Active virtual environment
`source .venv/bin/activate`

#install dependency
`pip install -r requirements.txt`

#run server
`python manage.py runserver`

#make migrations
`python manage.py makemigrations`

#Migrate
`python manage.py migrate`

