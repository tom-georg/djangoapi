pip freeze > requirements.txt

rsync -avz --exclude='.git/' ./ tom@combinator.de:djangoapi.combinator.de

pip install -r requirements.txt


djangoapi/gunicorn djangoapi.wsgi  