# Get into the file 
`cd local_art`
# setup virtiul environment
`python -m venv .venv`
# Active virtual environment
`source .venv/bin/activate`

# install dependency
`pip install -r requirements.txt`

# run server
`python manage.py runserver`

# make migrations
`python manage.py makemigrations`

# Migrate
`python manage.py migrate`

## test api via post mane

# registration:
`http://127.0.0.1:8000/api/register`
in body:

`{
    "artist_name": "example",
    "email": "example@gmail.com",
    "bio": "example",
    "password": "1234"
}`

# login: post:
`http://127.0.0.1:8000/api/login`

in body
`{
    "email": "example@gmail.com",
    "password": "1234"
}`

# get user:

pass jwt token in header
