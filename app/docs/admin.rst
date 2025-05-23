

Admin
=====

The powerful abstractions of iommi enable us to build an admin interface
that is automagically created based on your models, while retaining the full
feature set of iommi.

Index page (with configuration to show `Artist`, `Album` and `Track` models):

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('1b302f29-fb31-44e9-b994-298264e1bc2a', this)">▼ Hide result</div>
    <iframe id="1b302f29-fb31-44e9-b994-298264e1bc2a" src="doc_includes/admin/test_admin.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Displaying albums:

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('d864e933-098e-4f14-ad71-e468040ed4be', this)">▼ Hide result</div>
    <iframe id="d864e933-098e-4f14-ad71-e468040ed4be" src="doc_includes/admin/test_admin1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Editing an album:

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('88423ff5-25e3-4afd-abf2-c792d8b69e3b', this)">▼ Hide result</div>
    <iframe id="88423ff5-25e3-4afd-abf2-c792d8b69e3b" src="doc_includes/admin/test_admin2.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Delete page for an album:

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('c3beebdd-2bb5-40be-8d3e-4189ff1b9d54', this)">▼ Hide result</div>
    <iframe id="c3beebdd-2bb5-40be-8d3e-4189ff1b9d54" src="doc_includes/admin/test_admin3.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Installation
~~~~~~~~~~~~

First declare a subclass of `Admin`:

.. code-block:: python

    from iommi.admin import Admin

    class MyAdmin(Admin):
        pass

This is the place you will put global configuration. If you don't need any you
can skip this step. Next plug it into your urls:

.. code-block:: python

    urlpatterns = [
        # ...

        path('iommi-admin/', include(MyAdmin.urls())),
    ]

Now you have the iommi admin gui for your app!

Customization
~~~~~~~~~~~~~

Add a model to the admin
------------------------

You can add an app to your admin from your global config like this:

.. code-block:: python

    class MyAdmin(Admin):
        class Meta:
            apps__myapp_mymodel__include = True

This is especially useful for adding config to a third party app that doesn't have built in iommi admin configuration.

You can also add the config in the app, by creating a `iommi_admin.py` file in your app, and putting the configuration there:

.. code-block:: python

    class Meta:
        apps__myapp_mymodel__include = True

Remove a model from the admin
-----------------------------

By default iommi displays the built in Django `User` and `Group` models. You can override this like:

.. code-block:: python

    class MyAdmin(Admin):
        class Meta:
            apps__auth_user__include = False

This turns off the admin of the `User` table in the `auth` app. Your global config always has priority.

Permissions
-----------

By default staff users have access to the admin. You can change this by
overriding `has_permission`:

.. code-block:: python

    from iommi.admin import Admin

    class MyAdmin(Admin):
        @staticmethod
        def has_permission(request, operation, model=None, instance=None):
            # This is the default implementation
            return request.user.is_staff

`operation` is one of `create`, `edit`, `delete`, `list` and `all_models`. The
`model` parameter will be given for create/edit/delete/list, and instance will
be supplied in edit/delete.

HTML attributes
---------------

You can configure attributes in the admin similarly to the rest of iommi, on
the `Meta` class:

.. code-block:: python

    class MyAdmin(Admin):
        class Meta:
            parts__list_docs_album__columns__name__header__attrs__style__background = 'yellow'

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('f1cc2f9f-f4dd-424c-af8b-8d7c73249a6b', this)">▼ Hide result</div>
    <iframe id="f1cc2f9f-f4dd-424c-af8b-8d7c73249a6b" src="doc_includes/admin/test_html_attributes.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

The easiest way to find the path for configuration is to have
`settings.IOMMI_DEBUG` turned on (by default on if `DEBUG` is on), and use
the pick feature and click on the element. You'll get the path and also
the type so you can click your way to the documentation for that class.

In the example above the `data-iommi-path` would be
`parts__all_models__columns__model_name__cell` and `data-iommi-type` is
:doc:`Cell`. In the docs for `Cell` you can find that cells have `attrs`.

Change grouping of models
-------------------------

By default iommi groups models in the admin by the app they belong to. You can override this with the `group` argument:

.. code-block:: python

    class MyAdmin(Admin):
        class Meta:
            apps__docs_album__group = 'The endless search for where you are'

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('1959f178-2792-46fa-a242-322b01f1c794', this)">▼ Hide result</div>
    <iframe id="1959f178-2792-46fa-a242-322b01f1c794" src="doc_includes/admin/test_change_grouping.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

