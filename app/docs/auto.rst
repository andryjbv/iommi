

.. _auto:

`auto`
------

The `auto` configuration namespace is used to generate forms/tables/etc from Django models. The simplest example is:

.. code-block:: python

    form = Form(auto__model=Album)

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('2cdca7bd-229e-4fef-89a5-73df7e1d0317', this)">▼ Hide result</div>
    <iframe id="2cdca7bd-229e-4fef-89a5-73df7e1d0317" src="doc_includes/auto/test_auto.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

By default you will get all fields from the model except the primary key. You can use `include` to include it again:

.. code-block:: python

    form = Form(
        auto__model=Album,
        fields__pk__include=True,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('a6967d0a-67b1-4e6d-bbb3-9f5027811c58', this)">▼ Hide result</div>
    <iframe id="a6967d0a-67b1-4e6d-bbb3-9f5027811c58" src="doc_includes/auto/test_auto1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

You can specify which model fields to include via `auto__include` to include just the fields you want, or `auto__exclude` to take all fields except some excluded fields. Fields/columns/etc can be excluded/included later using `include` on the field:

.. code-block:: python

    form = Form(
        auto__model=Album,
        auto__include=['name', 'artist', 'year'],
        fields__name__include=False,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('95ed77b0-5a11-4d32-ba83-8336f4a848f6', this)">▼ Hide result</div>
    <iframe id="95ed77b0-5a11-4d32-ba83-8336f4a848f6" src="doc_includes/auto/test_auto2.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

