

Porting
-------

Existing function based views often have an initial part building a set of values from the view parameters that then is passed on as a context to the template rendering.

When refactoring this to the more iommi idiomatic style of calculating values in callbacks, it can sometimes be helpful to not have to move everything at once.

Let's look at an example to make this more concrete:

.. code-block:: python

    def some_function(a, b):
        return a + b

    def legacy_view(request, a, b):
        context = dict(a=a, b=b, c=some_function(a, b))
        return HttpResponse(Template('{{a}} + {{b}} = {{c}}').render(RequestContext(request, context)))

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('96cb76af-be8d-4dae-8ff0-1420dcf3c724', this)">▼ Hide result</div>
    <iframe id="96cb76af-be8d-4dae-8ff0-1420dcf3c724" src="doc_includes/cookbook_porting/test_existing_views.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

There is a configurable callback, `extra_params`, to provide extra parameters given, on top of the parameters already provided by Django and the iommi path machinery:

.. code-block:: python

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

    <div class="iframe_collapse" onclick="toggle('2dd99643-0dc8-44a9-9af2-a9842f1b0e7f', this)">▼ Hide result</div>
    <iframe id="2dd99643-0dc8-44a9-9af2-a9842f1b0e7f" src="doc_includes/cookbook_porting/test_existing_views1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

