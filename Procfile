setup:
    addons:
        - plan: heroku-postgresql
    build:
        docker:
            web: Dockerfile
    release:
        image: web
        command:
            - python manage.py collectstatic --noinput
    run:
        web: gunicorn SoundWorld.wsgi