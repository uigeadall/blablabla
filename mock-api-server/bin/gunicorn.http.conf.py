bind = '0.0.0.0:80'
timeout = 120
graceful_timeout = 120
# log into stdout
accesslog = '-'
loglevel = 'debug'


def pre_request(worker, req):
    worker.log.debug("%s %s %s", req.scheme.upper(), req.method, req.path)
