

Action
======

Base class: :doc:`Fragment`

The `Action` class describes buttons and links.

Examples:

.. code-block:: python

    # Link
    example=Action(attrs__href='http://example.com'),

    # Link with icon
    edit=Action.icon('pencil-square', attrs__href="edit/"),

    # Button
    button=Action.button(display_name='Button title!'),

    # A submit button
    submit=Action.submit(display_name='Do this'),

    # The primary submit button on a form.
    primary=Action.primary(),

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('dc809662-95f7-4c17-ab4d-fb87b4da4250', this)">▼ Hide result</div>
    <iframe id="dc809662-95f7-4c17-ab4d-fb87b4da4250" src="doc_includes/Action/test_base.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Notice that because forms
with a single primary submit button are so common, iommi assumes
that if you have an action called submit and do NOT explicitly
specify the action that it is a primary action. This is only
done for the action called `submit`, inside the Forms actions
`Namespace`.

For that reason this works:

.. code-block:: python

    class MyForm(Form):
        class Meta:
            @staticmethod
            def actions__submit__post_handler(form, **_):
                if not form.is_valid():
                    return

                ...

and is roughly equivalent to

.. code-block:: python

    def on_submit(form, **_):
        if not form.is_valid():
            return

    class MyOtherForm(Form):
        class Meta:
            actions__submit = Action.primary(post_handler=on_submit)

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


`display_name`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `str`

Default: `lambda action, **_: capitalize(action._name).replace('_', ' ')`
    See :ref:`name <name>`


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


`group`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `str`


`include`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `bool`

    See :ref:`include <include>`


`iommi_style`
^^^^^^^^^^^^^

Type: `str`

    See :ref:`iommi_style <iommi_style>`


`post_handler`
^^^^^^^^^^^^^^

Type: `Callable`


Cookbook:
    :ref:`nested-forms`


`tag`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default: `a`
    See :ref:`tag <tag>`


`template`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Union[str, iommi._web_compat.Template]`

    See :ref:`template <template>`


Shortcuts
---------

`Action.button`
^^^^^^^^^^^^^^^

Defaults
++++++++

* `tag`
    * `button`

`Action.delete`
^^^^^^^^^^^^^^^

Parent: Action.submit_

`Action.icon`
^^^^^^^^^^^^^

Defaults
++++++++

* `extra__icon_attrs__class`
    * `Namespace()`
* `extra__icon_attrs__style`
    * `Namespace()`

`Action.primary`
^^^^^^^^^^^^^^^^

Parent: Action.submit_

`Action.submit`
^^^^^^^^^^^^^^^

Parent: Action.button_

Defaults
++++++++

* `attrs__accesskey`
    * `s`
* `attrs__name`
    * `lambda action, **_: action.own_target_marker()`
* `display_name`
    * `Submit`

Methods
-------

`is_target`
^^^^^^^^^^^

`on_bind`
^^^^^^^^^

`on_refine_done`
^^^^^^^^^^^^^^^^

`own_evaluate_parameters`
^^^^^^^^^^^^^^^^^^^^^^^^^

`own_target_marker`
^^^^^^^^^^^^^^^^^^^

