

Edit tables
-----------

.. _edit-table-one-to-one:

How do you edit one-to-one fields in an edit table?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses EditColumn.field
.. uses EditColumn.columns
.. uses EditColumn.auto

Include them in `auto__include`. Say you have a profile model for an artist:

.. code-block:: python

    profile = Profile.objects.create(artist=black_sabbath)

Then you can include the artist name field:

.. code-block:: python

    edit_table = EditTable(
        auto__model=Profile,
        auto__include=['artist__name'],
        columns__artist_name__field__include=True,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('055f4637-5c3a-455d-a13d-ac325b15872b', this)">▼ Hide result</div>
    <iframe id="055f4637-5c3a-455d-a13d-ac325b15872b" src="doc_includes/cookbook_edit_tables/test_how_do_you_edit_one_to_one_in_a_table.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

