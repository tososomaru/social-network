[JTW Debugger](https://jwt.io)

 [Deta](https://www.deta.sh/) - is a free cloud


 *main.py* - entrypoint:
 ```bash
 uvicorn main:app --reload
 ```

docker-compose up --build
alembic revision --autogenerate -m "init"
alembic upgrade head