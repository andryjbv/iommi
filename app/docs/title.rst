.. _title:

.. _h_tag:

`title`/`h_tag`
---------------

The `title` attribute is for setting the title or heading of a component. To customize the exact rendering you use `h_tag`.



`title`
~~~~~~~

.. code-block:: python

    form = Form.create(
        auto__model=Artist,
        title='Custom title',
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('6c33b243-b69a-4631-be5b-41e4565d88ae', this)">▼ Hide result</div>
    <iframe id="6c33b243-b69a-4631-be5b-41e4565d88ae" src="doc_includes/title/test_template_as_path.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

`h_tag`
~~~~~~~

.. code-block:: python

    form = Form.create(
        auto__model=Artist,
        h_tag__attrs__style__background='blue',
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('3237f0db-dfbd-4385-9e3d-df2c90f1dc8a', this)">▼ Hide result</div>
    <iframe id="3237f0db-dfbd-4385-9e3d-df2c90f1dc8a" src="doc_includes/title/test_template_objects.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

