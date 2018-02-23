from flask import Flask, request
from app.utils import root
import os
import sys
from gunicorn.six import iteritems
import logging

app = Flask(__name__)
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
app.logger.debug('this will show in the log')

app.register_blueprint(root, url_prefix='/')

@app.cli.command()
def gen_certs():
    """gen certs"""
    cert_path = os.path.split(os.path.realpath(__file__))[0]+"/certs/"
    try:

        os.mkdir(cert_path)
    except:
        pass

    import rsa
    (pubkey, privkey) = rsa.newkeys(1024)
    pub = pubkey.save_pkcs1()
    pubfile = open(cert_path+'rsa_public_key.pem', 'w+')
    print(pub.decode())
    pubfile.write(pub.decode())
    pubfile.close()

    pri = privkey.save_pkcs1()
    prifile = open(cert_path+'rsa_private_key.pem', 'w+')
    prifile.write(pri.decode())
    prifile.close()



@app.cli.command()
def run():
    """Run app."""
    print("=======================================================================\n"
          "================================ start ================================\n"
          "=======================================================================")
    app.run(port=8000, debug=True)


@app.cli.command()
def deploy():
    """Deploy app."""
    app.config.update(
        DEBUG=False,
        TESTING=False,

    )


    try:
        os.mkdir("log")
    except:
        pass

    for file_name in ["log/error.log", "log/access.log"]:
        if not os.path.exists(file_name):
            os.mknod(file_name)

    from gunicorn.app.wsgiapp import WSGIApplication
    gui_app = WSGIApplication()
    gui_app.app_uri = 'manage:app'

    options = {
        'workers': 4,
        'accesslog': 'log/access.log',
        'errorlog': 'log/error.log',
        'loglevel': 'info',
        'bind': '127.0.0.1:8000',
    }

    config = dict([(key, value) for key, value in iteritems(options)])

    for key, value in iteritems(config):
        gui_app.cfg.set(key, value)

    print("=======================================================================\n"
          "============================ start guicorn ============================\n"
          "=======================================================================")
    return gui_app.run()

if __name__ == '__main__':
    app.run(port=8000, debug=True)