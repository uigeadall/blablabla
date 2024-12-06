bind = '0.0.0.0:443'
timeout = 120
graceful_timeout = 120
# log into stdout
accesslog = '-'
loglevel = 'debug'

keyfile = '/root/ca/rsa/intermediate/private/mock.key.pem'
certfile = '/root/ca/rsa/intermediate/certs/mock.cert.pem'
ca_certs = '/root/ca/rsa/certs/ca-chain.cert.pem'
# Min version
ssl_version = 'TLSv1_2'


def pre_request(worker, req):
    worker.log.debug("%s %s %s", req.scheme.upper(), req.method, req.path)
