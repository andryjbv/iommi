.. _include:

`include`
---------

The `include` configuration is used to include or exclude parts programmatically. Let's start with a simple example of a table:



.. code-block:: python

    table = Table(
        auto__model=Album,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('fda0c5e8-9b21-4923-9198-86353f9014bc', this)">▼ Hide result</div>
    <iframe id="fda0c5e8-9b21-4923-9198-86353f9014bc" src="doc_includes/include/test_include.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

We could make the `name` column only visible for staff users:

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__name__include=lambda user, **_: user.is_staff,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('44cd9aae-1a72-4850-bc90-6e5dee1d8628', this)">▼ Hide result</div>
    <iframe id="44cd9aae-1a72-4850-bc90-6e5dee1d8628" src="doc_includes/include/test_include1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

