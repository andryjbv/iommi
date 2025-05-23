

.. _pages:

Pages
=====

iommi pages are used to compose parts of a page into a full page. A "part" can be any iommi component (like :ref:`Table <tables>`, :ref:`Form <forms>`, :doc:`Fragment`), or a plain Python string, or a Django `Template <https://docs.djangoproject.com/en/5.1/topics/templates/>`_.

The `html`_ builder function is used to create simple :doc:`Fragment` objects for div, h1, span, etc.

Example
-------

.. code-block:: python

    class MyPage(Page):
        title = html.h1('My page')
        users = Table(auto__model=User)
        create_user = Form.create(auto__model=User)

This creates a page with an h1 tag, a table of users and a form to create a
new user. You can add it your `urls.py` like this: `path('my_page/', MyPage().as_view())`, or make a function based view and `return MyPage()`.

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('bc94df9e-e62b-4805-b553-8c1956c403c2', this)">► Show result</div>
    <iframe id="bc94df9e-e62b-4805-b553-8c1956c403c2" src="doc_includes/pages/test_example.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Page
----

The `Page` class is used to compose pages. Use `.as_view()` to create a view from a `Page`.
If you have installed the iommi middleware you can also return them directly from your views. They accept
`str`, `Part` and Django `Template` types:

.. code-block:: python

    class MyPage(Page):
        # Using the html builder to create a tag safely
        h1 = html.h1('Welcome!')

        # If you write an HTML tag in here it will be
        # treated as unsafe and escaped by Django like normal
        body_text = 'Welcome to my iommi site...'

        # You can nest Page objects!
        some_other_page = MyOtherPage()

        # Table and Form are Part types
        my_table = Table(auto__model=Artist)

        # Django template
        other_stuff = Template('<div>{{ foo }}</div>')

The types here that aren't `Part` will be converted to a `Part` derived class
as needed.

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('bfcf7cf4-fae4-4d80-8622-cece7fedbe66', this)">► Show result</div>
    <iframe id="bfcf7cf4-fae4-4d80-8622-cece7fedbe66" src="doc_includes/pages/test_page.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Add more parameters to a `Page`
-------------------------------

.. code-block:: python

    class MyPage(Page):
        class Meta:
            @staticmethod
            def extra_params(**_):
                return dict(
                    extra_param='foo',
                )

        text = html.div(lambda extra_param, **_: extra_param + 'bar')

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('8076d6cb-53ba-40b2-8ec1-549d7219db20', this)">▼ Hide result</div>
    <iframe id="8076d6cb-53ba-40b2-8ec1-549d7219db20" src="doc_includes/pages/test_extra_params.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Or the functional syntax for the same thing:

.. code-block:: python

    my_page = Page(
        extra_params=lambda **_: dict(extra_param='foo'),
        parts__text=html.div(lambda extra_param, **_: extra_param + 'bar'),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('880875ac-3a22-4ac2-97d3-00e6eff7d9a9', this)">► Show result</div>
    <iframe id="880875ac-3a22-4ac2-97d3-00e6eff7d9a9" src="doc_includes/pages/test_extra_params1.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _html:

html
----


html is a little builder object to create simple elements. You just do
`html.h1('some text')` to create an h1 html tag. It works by creating `Fragment`
instances, so the `html.h1('foo')` is the same as
`Fragment('some text', tag='h1')`, which is itself a convenient short way to
write `Fragment(children__text='some text', tag='h1')`. See `Fragment` for more
available parameters.


Part
--------

`Part` is the base class/API for objects that can be composed into a page.

Fragment
--------

Advanced example:

.. code-block:: python

    Fragment(
        'foo',
        tag='div',
        children__bar=Fragment('bar'),
        attrs__baz='quux',
    )

This fragment will render as:

.. code-block:: html

    <div baz='quux'>foobar</div>

This might seem overly complex for such a simple thing, but when used in
reusable components in iommi `Fragment` objects can be further customized
with high precision.

