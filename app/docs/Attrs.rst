

Attrs
=====

Base class: `Namespace`

The `attrs` namespace on `Field`, `Form`, `Header`, `Cell` and more is used to customize HTML attributes.

.. code-block:: python

    form = Form(
        auto__model=Album,
        fields__artist__attrs__foo='bar',
        fields__name__attrs__class__bar=True,
        fields__name__attrs__style__baz='qwe',
    )

or more succinctly:

.. code-block:: python

    form = Form(
        auto__model=Album,
        fields__artist__attrs__foo='bar',
        fields__name__attrs=dict(
            class__bar=True,
            style__baz='qwe',
        )
    )

The thing to remember is that the basic namespace is a dict with key value
pairs that gets projected out into the HTML, but there are two special cases
for `style` and `class`. The example above will result in the following
attributes on the field tag:

.. code-block:: html

   <div foo="bar" class="bar" style="baz: qwe">

The values in these dicts can be callables:

.. code-block:: python

    form = Form(
        auto__model=Album,
        fields__name__attrs__class__bar=
            lambda request, **_: request.user.is_staff,
    )

