

Part
====

Base class: :doc:`Traversable`

`Part` is the base class for parts of a page that can be rendered as html, and can respond to ajax and post.

See the `howto <https://docs.iommi.rocks//cookbook_parts_pages.html#parts-pages>`_ for example usages.

Refinable members
-----------------


`after`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Union[int, str]`

    See :ref:`after <after>`


`assets`
^^^^^^^^

Type: `Namespace`

    See :ref:`assets <assets>`


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


`include`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `bool`

Default: `True`
    See :ref:`include <include>`


`iommi_style`
^^^^^^^^^^^^^

Type: `str`

    See :ref:`iommi_style <iommi_style>`


Methods
-------

`bind`
^^^^^^

`iommi_collected_assets`
^^^^^^^^^^^^^^^^^^^^^^^^

`on_refine_done`
^^^^^^^^^^^^^^^^

`perform_dispatch`
^^^^^^^^^^^^^^^^^^

`render_to_response`
^^^^^^^^^^^^^^^^^^^^

