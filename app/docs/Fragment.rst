

Fragment
========

Base class: :doc:`Part`

.. _Fragment:

`Fragment` is a class used to build small HTML fragments that plug into iommi's structure.

.. code-block:: python

    h1 = Fragment(children__text='Tony', tag='h1')

    # There is also a shorthand version that is identical to the above:
    h1 = Fragment('Tony', tag='h1')

It's easiest to use via the html builder:

.. code-block:: python

    h1 = html.h1('Tony')

Fragments are useful because attrs, template and tag are evaluated, so if
you have a `Page` with a fragment in it you can configure it later:

.. code-block:: python

    class MyPage(Page):
        header = html.h1(
            'Hi!',
            attrs__class__staff=
                lambda request, **_: request.user.is_staff,
        )

Rendering a `MyPage` will result in a `<h1>`, but if you do
`MyPage(parts__header__tag='h2')` it will be rendered with a `<h2>`.

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


`attrs`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: :doc:`Attrs`

    See :ref:`attributes <attributes>`


`children`
^^^^^^^^^^


Cookbook:
    :ref:`override-part-of-page`


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

    See :ref:`include <include>`


`iommi_style`
^^^^^^^^^^^^^

Type: `str`

    See :ref:`iommi_style <iommi_style>`


`tag`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    See :ref:`tag <tag>`


`template`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Union[str, iommi._web_compat.Template]`

    See :ref:`template <template>`


Cookbook:
    :ref:`field-input-template`


Methods
-------

`on_bind`
^^^^^^^^^

`on_refine_done`
^^^^^^^^^^^^^^^^

`own_evaluate_parameters`
^^^^^^^^^^^^^^^^^^^^^^^^^

`render_text_or_children`
^^^^^^^^^^^^^^^^^^^^^^^^^

