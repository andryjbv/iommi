

.. _cookbook-tables:

Tables
------

How do I customize the rendering of a table?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Table rendering can be customized on multiple levels. You pass a template with the `template` argument, which
is either a template name or a `Template` object.

Customize the HTML attributes of the table tag via the `attrs` argument. See :ref:`attrs <attributes>`.

To customize the row, see `How do I customize the rendering of a row?`_

To customize the cell, see `How do I customize the rendering of a cell?`_

To customize the rendering of the table, see `table-as-div`_

.. _turn-off-pagination:

How do you turn off pagination?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Table.page_size
.. uses EditTable.page_size
.. uses TableAutoConfig.model

Specify `page_size=None`:

.. code-block:: python

    table = Table(
        auto__model=Album,
        page_size=None,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('6e28ee98-4ea3-4f2e-b2a2-e3bb0d5d2f11', this)">▼ Hide result</div>
    <iframe id="6e28ee98-4ea3-4f2e-b2a2-e3bb0d5d2f11" src="doc_includes/cookbook_tables/test_how_do_you_turn_off_pagination.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Or in the declarative style:

.. code-block:: python

    class MyTable(Table):
        name = Column()

        class Meta:
            page_size = None

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('216aa842-6dfa-4e85-a088-e60127ccde40', this)">▼ Hide result</div>
    <iframe id="216aa842-6dfa-4e85-a088-e60127ccde40" src="doc_includes/cookbook_tables/test_how_do_you_turn_off_pagination1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _customize-table-cell-render:

How do I customize the rendering of a cell?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Attrs
.. uses Cell.attrs
.. uses Cell.template
.. uses Cell.url
.. uses EditCell.attrs
.. uses EditCell.template
.. uses EditCell.url
.. uses Column.cell
.. uses EditColumn.cell

You can customize the :doc:`Cell` rendering in several ways:

- You can modify the html attributes via `cell__attrs`. See :ref:`attrs <attributes>`.

- Use `cell__template` to specify a template. You can give a string and it will be interpreted as a template name, or you can pass a `Template` object.

- Pass a url (or callable that returns a url) to `cell__url` to make the cell a link (see next question).

.. _cell-link:

How do I make a link in a cell?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Cell.url
.. uses EditCell.url
.. uses Column.cell
.. uses EditColumn.cell
.. uses Table.columns
.. uses TableAutoConfig.model

This is such a common case that there's a special case for it: pass the `url` and `url_title` parameters to the `cell`:

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__name__cell__url='http://example.com',
        columns__name__cell__url_title='go to example',
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('6a1daa1d-dff2-44ac-8dbc-224c98081a5f', this)">▼ Hide result</div>
    <iframe id="6a1daa1d-dff2-44ac-8dbc-224c98081a5f" src="doc_includes/cookbook_tables/test_how_do_i_make_a_link_in_a_cell.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _column-computed-data:

How do I create a column based on computed data (i.e. a column not based on an attribute of the row)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Cell.value
.. uses Cell.format
.. uses EditCell.value
.. uses EditCell.format
.. uses Column.cell
.. uses EditColumn.cell
.. uses Table.columns
.. uses TableAutoConfig.model

Let's say we have a model like this:

.. code-block:: python

    class Foo(models.Model):
        value = models.IntegerField()

And we want a computed column `square` that is the square of the value, then we can do:

.. code-block:: python

    table = Table(
        auto__model=Foo,
        columns__square=Column(
            # computed value:
            cell__value=lambda row, **_: row.value * row.value,
        )
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('27d3f0cb-a61c-41e7-ac36-4ff8b382bf63', this)">▼ Hide result</div>
    <iframe id="27d3f0cb-a61c-41e7-ac36-4ff8b382bf63" src="doc_includes/cookbook_tables/test_how_do_i_create_a_column_based_on_computed_data_.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

or we could do:

.. code-block:: python

    Table(
        auto__model=Foo,
        columns__square=Column(
            attr='value',
            cell__format=lambda value, **_: value * value,
        )
    )

This only affects the formatting when we render the cell value. Which might make more sense depending on your situation but for the simple case like we have here the two are equivalent.

How do I get iommi tables to understand my Django ModelField subclasses?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See :doc:`registrations`.

.. _reorder-columns:

How do I reorder columns?
~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Column.after
.. uses EditColumn.after
.. uses Table.columns
.. uses TableAutoConfig.model

By default the columns come in the order defined so if you have an explicit table defined, just move them around there. If the table is generated from a model definition, you can also move them in the model definition if you like, but that might not be a good idea. So to handle this case we can set the ordering on a column by giving it the `after` argument. Let's start with a simple model:

.. code-block:: python

    class Foo(models.Model):
        a = models.IntegerField()
        b = models.IntegerField()
        c = models.IntegerField()

If we just do `Table(auto__model=Foo)` we'll get the columns in the order a, b, c. But let's say I want to put c first, then we can pass it the `after` value `-1`:

.. code-block:: python

    table = Table(auto__model=Foo, columns__c__after=-1)

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('d54b128b-870c-4a42-b0ad-3ab85a4051db', this)">▼ Hide result</div>
    <iframe id="d54b128b-870c-4a42-b0ad-3ab85a4051db" src="doc_includes/cookbook_tables/test_how_do_i_reorder_columns.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

`-1` means the first, other numbers mean index. We can also put columns after another named column like so:

.. code-block:: python

    table = Table(auto__model=Foo, columns__c__after='a')

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('400ee03c-fa95-446e-b34b-6a5beb6bd0cc', this)">▼ Hide result</div>
    <iframe id="400ee03c-fa95-446e-b34b-6a5beb6bd0cc" src="doc_includes/cookbook_tables/test_how_do_i_reorder_columns1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

this will put the columns in the order a, c, b.

There is a special value `LAST` (import from `iommi.declarative`) to put something last in a list:

.. code-block:: python

    table = Table(auto__model=Foo, columns__a__after=LAST)

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('fcf0a39e-7ca4-42bd-9634-c90d8f8969cf', this)">▼ Hide result</div>
    <iframe id="fcf0a39e-7ca4-42bd-9634-c90d8f8969cf" src="doc_includes/cookbook_tables/test_how_do_i_reorder_columns2.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _filter-column:

How do I enable searching/filter on columns?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Column.filter
.. uses EditColumn.filter
.. uses Filter.include
.. uses TableAutoConfig.model

Pass the value `filter__include=True` to the column, to enable searching
in the advanced query language.

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__name__filter__include=True,
    )

The `filter` namespace here is used to configure a :doc:`Filter` so you can
configure the behavior of the searching by passing parameters here.

The `filter__field` namespace is used to configure the :doc:`Field`, so here you
can pass any argument to `Field` here to customize it.

If you just want to have the filter available in the advanced query language,
you can turn off the field in the generated form by passing
`filter__field__include=False`:

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('495ac683-e342-41dd-b4d3-425a51563ced', this)">▼ Hide result</div>
    <iframe id="495ac683-e342-41dd-b4d3-425a51563ced" src="doc_includes/cookbook_tables/test_how_do_i_enable_searching_filter_on_columns.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _freetext-column:

How do I make a freetext search field?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Filter.freetext
.. uses Column.filter
.. uses TableAutoConfig.model

If you want to filter based on a freetext query on one or more columns we've got a nice little feature for this:

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__name__filter=dict(
            freetext=True,
            include=True,
        ),
        columns__year__filter__freetext=True,
        columns__year__filter__include=True,
    )

This will display one search box to search both `year` and `name` columns:

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('6a97c53d-0ba2-4254-9893-cd839eb98ee1', this)">▼ Hide result</div>
    <iframe id="6a97c53d-0ba2-4254-9893-cd839eb98ee1" src="doc_includes/cookbook_tables/test_how_do_i_make_a_freetext_search_field.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

How do I customize HTML attributes, CSS classes or CSS style specifications?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Table.attrs
.. uses Form.attrs
.. uses Field.attrs

The `attrs` namespace has special handling to make it easy to customize. There are three main cases:

First the straight forward case where a key/value pair is rendered in the output:

.. code-block:: pycon

    >>> from iommi.attrs import render_attrs
    >>> from iommi.declarative.namespace import Namespace
    >>> render_attrs(Namespace(foo='bar'))
    ' foo="bar"'

Then there's a special handling for CSS classes:

.. code-block:: pycon

    >>> render_attrs(Namespace(class__foo=True, class__bar=True))
    ' class="bar foo"'

Note that the class names are sorted alphabetically on render.

Lastly there is the special handling of `style`:

.. code-block:: pycon

    >>> render_attrs(Namespace(style__font='Arial'))
    ' style="font: Arial"'

If you need to add a style with `-` in the name you have to do this:


.. code-block:: pycon

    >>> render_attrs(Namespace(**{'style__font-family': 'sans-serif'}))
    ' style="font-family: sans-serif"'


Everything together:

.. code-block:: pycon

    >>> render_attrs(
    ...     Namespace(
    ...         foo='bar',
    ...         class__foo=True,
    ...         class__bar=True,
    ...         style__font='Arial',
    ...         **{'style__font-family': 'serif'}
    ...     )
    ... )
    ' class="bar foo" foo="bar" style="font-family: serif; font: Arial"'

.. _customize-rendering-row:

How do I customize the rendering of a row?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Table.row
.. uses EditTable.row
.. uses RowConfig.attrs
.. uses RowConfig.template

You can customize the row rendering in two ways:

- You can modify the html attributes via `row__attrs`. See :ref:`attrs <attributes>`.

- Use `row__template` to specify a template. You can give a string and it will be interpreted as a template name, or you can pass a `Template` object.

In templates you can access the raw row via `row`. This would typically be one of your model objects. You can also access the cells of the table via `cells`. A naive template for a row would be `<tr>{% for cell in cells %}<td>{{ cell }}{% endfor %}</tr>`. You can access specific cells by their column names like `{{ cells.artist }}`.

To customize the cell, see `How do I customize the rendering of a cell?`_

.. _customize-header:

How do I customize the rendering of a header?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Column.header
.. uses EditColumn.header

You can customize headers in two ways:

- You can modify the html attributes via `header__attrs`. See :ref:`attrs <attributes>`.

- Use `header__template` to specify a template. You can give a string and it will be interpreted as a template name, or you can pass a `Template` object.

.. _turn-off-header:

How do I turn off the header?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Table.header
.. uses EditTable.header

Set `header__template` to `None`.

How do I add fields to a table that is generated from a model?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the question `column-computed-data`_

.. _show-columns:

How do I specify which columns to show?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Column.include
.. uses EditColumn.include
.. uses Column.render_column
.. uses TableAutoConfig.model
.. uses TableAutoConfig.include
.. uses TableAutoConfig.exclude
.. uses TableAutoConfig.default_included

Pass `include=False` to hide the column or `include=True` to show it. By default columns are shown, except the primary key column that is by default hidden. You can also pass a callable here like so:

.. code-block:: python

    Table(
        auto__model=Album,
        columns__name__include=
            lambda request, **_: request.GET.get('some_parameter') == 'hello!',
    )

This will show the column `name` only if the GET parameter `some_parameter` is set to `hello!`.

To be more precise, `include` turns off the entire column. Sometimes you want to have the searching turned on, but disable the rendering of the column. To do this use the `render_column` parameter instead. This is useful to for example turn on filtering for a column, but not render it:

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__year__render_column=False,
        columns__year__filter__include=True,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('64d5bd5c-ccf1-4dff-8d21-56cbc3e2c0ad', this)">▼ Hide result</div>
    <iframe id="64d5bd5c-ccf1-4dff-8d21-56cbc3e2c0ad" src="doc_includes/cookbook_tables/test_how_do_i_specify_which_columns_to_show.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Use `auto__include`, to specify the complete list of columns you want:

.. code-block:: python

    table = Table(
        auto__model=Album,
        auto__include=['name', 'artist'],
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('b1f90f03-ce94-4431-b3fb-4a9efcf5bdba', this)">▼ Hide result</div>
    <iframe id="b1f90f03-ce94-4431-b3fb-4a9efcf5bdba" src="doc_includes/cookbook_tables/test_how_do_i_specify_which_columns_to_show1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Instead of using `auto__include`, you can also use `auto__exclude` to just exclude the columns you don't want:

.. code-block:: python

    table = Table(
        auto__model=Album,
        auto__exclude=['year'],
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('fa076db6-a8c4-4c5a-bfec-56ed12429160', this)">▼ Hide result</div>
    <iframe id="fa076db6-a8c4-4c5a-bfec-56ed12429160" src="doc_includes/cookbook_tables/test_how_do_i_specify_which_columns_to_show2.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

There is also a config option `default_included` which is by default `True`, which is where iommi's default behavior of showing all columns comes from. If you set it to `False` columns are now opt-in:

.. code-block:: python

    table = Table(
        auto__model=Album,
        auto__default_included=False,
        # Turn on only the name column
        columns__name__include=True,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('30c6b226-f93b-4fdc-8fba-563bdf0e8252', this)">▼ Hide result</div>
    <iframe id="30c6b226-f93b-4fdc-8fba-563bdf0e8252" src="doc_includes/cookbook_tables/test_how_do_i_specify_which_columns_to_show3.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _programmatic-table-data-access:

How do I access table data programmatically (like for example to dump to json)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.cells_for_rows
.. uses EditTable.cells_for_rows

Here's a simple example that prints a table to stdout:

.. code-block:: python

    def print_table(table):
        for row in table.cells_for_rows():
            for cell in row:
                print(cell.render_formatted(), end=' ')
            print()

    table = Table(auto__model=Album).bind(request=req('get'))
    print_table(table)

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('18c05b1a-1833-4767-bcba-1d4b77ad5269', this)">▼ Hide result</div>
    <iframe id="18c05b1a-1833-4767-bcba-1d4b77ad5269" src="doc_includes/cookbook_tables/test_how_do_i_access_table_data_programmatically_.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _fk-related-data-access:

How do I access foreign key related data in a column?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Column.attr
.. uses Table.auto
.. uses EditColumn.attr
.. uses EditTable.auto

Let's say we have two models:

.. code-block:: python

    class Foo(models.Model):
        a = models.IntegerField()

.. code-block:: python

    class Bar(models.Model):
        b = models.IntegerField()
        c = models.ForeignKey(Foo, on_delete=models.CASCADE)

we can build a table of `Bar` that shows the data of `a` like this:

.. code-block:: python

    table = Table(
        auto__model=Bar,
        columns__a=Column(attr='c__a'),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('0a569ff7-823e-41c5-8fbb-8f1e3ff68548', this)">▼ Hide result</div>
    <iframe id="0a569ff7-823e-41c5-8fbb-8f1e3ff68548" src="doc_includes/cookbook_tables/test_how_do_i_access_foreign_key_related_data_in_a_column.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Or like this:

.. code-block:: python

    table = Table(
        auto__model=Bar,
        include=['b', 'c__a'],
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('1817e357-8c67-4876-baec-c314c521df8f', this)">▼ Hide result</div>
    <iframe id="1817e357-8c67-4876-baec-c314c521df8f" src="doc_includes/cookbook_tables/test_how_do_i_access_foreign_key_related_data_in_a_column1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

iommi will do automatic `select_related` and/or `prefetch_related` as appropriate in many cases too, so you mostly don't need to worry about that.

.. _table-sorting:

How do I turn off sorting? (on a column or table wide)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.sortable
.. uses Column.sortable
.. uses EditTable.sortable
.. uses EditColumn.sortable

To turn off column on a column pass it `sortable=False` (you can also use a lambda here!):

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__name__sortable=False,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('de39e575-c8a6-4ce3-a87a-e402b4c6a0ec', this)">▼ Hide result</div>
    <iframe id="de39e575-c8a6-4ce3-a87a-e402b4c6a0ec" src="doc_includes/cookbook_tables/test_how_do_i_turn_off_sorting.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

and to turn it off on the entire table:

.. code-block:: python

    table = Table(
        auto__model=Album,
        sortable=False,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('78bb4434-d72f-4cb6-b373-6af2c04eefaf', this)">▼ Hide result</div>
    <iframe id="78bb4434-d72f-4cb6-b373-6af2c04eefaf" src="doc_includes/cookbook_tables/test_how_do_i_turn_off_sorting1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _header-title:

How do I specify the title of a header?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Column.display_name
.. uses EditColumn.display_name

The `display_name` property of a column is displayed in the header.

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__name__display_name='header title',
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('64a05c49-69a1-47a7-bbb6-71ca44fc6dc3', this)">▼ Hide result</div>
    <iframe id="64a05c49-69a1-47a7-bbb6-71ca44fc6dc3" src="doc_includes/cookbook_tables/test_how_do_i_specify_the_title_of_a_header.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _sort-direction:

How do I set the default sort direction of a column to be descending instead of ascending?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Column.sort_default_desc
.. uses EditColumn.sort_default_desc

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__name__sort_default_desc=True,  # or a lambda!
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('a088d078-c92e-47d8-8a18-2be0c5bdfc77', this)">► Show result</div>
    <iframe id="a088d078-c92e-47d8-8a18-2be0c5bdfc77" src="doc_includes/cookbook_tables/test_how_do_i_set_the_default_sort_order_of_a_column_to_be_descending_instead_of_ascending.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _default-sort-order:

How do I set the default sorting column of a table?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.default_sort_order

Tables are sorted by default on the order specified in the models `Meta` and then on `pk`. Set `default_sort_order` to set another default ordering:

.. code-block:: python

    table = Table(
        auto__model=Album,
        default_sort_order='year',
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('3e4a7c24-4843-4579-a75c-e0921956bcba', this)">▼ Hide result</div>
    <iframe id="3e4a7c24-4843-4579-a75c-e0921956bcba" src="doc_includes/cookbook_tables/test_how_do_i_set_the_default_sort_order_on_a_table.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _group-columns:

How do I group columns?
~~~~~~~~~~~~~~~~~~~~~~~
.. uses Column.group
.. uses EditColumn.group
.. uses TableAutoConfig.model

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__name__group='foo',
        columns__artist__group='bar',
        columns__year__group='bar',
    )

The grouping only works if the columns are next to each other, otherwise you'll get multiple groups. The groups are rendered by default as a second header row above the normal header row with colspans to group the headers.

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('06a197f8-5409-43a4-b1b5-92575a77295c', this)">▼ Hide result</div>
    <iframe id="06a197f8-5409-43a4-b1b5-92575a77295c" src="doc_includes/cookbook_tables/test_how_do_i_group_columns.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _group-rows:

How do I group rows?
~~~~~~~~~~~~~~~~~~~~
.. uses Column.row_group
.. uses EditColumn.row_group
.. uses TableAutoConfig.rows

Use `row_group`. By default this will output a `<th>` tag. You can configure it like any other fragment if you want to change that to a `<td>`. Note that the order of the columns in the table is used for grouping. This is why in the example below the `year` column is moved to index zero: we want to group on year first.

.. code-block:: python

    table = Table(
        auto__rows=Album.objects.order_by('year', 'artist', 'name'),
        columns__artist=dict(
            row_group__include=True,
            render_column=False,
        ),
        columns__year=dict(
            after=0,
            render_column=False,
            row_group=dict(
                include=True,
                template=Template('''
                <tr>
                    {{ row_group.iommi_open_tag }}
                        {{ value }} in our hearts
                    {{ row_group.iommi_close_tag }}
                </tr>
                '''),
            ),
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('8d9200b4-a529-41be-8beb-346fde15c53c', this)">▼ Hide result</div>
    <iframe id="8d9200b4-a529-41be-8beb-346fde15c53c" src="doc_includes/cookbook_tables/test_how_do_i_group_rows.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _rowspan:

How do I get rowspan on a table?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Column.auto_rowspan
.. uses EditColumn.auto_rowspan

You can manually set the rowspan attribute via `row__attrs__rowspan` but this is tricky to get right because you also have to hide the cells that are "overwritten" by the rowspan. We supply a simpler method: `auto_rowspan`. It automatically makes sure the rowspan count is correct and the cells are hidden. It works by checking if the value of the cell is the same, and then it becomes part of the rowspan.

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__year__auto_rowspan=True,
        columns__year__after=0,  # put the column first
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('6a6fc49c-f268-43a4-9329-ac88fde3a399', this)">▼ Hide result</div>
    <iframe id="6a6fc49c-f268-43a4-9329-ac88fde3a399" src="doc_includes/cookbook_tables/test_how_do_i_get_rowspan_on_a_table.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _bulk-edit:

How do I enable bulk editing?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Column.bulk
.. uses EditColumn.bulk

Editing multiple items at a time is easy in iommi with the built in bulk
editing. Enable it for a columns by passing `bulk__include=True`:

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__select__include=True,
        columns__year__bulk__include=True,
    )

The bulk namespace here is used to configure a `Field` for the GUI so you
can pass any parameter you can pass to `Field` there to customize the
behavior and look of the bulk editing for the column.

You also need to enable the select column, otherwise you can't select
the columns you want to bulk edit.

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('78202b15-f130-479c-8bb6-2b6018c57aaa', this)">▼ Hide result</div>
    <iframe id="78202b15-f130-479c-8bb6-2b6018c57aaa" src="doc_includes/cookbook_tables/test_how_do_i_enable_bulk_editing.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _bulk-delete:

How do I enable bulk delete?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.bulk
.. uses EditTable.bulk

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__select__include=True,
        bulk__actions__delete__include=True,
    )

To enable the bulk delete, enable the `delete` action.

You also need to enable the select column, otherwise you can't select
the columns you want to delete.

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('b723be5d-1f4a-4410-8516-cc4338930120', this)">▼ Hide result</div>
    <iframe id="b723be5d-1f4a-4410-8516-cc4338930120" src="doc_includes/cookbook_tables/test_how_do_i_enable_bulk_delete.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _custom-bulk-action:

How do I make a custom bulk action?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.bulk
.. uses EditTable.bulk

You need to first show the select column by passing
`columns__select__include=True`, then define a submit `Action` with a post
handler:

.. code-block:: python

    def my_action_post_handler(table, request, **_):
        queryset = table.bulk_queryset()
        queryset.update(name='Paranoid')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    t = Table(
        auto__model=Album,
        columns__select__include=True,
        bulk__actions__my_action=Action.submit(
            post_handler=my_action_post_handler,
        )
    )

.. _attr-name-diff:

What is the difference between `attr` and `_name`?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Column.attr
.. uses Column.name
.. uses EditColumn.attr
.. uses EditColumn.name
.. uses Column.cell
.. uses EditColumn.cell

`attr` is the attribute path of the value iommi reads from a row. In the simple case it's just the attribute name, but if you want to read the attribute of an attribute you can use `__`-separated paths for this: `attr='foo__bar'` is functionally equivalent to `cell__value=lambda row, **_: row.foo.bar`. Set `attr` to `None` to not read any attribute from the row.

`_name` is the name used internally. By default `attr` is set to the value of `_name`. This name is used when accessing the column from `Table.columns` and it's the name used in the GET parameter to sort by that column. This is a required field.

.. _reverse-fk-table:

How do I show a reverse foreign key relationship?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Column.include
.. uses EditColumn.include

By default reverse foreign key relationships are hidden. To turn it on, pass `include=True` to the column:

.. code-block:: python

    t = Table(
        auto__model=Artist,
        columns__albums__include=True,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('098f547a-8f9e-493a-9d55-e5e64ee25404', this)">▼ Hide result</div>
    <iframe id="098f547a-8f9e-493a-9d55-e5e64ee25404" src="doc_includes/cookbook_tables/test_table_with_foreign_key_reverse.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _reverse-m2m:

How do I show a reverse many-to-many relationship?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Column.include
.. uses EditColumn.include

By default reverse many-to-many relationships are hidden. To turn it on, pass `include=True` to the column:

.. code-block:: python

    t = Table(
        auto__model=Genre,
        columns__albums__include=True,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('18b246de-abe9-4108-9c72-b3f7389b544d', this)">▼ Hide result</div>
    <iframe id="18b246de-abe9-4108-9c72-b3f7389b544d" src="doc_includes/cookbook_tables/test_table_with_m2m_key_reverse.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _arbitrary-html:

How do I insert arbitrary html into a Table?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.container
.. uses Table.outer
.. uses EditTable.container
.. uses EditTable.outer

Sometimes you want to insert some extra html, css, or `Part` into a
`Table`. You can do this with the `container` or `outer` namespaces.

For `container`, by default items are added after the table but you
can put them above with `after=0`.

For `outer`, you can put content before the `h` tag even.

.. code-block:: python

    t = Table(
        auto__model=Genre,
        container__children__foo='Foo',
        container__children__bar=html.div('Bar', after=0),
        outer__children__bar=html.div('Baz', after=0),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('6f8833b1-8603-4cb9-a81e-9cc43e3d4d69', this)">▼ Hide result</div>
    <iframe id="6f8833b1-8603-4cb9-a81e-9cc43e3d4d69" src="doc_includes/cookbook_tables/test_insert_arbitrary_html.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _custom-actions:

How do I add custom actions/links to a table?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.actions
.. uses Cell.url
.. uses Column.link
.. uses EditTable.actions
.. uses EditCell.url
.. uses EditColumn.link

For the entire table:

.. code-block:: python

    t = Table(
        auto__model=Album,
        actions__link=Action(attrs__href='/'),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('00b737f7-6fa5-4f56-9034-65273674be6a', this)">▼ Hide result</div>
    <iframe id="00b737f7-6fa5-4f56-9034-65273674be6a" src="doc_includes/cookbook_tables/test_custom_actions.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Or as a column:

.. code-block:: python

    t = Table(
        auto__model=Album,
        columns__link=Column.link(attr=None, cell__url='/', cell__value='Link'),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('377f7982-9d7e-4668-91b2-31c8c0f48026', this)">▼ Hide result</div>
    <iframe id="377f7982-9d7e-4668-91b2-31c8c0f48026" src="doc_includes/cookbook_tables/test_custom_actions1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _additional-rows:

How do I render additional rows?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.rows
.. uses EditTable.rows
.. uses RowConfig.template

Using `rows__template` you can render the default row with `{{ cells.render }}` and then your own custom data:

.. code-block:: python

    t = Table(
        auto__model=Album,
        row__template=Template('''
            {{ cells.render }}
            <tr>
                <td style="text-align: center" colspan="{{ cells|length }}">🤘🤘</td>
            </tr>
        '''),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('1f746644-94cf-4e95-b60d-41c6c702c2c6', this)">▼ Hide result</div>
    <iframe id="1f746644-94cf-4e95-b60d-41c6c702c2c6" src="doc_includes/cookbook_tables/test_render_additional_rows.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _initial-filter:

How do I set an initial filter to a table?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.query
.. uses EditTable.query
.. uses Query.form

The `Query` of a `Table` has a `Form` where you can set the initial value:

.. code-block:: python

    t = Table(
        auto__model=Album,
        columns__artist__filter__include=True,
        query__form__fields__artist__initial=lambda **_: Artist.objects.get(name='Dio'),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('561ffcd6-24d3-4ae1-a92e-3f3bd717e5db', this)">▼ Hide result</div>
    <iframe id="561ffcd6-24d3-4ae1-a92e-3f3bd717e5db" src="doc_includes/cookbook_tables/test_initial_filter_on_table.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _row-numbers:

How do I show row numbers?
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Cells.row_index
.. uses Cell.value
.. uses EditCells.row_index
.. uses EditCell.value
.. uses Column.cell
.. uses EditColumn.cell

Use `cells.row_index` to get the index of the row in the current rendering.

.. code-block:: python

    t = Table(
        auto__model=Album,
        columns__index=Column(
            after=0,
            cell__value=lambda row, cells, **_: cells.row_index
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('ca732ce7-c80f-4516-8e0f-33fb0dec7e04', this)">▼ Hide result</div>
    <iframe id="ca732ce7-c80f-4516-8e0f-33fb0dec7e04" src="doc_includes/cookbook_tables/test_indexed_rows.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _nested-fk:

How do I show nested foreign key relationships?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.auto
.. uses EditTable.auto
.. uses Column.cell
.. uses EditColumn.cell
.. uses TableAutoConfig.include

Say you have a list of tracks and you want to show the album and then from that album, you also want to show the artist:

.. code-block:: python

    t = Table(
        auto__model=Track,
        auto__include=[
            'name',
            'album',
            'album__artist',  # <--
        ]
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('4be35be1-53f1-43bc-8893-9bdf7e063ad9', this)">▼ Hide result</div>
    <iframe id="4be35be1-53f1-43bc-8893-9bdf7e063ad9" src="doc_includes/cookbook_tables/test_nested_foreign_keys.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

The column created is named `album_artist` (as `__` is reserved for traversing a namespace), so that's the name you need to reference is you need to add more configuration to that column:

.. code-block:: python

    t = Table(
        auto__model=Track,
        auto__include=[
            'name',
            'album',
            'album__artist',
        ],
        columns__album_artist__cell__attrs__style__background='blue',
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('e7a5caee-e5e3-423d-858e-c94d6e775ecb', this)">▼ Hide result</div>
    <iframe id="e7a5caee-e5e3-423d-858e-c94d6e775ecb" src="doc_includes/cookbook_tables/test_nested_foreign_keys1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _stop-header-render:

How do I stop rendering the header?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.header
.. uses EditTable.header
.. uses HeaderConfig.include

Use `header__template=None` to not render the header, or
`header__include=False` to remove the processing of the header totally. The
difference being that you might want the header object to access
programmatically for some reason, so then it's appropriate to use the
`template=None` method.

.. code-block:: python

    t = Table(
        auto__model=Album,
        header__include=False,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('2a8d362c-ceb8-45b0-9c3b-4ab1da0d18b4', this)">▼ Hide result</div>
    <iframe id="2a8d362c-ceb8-45b0-9c3b-4ab1da0d18b4" src="doc_includes/cookbook_tables/test_dont_render_header.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. code-block:: python

    t = Table(
        auto__model=Album,
        header__template=None,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('2162b3cb-5d2e-4197-9ffa-f6f462376ebb', this)">▼ Hide result</div>
    <iframe id="2162b3cb-5d2e-4197-9ffa-f6f462376ebb" src="doc_includes/cookbook_tables/test_dont_render_header1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _table-as-div:

How do I render a Table as divs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.tag
.. uses Table.tbody
.. uses Table.cell
.. uses CellConfig.tag
.. uses RowConfig.tag
.. uses Table.header
.. uses Header.template

You can render a `Table` as a div with the shortcut `Table.div`:

.. code-block:: python

    table = Table.div(
        auto__model=Album,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('c334f01c-71e4-4a2f-8bd0-140ce23d6ac1', this)">▼ Hide result</div>
    <iframe id="c334f01c-71e4-4a2f-8bd0-140ce23d6ac1" src="doc_includes/cookbook_tables/test_render_table_as_div.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

This shortcut changes the rendering of the entire table from `<table>` to `<div>` by specifying the `tag` configuration, changes the `<tbody>` to a `<div>` via `tbody__tag`, the row via `row__tag` and removes the header with `header__template=None`.

.. table-preprocess_rows:

How do I do custom processing on rows before rendering?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.preprocess_row
.. uses Table.preprocess_rows
.. uses EditTable.preprocess_row
.. uses EditTable.preprocess_rows

Sometimes it's useful to further process the rows before rendering, by fetching more data, doing calculations, etc. If you can use `QuerySet.annotate()`, that's great, but sometimes that's not enough. This is where `preprocess_row` and `preprocess_rows` come in. The first is called on each row, and the second is called for the entire list as a whole.

Note that this is all done *after* pagination.

Modifying row by row:

.. code-block:: python

    def preprocess_album(row, **_):
        row.year += 1000
        return row

    table = Table(
        auto__model=Album,
        preprocess_row=preprocess_album,
    )

Note that `preprocess_row` requires that you return the object. This is because you can return a different object if you'd like.

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('7ebd1a69-53a1-4d84-ade1-4de6a1bee666', this)">▼ Hide result</div>
    <iframe id="7ebd1a69-53a1-4d84-ade1-4de6a1bee666" src="doc_includes/cookbook_tables/test_how_do_i_do_custom_processing_on_rows.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Modifying the entire list:

.. code-block:: python

    def preprocess_albums(rows, **_):
        for i, row in enumerate(rows):
            row.index = i
        return rows

    table = Table(
        auto__model=Album,
        preprocess_rows=preprocess_albums,
        columns__index=Column.number(),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('4896d1e5-44b5-4505-894a-7b69f36da725', this)">▼ Hide result</div>
    <iframe id="4896d1e5-44b5-4505-894a-7b69f36da725" src="doc_includes/cookbook_tables/test_how_do_i_do_custom_processing_on_rows1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Note that `preprocess_rows` requires that you return the list. That is because you can also return a totally new list if you'd like.

.. table-empty-message:

How do I set an empty message?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Table.empty_message
.. uses EditTable.empty_message

By default iommi will render an empty table simply as empty:

.. code-block:: python

    table = Table(
        auto__model=Album,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('cb33cd78-5f7b-4e04-b499-7035b4740d9f', this)">▼ Hide result</div>
    <iframe id="cb33cd78-5f7b-4e04-b499-7035b4740d9f" src="doc_includes/cookbook_tables/test_how_do_i_set_an_empty_message.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

If you want to instead display an explicit message when the table is empty, you use `empty_message`:

.. code-block:: python

    table = Table(
        auto__model=Album,
        empty_message='Destruction of the empty spaces is my one and only crime',
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('ecca310f-4ef6-4b05-9d44-bc9b97888579', this)">▼ Hide result</div>
    <iframe id="ecca310f-4ef6-4b05-9d44-bc9b97888579" src="doc_includes/cookbook_tables/test_how_do_i_set_an_empty_message1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

This setting is probably something you want to set up in your `Style`, and not per table.

