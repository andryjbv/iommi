

Parts & Pages
-------------

.. _override-part-of-page:

How do I override part of a part/page?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Page.parts
.. uses Fragment.children
.. Attrs

This is all just *standard* iommi declarative magic, but as you are likely new to it
this might take a while to get used to. Let's say you created yourself a master template
for your site.

.. code-block:: python

    class BasePage(Page):
        title = html.h1('My awesome webpage')
        subtitle = html.h2('It rocks')

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('6dad1f89-05c8-4368-b086-6c95792abfa3', this)">▼ Hide result</div>
    <iframe id="6dad1f89-05c8-4368-b086-6c95792abfa3" src="doc_includes/cookbook_parts_pages/test_how_do_i_override_part_of_a_part_page.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Which you can use like this:

.. code-block:: python

    class IndexPage(BasePage):
        body = 'body'

    index = IndexPage(parts__subtitle__children__child='Still rocking...').as_view()

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('fb553163-7ef9-4974-8ee8-5799887a899b', this)">▼ Hide result</div>
    <iframe id="fb553163-7ef9-4974-8ee8-5799887a899b" src="doc_includes/cookbook_parts_pages/test_how_do_i_override_part_of_a_part_page1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

or as a function based view:

.. code-block:: python

    def index(request):
        return IndexPage(parts__subtitle__children__child='Still rocking...')

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('e56afba7-750c-4923-834e-1e7498061f1b', this)">► Show result</div>
    <iframe id="e56afba7-750c-4923-834e-1e7498061f1b" src="doc_includes/cookbook_parts_pages/test_how_do_i_override_part_of_a_part_page2.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Here you can see that `Part` s (`Page` s are themselves `Part` s) form a tree and the direct children are gathered in the `parts` namespace. Here we overwrote a leaf of
an existing namespace, but you can also add new elements or replace bigger
parts (and most of the time it doesn't matter if you use the `class Meta` or the
keyword arguments to init syntax):

.. code-block:: python

    class IndexPage(BasePage):
        title = html.img(
            attrs=dict(
                src='https://docs.iommi.rocks/_static/logo_with_outline.svg',
                alt='iommi logo',
                width='70px',
            ),
        )

    index = IndexPage(parts__subtitle=None)

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('15e511cf-40b9-43c0-9c2e-907dd5b73c87', this)">▼ Hide result</div>
    <iframe id="15e511cf-40b9-43c0-9c2e-907dd5b73c87" src="doc_includes/cookbook_parts_pages/test_how_do_i_override_part_of_a_part_page3.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

In the above we replaced the title and removed the subtitle element completely. The
latter of which shows one of the gotchas as only `str`, `Part` and the django
template types are gathered into the parts structure when a `Part` class definition
is processed. As `None` is not an instance of those types, you can remove things
by setting their value to `None`.

.. _title-of-page:

How do I set the title of my page?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Page.title

As in the text shown in the browser status bar?

.. code-block:: python

    Page(title='The title in the browser')

Note that this is different from

.. code-block:: python

    class MyPage(Page):
        title = Header('A header element in the dom')

    MyPage()

Which is equivalent to:

.. code-block:: python

    Page(parts__title=Header('A header element in the dom'))

.. _context-of-page:

How do I specify the context used when a Template is rendered?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Page.context

.. code-block:: python

    class MyPage(Page):
        body = Template("""A django template was rendered on {{today}}.""")


    def index(request):
        context = {'today': date.today()}

        return MyPage(context=context)

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('e69de9d0-aced-4f94-a284-a25456b83235', this)">▼ Hide result</div>
    <iframe id="e69de9d0-aced-4f94-a284-a25456b83235" src="doc_includes/cookbook_parts_pages/test_how_do_i_specify_the_context_used_when_a_template_is_rendered.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

You can also insert items in the context via the declaration. This
not only makes the above shorter, but also makes it easy to write abstractions that
can be extended later:

.. code-block:: python

    my_page = Page(
        parts__body=Template("""A django template was rendered on {{today}}."""),
        context__today=lambda **_: date.today(),
    ).as_view()

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('2cf65410-fc7e-47a4-9211-b1332c0f51b5', this)">▼ Hide result</div>
    <iframe id="2cf65410-fc7e-47a4-9211-b1332c0f51b5" src="doc_includes/cookbook_parts_pages/test_how_do_i_specify_the_context_used_when_a_template_is_rendered1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

