# DuerOS-Python-Server
DuerOS skill deploy support.

## 1.Intro

For full request documentation please visit [DuerOS doc](https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/request_markdown)

## 2.Enviroment

python3, pip

## 3.Requirements

* requests
* flask
* gunicorn
* rsa
* sqlite3
* Flask_SQLAlchemy
* Flask_PyMongo
* mysql-connector-python-rf

## 4.Tree

```shell
├── README.md
├── app
│   ├── __init__.py
│   ├── tools
│   │   └── record.py
│   └── utils.py (handle requests)
├── config.py
├── database.db
├── defaults
│   └── settings.cfg (default config)
├── dueros.py
├── models
│   └── mysql
│       ├── activity.py (log activity)
│       └── init.py (init database)
├── requirements.txt
├── settings.cfg (copy from defaults/settings.cfg and edit with your config)
└── setup.py
```

## 5.Setup

### Option 1: Using requirements.txt
```shell
git clone https://github.com/fredliang44/DuerOS-Python-Server.git
cd DuerOS-Python-Server
pip3 install -r requirements.txt
export FLASK_APP=$(pwd)/DuerOS-Python-Server/dueros.py
```

### Option 2: Using setuptools
```shell
git clone https://github.com/fredliang44/DuerOS-Python-Server.git
cd DuerOS-Python-Server
python3 setup.py install
export FLASK_APP=$(pwd)/DuerOS-Python-Server/dueros.py
```


Please edit and uncomment your config in`defaults/settings.cfg`

Then move the file to root dir (inside dir `DuerOS-Python-Server`)

Support mongodb(recommend), sqlite, mysql as backend database(still testing)

## 6.Init db
If you are using sql database, please init before using new database.

```shell
flask init
```

## 7.Run
```shell
flask run
```

## 8.Gen Certs
For more information: [DuerOS certs doc](https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-deploy/authentication_markdown#%E9%AA%8C%E8%AF%81%E8%BF%87%E7%A8%8B)

```shell
flask gen_certs
```

## Deploy
### Option1: Using gunicorn cli

```shell
gunicorn -w 4 -b 0.0.0.0:8000 dueros:app
```

### Option2: Using flask cli start gunicorn
log path `log/`
```shell
flask deploy
```

[![Maintainability](https://api.codeclimate.com/v1/badges/e4d1aea980a7d29d84b6/maintainability)](https://codeclimate.com/github/fredliang44/DuerOS-Python-Server/maintainability)

