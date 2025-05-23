

EditTable
=========

Base class: :doc:`Table`

Describe an editable table. Example:

.. code-block:: python

    table = EditTable(
        auto__model=Album,
        columns__name__field__include=True,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('b8e1f497-b7a5-40b1-a579-2aa232e23490', this)">▼ Hide result</div>
    <iframe id="b8e1f497-b7a5-40b1-a579-2aa232e23490" src="doc_includes/EditTable/test_base.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Refinable members
-----------------


`action_class`
^^^^^^^^^^^^^^

Type: `Type[iommi.action.Action]`


`actions`
^^^^^^^^^

Type: `Dict[str, iommi.action.Action]`


Cookbook:
    :ref:`custom-actions`


`actions_below`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `bool`

Default: `False`

`actions_template`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Union[str, iommi._web_compat.Template]`

Default: `iommi/form/actions.html`

`after`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Union[int, str]`

    See :ref:`after <after>`


`assets`
^^^^^^^^

Type: `Namespace`

    See :ref:`assets <assets>`


`attrs`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

dict of strings to string/callable of HTML attributes to apply to the table

Type: :doc:`Attrs`

    See :ref:`attributes <attributes>`


`auto`
^^^^^^

Type: :doc:`TableAutoConfig`

    See :ref:`auto <auto>`


Cookbook:
    :ref:`fk-related-data-access`

    :ref:`nested-fk`


`bulk`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Optional[iommi.form.Form]`


Cookbook:
    :ref:`bulk-delete`

    :ref:`custom-bulk-action`


`bulk_container`
^^^^^^^^^^^^^^^^

Type: :doc:`Fragment`


`bulk_exclude`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

exclude filters to apply to the `QuerySet` before performing the bulk operation

Type: `Namespace`

Default: `{}`

`bulk_filter`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

filters to apply to the `QuerySet` before performing the bulk operation

Type: `Namespace`

Default: `{}`

`cell`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `CellConfig`


`cells_class`
^^^^^^^^^^^^^

Type: `Type[iommi.table.Cells]`


`columns`
^^^^^^^^^

(use this only when not using the declarative style) a list of Column objects

Type: `Dict[str, iommi.table.Column]`


`container`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: :doc:`Fragment`


Cookbook:
    :ref:`arbitrary-html`


`create_form`
^^^^^^^^^^^^^

Type: :doc:`Form`


`default_sort_order`
^^^^^^^^^^^^^^^^^^^^


`edit_actions`
^^^^^^^^^^^^^^

Type: `Dict[str, iommi.action.Action]`


`edit_form`
^^^^^^^^^^^

Type: :doc:`Form`


`empty_message`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `str`


Cookbook:
    :ref:`table-as-div`


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


`form_class`
^^^^^^^^^^^^

Type: `Type[iommi.form.Form]`


`h_tag`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Union[iommi.fragment.Fragment, str]`

    See :ref:`title <title>`


`header`
^^^^^^^^

Default: `Namespace()`

Cookbook:
    :ref:`turn-off-header`

    :ref:`stop-header-render`


`include`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `bool`

    See :ref:`include <include>`


`invalid_form_message`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `str`


`iommi_style`
^^^^^^^^^^^^^

Type: `str`

    See :ref:`iommi_style <iommi_style>`


`member_class`
^^^^^^^^^^^^^^

Type: `Type[iommi.table.Column]`


`model`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Type[django.db.models.base.Model]`


`outer`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: :doc:`Fragment`


Cookbook:
    :ref:`arbitrary-html`


`page_class`
^^^^^^^^^^^^

Type: `Type[iommi.page.Page]`


`page_size`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `int`

Default: `16`

Cookbook:
    :ref:`turn-off-pagination`


`parent_form`
^^^^^^^^^^^^^

Type: `Optional[iommi.form.Form]`


`parts`
^^^^^^^

Type: `Namespace`


`post_bulk_edit`
^^^^^^^^^^^^^^^^


`preprocess_row`
^^^^^^^^^^^^^^^^


Cookbook:
    :ref:`table-as-div`


`preprocess_row_for_create`
^^^^^^^^^^^^^^^^^^^^^^^^^^^


`preprocess_rows`
^^^^^^^^^^^^^^^^^


Cookbook:
    :ref:`table-as-div`


`query`
^^^^^^^


Cookbook:
    :ref:`initial-filter`


`query_class`
^^^^^^^^^^^^^

Type: `Type[iommi.query.Query]`


`query_from_indexes`
^^^^^^^^^^^^^^^^^^^^

Type: `bool`


`row`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `RowConfig`


Cookbook:
    :ref:`customize-rendering-row`


`row_group_class`
^^^^^^^^^^^^^^^^^

Type: `Type[iommi.table.RowGroup]`


`rows`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a list or QuerySet of objects


Cookbook:
    :ref:`additional-rows`


`sortable`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

set this to `False` to turn off sorting for all columns

Type: `bool`

Default: `True`

Cookbook:
    :ref:`table-sorting`


`sorter`
^^^^^^^^


`superheader`
^^^^^^^^^^^^^

Type: `Namespace`


`table_tag_wrapper`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: :doc:`Fragment`


`tag`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `str`

Default: `table`
    See :ref:`tag <tag>`


`tbody`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: :doc:`Fragment`


`template`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Union[str, iommi._web_compat.Template]`

Default: `iommi/table/table.html`
    See :ref:`template <template>`


`title`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `str`

    See :ref:`title <title>`


Shortcuts
---------

`EditTable.div`
^^^^^^^^^^^^^^^

Defaults
++++++++

* `tag`
    * `div`
* `tbody__tag`
    * `div`
* `cell__tag`
    * `None`
* `row__tag`
    * `div`
* `header__template`
    * `None`

Methods
-------

`cells_for_rows_for_create`
^^^^^^^^^^^^^^^^^^^^^^^^^^^


Yield a Cells instance for each create row sent from the client.


`get_errors`
^^^^^^^^^^^^

`is_valid`
^^^^^^^^^^

`on_bind`
^^^^^^^^^

`on_refine_done`
^^^^^^^^^^^^^^^^

`should_render_form_tag`
^^^^^^^^^^^^^^^^^^^^^^^^

