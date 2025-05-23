

Equivalence
===========

In iommi there are two equivalence principles that are important to grasp:
- declarative/programmatic hybrid API
- double underscore as a short hand syntax for nesting dicts

The model used for these examples is `Album`:

.. literalinclude:: models.py
     :start-at: class Album
     :end-before: def __str__
     :language: python


Declarative/programmatic hybrid API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The programmatic API is pretty straight forward: you have a class constructor that takes some arguments. The interesting part is how we can mirror that *exactly* into a declarative style.

.. code-block:: python

    table = Table(
        model=Album,
        columns=dict(
            name=Column(),
        ),
    )

This simple table can be written as a class definition:

.. code-block:: python

    class MyTable(Table):
        class Meta:
            model = Album

        name = Column()

There are two things to notice here: 

1. Variables declared in `class Meta` in iommi means they get passed into the constructor. `model = Album` in `Meta` is exactly the same as `Table(model=Album)`.
2. The `name` column is declared on the class itself, and the `columns` part of the argument (`Table(columns=dict(...)`) is implicit. For `Page` the same implicit name is called `parts`, and for `Form` it's called `fields`.

Double underscore short form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In iommi you can have very deeply nested object structures, and because you want to customize something deep inside a graph it would be cumbersome to nest dicts a lot. So `__` is used a separator.

Say we have a table, where we want to turn on filtering for a column, but we want to insert a special CSS class (called `special`) on the label of the search field:

.. code-block:: python

    table = Table(
        auto__model=Model,
        # Enable filtering
        columns__name__filter__include=True,
        # Set the CSS class on the label
        columns__name__filter__field__label__attrs__class__special=True,
    )

We could also write this without using `__` for nesting:

.. code-block:: python

    table = Table(
        auto=dict(model=Model),
        columns=dict(
            name=dict(
                filter=dict(
                    # Enable filtering
                    include=True,
                    # Set the CSS class on the label
                    field=dict(
                        label=dict(
                            attrs={
                                # have to use a dict literal here,
                                # because `class` is a reserved keyword in Python
                                'class': dict(
                                    special=True,
                                ),
                            },
                        ),
                    ),
                ),
            ),
        ),
    )

These two things have exactly the same meaning, but the `__` syntax is a lot shorter and cleaner.

Further examples
~~~~~~~~~~~~~~~~

We want to create a form to create an album for a specific artist. We already have the artist from the URL, so that field shouldn't be in the form.

The following forms all accomplish this goal (you can use `form.as_view()` to create a view from a `Form` instance):

.. code-block:: python

    form = Form.create(
        auto__model=Album,
        auto__exclude=['artist'],
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('3b2d753a-33da-41b5-ae7e-164d8183e3cf', this)">▼ Hide result</div>
    <iframe id="3b2d753a-33da-41b5-ae7e-164d8183e3cf" src="doc_includes/equivalency/test_equivalence.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. code-block:: python

    form = Form.create(
        auto=dict(
            model=Album,
            exclude=['artist'],
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('80e7f6a1-061a-446d-b89c-e1e31277062b', this)">► Show result</div>
    <iframe id="80e7f6a1-061a-446d-b89c-e1e31277062b" src="doc_includes/equivalency/test_equivalence1.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. code-block:: python

    form = Form.create(
        auto__model=Album,
        fields__artist__include=False,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('6c8d7e76-f412-4067-b015-6639c88d5ab7', this)">► Show result</div>
    <iframe id="6c8d7e76-f412-4067-b015-6639c88d5ab7" src="doc_includes/equivalency/test_equivalence2.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. code-block:: python

    class AlbumForm(Form):
        class Meta:
            auto__model = Album
            auto__exclude = ['artist']

    form = AlbumForm.create()

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('9f52fe05-d9a2-4509-a0b9-bea249dd04c9', this)">► Show result</div>
    <iframe id="9f52fe05-d9a2-4509-a0b9-bea249dd04c9" src="doc_includes/equivalency/test_equivalence3.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. code-block:: python

    class AlbumForm(Form):
        class Meta:
            auto__model = Album
            auto__include = ['name', 'year']

    form = AlbumForm.create()

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('b54af291-0a91-4848-9ab7-fb105b0712c0', this)">► Show result</div>
    <iframe id="b54af291-0a91-4848-9ab7-fb105b0712c0" src="doc_includes/equivalency/test_equivalence4.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. code-block:: python

    class AlbumForm(Form):
        class Meta:
            auto__model = Album
            fields__artist__include = False

    form = AlbumForm.create()

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('01dba5ec-2e28-4492-9c46-1fae6c8cd653', this)">► Show result</div>
    <iframe id="01dba5ec-2e28-4492-9c46-1fae6c8cd653" src="doc_includes/equivalency/test_equivalence5.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Without using the `auto` features:

.. code-block:: python

    class AlbumForm(Form):
        name = Field()
        year = Field.integer()

        class Meta:
            title = 'Create album'
            actions__submit__post_handler = create_album

    form = AlbumForm()

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('0d09941a-8d8e-4e00-a885-71a8a6bf7700', this)">► Show result</div>
    <iframe id="0d09941a-8d8e-4e00-a885-71a8a6bf7700" src="doc_includes/equivalency/test_equivalence6.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. code-block:: python

    form = Form(
        fields__name=Field(),
        fields__year=Field.integer(),
        title='Create album',
        actions__submit__post_handler=create_album,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('3e1bb22a-a1c5-49f6-a36b-b5d7e4a2980a', this)">► Show result</div>
    <iframe id="3e1bb22a-a1c5-49f6-a36b-b5d7e4a2980a" src="doc_includes/equivalency/test_equivalence7.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

You can read more about this in the philosophy section under :ref:`philosophy_hybrid_api`.

