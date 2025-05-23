.. _after:

`after`
-------

Ordering of fields and columns is based on the declared order, the order in the model (when using :ref:`auto`), and the `after` configuration. The last takes precedent over the others.

To order fields, set `after` to:

- `field_name` to place after the named field
- `>field_name` to place after the named field
- `<field_name` to place before the named field
- an integer index
- the special value `LAST` to put a field last

Using `after` is especially useful when you already have a complex object that you want to add one or a few fields to in some specific position.



.. code-block:: python

    form = Form(
        auto__model=Album,
        fields__name__after=LAST,
        fields__year__after='artist',
        fields__artist__after=0,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('fe04c0ed-0abf-47b6-916f-7fea0754913a', this)">▼ Hide result</div>
    <iframe id="fe04c0ed-0abf-47b6-916f-7fea0754913a" src="doc_includes/after/test_after.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

This will make the field order `artist`, `year`, `name`.

If there are multiple fields with the same index or name the order of the fields will be used to disambiguate.

