

QueryAutoConfig
===============

Base class: `AutoConfig`

Refinable members
-----------------


`default_included`
^^^^^^^^^^^^^^^^^^


`exclude`
^^^^^^^^^

A list of attribute names to exclude, use `__` to drill down to nested attributes. Example: `['album', 'album__year']`


`include`
^^^^^^^^^

A list of attribute names to include, use `__` to drill down to nested attributes. Example: `['album', 'album__year']`

    See :ref:`include <include>`


`model`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Django model class

Type: `Type[django.db.models.base.Model]`


`rows`
^^^^^^

A `QuerySet` object. If this field is specified, the `model` attribute will be automatically derived. This cannot be a callable, in that case set `model` and use `rows=lambda...` instead of `auto__rows`.

