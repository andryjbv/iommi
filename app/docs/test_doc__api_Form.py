
# NOTE: this file is automatically generated

from iommi import *
from iommi.admin import Admin
from iommi.struct import Struct
from django.urls import (
    include,
    path,
)
import pytest
from django.db import models
from tests.helpers import req, user_req, staff_req, show_output
from docs.models import *

pytestmark = pytest.mark.django_db

@pytest.fixture(autouse=True)
def auto_use(big_discography):
    pass

request = req('get')


# language=rst
"""
    
Form
====

Base class: :doc:`Part`

"""
def test_base():
    # language=rst
    """
Describe a Form. Example:

    """

    class MyForm(Form):
        a = Field()
        b = Field.email()

    form = MyForm().bind(request=request)

    # language=rst
    """
    You can also create an instance of a form with this syntax if it's more convenient:

    """

    form = Form(
        fields=dict(
            a=Field(),
            b=Field.email(),
        ),
    ).bind(request=request)

    # language=rst
    """
    In the common case the fields namespace will contain only instances of `Field`, but
iommi actually supports arbitrary `Part` objects. For example:

    """

    form = Form(
        fields=dict(
            # Display a and b inside a box
            box=html.div(
                attrs__class__box=True,
                children__a=Field(),
                children__b=Field.email(),
            ),
            # And c regularly
            c=Field(),
        )
    )

    # language=rst
    """
    So that writing the application logic (e.g. validation and post handlers) is independent
of minor changes to the layout, after bind the `fields` namespace of the form will contain
only instances of `Field` keyed by their `_name` independently of how deep they are in the
hierarchy. Given the above, an appropriate post_handler would be:

    """

    def post_handler(form, **_):
        if not form.is_valid():
            return

        print(form.fields.a.value, form.fields.b.value, form.fields.c.value)
        # And not:
        # print(form.fields.box.a.value, form.fields.box.b.value, form.fields.c.value)

    # @test
    assert post_handler(form=Struct(is_valid=lambda: False)) is None

    post_handler(form.bind(request=req('post')))
    # @end
    # language=rst
    """

    """

    # language=rst
    """

Refinable members
-----------------


`action_class`
^^^^^^^^^^^^^^

Type: `Type[iommi.action.Action]`


`actions`
^^^^^^^^^

Type: `Namespace`


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


`attr`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `str`

    See :ref:`attr <attr>`


`attrs`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: :doc:`Attrs`

    See :ref:`attributes <attributes>`


Cookbook:
    :ref:`freetext-column`


`auto`
^^^^^^

Type: :doc:`FormAutoConfig`

    See :ref:`auto <auto>`


Cookbook:
    :ref:`reverse-fk-form`

    :ref:`include-exclude-fields`


`editable`
^^^^^^^^^^

Type: `bool`

Default: `True`

Cookbook:
    :ref:`field-non-editable`


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


Cookbook:
    :ref:`form-redirect`


`extra_evaluated`
^^^^^^^^^^^^^^^^^

Type: `Dict[str, Any]`

    See :ref:`extra <extra>`


`extra_params`
^^^^^^^^^^^^^^

    See :ref:`extra_params <extra_params>`


`field_group`
^^^^^^^^^^^^^

Type: `Namespace`


`fields`
^^^^^^^^

Type: `Namespace`


Cookbook:
    :ref:`nested-forms`

    :ref:`dependent-fields`


`fields_template`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Union[str, iommi._web_compat.Template]`


Cookbook:
    :ref:`fields-templates`


`h_tag`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Union[iommi.fragment.Fragment, str]`

    See :ref:`title <title>`


`include`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `bool`

    See :ref:`include <include>`


`instance`
^^^^^^^^^^

Type: `Any`


`iommi_style`
^^^^^^^^^^^^^

Type: `str`

    See :ref:`iommi_style <iommi_style>`


`member_class`
^^^^^^^^^^^^^^

Type: `Type[iommi.form.Field]`


`model`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Type[django.db.models.base.Model]`


`page_class`
^^^^^^^^^^^^

Type: `Type[iommi.page.Page]`


`post_validation`
^^^^^^^^^^^^^^^^^


`read_nested_form_from_instance`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Read the nested forms instance from the parent forms instance.

This is analogous to `Field.read_from_instance` but for nested forms.




`template`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Union[str, iommi._web_compat.Template]`

Default: `iommi/form/form.html`
    See :ref:`template <template>`


`title`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: :doc:`Fragment`

    See :ref:`title <title>`


`write_nested_form_to_instance`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Write the nested_form to the instance.

This is analogous to `Field.write_to_instance` but for nested forms.




Shortcuts
---------

`Form.create`
^^^^^^^^^^^^^

Parent: Form.crud_

Defaults
++++++++

* `actions__submit__post_handler`
    * `iommi.form.create_object__post_handler`
* `extra__is_create`
    * `True`

`Form.create_or_edit`
^^^^^^^^^^^^^^^^^^^^^

Parent: Form.crud_

Defaults
++++++++

* `actions__submit__post_handler`
    * `iommi.form.create_or_edit_object__post_handler`
* `extra__is_create`
    * `None`


Cookbook:
    :ref:`create-or-edit-forms`

`Form.crud`
^^^^^^^^^^^

Defaults
++++++++

* `extra__pre_save_all_but_related_fields`
    * `lambda **kwargs: None, # pragma: no mutate`
* `extra__on_save_all_but_related_fields`
    * `lambda **kwargs: None, # pragma: no mutate`
* `extra__pre_save`
    * `lambda **kwargs: None, # pragma: no mutate`
* `extra__on_save`
    * `lambda **kwargs: None, # pragma: no mutate`
* `extra__on_delete`
    * `lambda **kwargs: None, # pragma: no mutate`
* `extra__redirect`
    * `lambda redirect_to, **_: HttpResponseRedirect(redirect_to)`
* `extra__redirect_to`
    * `None`
* `extra__crud_type`
    * `lambda form, **_: 'create' if form.instance is None else 'edit'`
* `extra__new_instance`
    * `lambda form, **_: form.model()`
* `auto`
    * `Namespace()`

`Form.delete`
^^^^^^^^^^^^^

Parent: Form.crud_

Defaults
++++++++

* `actions__submit__call_target__attribute`
    * `delete`
* `actions__submit__post_handler`
    * `iommi.form.delete_object__post_handler`
* `extra__crud_type`
    * `delete`
* `editable`
    * `False`
* `fields__iommi_default_text`
    * `{'call_target': <class 'iommi.fragment.Fragment'>, 'include': <function Form.<lambda> at 0x7f44078b1080>, 'after': 0, 'tag': 'p', 'children__text': <function Form.<lambda> at 0x7f44078b1620>}`

`Form.edit`
^^^^^^^^^^^

Parent: Form.crud_

Defaults
++++++++

* `actions__submit__post_handler`
    * `iommi.form.edit_object__post_handler`
* `extra__is_create`
    * `False`

Methods
-------

`add_error`
^^^^^^^^^^^



Explicitly add an error message to the forms global error set.

Example:

    """

    def post_validation(form, **_):
        form.add_error('global error')

    form = Form.create(
        auto__model=Album,
        post_validation=post_validation,
    )
    # @test
    form = form.bind(request=req('post', **{'-submit': '',}))
    assert form.get_errors()['global'] == {'global error'}
    show_output(form)
    # @end

    # language=rst
    """


`apply`
^^^^^^^



Write the new values specified in the form into the instance specified.



`as_view`
^^^^^^^^^

`get_errors`
^^^^^^^^^^^^



Get a dict containing two keys:

- `global` for errors global to the entire form.
- `fields` for errors specific to fields. This is itself a dict with a key for each field.



`is_target`
^^^^^^^^^^^

`is_valid`
^^^^^^^^^^



Is the form valid?  Can be called inside forms post_validation hook to determine if the
individual fields were all valid.



`on_bind`
^^^^^^^^^

`on_refine_done`
^^^^^^^^^^^^^^^^

`own_evaluate_parameters`
^^^^^^^^^^^^^^^^^^^^^^^^^

`validate`
^^^^^^^^^^

Static methods
--------------

`apply_field`
^^^^^^^^^^^^^

Class methods
-------------

`fields_from_model`
^^^^^^^^^^^^^^^^^^^

    """
