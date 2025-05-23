.. _iommi_style:

`iommi_style`
-------------

The :ref:`style` system is what you normally use to specify how your product should look and behave, but something you want something more limited for just one or a few places. You can then specify a :doc:`Style` object directly on a component:



.. code-block:: python

    from iommi.style_bootstrap5 import bootstrap5
    form = Form(
        auto__model=Album,
        iommi_style=Style(
            bootstrap5,  # Based on the bootstrap style
            Field=dict(
                input__attrs__style__background='blue',
            )
        )
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('4ed8f7ec-ece0-4ad4-ae9c-20ad3d74d06b', this)">▼ Hide result</div>
    <iframe id="4ed8f7ec-ece0-4ad4-ae9c-20ad3d74d06b" src="doc_includes/iommi_style/test_iommi_style.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

