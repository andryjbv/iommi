

FormAutoConfig
==============

Base class: `AutoConfig`

Refinable members
-----------------


`default_included`
^^^^^^^^^^^^^^^^^^


Cookbook:
    :ref:`show-fields`


`exclude`
^^^^^^^^^

A list of attribute names to exclude, use `__` to drill down to nested attributes. Example: `['album', 'album__year']`


Cookbook:
    :ref:`show-fields`


`include`
^^^^^^^^^

A list of attribute names to include, use `__` to drill down to nested attributes. Example: `['album', 'album__year']`

    See :ref:`include <include>`


Cookbook:
    :ref:`show-fields`


`instance`
^^^^^^^^^^

An instance of a Django model. If this field is specified, the `model` attribute will be automatically derived. This cannot be a callable, in that case set `model` and use `instance=lambda...` instead of `auto__instance`.


Cookbook:
    :ref:`field-non-editable`

    :ref:`reverse-fk-form`

    :ref:`form-redirect`


`model`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Django model class

Type: `Type[django.db.models.base.Model]`


Cookbook:
    :ref:`show-fields`


`type`
^^^^^^

