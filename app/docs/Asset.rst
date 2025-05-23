

Asset
=====

Base class: :doc:`Fragment`

Class that describes an asset in iommi. Assets are meant to be the elements that you refer
to in the HEAD of your document such as links to scripts, style sheets as well as
inline scripts or css. But if necessary you can specify an arbitrary django template.

Every :doc:`Part` can include the assets it needs. Similarly :doc:`Style` can include assets.
When a part is rendered all assets are included in the head of the document.

Because assets have names (:doc:`Everything has a name <philosophy>`), assets with the same name will overwrite
each other, resulting in only one asset with a given name being rendered.

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


`in_body`
^^^^^^^^^

Type: `bool`


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


Shortcuts
---------

`Asset.css`
^^^^^^^^^^^

To use this shortcut, pass `attrs__href='/my_url_to_the.css'`

Examples:

.. code-block:: python

    Asset.css(
        attrs__href='https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css',
        attrs__integrity='sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh',
        attrs__crossorigin='anonymous',
    )

    Asset.css('p { font-size: 18pt; }')

Defaults
++++++++

* `tag`
    * `link`
* `attrs__rel`
    * `stylesheet`

`Asset.js`
^^^^^^^^^^

To use this shortcut, pass `attrs__src='/my_url_to_the.js'`

Examples:

.. code-block:: python

    Asset.js(
        attrs__src='https://cdn.jsdelivr.net/npm/select2@4.0.12/dist/js/select2.min.js',
    )

    Asset.js('window.foo = bar')

Defaults
++++++++

* `tag`
    * `script`

