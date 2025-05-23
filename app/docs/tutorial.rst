Tutorial
~~~~~~~~

.. note::

    This tutorial is intended for a reader that is well versed in the Django basics of the ORM,
    urls routing, function based views, and templates.

    It is also expected that you have already installed iommi in your project. Read section 1 of :ref:`Getting started <getting-started>`.


This tutorial will build a discography app. Let's start with the models:


.. literalinclude:: models.py
    :pyobject: Artist
    :end-before: def __str__

.. literalinclude:: models.py
    :pyobject: Album
    :end-before: def __str__

.. literalinclude:: models.py
    :pyobject: Track
    :end-before: def __str__

We will build up to these pages:

- index page with album artwork
- an artist page
- an artists page
- an album page
- an albums page
- a tracks page

Plus we're going to enable the iommi admin for these models.



Example data
------------

If you want it to get the same example data as in this tutorial, run `this code`_.

.. _this code: https://raw.githubusercontent.com/iommirocks/iommi/master/docs/custom/big_discography.py

Tables
------

Creating a table view of a model in iommi is simple:

.. code-block:: python

    urlpatterns = [
        path('', Table(auto__model=Album).as_view()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('0ee8e29e-c78f-4595-ae9a-acb5aeed465f', this)">▼ Hide result</div>
    <iframe id="0ee8e29e-c78f-4595-ae9a-acb5aeed465f" src="doc_includes/tutorial/test_declarative_tables.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

You get sorting and pagination by default, and we're using the default bootstrap 5 style. iommi ships with :ref:`more styles <style>` that you can switch to, or you can :ref:`implement your own custom style <style>`.

At this point you might think "Hold on! Where is the template?". There isn't one. We don't need a template. iommi works at a higher level of abstraction. Don't worry, you can drop down to templates if you need to. There are examples of this in the :ref:`table cookbook <cookbook-tables>`, and much more. One of the most important concepts is to include or exclude columns using includes: `auto__include=['name', 'artist']`, or using excludes: `auto__exclude=['artist', 'year']`.

Pages
-----

So far we’ve just created a single table, but often you want something a little more complex, especially for your index page. iommi has a concept of a :ref:`Page <pages>` that is used to build up a bigger page from smaller building blocks. Let’s build out our simple web app to have separate pages for albums, artists and tracks:

.. code-block:: python

    urlpatterns = [
        path('albums/', Table(auto__model=Album).as_view()),
        path('artists/', Table(auto__model=Artist).as_view()),
        path('tracks/', Table(auto__model=Track).as_view()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('fb65fb8b-e279-44e2-8455-72f3b0041606', this)">► Show result</div>
    <iframe id="fb65fb8b-e279-44e2-8455-72f3b0041606" src="doc_includes/tutorial/test_pages.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('3c9e6979-e469-4397-ae3e-33b34d8efec0', this)">► Show result</div>
    <iframe id="3c9e6979-e469-4397-ae3e-33b34d8efec0" src="doc_includes/tutorial/test_pages1.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('8834a68f-4192-44b4-a7dc-9a9980c7905c', this)">► Show result</div>
    <iframe id="8834a68f-4192-44b4-a7dc-9a9980c7905c" src="doc_includes/tutorial/test_pages2.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

and an index page with three tables, a header and some text:

.. code-block:: python

    class IndexPage(Page):
        title = html.h1('Supernaut')
        welcome_text = 'This is a discography of the best acts in music!'

        artists = Table(auto__model=Artist, page_size=5)
        albums = Table(auto__model=Album, page_size=5)
        tracks = Table(auto__model=Track, page_size=5)

    urlpatterns = [
        path('', IndexPage().as_view()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('0f577632-a68b-4ce2-afa5-aa0a17179a2f', this)">▼ Hide result</div>
    <iframe id="0f577632-a68b-4ce2-afa5-aa0a17179a2f" src="doc_includes/tutorial/test_pages3.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

`html` is a little fragment builder to make it easier and faster to build small html parts. `html.div('foo')` is just a more convenient way to write `Fragment(tag='div', children__text='foo')`. Fragments are used internally throughout iommi, because they allow you to define a small bit of html that can be customized later. Let’s look at an example:

.. code-block:: pycon

    >>> class MyPage(Page):
    ...    title = html.h1('Supernaut')

    >>> MyPage().bind().__html__()
    '<h1>Supernaut</h1>'

    >>> MyPage(parts__title__attrs__class__foo=True).bind().__html__()
    '<h1 class="foo">Supernaut</h1>'

This is used throughout iommi to provide good defaults that can be customized easily when needed.

A `Page` can contain any `Part` (like `Fragment`, `Table`, `Form`, `Menu`, etc), plain strings or Django `Template` objects even. Escaping is handled like you’d expect from Django where strings are escaped, and you can use `format_html`/`mark_safe` to send your raw html straight through.

Path decoding
-------------

We’ll also introduce a page for an individual artist. We will use iommi's :doc:`path` here.

First we register the path component we want to decode (in your `AppConfig` `ready`):

.. code-block:: python

    register_path_decoding(
        artist_name=Artist.name,
    )

Then we define our page. Notice the lambdas we use to dynamically get the parameters to retrieve the correct data.

.. code-block:: python

    class ArtistPage(Page):
        title = html.h1(lambda artist, **_: artist.name)

        albums = Table(
            auto__model=Album,
            rows=lambda artist, **_: Album.objects.filter(artist=artist),
        )
        tracks = Table(
            auto__model=Track,
            rows=lambda artist, **_: Track.objects.filter(album__artist=artist),
        )

    urlpatterns = [
        path('artist/<artist_name>/', ArtistPage().as_view()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('55d2cfc5-23bd-4c1d-a366-13ccd7d95506', this)">▼ Hide result</div>
    <iframe id="55d2cfc5-23bd-4c1d-a366-13ccd7d95506" src="doc_includes/tutorial/test_path_decoding.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Path decoders in iommi can be more convenient compared to Django path
decoders, as instead of writing `<artist:artist>` everywhere, you can instead
write `<artist_name>` or `<artist_pk>`. They are also easier to set up and 
gives you hook points for access control if needed.

Deeper customization
--------------------

cell__format
============

In iommi you can customize the rendering on many different levels, depending
on what the situation requires. The last layer of customization is
`format` which is used to convert the value of a cell to a string that
is inserted into the html (or CSV or whatever output format you are targeting):

.. code-block:: python

    albums = Table(
        auto__model=Album,
        columns__artist__cell__format=lambda value, **_:
            format_html('<a href="/artist/{}/">{}</a>', value, value)
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('1384beb2-ab5d-4ec8-a1dc-a39f166187a2', this)">▼ Hide result</div>
    <iframe id="1384beb2-ab5d-4ec8-a1dc-a39f166187a2" src="doc_includes/tutorial/test_table_customization.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

`columns__artist__cell__format` should be read as something similar to
`columns.artist.cell.format`. This way of jumping namespace with `__` instead
of `.` (because `.` is syntactically invalid!) is something Django started 
doing for query sets and we really like it so we've taken this concept further
and it is now everywhere in iommi.

The other levels of customization are `value` which is how the value is 
extracted from the row, `attr` which is the attribute that is read (if
you don't customize `value`), and lastly `template` which you use to override
the entire rendering of the cell (including the `td` tag!). 

You can also override `template` on the row to customize the row rendering.
Again this includes the `tr` tag.


cell__url
=========

A very common case of tables is to show a link in the cell. You can do that
with `cell_format` and `cell__template` like above, but it's such a common
case that we supply a special convenience method `cell__url` for this. Let's
make the artist column link to the artist page in our table. First we add
a `get_absolute_url` on the model, then replace the 
`columns__artist__cell__format` we had above with:

.. code-block:: python

    albums = Table(
        auto__model=Album,
            columns__artist__cell__url=lambda value, **_: value.get_absolute_url(),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('ae8d4e90-6ac7-4966-b00d-aed06e8c32dd', this)">▼ Hide result</div>
    <iframe id="ae8d4e90-6ac7-4966-b00d-aed06e8c32dd" src="doc_includes/tutorial/test_table_customization1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Much better!

But actually, this is such a common case that we do this by default for you
for `ForeignKey` columns if the target model has `get_absolute_url`. So we
can just remove the `columns__artist__cell__url` specification entirely. But 
we do want the *name* column to link to the album page so the total definition
becomes:

.. code-block:: python

    albums = Table(
        auto__model=Album,
        columns__name__cell__url=lambda row, **_: row.get_absolute_url(),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('de77169e-b8a7-4716-9bed-26d439b55c5d', this)">▼ Hide result</div>
    <iframe id="de77169e-b8a7-4716-9bed-26d439b55c5d" src="doc_includes/tutorial/test_table_customization2.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Filters
=======

Tables also have built in filtering. To enable a filter make sure `include` is `True` for the `filter` of a column.

.. code-block:: python

    albums = Table(
        auto__model=Album,
        columns__name__filter__include=True,
        columns__year__filter__include=True,
        columns__year__filter__field__include=False,
        columns__artist__filter__include=True,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('dfd83d67-73d3-43a0-a6d1-93ef960f0afd', this)">▼ Hide result</div>
    <iframe id="dfd83d67-73d3-43a0-a6d1-93ef960f0afd" src="doc_includes/tutorial/test_table_customization3.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

`columns__year__filter__field__include=False` means we turn off the `Field` in
the form that is created, but we can still search for the year in the
advanced search language. 

To handle selecting from a choice field that is backed by a `QuerySet` that
can contain thousands or millions of rows, iommi by default uses a select2
filter control with an automatic ajax endpoint. The automatic endpoint is handled by iommi on the
same url as the view. An advantage to this approach is that we only need
to be sure our view has the correct permission checks and then we also know
the select box (or ajax endpoint) has the same checks. This makes it easy to
reason about the security of the product. 

The advanced filter means users can write queries like `year>1960 and title:war`
to find albums published after 1960 and that contain the word "war".

Actions
=======

An `Action` in iommi is a link or a button. We use them for submit buttons of
forms and for links that you can add to a part. A common use case is to add
links to a table. In our example app we want to add a create button for staff.

While we're at it, let's add some new columns for edit and delete links. There
are special shortcuts in iommi prebuild for that too: `Column.edit` and `Column.delete`.

.. code-block:: python

    albums = Table(
        auto__model=Album,
        actions__create_album=Action(
            attrs__href='/albums/create/',
            include=lambda request, **_: request.user.is_staff,
        ),
        columns__edit=Column.edit(
            after=0,
            include=lambda request, **_: request.user.is_staff,
        ),
        columns__delete=Column.delete(
            include=lambda request, **_: request.user.is_staff,
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('c49d137b-3346-4c49-afc6-545a5c0de930', this)">▼ Hide result</div>
    <iframe id="c49d137b-3346-4c49-afc6-545a5c0de930" src="doc_includes/tutorial/test__foo.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

For non-staff the "Create album" button isn't shown, neither are the edit and delete columns:

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('f5633af7-517a-4dcb-a924-90987ef38d96', this)">▼ Hide result</div>
    <iframe id="f5633af7-517a-4dcb-a924-90987ef38d96" src="doc_includes/tutorial/test__foo1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

cell__template
==============

Now that we have a basic app, we'd like to customize the look of the index page
a bit. A plain html table with text doesn't look very cool, so we will spice it
up with album covers. We'll start by removing the artists section. 

A custom cell template for albums might be a good start to make it look nicer.

.. code-block:: python

    albums = Table(
        auto__model=Album,
        columns__album_art=Column(
            attr=None,
            cell__template=Template('''
                <td>
                    <img 
                        height="30"
                        src="../../album_art/{{ row.artist }}/{{ row.name }}.jpg">
                </td>
            '''),
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('204cf143-b507-488c-9b9e-3dc1bde81a5b', this)">▼ Hide result</div>
    <iframe id="204cf143-b507-488c-9b9e-3dc1bde81a5b" src="doc_includes/tutorial/test__foo2.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

That's a start, but we want something a bit more showy, let's get rid of html
tables entirely:

row__template
=============

To override the rendering of an entire row we use `cell__template`. We also
change the table from rendering a `table` tag to a `div`, and turn off the 
table header:

.. code-block:: python

    albums = Table(
        auto__model=Album,
        tag='div',
        header__template=None,
        row__template=Template("""
            <div class="card" style="width: 15rem; display: inline-block;" {{ cells.attrs }}>
                <img class="card-img-top" src="../../album_art/{{ row.artist }}/{{ row.name|urlencode }}.jpg">
                <div class="card-body text-center">
                    <h5>{{ cells.name }}</h5>
                    <p class="card-text">
                        {{ cells.artist }}
                    </p>
                </div>
            </div>
        """),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('7741f380-c972-4deb-84cb-117a1bbba62e', this)">▼ Hide result</div>
    <iframe id="7741f380-c972-4deb-84cb-117a1bbba62e" src="doc_includes/tutorial/test__foo3.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

You can specify the name of a template file here instead of writing the
template inline like this. This way is nicer for small things and quick prototypes though.


Admin
-----

With these high level abstractions we've seen so far (pages, tables, queries, 
forms, fragments) we can easily build more powerful components. Which is what
we've done with the administration interface built into iommi. Installing it
is as simple as:

.. code-block:: python

    class MyAdmin(Admin):
        class Meta:
            pass

.. code-block:: python

    urlpatterns = [
        path('iommi-admin/', include(MyAdmin.urls())),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('c90d3a74-2045-4eb0-8d0b-152388da4c1c', this)">▼ Hide result</div>
    <iframe id="c90d3a74-2045-4eb0-8d0b-152388da4c1c" src="doc_includes/tutorial/test__foo4.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Customization is easy with `IOMMI_DEBUG` on (default on if `DEBUG` is on), 
here's how to use the pick tool:

.. raw:: html

    <video controls style="max-width: 100%"><source src="iommi-admin-customization.mp4"></video>

You can override an entire field rendering with `template`, the template 
of the label with `label__template`, the name of a field with `display_name`,
add a CSS class to the label tag with `label__attrs__class__foo=True`, and 
much more. Customization is at all levels, and in all these cases you can
supply a callable for even more flexibility.

Forms
-----

iommi also comes with a library for forms. This can look very much like the
forms library built into Django, but is different in some crucial ways. Let's
take a simple example of a `ModelForm`:

.. code-block:: python

    from django import forms

    class AlbumForm(forms.ModelForm):
        class Meta:
            model = Album
            fields = ['name', 'artist']

.. code-block:: html

    {% extends "base.html" %}
    {% block content %}

    <form action="/your-name/" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Submit">
    </form>

    {% endblock %}

In iommi the same can be written as:

.. code-block:: python

    class AlbumForm(Form):
        class Meta:
            auto__model = Album
            auto__include = ['name', 'artist']

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('ee59a7cd-fcab-4375-8686-f086fd4f4622', this)">▼ Hide result</div>
    <iframe id="ee59a7cd-fcab-4375-8686-f086fd4f4622" src="doc_includes/tutorial/test_forms.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

No template needed, and this is the view too with `Form.edit` or `Form.createcookbook-forms`.

In iommi you always get a form encoding specified on the form, so they all work
with file uploads. Missing form encoding on the form tag is a very common 
stumbling block for beginners. You also get a submit action by default which
you can configure via `actions__submit`:

.. code-block:: python

    class AlbumForm(Form):
        class Meta:
            auto__model = Album
            auto__include = ['name', 'artist']
            actions__submit__display_name = 'Save'

In iommi we use `class Meta` a lot, similar to Django, but in iommi it's not
just a bucket of values, it has a precise definition: values in `Meta` are 
passed into the constructor. So the example above is semantically the same as:

.. code-block:: python

    AlbumForm(
        auto__model=Album,
        auto__include=['name', 'artist'],
        actions__submit__display_name='Save',
    )

Worth pointing out is that values of `Meta` are defaults, so you can still
override at the constructor call.

An advantage to this strict definition is that we don't have silent failures
in iommi. If you make a spelling mistake for a setting in `Meta`, you will get
an error message.


There are many many more customizations options available, you can find more
in the :ref:`form cookbook <cookbook-forms>` and the docs for `Field`.


Automatic views
===============

iommi goes a step further than Django forms, by supplying full views that can
be used from either a declarative form or an auto generated form. An example
is to have a create view for an `Artist`:

.. code-block:: python

    urlpatterns = [
        path('create/', Form.create(auto__model=Artist).as_view()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('0575cd3d-7463-4cf4-8254-69616100f405', this)">▼ Hide result</div>
    <iframe id="0575cd3d-7463-4cf4-8254-69616100f405" src="doc_includes/tutorial/test_forms1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

There are four built in forms/views like this: `create`, `edit`, `create_and_edit` and `delete`.
The `delete` view is a read only form with some styling for the submit button
and a submit handler that delete the object. We find this to be really nice as
a confirmation page because you can see what you are about to delete.

Wrap up
-------

I'm glad you read this far! This has been a very shallow introduction, but
it has touched on all the major parts in some way, and there is a lot of
material to cover. We hope you want to give iommi a try.

