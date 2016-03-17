britney-cookies
===============

Cookie based session as a middleware for britney SPORE client

How to use it
-------------

::
    
    import britney

    my_client = britney.new('my_description.json')
    credentials = {'username': 'my_login', 'password': 'my_pass'}
    my_client.enable('Cookie', auth_func=my_client.auth_func, **credentials)

    response = my_client.get_info()

That's it !

`auth_func` is a method on the generated client that logges the client in and brings back a session-based cookie.
The cookie middleware will persist and use it on next submitted requests.
