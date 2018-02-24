import os
from gunicorn.six import iteritems
from config import app


@app.cli.command()
def gen_certs():
    """
    Gen certs
    """
    cert_path = os.path.split(os.path.realpath(__file__))[0] + "/certs/"
    try:
        os.mkdir(cert_path)
    except BaseException:
        pass

    import rsa
    (pubkey, privkey) = rsa.newkeys(1024)
    pub = pubkey.save_pkcs1()
    pubfile = open(cert_path + 'rsa_public_key.pem', 'w+')
    print(pub.decode())
    pubfile.write(pub.decode())
    pubfile.close()

    pri = privkey.save_pkcs1()
    prifile = open(cert_path + 'rsa_private_key.pem', 'w+')
    prifile.write(pri.decode())
    prifile.close()


@app.cli.command()
def run():
    """
    Run app
    """
    print("=======================================================================\n"
          "================================ start ================================\n"
          "=======================================================================")
    app.run(port=8000, debug=True)


@app.cli.command()
def deploy():
    """
    Deploy app
    """
    app.config.update(
        DEBUG=False,
        TESTING=False,
    )

    try:
        os.mkdir("log")
    except BaseException:
        pass

    for file_name in ["log/error.log", "log/access.log"]:
        if not os.path.exists(file_name):
            os.system("touch " + file_name)

    from gunicorn.app.wsgiapp import WSGIApplication
    guni_app = WSGIApplication()
    guni_app.app_uri = 'dueros:app'

    options = {
        'workers': 4,
        'accesslog': 'log/access.log',
        'errorlog': 'log/error.log',
        'loglevel': 'info',
        'bind': '127.0.0.1:8000',
    }
    #
    # import logging.config
    # logging.config.dictConfig(config= {
    #                             'version': 1,
    #                             'disable_existing_loggers': True,
    #                             'root': {
    #                                 'level': 'WARNING',
    #                                 'handlers': ['sentry'],
    #                             },
    #                             'formatters': {
    #                                 'verbose': {
    #                                     'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
    #                                 },
    #                                 'generic': {
    #                                     'format': '%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
    #                                     'datefmt': '%Y-%m-%d %H:%M:%S',
    #                                     '()': 'logging.Formatter',
    #                                 },
    #                             },
    #                             'handlers': {
    #                                 'sentry': {
    #                                     'level': 'ERROR',
    #                                     'class': 'raven.contrib.django.handlers.SentryHandler',
    #                                 },
    #                                 'console': {
    #                                     'level': 'DEBUG',
    #                                     'class': 'logging.StreamHandler',
    #                                     'formatter': 'verbose'
    #                                 },
    #                                 'error_file': {
    #                                     'class': 'logging.FileHandler',
    #                                     'formatter': 'generic',
    #                                     'filename': 'log/error.log',
    #
    #                                 },
    #                                 'access_file': {
    #                                     'class': 'logging.FileHandler',
    #                                     'formatter': 'generic',
    #                                     'filename':'log/access.log',
    #                                 },
    #                             },
    #                             'loggers': {
    #                                 'django.db.backends': {
    #                                     'level': 'ERROR',
    #                                     'handlers': ['console'],
    #                                     'propagate': False,
    #                                 },
    #                                 'raven': {
    #                                     'level': 'DEBUG',
    #                                     'handlers': ['console'],
    #                                     'propagate': False,
    #                                 },
    #                                 'sentry.errors': {
    #                                     'level': 'DEBUG',
    #                                     'handlers': ['console'],
    #                                     'propagate': False,
    #                                 },
    #                                 'gunicorn.error': {
    #                                     'level': 'INFO',
    #                                     'handlers': ['error_file'],
    #                                     'propagate': True,
    #                                 },
    #                                 'gunicorn.access': {
    #                                     'level': 'INFO',
    #                                     'handlers': ['access_file'],
    #                                     'propagate': False,
    #                                 },
    #                             },
    #                         }
    #                         )

    config = dict([(key, value) for key, value in iteritems(options)])

    for key, value in iteritems(config):
        guni_app.cfg.set(key, value)

    print("=======================================================================\n"
          "============================ start gunicorn ===========================\n"
          "=======================================================================")
    return guni_app.run()


@app.cli.command()
def init():
    """
    Init file
    """
    if app.config["DATABASE_TYPE"] in ["mysql", "sqlite"]:
        print("=======================================================================\n"
              "=============================== init db ===============================\n"
              "=======================================================================")
        from models.mysql.init import init_db
        init_db()
    elif app.config["DATABASE_TYPE"] == "mongodb":
        print("=======================================================================\n"
              "======================= no need to init mongodb =======================\n"
              "=======================================================================")


if __name__ == '__main__':
    app.run(port=8000, debug=True)
