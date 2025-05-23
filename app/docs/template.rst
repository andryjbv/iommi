.. _template:

`template`
----------

With the :ref:`philosophy of escape hatches <escape-hatches>`, at the edge we enable replacing the entire rendering of components with the `template` config. You can use it in `Table` cells, to render table rows, to replace the rendering of fields, inputs, headers, and more. The `template` argument supports two types of values:



Template path
~~~~~~~~~~~~~

Strings are interpreted as template paths:

.. code-block:: python

    form = Form.create(
        auto__model=Artist,
        fields__name__template='test_template_as_path.html',
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('f9c47df9-af5b-48b5-bb55-cd1468cbd801', this)">▼ Hide result</div>
    <iframe id="f9c47df9-af5b-48b5-bb55-cd1468cbd801" src="doc_includes/template/test_template_as_path.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

`Template` object
~~~~~~~~~~~~~~~~~

Pass a Django `Template` object to write the template code you want inline:

.. code-block:: python

    form = Form.create(
        auto__model=Artist,
        fields__name__template=Template('template contents <b>here</b>'),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('5310f48f-12a2-4303-a3ab-afb62a0b6962', this)">▼ Hide result</div>
    <iframe id="5310f48f-12a2-4303-a3ab-afb62a0b6962" src="doc_includes/template/test_template_objects.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

