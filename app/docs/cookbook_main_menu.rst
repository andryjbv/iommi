

.. _cookbook-main-menu:

Main menu
---------



How do I control which menu items are shown for a user?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses M.include

Using `include` you can control which menu items are shown for a given user. This also controls access, so you can know that your menu and your access control are always in sync.

.. code-block:: python

    menu = MainMenu(
        items=dict(
            albums=M(
                view=albums_view,
            ),
            artists=M(
                view=artists_view,
                include=lambda user, **_: user.is_staff,
            ),
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('97f28c77-f4e4-4b48-8f83-f7d5a139dfaa', this)">▼ Hide result</div>
    <iframe id="97f28c77-f4e4-4b48-8f83-f7d5a139dfaa" src="doc_includes/cookbook_main_menu/test_include.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('92b32572-b8e1-4f64-9636-ce597f3068ec', this)">▼ Hide result</div>
    <iframe id="92b32572-b8e1-4f64-9636-ce597f3068ec" src="doc_includes/cookbook_main_menu/test_include1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

How do I control the display name of a menu item?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses M.display_name

By default the display name is derived from the `name` of the `M` object. So given:

.. code-block:: python

    menu = MainMenu(
        items=dict(
            albums=M(view=albums_view),
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('3dbdab32-c58a-4e75-b450-b9b1763b16b6', this)">▼ Hide result</div>
    <iframe id="3dbdab32-c58a-4e75-b450-b9b1763b16b6" src="doc_includes/cookbook_main_menu/test_display_name.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

The `name` would be "albums", and the display name is automatically derived as "Albums". The translation from `name` to `display_name` replaces `_` with space, runs `gettext_lazy()` on the result, and then capitalizes that.

If you want to do something else, pass the `display_name` parameter:

.. code-block:: python

    menu = MainMenu(
        items=dict(
            albums=M(
                view=albums_view,
                display_name=gettext_lazy('Discography'),
            ),
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('9f497339-faaf-45a8-9379-f03474d891fe', this)">▼ Hide result</div>
    <iframe id="9f497339-faaf-45a8-9379-f03474d891fe" src="doc_includes/cookbook_main_menu/test_display_name1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Note that `display_name` can be a function too.

How do I add sub-paths for a menu item?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses M.paths

Since the menu system can control access, it is useful to nest path mappings under a specific menu item without showing them in the menu. This is done with the `paths` argument:

.. code-block:: python

    menu = MainMenu(
        items=dict(
            albums=M(
                view=albums_view,
                paths=[
                    path('<album_pk>/edit/', edit_album_view),
                ],
            ),
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('80307c40-9451-41e1-b125-b639162caa69', this)">► Show result</div>
    <iframe id="80307c40-9451-41e1-b125-b639162caa69" src="doc_includes/cookbook_main_menu/test_paths.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

How do I add external links in the menu?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses M.url
.. uses EXTERNAL

Use the special value `EXTERNAL` for the `view` argument, and use `url` argument:

.. code-block:: python

    menu = MainMenu(
        items=dict(
            albums=M(
                view=EXTERNAL,
                url='https://docs.iommi.rocks',
            ),
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('3351b253-8d55-434c-abb5-823742a9d68b', this)">▼ Hide result</div>
    <iframe id="3351b253-8d55-434c-abb5-823742a9d68b" src="doc_includes/cookbook_main_menu/test_external_links.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Note the icon added by default for an external link. This is configurable via the `icon_formatter` on your `Style`.

How do I nest menu items?
~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses M.items
.. uses M.open

You can create a menu hierarchy with the `items` argument, which produces expandable sections. iommi will open the menu items that matches the current URL by default. You can also force a submenu to be open with the `open` argument:

.. code-block:: python

    menu = MainMenu(
        items=dict(
            things=M(
                view=things_view,
                open=True,  # force open
                items=dict(
                    albums=M(
                        view=albums_view,
                    ),
                    artists=M(
                        view=artists_view,
                    )
                ),
            ),
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('e5441cfc-e595-451f-8f35-5dea49de108b', this)">▼ Hide result</div>
    <iframe id="e5441cfc-e595-451f-8f35-5dea49de108b" src="doc_includes/cookbook_main_menu/test_nesting.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

The `open` argument can be a callable.

How do I put arbitrary html in the menu?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses M.template

With the `template` argument you can put arbitrary html into menu items:

.. code-block:: python

    menu = MainMenu(
        items=dict(
            albums=M(
                view=EXTERNAL,
                template=Template('''
                <li style="margin-left: 1rem">
                    <span style="display: inline-block; width: 1.5rem; background: red; border-radius: 50%">&nbsp;</span>
                    <span style="display: inline-block; width: 1.5rem; background: orange; border-radius: 50%">&nbsp;</span>
                    <span style="display: inline-block; width: 1.5rem; background: yellow; border-radius: 50%">&nbsp;</span>
                    <span style="display: inline-block; width: 1.5rem; background: green; border-radius: 50%">&nbsp;</span>
                    <span style="display: inline-block; width: 1.5rem; background: blue; border-radius: 50%">&nbsp;</span>
                </li>
                ''')
            ),
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('8ee956db-ffb5-4486-84ec-51052282675e', this)">▼ Hide result</div>
    <iframe id="8ee956db-ffb5-4486-84ec-51052282675e" src="doc_includes/cookbook_main_menu/test_template.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Note that you want to include the `<li>` tag.

You can also override the base template via your `Style`.

How do I show which specific object I am on in the menu?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses M.path
.. uses M.url
.. uses M.params

If you have a list of objects and you click into one of them, you might want to show that item in the menu, and potentially also sub-pages for that item. You do that by using iommi path decoders, and mapping everything together with `display_name`, `path`, `params` and `url`:

.. code-block:: python

    menu = MainMenu(
        items=dict(
            albums=M(
                view=albums_view,
                items=dict(
                    album=M(
                        view=album_view,
                        display_name=lambda album, **_: str(album),
                        path='<album_pk>/',
                        params={'album'},
                        url=lambda album, **_: f'/albums/{album.pk}/',
                    ),
                )
            ),
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('be854b29-ec64-4467-b8bc-bf37f0aea384', this)">▼ Hide result</div>
    <iframe id="be854b29-ec64-4467-b8bc-bf37f0aea384" src="doc_includes/cookbook_main_menu/test_drill_down.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

How do I make a data driven dynamic submenu?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses M.items

There can be cases where you want a dynamic submenu where the items come from the database. To do this, specify `items` as a callable. Note that urls here can't be mapped to paths, as paths need to be known at startup.

.. code-block:: python

    menu = MainMenu(
        items=dict(
            albums=M(
                view=albums_view,
                items=lambda **_: {
                    f'album_{album.pk}': M(
                        view=EXTERNAL,
                        display_name=str(album),
                        url=album.get_absolute_url(),
                    )
                    for album in Album.objects.all()
                }
            )
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('73303aab-518e-4c3f-b74c-e47f3957c753', this)">▼ Hide result</div>
    <iframe id="73303aab-518e-4c3f-b74c-e47f3957c753" src="doc_includes/cookbook_main_menu/test_dynamic_submenu.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

