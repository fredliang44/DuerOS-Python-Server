# DuerOS-Python-Server
DuerOS skill deploy support.

## Intro

For full request documentation please visit [DuerOS doc](https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/request_markdown)

## Enviroment

python3, pip

## Requirements

* requests
* flask
* gunicorn
* rsa
* sqlite3
* Flask_SQLAlchemy
* Flask_PyMongo
* mysql-connector-python-rf

## Tree

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

## Setup

### Option 1: Using requirements.txt
```shell
git clone https://github.com/fredliang44/DuerOS-Python-Server.git
pip3 install -r requirements.txt
export FLASK_APP=$(pwd)/DuerOS-Python-Server/dueros.py
```

### Option 2: Using setuptools
```shell
git clone https://github.com/fredliang44/DuerOS-Python-Server.git
python setup.py install
export FLASK_APP=$(pwd)/DuerOS-Python-Server/dueros.py
```


Please edit and uncomment your config in`defaults/settings.cfg`
Then move the file to root dir (inside `DuerOS-Python-Server`)

Support sqlite, mysql, mongodb as backend database(still testing)

## Init db
If you are using sql database, please init before using new database.

```shell
flask init
```

## Run
```shell
flask run
```

## Gen Certs
For more information: [DuerOS certs doc](https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-deploy/authentication_markdown#%E9%AA%8C%E8%AF%81%E8%BF%87%E7%A8%8B)

```shell
flask gen_certs
```

## Deploy

Using guicorn

```shell
gunicorn -w 4 -b 0.0.0.0:5000 dueros:app
```




