

Filter
======

Base class: :doc:`Part`

Class that describes a filter that you can search for.

See :doc:`Query` for more complete examples.

Parameters with the prefix `field__` will be passed along downstream to the `Field` instance if applicable. This can be used to tweak the basic style interface.

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


`attr`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    See :ref:`attr <attr>`


`choices`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


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


`field`
^^^^^^^

Type: `Namespace`


`freetext`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Cookbook:
    :ref:`freetext-column`


`include`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `bool`

    See :ref:`include <include>`


Cookbook:
    :ref:`filter-column`


`iommi_style`
^^^^^^^^^^^^^

Type: `str`

    See :ref:`iommi_style <iommi_style>`


`is_valid_filter`
^^^^^^^^^^^^^^^^^

Default: `iommi.query.default_filter__is_valid_filter`

`model`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Type[django.db.models.base.Model]`


`model_field`
^^^^^^^^^^^^^


`model_field_name`
^^^^^^^^^^^^^^^^^^


`parse`
^^^^^^^


`pk_lookup_to_q`
^^^^^^^^^^^^^^^^


`query_name`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default: `lambda filter, **_: filter.iommi_name()`

Cookbook:
    :ref:`control-q`


`query_operator_for_field`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `str`

Default: `=`

`query_operator_to_q_operator`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Cookbook:
    :ref:`override-operator`


`search_fields`
^^^^^^^^^^^^^^^


`unary`
^^^^^^^


`value_to_q`
^^^^^^^^^^^^


Cookbook:
    :ref:`control-q`


Shortcuts
---------

`Filter.boolean`
^^^^^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `boolean`
* `parse`
    * `iommi.form.bool_parse`
* `unary`
    * `True`
* `query_operator_to_q_operator`
    * `iommi.query.boolean__query_operator_to_q_operator`

`Filter.boolean_tristate`
^^^^^^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `boolean_tristate`
* `parse`
    * `iommi.form.boolean_tristate__parse`
* `query_operator_to_q_operator`
    * `iommi.query.boolean__query_operator_to_q_operator`
* `unary`
    * `True`

`Filter.case_sensitive`
^^^^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `query_operator_to_q_operator`
    * `iommi.query.case_sensitive_query_operator_to_q_operator`

`Filter.choice`
^^^^^^^^^^^^^^^

Field that has one value out of a set.



Defaults
++++++++

* `field__call_target__attribute`
    * `choice`

`Filter.choice_queryset`
^^^^^^^^^^^^^^^^^^^^^^^^

Field that has one value out of a set.



Defaults
++++++++

* `field__call_target__attribute`
    * `choice_queryset`
* `query_operator_to_q_operator`
    * `lambda op: 'exact'`
* `value_to_q`
    * `iommi.query.choice_queryset_value_to_q`
* `is_valid_filter`
    * `iommi.query.choice_queryset__is_valid_filter`

`Filter.date`
^^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `date`
* `parse`
    * `iommi.form.date_parse`

`Filter.datetime`
^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `date`
* `parse`
    * `iommi.form.date_parse`
* `extra_evaluated__is_tz_aware`
    * `lambda **_: settings.USE_TZ`

`Filter.decimal`
^^^^^^^^^^^^^^^^

Parent: Filter.number_

Defaults
++++++++

* `field__call_target__attribute`
    * `decimal`

`Filter.duration`
^^^^^^^^^^^^^^^^^

Parent: Filter.text_

Defaults
++++++++

* `field__call_target__attribute`
    * `duration`

`Filter.email`
^^^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `email`

`Filter.file`
^^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `file`

`Filter.float`
^^^^^^^^^^^^^^

Parent: Filter.number_

Defaults
++++++++

* `field__call_target__attribute`
    * `float`
* `parse`
    * `iommi.form.float_parse`

`Filter.foreign_key`
^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `foreign_key`

`Filter.foreign_key_reverse`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `foreign_key_reverse`

`Filter.integer`
^^^^^^^^^^^^^^^^

Parent: Filter.number_

Defaults
++++++++

* `field__call_target__attribute`
    * `integer`
* `parse`
    * `iommi.form.int_parse`

`Filter.many_to_many`
^^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `many_to_many`

`Filter.many_to_many_reverse`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Filter.multi_choice`
^^^^^^^^^^^^^^^^^^^^^

Field that has one value out of a set.



Defaults
++++++++

* `field__call_target__attribute`
    * `multi_choice`

`Filter.multi_choice_queryset`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `multi_choice_queryset`

`Filter.number`
^^^^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `number`
* `query_operator_to_q_operator`
    * `iommi.query.case_sensitive_query_operator_to_q_operator`

`Filter.text`
^^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `text`
* `query_operator_for_field`
    * `:`

`Filter.textarea`
^^^^^^^^^^^^^^^^^

Parent: Filter.text_

`Filter.time`
^^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `time`
* `parse`
    * `iommi.form.time_parse`

`Filter.url`
^^^^^^^^^^^^

Defaults
++++++++

* `field__call_target__attribute`
    * `url`

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

