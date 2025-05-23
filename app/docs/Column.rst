

Column
======

Base class: :doc:`Part`

Class that describes a column, i.e. the text of the header, how to get and display the data in the cell, etc.

See :doc:`Table` for more complete examples.

Parameters with the prefix `filter__` will be passed along downstream to the `Filter` instance if applicable. This can be used to tweak the filtering of a column.

Refinable members
-----------------


`after`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the order of columns, see the `howto on ordering <https://docs.iommi.rocks//cookbook_tables.html#how-do-i-reorder-columns>`_ for an example.

Type: `Union[int, str]`

    See :ref:`after <after>`


Cookbook:
    :ref:`reorder-columns`


`assets`
^^^^^^^^

Type: `Namespace`

    See :ref:`assets <assets>`


`attr`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

What attribute to use, defaults to same as name. Follows django conventions to access properties of properties, so `foo__bar` is equivalent to the python code `foo.bar`. This parameter is based on the filter name of the Column if you use the declarative style of creating tables.

Type: `str`

    See :ref:`attr <attr>`


Cookbook:
    :ref:`fk-related-data-access`

    :ref:`attr-name-diff`


`auto_rowspan`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

enable automatic rowspan for this column. To join two cells with rowspan, just set this `auto_rowspan` to `True` and make those two cells output the same text and we'll handle the rest.

Type: `bool`

Default: `False`

Cookbook:
    :ref:`rowspan`


`bulk`
^^^^^^

Namespace to configure bulk actions. See `howto on bulk editing <https://docs.iommi.rocks//cookbook_tables.html#how-do-i-enable-bulk-editing>`_ for an example and more information.

Type: `Namespace`


Cookbook:
    :ref:`bulk-edit`


`cell`
^^^^^^

Customize the cell, see See `howto on rendering <https://docs.iommi.rocks//cookbook_tables.html#how-do-i-customize-the-rendering-of-a-cell>`_ and `howto on links <https://docs.iommi.rocks//cookbook_tables.html#how-do-i-make-a-link-in-a-cell>`_

Type: `Namespace`


Cookbook:
    :ref:`customize-table-cell-render`

    :ref:`cell-link`

    :ref:`row-numbers`

    :ref:`attr-name-diff`

    :ref:`column-computed-data`

    :ref:`nested-fk`


`choices`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Iterable`


`data_retrieval_method`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default: `DataRetrievalMethods.attribute_access`

`display_name`
^^^^^^^^^^^^^^

the text of the header for this column. By default this is based on the `_name` so normally you won't need to specify it.

    See :ref:`name <name>`


Cookbook:
    :ref:`header-title`


`endpoints`
^^^^^^^^^^^

Type: `Namespace`

    See :ref:`endpoints <endpoints>`


`extra`
^^^^^^^

Type: `Dict[str, Any]`

    See :ref:`extra <extra>`


`extra_evaluated`
^^^^^^^^^^^^^^^^^

Type: `Dict[str, Any]`

    See :ref:`extra <extra>`


`extra_params`
^^^^^^^^^^^^^^

    See :ref:`extra_params <extra_params>`


`filter`
^^^^^^^^

Type: `Namespace`


Cookbook:
    :ref:`freetext-column`

    :ref:`filter-column`


`group`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

string describing the group of the header. If this parameter is used the header of the table now has two rows. Consecutive identical groups on the first level of the header are joined in a nice way.

Type: `Optional[str]`


Cookbook:
    :ref:`group-columns`


`header`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Namespace`


Cookbook:
    :ref:`customize-header`


`include`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

set this to `False` to hide the column

Type: `bool`

    See :ref:`include <include>`


Cookbook:
    :ref:`reverse-m2m`

    :ref:`show-columns`

    :ref:`reverse-fk-table`


`iommi_style`
^^^^^^^^^^^^^

Type: `str`

    See :ref:`iommi_style <iommi_style>`


`model`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Type[django.db.models.base.Model]`


`model_field`
^^^^^^^^^^^^^


`model_field_name`
^^^^^^^^^^^^^^^^^^


`render_column`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If set to `False` the column won't be rendered in the table, but still be available in `table.columns`. This can be useful if you want some other feature from a column like filtering.

Type: `bool`

Default: `True`

Cookbook:
    :ref:`show-columns`


`row_group`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Namespace`


Cookbook:
    :ref:`group-rows`


`sort_default_desc`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set to `True` to make table sort link to sort descending first.

Type: `bool`

Default: `False`

Cookbook:
    :ref:`sort-direction`


`sort_key`
^^^^^^^^^^

string denoting what value to use as sort key when this column is selected for sorting. (Or callable when rendering a table from list.)


`sortable`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

set this to `False` to disable sorting on this column

Type: `bool`

Default: `lambda column, **_: column.attr is not None`

Cookbook:
    :ref:`table-sorting`


`superheader`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Shortcuts
---------

`Column.boolean`
^^^^^^^^^^^^^^^^

Shortcut to render booleans as a check mark if true or blank if false.

.. code-block:: python

    table = Table(
        columns__name=Column(),
        columns__boolean=Column.boolean(),
        rows=[
            Struct(name='true!', boolean=True),
            Struct(name='false!', boolean=False),
        ]
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('d158294e-ab6c-4fc1-9cca-348eea5e3ec7', this)">▼ Hide result</div>
    <iframe id="d158294e-ab6c-4fc1-9cca-348eea5e3ec7" src="doc_includes/Column/test_base.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Defaults
++++++++

* `filter__call_target__attribute`
    * `boolean`
* `filter__field__call_target__attribute`
    * `boolean_tristate`
* `bulk__call_target__attribute`
    * `boolean`
* `cell__format`
    * `lambda value, **_: mark_safe(f'<span title="{gettext_lazy("Yes")}">&#10004;</span>') if value else ''`

`Column.boolean_tristate`
^^^^^^^^^^^^^^^^^^^^^^^^^

This shortcut sets up `boolean_tristate` for the filter.



Parent: Column.boolean_

Defaults
++++++++

* `filter__call_target__attribute`
    * `boolean_tristate`

`Column.choice`
^^^^^^^^^^^^^^^

This shortcut sets up `choices` for the filter and bulk form.



Defaults
++++++++

* `bulk__call_target__attribute`
    * `choice`
* `bulk__choices`
    * `iommi.table.get_choices_from_column`
* `filter__call_target__attribute`
    * `choice`
* `filter__choices`
    * `iommi.table.get_choices_from_column`

`Column.choice_queryset`
^^^^^^^^^^^^^^^^^^^^^^^^

This shortcut sets up `choices` for the filter and bulk form for the choice queryset case.



Parent: Column.choice_

Defaults
++++++++

* `bulk__call_target__attribute`
    * `choice_queryset`
* `filter__call_target__attribute`
    * `choice_queryset`

`Column.date`
^^^^^^^^^^^^^

Defaults
++++++++

* `filter__call_target__attribute`
    * `date`
* `filter__query_operator_to_q_operator`
    * `lambda op: {'=': 'exact', ':': 'contains'}.get(op)`
* `bulk__call_target__attribute`
    * `date`

`Column.datetime`
^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `filter__call_target__attribute`
    * `datetime`
* `filter__query_operator_to_q_operator`
    * `lambda op: {'=': 'exact', ':': 'contains'}.get(op)`
* `bulk__call_target__attribute`
    * `datetime`

`Column.decimal`
^^^^^^^^^^^^^^^^

Defaults
++++++++

* `bulk__call_target__attribute`
    * `decimal`
* `filter__call_target__attribute`
    * `decimal`

`Column.delete`
^^^^^^^^^^^^^^^

Shortcut for creating a clickable delete icon. The URL defaults to `your_object.get_absolute_url() + 'delete/'`. Specify the option cell__url to override.

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__delete=Column.delete(),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('2cb6e5e2-d559-42d3-a187-2d9e24c34157', this)">▼ Hide result</div>
    <iframe id="2cb6e5e2-d559-42d3-a187-2d9e24c34157" src="doc_includes/Column/test_base1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Parent: Column.icon_

Defaults
++++++++

* `cell__url`
    * `lambda row, **_: row.get_absolute_url() + 'delete/'`
* `display_name`
    * `Delete`

`Column.download`
^^^^^^^^^^^^^^^^^

Shortcut for creating a clickable download icon. The URL defaults to `your_object.get_absolute_url() + 'download/'`. Specify the option cell__url to override.

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__download=Column.download(),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('84a001af-78fa-4fb5-ab91-e5789a3f0f1e', this)">▼ Hide result</div>
    <iframe id="84a001af-78fa-4fb5-ab91-e5789a3f0f1e" src="doc_includes/Column/test_base2.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Parent: Column.icon_

Defaults
++++++++

* `cell__url`
    * `lambda row, **_: row.get_absolute_url() + 'download/'`
* `cell__value`
    * `lambda row, **_: getattr(row, 'pk', False)`
* `display_name`
    * `Download`

`Column.duration`
^^^^^^^^^^^^^^^^^

Parent: Column.text_

Defaults
++++++++

* `bulk__call_target__attribute`
    * `duration`
* `filter__call_target__attribute`
    * `duration`

`Column.edit`
^^^^^^^^^^^^^

Shortcut for creating a clickable edit icon. The URL defaults to `your_object.get_absolute_url() + 'edit/'`. Specify the option cell__url to override.

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__edit=Column.edit(after=0),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('9532d9ef-3c82-475b-bd1e-048251009bed', this)">▼ Hide result</div>
    <iframe id="9532d9ef-3c82-475b-bd1e-048251009bed" src="doc_includes/Column/test_base3.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Parent: Column.icon_

Defaults
++++++++

* `cell__url`
    * `lambda row, **_: row.get_absolute_url() + 'edit/'`
* `display_name`
    * `Edit`

`Column.email`
^^^^^^^^^^^^^^

Defaults
++++++++

* `filter__call_target__attribute`
    * `email`
* `bulk__call_target__attribute`
    * `email`

`Column.file`
^^^^^^^^^^^^^

Defaults
++++++++

* `bulk__call_target__attribute`
    * `file`
* `filter__call_target__attribute`
    * `file`
* `cell__format`
    * `lambda value, **_: str(value)`

`Column.float`
^^^^^^^^^^^^^^

Parent: Column.number_

Defaults
++++++++

* `filter__call_target__attribute`
    * `float`
* `bulk__call_target__attribute`
    * `float`

`Column.foreign_key`
^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `bulk__call_target__attribute`
    * `foreign_key`
* `filter__call_target__attribute`
    * `foreign_key`
* `data_retrieval_method`
    * `DataRetrievalMethods.select`
* `sort_key`
    * `iommi.table.foreign_key__sort_key`

`Column.foreign_key_reverse`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `bulk__call_target__attribute`
    * `foreign_key_reverse`
* `filter__call_target__attribute`
    * `foreign_key_reverse`
* `cell__format`
    * `lambda value, **_: ', '.join(['%s' % x for x in value.all()])`
* `data_retrieval_method`
    * `DataRetrievalMethods.prefetch`
* `sortable`
    * `False`
* `extra__django_related_field`
    * `True`
* `display_name`
    * `lambda column, **_: capitalize(column.model_field.remote_field.model._meta.verbose_name_plural)`

`Column.icon`
^^^^^^^^^^^^^

Shortcut to create font awesome-style icons.



Parameters
++++++++++

* `extra__icon`
    * `the name of the icon`

Defaults
++++++++

* `display_name`
    * `""`
* `cell__value`
    * `lambda table, **_: True`
* `cell__format`
    * `iommi.table.default_icon__cell__format`
* `attr`
    * `None`

`Column.integer`
^^^^^^^^^^^^^^^^

Parent: Column.number_

Defaults
++++++++

* `filter__call_target__attribute`
    * `integer`
* `bulk__call_target__attribute`
    * `integer`

`Column.link`
^^^^^^^^^^^^^

Shortcut for creating a cell that is a link. The URL is the result of calling `get_absolute_url()` on the object.




Cookbook:
    :ref:`custom-actions`

`Column.many_to_many`
^^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `bulk__call_target__attribute`
    * `many_to_many`
* `filter__call_target__attribute`
    * `many_to_many`
* `cell__format`
    * `lambda value, **_: ', '.join(['%s' % x for x in value.all()])`
* `data_retrieval_method`
    * `DataRetrievalMethods.prefetch`
* `sortable`
    * `False`
* `extra__django_related_field`
    * `True`

`Column.many_to_many_reverse`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `bulk__call_target__attribute`
    * `many_to_many_reverse`
* `filter__call_target__attribute`
    * `many_to_many_reverse`
* `display_name`
    * `lambda column, **_: capitalize(column.model_field.remote_field.model._meta.verbose_name_plural)`

`Column.multi_choice`
^^^^^^^^^^^^^^^^^^^^^

This shortcut sets up `choices` for the filter and bulk form for the multi choice case.



Parent: Column.choice_

Defaults
++++++++

* `bulk__call_target__attribute`
    * `multi_choice`
* `filter__call_target__attribute`
    * `multi_choice`

`Column.multi_choice_queryset`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This shortcut sets up `choices` for the filter and bulk form for the multi choice queryset case.



Parent: Column.choice_queryset_

Defaults
++++++++

* `bulk__call_target__attribute`
    * `multi_choice_queryset`
* `filter__call_target__attribute`
    * `multi_choice_queryset`

`Column.number`
^^^^^^^^^^^^^^^

`Column.run`
^^^^^^^^^^^^

Shortcut for creating a clickable run icon. The URL defaults to `your_object.get_absolute_url() + 'run/'`. Specify the option cell__url to override.

.. code-block:: python

    table = Table(
        auto__model=Album,
        columns__run=Column.run(),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('f0de66e1-38b2-40b0-84e8-2bf504646207', this)">▼ Hide result</div>
    <iframe id="f0de66e1-38b2-40b0-84e8-2bf504646207" src="doc_includes/Column/test_base4.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Parent: Column.icon_

Defaults
++++++++

* `cell__url`
    * `lambda row, **_: row.get_absolute_url() + 'run/'`
* `display_name`
    * `Run`

`Column.select`
^^^^^^^^^^^^^^^

Shortcut for a column of checkboxes to select rows. This is useful for implementing bulk operations.

By default tables have a column named `select` that is hidden that is used for this purpose, so you only
need to turn it on to get it. See the example below.

To implement a custom post handler that operates on the selected rows, do

.. code-block:: python

    def my_handler(table):
        rows = table.selection()
        # rows will either be a queryset, or a list of elements
        # matching the type of rows of the table
        ...

    table = Table(
        auto__model=Album,
        columns__select__include=True,
        bulk__actions__submit=Action.submit(post_handler=my_handler)
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('a1e48199-ca5c-4929-9ccf-fa8451f07f50', this)">▼ Hide result</div>
    <iframe id="a1e48199-ca5c-4929-9ccf-fa8451f07f50" src="doc_includes/Column/test_base5.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Parameters
++++++++++

* `extra__checkbox_name`
    * `the name of the checkbox. Default is `"pk"`, resulting in checkboxes like `"pk_1234"`.`
* `extra__checked`
    * `callable to specify if the checkbox should be checked initially. Defaults to `False`.`

Defaults
++++++++

* `header__template`
    * `iommi/table/select_column_header.html`
* `sortable`
    * `False`
* `filter__is_valid_filter`
    * `lambda **_: (True, '')`
* `filter__field__include`
    * `False`
* `attr`
    * `None`
* `cell__value`
    * `lambda table, cells, row, **_: (       row.pk       if isinstance(table.rows, QuerySet)       # row_index is the visible row number       # See selection() for the code that does the lookup       else cells.row_index     )`
* `cell__format`
    * `lambda column, row, value, **kwargs: format_html(       # language=HTML       '<input type="checkbox" class="checkbox" name="{checkbox_name}_{row_id}" {checked_str} />',       checkbox_name=column.extra.checkbox_name,       row_id=value,       checked_str=(         'checked'         if evaluate_strict(column.extra.checked, column=column, row=row, value=value, **kwargs)         else ''       ),     )`
* `extra__checkbox_name`
    * `pk`
* `extra__checked`
    * `lambda **_: False`
* `extra__icon`
    * `fa fa-check-square-o`

`Column.substring`
^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `filter__query_operator_for_field`
    * `:`

`Column.text`
^^^^^^^^^^^^^

This is an explicit synonym for `Column()`.



Defaults
++++++++

* `bulk__call_target__attribute`
    * `text`
* `filter__call_target__attribute`
    * `text`

`Column.textarea`
^^^^^^^^^^^^^^^^^

Parent: Column.text_

`Column.time`
^^^^^^^^^^^^^

Defaults
++++++++

* `filter__call_target__attribute`
    * `time`
* `filter__query_operator_to_q_operator`
    * `lambda op: {'=': 'exact', ':': 'contains'}.get(op)`
* `bulk__call_target__attribute`
    * `time`

Methods
-------

`on_bind`
^^^^^^^^^

`on_refine_done`
^^^^^^^^^^^^^^^^

`own_evaluate_parameters`
^^^^^^^^^^^^^^^^^^^^^^^^^

Class methods
-------------

`checkboxes`
^^^^^^^^^^^^

`from_model`
^^^^^^^^^^^^

