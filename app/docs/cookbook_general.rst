

General
-------

How do I find the path to a parameter?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Navigating the namespaces can sometimes feel a bit daunting. To help with
this iommi has a special debug mode that can help a lot. By default it's
set to settings.DEBUG, but to set it explicitly put this in your settings:

.. code-block:: python

    IOMMI_DEBUG = True

Now iommi will output `data-iommi-path` attributes in the HTML that will
help you find the path to stuff to configure. E.g. in the kitchen
sink table example a cell looks like this:

.. code-block:: html

    <td data-iommi-path="columns__e__cell">explicit value</td>

To customize this cell you can pass for example
`columns__e__cell__format=lambda value, **_: value.upper()`. 

Instead of looking at the DOM, you can use the "pick" tool where you can get
the path by clicking on the item you want. You will also get a link to the 
right place into the API docs for the thing you clicked on. 

Another nice way to find what is available is to append `?/debug_tree` in the
url of your view. You will get a table of available paths with the ajax
endpoint path, and their types with links to the appropriate documentation.

If `IOMMI_DEBUG` is on you will also get the iommi debug toolbar on your pages.
`Code` will jump to the code for the current view
in PyCharm. You can configure the URL builder to make it open your favored
editor by setting `IOMMI_DEBUG_URL_BUILDER` in settings:

.. code-block:: python

    IOMMI_DEBUG_URL_BUILDER = lambda filename, lineno: f'my_editor://{filename}:{lineno}'

Visual Studio Code example:

.. code-block:: python

    IOMMI_DEBUG_URL_BUILDER = lambda filename, lineno: f"vscode://file/{filename}:{lineno}:0"

The `Tree` link will open the `?/debug_tree` page mentioned above.

How do I access a sibling component?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's say we have a `Page` with a form and a custom template, and we want
to access the form, we can do that via the `root` object:

.. code-block:: python

    class MyPage(Page):
        edit_album = Form.edit(auto__model=Album, instance=album)
        view_album = Template('''
            {{ root.parts.edit_album.fields.name.value }}
        ''')

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('c6691f61-bc86-4141-8579-8bf4b9d4d9a2', this)">▼ Hide result</div>
    <iframe id="c6691f61-bc86-4141-8579-8bf4b9d4d9a2" src="doc_includes/cookbook_general/test_access_other_component.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

