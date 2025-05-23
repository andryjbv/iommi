

.. _getting-started:

Getting started
===============

.. note::

    This guide is intended for a reader that is well versed in the Django basics of the ORM,
    urls routing, function based views, and templates.

1. Install
----------

First:

`pip install iommi`.

Add `iommi` to installed apps:

.. code-block:: python

    INSTALLED_APPS = [
        # [...]
        'iommi',
    ]

Add iommi's middleware:

.. code-block:: python

    MIDDLEWARE = [
        # These three are optional, but highly recommended!
        'iommi.live_edit.Middleware',

        # [... Django middleware ...]

        'iommi.sql_trace.Middleware',
        'iommi.profiling.Middleware',

        # [... your other middleware ...]

        'iommi.middleware',
    ]

.. note::

    The iommi middleware must be the last middleware in the list!

By default iommi uses a very basic bootstrap base template. We'll get to how to integrate it into your site later.

2. Your first form
------------------

From this point this guide is aimed at users trying iommi in an existing project. :doc:`The tutorial <tutorial>` is a more in-depth guide to building a full application with iommi from scratch.

Pick a model from your app, and let's build a create form for it! I'm using `Album` here, but you should replace it with some your model. Add this to your `urls.py`:

.. code-block:: python

    from iommi import Form

    # Import any models you need from your models.  Here I'm using Album
    from .models import Album

    urlpatterns = [
        # ...your urls...
        path('iommi-form-test/', Form.create(auto__model=Album).as_view()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('2e0376bb-d23b-482e-8a6e-48e5defb19c1', this)">▼ Hide result</div>
    <iframe id="2e0376bb-d23b-482e-8a6e-48e5defb19c1" src="doc_includes/getting_started/test_2__your_first_form.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

3. Your first table
-------------------

Pick a model from your app, and let's build a table for it! Add this to your `urls.py`:

.. code-block:: python

    from iommi import Table

    # Import any models you need from your models.  Here I'm using Album
    from .models import Album

    urlpatterns = [
        # ...your urls...
        path('iommi-table-test/', Table(auto__model=Album).as_view()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('c681fa13-66a7-4a85-8346-64e4490f62f7', this)">▼ Hide result</div>
    <iframe id="c681fa13-66a7-4a85-8346-64e4490f62f7" src="doc_includes/getting_started/test_3__your_first_table.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

If you want, add a filter for some column:

.. code-block:: python

    urlpatterns = [
        # ...your urls...
        path('iommi-table-test/', Table(
            auto__model=Album,
            columns__name__filter__include=True,  # <--- replace `name` with some field from your model
        ).as_view()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('7c9ffb0a-4b90-4729-9846-e9c6161bf888', this)">▼ Hide result</div>
    <iframe id="7c9ffb0a-4b90-4729-9846-e9c6161bf888" src="doc_includes/getting_started/test_3__your_first_table1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

4. Your first page
------------------

Pages are the method to compose complex pages from parts. Add this to your `views.py`:

.. code-block:: python

    from iommi import Page, Form, Table

    # Import any models you need from your models.  Here I'm using Artist
    from .models import Artist

    class TestPage(Page):
        create_form = Form.create(auto__model=Artist)
        a_table = Table(auto__model=Artist)

        class Meta:
            title = 'An iommi page!'

then hook into `urls.py`:

.. code-block:: python

    urlpatterns = [
        # ...your urls...
        path(
            'iommi-page-test/',
            TestPage().as_view()
        ),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('824363ca-4b3f-4120-b434-e9c28d7834fa', this)">▼ Hide result</div>
    <iframe id="824363ca-4b3f-4120-b434-e9c28d7834fa" src="doc_includes/getting_started/test_4__your_first_page.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

5. A simple function based view
-------------------------------

It's often useful to have a function based view around your iommi code to do
some basic setup. So we'll add an example for that too. With iommis
middleware you can return iommi objects from your view:


`views.py`:

.. code-block:: python

    def iommi_view(request, name):
        return TestPage(title=f'Hello {name}')

`urls.py`:

.. code-block:: python

    urlpatterns = [
        # ...your urls...
        path(
            'iommi-view-test/<name>/',
            iommi_view
        ),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('5ca8e208-2d54-4b04-b8c3-eb9fc2c32977', this)">▼ Hide result</div>
    <iframe id="5ca8e208-2d54-4b04-b8c3-eb9fc2c32977" src="doc_includes/getting_started/test_5__a_simple_function_based_view.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

6. Make iommi pages fit into your projects design
-------------------------------------------------

So far all the views we've created are rendered in plain bootstrap. Let's fit
the iommi views you've already added into the design of your project.

The simplest is to add something like this to your `settings.py`:

.. code-block:: python

    # These imports need to be at the bottom of the file!
    from iommi import Style, Asset
    from iommi.style_bootstrap import bootstrap

    IOMMI_DEFAULT_STYLE = Style(
        bootstrap,
        base_template='my_project/iommi_base.html',
        root__assets=dict(
            my_project_custom_css=Asset.css(attrs__href='/static/custom.css'),
            my_project_custom_js=Asset.js(attrs__src='/static/custom.js'),
        ),
    )

Where `my_project/iommi_base.html` could look something like this:

.. code-block:: html

    {% extends "iommi/base.html" %}

    {% block iommi_top %}
        {% include "my_menu.html" %}
    {% endblock %}

    {% block iommi_bottom %}
        {% include "my_footer.html" %}
    {% endblock %}


After you've set up your base style successfully, all the test pages you made
before (form, table, page, view) are now using your style.

