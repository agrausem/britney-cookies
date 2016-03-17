"""
britney_cookies
~~~~~~~~~~~~~~~

Add a cookie based session in a britney spore client.
"""

import functools
from britney.middleware import base
from britney.middleware.auth import Auth


class Cookie(Auth):

    """ Middleware that handles cookie based session informations.

    A cookie is set in headers of every request sent to the server. A Spore
    auth function available at client instance is required
    """

    def __init__(self, auth_func, **kwargs):
        """
        :param auth_func: auth func to pass
        :param kwargs: kwargs to pass to auth func (i.e credentials)
        """
        self.auth_func = functools.partial(auth_func, payload=kwargs)
        self._cookie = None

    def is_auth_func(self, environ):
        return self.auth_func.func.name == environ.get('spore.method')

    def process_request(self, environ):
        if not self.is_auth_func(environ) and self._cookie is None:
            response = self.auth_func()
            if 'Set-Cookie' in response.headers:
                self._cookie = response.headers.get('Set-Cookie')

        if self._cookie is not None:
            base.add_header(environ, 'Cookie', self._cookie)
