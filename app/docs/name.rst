.. _name:

.. _display_name:

.. _iommi_name:

.. _iommi_path:


`name`/`display_name`/`iommi_path`
-----------------------------------------------

The different name concepts in iommi can be confusing, but each has a logical place.



`name`
~~~~~~

The `name` is the name used in configuration for a part:

.. code-block:: python

    class MyTable(Table):
        foo = Column()

The `name` is "foo". 

There is a special situation when using deep dunder paths with :ref:`auto`:

.. code-block:: python

    table = Table(
        auto__model=Track,
        auto__include=[
            'album__artist__name',
        ],
    )

Here the `name` of the column is `album_artist_name`, with the double underscore collapsed down to single underscores. This is because otherwise iommi can't know if `__` means "enter the configuration namespace of the `Column` object, or if it means "traverse the foreign key to go from one model to another". So in this situation, to further configure the artist name column, you need the configuration path `columns__album_artist_name`.

`display_name`
~~~~~~~~~~~~~~

By default iommi will pick up `verbose_name` from your model if you use :ref:`auto`, and if there is no such information, it will take the `name` and capitalize it. If you want to override this you specify `display_name`:

.. code-block:: python

    table = Table(
        auto__model=Track,
        auto__include=[
            'album__artist__name',
        ],
        columns__album_artist_name__display_name='Hello',
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('6c198931-6911-4aab-b239-1adb101a6184', this)">▼ Hide result</div>
    <iframe id="6c198931-6911-4aab-b239-1adb101a6184" src="doc_includes/name/test_display_name.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

`iommi_path`
~~~~~~~~~~~~

The `iommi_path` is used in HTTP dispatching, so AJAX endpoints, and POST requests. Normally you don't need to use this yourself. These paths are `/` separated.

`iommi_dunder_path`
~~~~~~~~~~~~~~~~~~~
This is useful for finding the full path for an object. It's the value you get with the pick tool, and it's the same as `iommi_path` except `__` replaces `/`.

