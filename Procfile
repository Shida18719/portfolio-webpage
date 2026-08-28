release: python manage.py migrate
web: gunicorn agog_dev.asgi:application -k uvicorn.workers.UvicornWorker
