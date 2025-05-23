

Query
=====

Base class: :doc:`Part`

Declare a query language. Example:

.. code-block:: python

    class AlbumQuery(Query):
        year = Filter.integer()
        name = Filter()

    query_set = Album.objects.filter(
        AlbumQuery().bind(request=request).get_q()
    )

Refinable members
-----------------


`advanced`
^^^^^^^^^^

Type: `Namespace`


`after`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Union[int, str]`

    See :ref:`after <after>`


`assets`
^^^^^^^^

Type: `Namespace`

    See :ref:`assets <assets>`


`auto`
^^^^^^

Type: :doc:`QueryAutoConfig`

    See :ref:`auto <auto>`


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


`filters`
^^^^^^^^^

Type: `Namespace`


`form`
^^^^^^

Type: `Namespace`


Cookbook:
    :ref:`initial-filter`


`form_class`
^^^^^^^^^^^^

Type: `Type[iommi.form.Form]`


`form_container`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: :doc:`Fragment`


`include`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `bool`

    See :ref:`include <include>`


`iommi_style`
^^^^^^^^^^^^^

Type: `str`

    See :ref:`iommi_style <iommi_style>`


`member_class`
^^^^^^^^^^^^^^

Type: `Type[iommi.query.Filter]`


`model`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Type[django.db.models.base.Model]`


`postprocess`
^^^^^^^^^^^^^


`rows`
^^^^^^


`template`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Union[str, iommi._web_compat.Template]`

    See :ref:`template <template>`


Methods
-------

`get_advanced_query_param`
^^^^^^^^^^^^^^^^^^^^^^^^^^

`get_q`
^^^^^^^



Create a query set based on the data in the request.



`get_query_string`
^^^^^^^^^^^^^^^^^^



Based on the data in the request, return the equivalent query string that you can use with parse_query_string() to create a query set.



`on_bind`
^^^^^^^^^

`on_refine_done`
^^^^^^^^^^^^^^^^

`own_evaluate_parameters`
^^^^^^^^^^^^^^^^^^^^^^^^^

`parse_query_string`
^^^^^^^^^^^^^^^^^^^^

Class methods
-------------

`filters_from_model`
^^^^^^^^^^^^^^^^^^^^

