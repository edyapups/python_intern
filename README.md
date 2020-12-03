# python_intern
---

## requirements

- python 3.9
- В изначальном коде менять можно *всё*, вплоть до структуры файлов. 
- Использовать можно всё что угодно. 
- Таски со звёздочкой можно пропускать (или делать часть из них)
- Решение выложить через fork/копию/etc репозитория на github


## TODO

- реализовать функцию [is_alive_host](./app.py)

- покрыть функцию [тестами](./tests.py)

- развернуть вокруг функции веб сервис c помощью [fastapi](https://fastapi.tiangolo.com/)
```
>> curl your_service.loc:8001/healthz?hostname=semrush.com
{status: [up|down]}
```

- задача со *звёздочкой*: завернуть приложение в docker
- задача на *две звёздочки*: выложить куда-либо (heroku/DigitalOcean/etc) с помощью github-actions/gitlab/jenkins/etc

## Установка и запуск
1. Установить зависимости
```
>> pip3 install -r requirements.txt
```

2. Запустить
```
>> gunicorn app.main:app --bind={ip}:{port} -w {worker count} -k uvicorn.workers.UvicornH11Worker
```

## Docker
1. Собрать образ
```
>> docker build --tag {tag} .
```
2. Запустить контейнер
```
>> docker run -p {port}:{port} -e PORT={port} -d {tag}
```

## post scriptum

CI есть, CD допилится, когда появится время. 
