

.. _attr:

`attr`
------

`attr` is the configuration for specifying what Python attribute is read from or written to. Set it to `None` to make a `Field`/`Column`/etc that does not write or read from an attribute on the objects it works on. This is useful for displaying computed data without needing to pollute your model class with single use methods.

`attr` defaults to the `name`, so this:

.. code-block:: python

    class MyForm(Form):
        foo = Field()

is the same as:

.. code-block:: python

    class MyForm(Form):
        foo = Field(attr='foo')

`attr` values can be dunder paths:

.. code-block:: python

    class TrackTable(Table):
        artist_name = Column(attr='album__artist__name')

        class Meta:
            auto__model = Track
            auto__include = []

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('4b7576c3-20fb-47bf-9106-6ac884bfb736', this)">▼ Hide result</div>
    <iframe id="4b7576c3-20fb-47bf-9106-6ac884bfb736" src="doc_includes/attr/test_attr_dunder_paths.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

(Although this example is more idiomatically written with `auto`)

