# api
transfer
# Python Flask Api
when run api server，you will see swagger on http://localhost:5000。
suggest using gunicorn( gunicorn -c ./gunicorn.conf.py app:app)
# Dockerfile
sudo docker build -t api:v1.0.0 . \n
sudo docker run -p 5000:5000 api:v1.0.0
# Pytest
pytest test_app.py
