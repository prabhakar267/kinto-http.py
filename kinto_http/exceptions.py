class KintoException(Exception):
    request = None
    response = None

    def __init__(self, message=None, exception=None):
        super(KintoException, self).__init__(self, message)
        self.message = message
        if exception is not None:
            self.request = exception.request
            self.response = exception.response
        else:
            self.request = None
            self.response = None


class BucketNotFound(KintoException):
    pass
