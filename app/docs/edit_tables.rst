

.. _edit-tables:

Edit tables
===========

iommi edit tables builds on top of iommi tables but enable editing of cells too.

A simple example:

.. code-block:: python

    EditTable(
        auto__model=Album,
        page_size=10,
        # Turn on the edit feature for the year column
        columns__year__field__include=True,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('70dc2dfb-4269-43da-81ff-7184826477cd', this)">▼ Hide result</div>
    <iframe id="70dc2dfb-4269-43da-81ff-7184826477cd" src="doc_includes/edit_tables/test_edit_tables.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

