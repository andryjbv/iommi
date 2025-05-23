.. _extra_params:


`extra_params`
--------------



`extra_params` is used to provide extra parameters, on top of the parameters already provided by Django and the iommi path machinery:

.. code-block:: python

    def some_function(a, b):
        return a + b

    class IommiPage(Page):
        class Meta:
            @staticmethod
            def extra_params(request, a, b):
                return dict(
                    c=some_function(a, b),
                )

        content = Template('{{ params.a }} + {{ params.b }} = {{ params.c }}')

    iommi_view = IommiPage().as_view()

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('09ffc9cd-2969-4ce0-815a-cb3978bd1904', this)">▼ Hide result</div>
    <iframe id="09ffc9cd-2969-4ce0-815a-cb3978bd1904" src="doc_includes/extra_params/test_extra_params.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

