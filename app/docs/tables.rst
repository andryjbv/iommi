

.. _tables:

Tables
======

iommi tables makes it easy to create full featured HTML tables easily:

* generates header, rows and cells
* sorting
* filtering
* pagination
* bulk edit
* link creation
* customization on multiple levels, all the way down to templates for cells
* automatic rowspan
* grouping of headers

A simple example:

.. code-block:: python

    Table(
        auto__model=Album,
        page_size=10,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('4663af30-4513-4fda-a7c0-bd0283c33bfd', this)">▼ Hide result</div>
    <iframe id="4663af30-4513-4fda-a7c0-bd0283c33bfd" src="doc_includes/tables/test_tables.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Read the full documentation and the :doc:`cookbook` for more.

Creating tables from models
---------------------------

Say I have some model:

.. code-block:: python

    class Foo(models.Model):
        a = models.IntegerField()

        def __str__(self):
            return f'Foo: {self.a}'

.. code-block:: python

    class Bar(models.Model):
        b = models.ForeignKey(Foo, on_delete=models.CASCADE)
        c = models.CharField(max_length=255)

Now I can display a list of `Bar` in a table like this:

.. code-block:: python

    def my_view(request):
        return Table(auto__model=Bar)

This automatically creates a table with pagination and sorting. If you pass
`query_from_indexes=True` you will get filters for all the model fields
that have database indexes. This filtering system includes an advanced filter
language. See :doc:`queries` for more on filtering.

Explicit tables
---------------

You can also create tables explicitly:

.. code-block:: python

    class AlbumTable(Table):
        # Shortcut for creating checkboxes to select rows
        select = Column.select()

        name = Column()

        # Show the name field from Artist. This works for plain old objects too.
        artist_name = Column(
            attr='artist__name',

            # put this field into the query language
            filter__include=True,
        )
        year = Column.number(
            # Enable bulk editing for this field
            bulk__include=True,
        )

        class Meta:
            rows = Album.objects.all()
            title = 'Albums'

    albums = AlbumTable().as_view()

This gives me a view with filtering, sorting, bulk edit and pagination.

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('6c6cea37-3fca-4f59-a1e5-611d3fa7cb2a', this)">▼ Hide result</div>
    <iframe id="6c6cea37-3fca-4f59-a1e5-611d3fa7cb2a" src="doc_includes/tables/test_explicit_tables.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Table as CSV
------------

Tables are able to render as CSV files. This is enabled if there is specified a name to use on the resulting file,
as a value of the table parameter `extra_evaluated__report_name`, and a file header name for each column that is
to be included, specified by the column parameter `extra_evaluated__report_name`.

For example:

.. code-block:: python

    class AlbumTable(Table):
        class Meta:
            extra_evaluated__report_name = 'Albums'
            actions__download = Action(
                attrs__href=lambda table, **_: '?' + table.endpoints.csv.endpoint_path,
            )
            rows = Album.objects.all()

        name = Column(extra_evaluated__report_name='Name')
        artist = Column(extra_evaluated__report_name='Artist')
        year = Column.number(extra_evaluated__report_name='Artist')

    albums = AlbumTable().as_view()

This will behave like an ordinary table but when the csv rendering endpoint is invoked the content will be
returned as a text file in CSV format.

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('6c16e45f-fcb0-49ba-8096-b517d4bdbc83', this)">▼ Hide result</div>
    <iframe id="6c16e45f-fcb0-49ba-8096-b517d4bdbc83" src="doc_includes/tables/test_table_csv.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

You can also pass kwargs to the `csv.writer` such as `delimiter`, `quotechar`, etc. 
with `extra_evaluated__csv_writer_kwargs = {'delimiter': ';', ...}`.

Table of plain python objects
-----------------------------

.. code-block:: python

    # Say I have a class...
    class Foo(object):
        def __init__(self, i):
            self.a = i
            self.b = 'foo %s' % (i % 3)
            self.c = (i, 1, 2, 3, 4)

    # I can declare a table:
    class FooTable(Table):
        a = Column.number()

        b = Column()

        # Display the last value of the tuple
        c = Column(
            cell__format=lambda value, **_: value[-1],
        )

        # Calculate a value not present in Foo
        sum_c = Column(
            cell__value=lambda row, **_: sum(row.c),
            sortable=False,
        )

    def plain_objs_view(request):
        # and now create a list of items
        foos = [Foo(i) for i in range(4)]

        # now to get an HTML table:
        return FooTable(rows=foos)

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('26fdb47d-c678-4ed5-ab8f-fd8bdb13aec9', this)">▼ Hide result</div>
    <iframe id="26fdb47d-c678-4ed5-ab8f-fd8bdb13aec9" src="doc_includes/tables/test_table_of_plain_python_objects.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

All these examples and a bigger example using many more features can be found in the examples project.

