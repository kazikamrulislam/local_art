@LOCAL ARTIST ATRWOTK

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
`http://127.0.0.1:8000/api/user`
pass jwt token in header

# get Artwork 
`http://127.0.0.1:8000/api/artwork`
pass jwt token in header 

# POST Artwork 
`http://127.0.0.1:8000/api/artwork`  // i was unable to make it happen but
pass jwt token in header // i was unable to make it happen but 

''{
    "art_title": "Sunset at Sea",
    "description": "A beautiful painting capturing the colors of the setting sun over the ocean.",
    "photo_main": "photos/2024/04/10/sunset_at_sea.jpg",
    "artist": [
            {
                "id": 1
            }
    ],
    "list_date": "2024-04-10T01:40:24Z"
}''

