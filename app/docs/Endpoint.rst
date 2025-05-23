

Endpoint
========

Base class: :doc:`Traversable`

Class that describes an endpoint in iommi. You can create your own custom
endpoints on any :doc:`Part`.

An endpoint can return an `HttpResponse` directly, or a `Part` (which is
rendered for you); everything else we try to dump to json for you.

Example:

.. code-block:: python

    def my_view(request):
        return Page(
            parts__h1=html.h1('Hi!'),
            endpoints__echo__func=lambda value, **_: value,
        )

This page will respond to `?/echo=foo` by returning a json response `"foo"`.

Refinable members
-----------------


`extra_params`
^^^^^^^^^^^^^^

    See :ref:`extra_params <extra_params>`


`func`
^^^^^^

Type: `Callable`


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

`on_bind`
^^^^^^^^^

`own_evaluate_parameters`
^^^^^^^^^^^^^^^^^^^^^^^^^

