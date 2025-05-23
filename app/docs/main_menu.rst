

Main menu
~~~~~~~~~

.. warning::

    The `MainMenu` component is considered experimental. That means the API can change in breaking ways in minor releases of iommi. It also means you import from `iommi.experimental` to make that clear.

The main menu component in iommi is used to create the main navigation for your app. This is primarily useful for SaaS or internal apps. It creates a sidebar menu with support for nested menu items, and centralized access control that automatically shows only menu items the user has access to.

To set up your main menu:

- add the `iommi.experimental.main_menu.main_menu_middleware` middleware to the `MIDDLEWARE` list
- declare your `MainMenu`
- define the `IOMMI_MAIN_MENU` setting to point to where you have defined your menu (like `IOMMI_MAIN_MENU = 'your_app.main_menu.main_menu'`).
- add the url patterns from the menu to your app

Access control is recursive, meaning that if a user does not have access to a menu item, it is automatically denied access to all subitems.

.. note::

    There are many more examples in :doc:`the cookbook <cookbook_main_menu>`.

.. code-block:: python

    menu_declaration = MainMenu(
        items=dict(
            artists=M(
                icon='people',
                view=artists_view,
            ),
            albums=M(
                icon='disc',
                view=albums_view,
            ),
        ),
    )

Add the url patterns from the menu to your app:

.. code-block:: python

    urlpatterns = menu_declaration.urlpatterns()

Your views will now get the menu rendered on standard iommi views. For non-iommi views you can render the menu with `{{ request.iommi_main_menu }}`.

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('da8b5c61-1d37-4368-999a-b7ad8d57754d', this)">▼ Hide result</div>
    <iframe id="da8b5c61-1d37-4368-999a-b7ad8d57754d" src="doc_includes/main_menu/test_base.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

