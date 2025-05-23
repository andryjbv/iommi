

Field
=====

Base class: :doc:`Part`

Class that describes a field, i.e. what input controls to render, the label, etc.

See :doc:`Form` for more complete examples.

The life cycle of the data is:

    1. `raw_data`: will be set if the corresponding key is present in the HTTP request
    2. `parsed_data`: set if parsing is successful, which only happens if the previous step succeeded
    3. `value`: set if validation is successful, which only happens if the previous step succeeded

Note that, in addition to the parameters with the defined behavior below, you can pass in any keyword argument you need yourself, including callables that conform to the protocol, and they will be added and evaluated as members.

All these parameters can be callables, and if they are, will be evaluated with the keyword arguments form and field. The only exceptions are `is_valid` (which gets `form`, `field` and `parsed_data`), `render_value` (which takes `form`, `field` and `value`) and `parse` (which gets `form`, `field`, `string_value`). Example of using a lambda to specify a value:

.. code-block:: python

        Field(attrs__id=lambda form, field: 'my_id_%s' % field._name)

Refinable members
-----------------


`after`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the order of columns, see the `howto <https://docs.iommi.rocks//cookbook_forms.html#how-do-i-change-the-order-of-the-fields>`_ for an example.

Type: `Union[int, str]`

    See :ref:`after <after>`


Cookbook:
    :ref:`field-order`


`assets`
^^^^^^^^

Type: `Namespace`

    See :ref:`assets <assets>`


`attr`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The attribute path to apply or get the data from. For example using `foo__bar__baz` will result in `your_instance.foo.bar.baz` will be set by the `apply()` function. Setting this to `None` will mean no attribute is read or written by `apply()`. Defaults to same as `name`.

Type: `str`

    See :ref:`attr <attr>`


`attrs`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A dict containing any custom html attributes to be sent to the `input__template`.

Type: :doc:`Attrs`

    See :ref:`attributes <attributes>`


Cookbook:
    :ref:`freetext-column`


`choice_display_name_formatter`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Callback given the keyword argument `choice` in addition to standard parameters, to obtain the display name representing a given choice to the end user. Default implementation will use `str(choice)`

Type: `Callable[..., str]`

Default: `lambda choice, **_: '%s' % choice`

`choice_id_formatter`
^^^^^^^^^^^^^^^^^^^^^

Callback given the keyword argument `choice` in addition to standard parameters, to obtain the string value to represent the identity of a given `choice`. Default implementation will use `str(choice)`

Type: `Callable[..., str]`

Default: `lambda choice, **_: '%s' % choice`

`choice_to_optgroup`
^^^^^^^^^^^^^^^^^^^^

Type: `Optional[Callable[..., Optional[str]]]`


`choices`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Callable[..., List[Any]]`


Cookbook:
    :ref:`dependent-fields2`

    :ref:`dependent-fields`


`display_name`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The text in the HTML label tag. Default: `capitalize(name).replace('_', ' ')`

Type: `str`

    See :ref:`name <name>`


`editable`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Is this field editable.

Type: `bool`

Default: `True`

Cookbook:
    :ref:`field-non-editable`

    :ref:`non-rendered-field`

    :ref:`create-or-edit-forms`


`empty_label`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `str`

Default: `---`

`endpoints`
^^^^^^^^^^^

Type: `Namespace`

    See :ref:`endpoints <endpoints>`


`errors`
^^^^^^^^

Type: `Errors`


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


`group`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `str`


Cookbook:
    :ref:`group-fields`


`help`
^^^^^^

Type: :doc:`Fragment`


`help_text`
^^^^^^^^^^^

The help text will be grabbed from the django model if specified and available.


`include`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `bool`

    See :ref:`include <include>`


Cookbook:
    :ref:`include-exclude-fields`

    :ref:`show-fields`

    :ref:`field-reverse-m2m`


`initial`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Initial value of the field

Type: `Any`


Cookbook:
    :ref:`field-initial-value`

    :ref:`non-rendered-field`


`input`
^^^^^^^

Type: :doc:`Fragment`


Cookbook:
    :ref:`field-input-template`


`iommi_style`
^^^^^^^^^^^^^

Type: `str`

    See :ref:`iommi_style <iommi_style>`


`is_boolean`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `bool`

Default: `False`

`is_list`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Interpret request data as a list (can NOT be a callable). Default: `False``

Type: `bool`

Default: `False`

`is_valid`
^^^^^^^^^^


Validation function. Should return a tuple of `(bool, reason_for_failure_if_bool_is_false)` or raise ValidationError.

.. code-block:: python

    form = Form.create(
        auto__model=Artist,
        fields__name__is_valid=lambda parsed_data, **_: (parsed_data.startswith('H'), 'Must start with H!'),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('557fca85-f00d-4952-a0c1-768f726b6ae0', this)">▼ Hide result</div>
    <iframe id="557fca85-f00d-4952-a0c1-768f726b6ae0" src="doc_includes/Field/test_base.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Cookbook:
    :ref:`custom-validator`

    :ref:`validate-multiple-fields-together`


`label`
^^^^^^^

Type: :doc:`Fragment`


`model`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Optional[Type[django.db.models.base.Model]]`


`model_field`
^^^^^^^^^^^^^

Type: `Optional[django.db.models.fields.Field]`


`model_field_name`
^^^^^^^^^^^^^^^^^^


`non_editable_input`
^^^^^^^^^^^^^^^^^^^^

Type: :doc:`Fragment`

Default: `{'call_target': <class 'iommi.fragment.Fragment'>, 'children__text': <function Field.<lambda> at 0x7f44078a7100>, 'attrs__value': <function Field.<lambda> at 0x7f44078a71a0>}`

`parse`
^^^^^^^


Parse function. Default just returns the string input unchanged. This function can raise `ValueError` or `ValidationError` to produce a field error message.




Cookbook:
    :ref:`supply-custom-parser-field`


`parse_empty_string_as_none`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `bool`

Default: `True`

`parsed_data`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Any`


Cookbook:
    :ref:`field-non-editable`


`post_validation`
^^^^^^^^^^^^^^^^^


`raw_data`
^^^^^^^^^^

Type: `str`


`read_from_instance`
^^^^^^^^^^^^^^^^^^^^

Callback to retrieve value from edited instance. Invoked with parameters field and instance.


`render_value`
^^^^^^^^^^^^^^


Render the parsed and validated value into a string. Default just converts to `str`.

.. code-block:: python

    sentinel = '!!custom!!'
    form = Form(
        fields__foo=Field(
            initial='not sentinel value',
            render_value=lambda form, field, value, **_: sentinel,
        )
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('0de18fc5-9718-4d0f-bdb6-68e93163a3c5', this)">▼ Hide result</div>
    <iframe id="0de18fc5-9718-4d0f-bdb6-68e93163a3c5" src="doc_includes/Field/test_base1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

`render_value_on_error`
^^^^^^^^^^^^^^^^^^^^^^^


`required`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the field is a required field. Default: `True`

Type: `bool`

Default: `True`

Cookbook:
    :ref:`field-required`


`search_fields`
^^^^^^^^^^^^^^^


Cookbook:
    :ref:`field-search-fields`


`strip_input`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Runs the input data through standard python .strip() before passing it to the parse function (can NOT be callable). Default: `True`

Type: `bool`

Default: `True`

`tag`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `str`

Default: `div`
    See :ref:`tag <tag>`


`template`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Django template filename or `Template` instance for the entire row. Normally you shouldn't need to override on this level. Prefer overriding `input__template`, `label__template` or `error__template` as needed.

Type: `Union[str, iommi._web_compat.Template]`

    See :ref:`template <template>`


Cookbook:
    :ref:`field-template`


`write_to_instance`
^^^^^^^^^^^^^^^^^^^

Callback to write value to instance. Invoked with parameters field, instance and value.


Shortcuts
---------

`Field.boolean`
^^^^^^^^^^^^^^^

Defaults
++++++++

* `parse`
    * `iommi.form.bool_parse`
* `required`
    * `False`
* `is_boolean`
    * `True`

`Field.boolean_tristate`
^^^^^^^^^^^^^^^^^^^^^^^^

Parent: Field.choice_

Defaults
++++++++

* `choices`
    * `[True, False]`
* `choice_id_formatter`
    * `lambda choice, **_: 'true' if choice else 'false'`
* `choice_display_name_formatter`
    * `lambda choice, **_: gettext_lazy('Yes') if choice else gettext_lazy('No')`
* `parse`
    * `iommi.form.boolean_tristate__parse`
* `required`
    * `False`

`Field.checkboxes`
^^^^^^^^^^^^^^^^^^

Parent: Field.multi_choice_

Defaults
++++++++

* `input__attrs__id`
    * `None`
* `extra_evaluated__id`
    * `iommi.form.default_input_id`

`Field.choice`
^^^^^^^^^^^^^^

Shortcut for single choice field. If required is false it will automatically add an option first with the value '' and the title '---'. To override that text pass in the parameter empty_label.



Defaults
++++++++

* `required`
    * `True`
* `is_list`
    * `False`
* `is_valid`
    * `iommi.form.choice_is_valid`
* `input__attrs__multiple`
    * `lambda field, **_: True if field.is_list else None`
* `parse`
    * `iommi.form.choice_parse`

`Field.choice_queryset`
^^^^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `parse`
    * `iommi.form.choice_queryset__parse`
* `choice_id_formatter`
    * `lambda choice, **_: choice.pk`
* `endpoints__choices__func`
    * `iommi.form.choice_queryset__endpoint_handler`
* `is_valid`
    * `iommi.form.choice_queryset__is_valid`
* `extra__filter_and_sort`
    * `iommi.form.choice_queryset__extra__filter_and_sort`
* `extra__model_from_choices`
    * `iommi.form.choice_queryset__extra__model_from_choices`

`Field.date`
^^^^^^^^^^^^

Defaults
++++++++

* `parse`
    * `iommi.form.date_parse`
* `render_value`
    * `iommi.form.date_render_value`

`Field.datetime`
^^^^^^^^^^^^^^^^

Defaults
++++++++

* `parse`
    * `iommi.form.datetime_parse`
* `render_value`
    * `iommi.form.datetime_render_value`
* `extra_evaluated__is_tz_aware`
    * `lambda **_: settings.USE_TZ`

`Field.decimal`
^^^^^^^^^^^^^^^

Parent: Field.number_

Defaults
++++++++

* `parse`
    * `iommi.form.decimal_parse`

`Field.duration`
^^^^^^^^^^^^^^^^

Parent: Field.text_

Defaults
++++++++

* `parse`
    * `iommi.form.duration_parse`
* `render_value`
    * `iommi.form.duration_render_value`

`Field.email`
^^^^^^^^^^^^^

Defaults
++++++++

* `input__attrs__type`
    * `email`
* `parse`
    * `iommi.form.email_parse`

`Field.file`
^^^^^^^^^^^^

Defaults
++++++++

* `input__attrs__type`
    * `file`
* `raw_data`
    * `iommi.form.file__raw_data`
* `write_to_instance`
    * `iommi.form.file_write_to_instance`
* `extra__django_related_field`
    * `True`

`Field.float`
^^^^^^^^^^^^^

Parent: Field.number_

Defaults
++++++++

* `parse`
    * `iommi.form.float_parse`

`Field.foreign_key`
^^^^^^^^^^^^^^^^^^^

`Field.foreign_key_reverse`
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `editable`
    * `False`
* `display_name`
    * `lambda field, **_: capitalize(field.model_field.related_model._meta.verbose_name_plural)`
* `help_text`
    * `None`

`Field.heading`
^^^^^^^^^^^^^^^

Defaults
++++++++

* `editable`
    * `False`
* `attr`
    * `None`

`Field.hidden`
^^^^^^^^^^^^^^

Defaults
++++++++

* `input__attrs__type`
    * `hidden`
* `attrs__style__display`
    * `none`


Cookbook:
    :ref:`field-hidden`

`Field.image`
^^^^^^^^^^^^^

Parent: Field.file_

Defaults
++++++++

* `template`
    * `iommi/form/image_row.html`

`Field.info`
^^^^^^^^^^^^

Shortcut to create an info entry.



Defaults
++++++++

* `editable`
    * `False`
* `attr`
    * `None`

`Field.integer`
^^^^^^^^^^^^^^^

Parent: Field.number_

Defaults
++++++++

* `parse`
    * `iommi.form.int_parse`

`Field.many_to_many`
^^^^^^^^^^^^^^^^^^^^

`Field.many_to_many_reverse`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `display_name`
    * `lambda field, **_: capitalize(field.model_field.remote_field.model._meta.verbose_name_plural)`
* `help_text`
    * `None`

`Field.multi_choice`
^^^^^^^^^^^^^^^^^^^^

Parent: Field.choice_

Defaults
++++++++

* `is_list`
    * `True`

`Field.multi_choice_queryset`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `is_list`
    * `True`

`Field.non_rendered`
^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `template`
    * `<iommi._web_compat.Template object at 0x7f440781d090>`
* `editable`
    * `False`


Cookbook:
    :ref:`non-rendered-field`

`Field.number`
^^^^^^^^^^^^^^

`Field.password`
^^^^^^^^^^^^^^^^

Defaults
++++++++

* `input__attrs__type`
    * `password`
* `render_value`
    * `lambda **_: ''`
* `render_value_on_error`
    * `lambda **_: ''`

`Field.phone_number`
^^^^^^^^^^^^^^^^^^^^

Defaults
++++++++

* `is_valid`
    * `iommi.form.phone_number_is_valid`

`Field.radio`
^^^^^^^^^^^^^

Parent: Field.choice_

Defaults
++++++++

* `input__attrs__id`
    * `None`
* `extra_evaluated__id`
    * `iommi.form.default_input_id`

`Field.text`
^^^^^^^^^^^^

Defaults
++++++++

* `input__attrs__type`
    * `text`

`Field.textarea`
^^^^^^^^^^^^^^^^

Defaults
++++++++

* `input__tag`
    * `textarea`
* `input__attrs__type`
    * `None`
* `input__attrs__value`
    * `None`
* `input__children__text`
    * `lambda field, **_: field.rendered_value`

`Field.time`
^^^^^^^^^^^^

Defaults
++++++++

* `parse`
    * `iommi.form.time_parse`
* `render_value`
    * `iommi.form.time_render_value`

`Field.url`
^^^^^^^^^^^

Defaults
++++++++

* `input__attrs__type`
    * `url`
* `parse`
    * `iommi.form.url_parse`

Methods
-------

`add_error`
^^^^^^^^^^^

`bind_from_instance`
^^^^^^^^^^^^^^^^^^^^

`get_errors`
^^^^^^^^^^^^

`on_bind`
^^^^^^^^^

`on_refine_done`
^^^^^^^^^^^^^^^^

`own_evaluate_parameters`
^^^^^^^^^^^^^^^^^^^^^^^^^

Class methods
-------------

`from_model`
^^^^^^^^^^^^

`hardcoded`
^^^^^^^^^^^

