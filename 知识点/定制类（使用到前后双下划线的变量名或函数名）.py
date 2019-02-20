class Chain(object):        # SDK动态调用不同的api地址
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('{}/{}'.format(self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

    def __call__(self, param):
        return Chain('{}/{}'.format(self._path, param))


path = Chain().status.user('lr').timeline.list
print(path)
