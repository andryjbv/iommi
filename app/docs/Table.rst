

Table
=====

Base class: :doc:`Part`

Describe a table. Example:

.. code-block:: python

    class AlbumTable(Table):
        name = Column()
        artist = Column()

        class Meta:
            sortable = False

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('ea32e51f-5684-4a35-aa1b-3dd563c3d863', this)">▼ Hide result</div>
    <iframe id="ea32e51f-5684-4a35-aa1b-3dd563c3d863" src="doc_includes/Table/test_base.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

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


Cookbook:
    :ref:`freetext-column`


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


Cookbook:
    :ref:`table-as-div`


`cells_class`
^^^^^^^^^^^^^

Type: `Type[iommi.table.Cells]`


`columns`
^^^^^^^^^

(use this only when not using the declarative style) a list of Column objects

Type: `Dict[str, iommi.table.Column]`


Cookbook:
    :ref:`cell-link`

    :ref:`column-computed-data`

    :ref:`reorder-columns`


`container`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: :doc:`Fragment`


Cookbook:
    :ref:`arbitrary-html`


`default_sort_order`
^^^^^^^^^^^^^^^^^^^^


Cookbook:
    :ref:`default-sort-order`


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

    :ref:`table-as-div`


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


`parts`
^^^^^^^

Type: `Namespace`


`post_bulk_edit`
^^^^^^^^^^^^^^^^


`preprocess_row`
^^^^^^^^^^^^^^^^


Cookbook:
    :ref:`table-as-div`


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


Cookbook:
    :ref:`table-as-div`


`tbody`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: :doc:`Fragment`


Cookbook:
    :ref:`table-as-div`


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

`Table.div`
^^^^^^^^^^^

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

`as_view`
^^^^^^^^^

`bulk_queryset`
^^^^^^^^^^^^^^^


Return the queryset that contains only the selected rows with
        bulk_filter and bulk_exclude applied.

        For use in post_handlers. Only valid when rows was a queryset.



`cells_for_rows`
^^^^^^^^^^^^^^^^


Yield a Cells instance for each visible row on the screen.


`get_visible_rows`
^^^^^^^^^^^^^^^^^^

`on_bind`
^^^^^^^^^

`on_refine_done`
^^^^^^^^^^^^^^^^

`own_evaluate_parameters`
^^^^^^^^^^^^^^^^^^^^^^^^^

`selection`
^^^^^^^^^^^


Return the selected rows.

        For use in post_handlers. It's a queryset if rows is a queryset and a list otherwise.
        Unlike bulk_queryset neither bulk_filter nor bulk_exclude are applied.



`should_render_form_tag`
^^^^^^^^^^^^^^^^^^^^^^^^

Class methods
-------------

`columns_from_model`
^^^^^^^^^^^^^^^^^^^^

