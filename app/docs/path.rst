

Path decoding
=============

Path decoding for Django function based views is simple and elegant. Declare your function:

.. code-block:: python

    def album_view(request, album_pk):
        album = get_object_or_404(Album, pk=album_pk)
        ...

Then declare your path mapping:

.. code-block:: python

    urlpatterns = [
        path('<album_pk>/', album_view),
    ]

For class based views it's a little more awkward with `self.kwargs`, but
mostly the same. In iommi we have another approach that we think is more
elegant and faster to develop with:

URLConf and iommi
~~~~~~~~~~~~~~~~~

The url parameters, or path components, are available in iommi under the `params` namespace and also as keyword arguments directly. A simple example is:

.. code-block:: python

    class MyPage(Page):
        hello = html.div(
            lambda name, **_: f'Hello {name}',
        )

    urlpatterns = [
        path('<name>/', MyPage().as_view()),
    ]

This simple view will take the `name` path parameter and print it on the page. This is sometimes useful, but it's more common to need some more complex lookup on our parameters, so that leads us to path decoders:

iommi path decoders
~~~~~~~~~~~~~~~~~~~

In iommi we have a powerful and easy to use system for path decoding that also
works smoothly with iommi views. It builds on top of the params feature
described above. Let's look at an example: 

Register your models:

.. code-block:: python

    register_path_decoding(
        artist_name=Artist.name,
        artist_pk=Artist,
        album_pk=Album,
    )

Now in your path mapping you can write:

.. code-block:: python

    urlpatterns = [
        path('<artist_name>/<album_pk>/', MyPage().as_view()),
    ]

...and you will get an `Artist` instance as `artist` (also in `params.artist`) and an `Album`
instance in `album`. The name lookup
assumes your name field is called `name` on the model. There's an advanced
registration system for more complex lookups, but this should cover most
usages.


Use iommi decoders on a function based view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the iommi path decoders on a normal FBV too:

.. code-block:: python

    @decode_path
    def my_view(request, artist, album):
        return artist, album

If you want to get any of the raw values before they are decoded you can access them
via `request.iommi_view_params` which has both the undecoded and the decoded parameters.

Advanced path decoders
~~~~~~~~~~~~~~~~~~~~~~

For cases where you want to decode something other than a pk or name you need the advanced path decoders. Here's a simple example:

.. code-block:: python

    register_path_decoding(
        user_pk=User,
        user_username=User.username,
        user_email=User.email,
        track_foo=lambda string, request, decoded_kwargs, kwargs, **_: Track.objects.get(name__iexact=string.strip())
    )

This will allow you to do `<user_pk>`, `<user_username>`, `<user_email>` in your url pattern for the `User` model, and `track_foo` for the `Track` model.  

The first example just maps `pk`, `username` and `email` one to one to the model. So for an email lookup it will run `User.objects.get(email=params.email)` to get the `User` object. 

The second example is for more complex use cases. As you have access to `request`, `decoded_kwargs` and `kwargs` in addition to the model you can perform path decoding that is not possible with Django path decoders.

Path decoders for access control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Access control on path decoder level can be very powerful if you have row-level access rules. Let's say that only staff users can edit Black Sabbath albums:

.. code-block:: python

    def album_pk_decoder(string, request, **_):
        album = Album.objects.get(pk=string)
        if album.artist.name == 'Black Sabbath' and not request.user.is_staff:
            raise PermissionError('Only staff can edit Black Sabbath albums')
        return album

.. code-block:: python

    register_path_decoding(album_pk=PathDecoder(decode=album_pk_decoder, name='album'))

The beauty of this approach is that if you do this consistently in your product, all views get decoded objects that are safe to user without further checks.

