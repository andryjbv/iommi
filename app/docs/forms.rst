

.. _forms:

Forms
=====

iommi forms is an alternative forms system for Django. It is inspired by the standard Django forms, while improving on its weaknesses.

Major features compared to Django forms:

- Nice rendering to HTML out of the box. Default bootstrap but more built in and can be adapted to your design system.
- AJAX-backed select widgets for your foreign key relationships.
- Supports `__` syntax for going across table/object boundaries, similar to how Django does with QuerySets.
- Send in a callable that is late evaluated to determine if a field should be displayed (`include`). This is very handy for showing a slightly different form to administrators for example.
- Easily add a CSS class or style to just the thing you need just now.
- Easy configuration without writing entire classes that are only used in one place anyway.

Read the full documentation and the :doc:`cookbook` for more.

iommi pre-packages sets of defaults for common field types as 'shortcuts'.
Some examples include `Field.boolean`, `Field.integer` and `Field.choice`.
The full list of shortcuts can be found in the
`API documentation for Field <api.html#iommi.Field>`_.

iommi also comes with full `edit`, `create` and `delete` views. See below for more.

Fully automatic forms
---------------------

Generating forms from Django models automatically is the most powerful and common use for iommi forms:

.. code-block:: python

    form = Form.create(auto__model=Album)

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('0a4f889f-4d83-428a-b95b-1a5d00201b28', this)">▼ Hide result</div>
    <iframe id="0a4f889f-4d83-428a-b95b-1a5d00201b28" src="doc_includes/forms/test_fully_automatic_forms.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Forms in iommi scale with higher complexity:

.. code-block:: python

    edit_user_form = Form.edit(
        auto__model=User,
        instance=lambda user_pk, **_: User.objects.get(pk=user_pk),
        fields__username__is_valid=
            lambda parsed_data, **_: (
                parsed_data.startswith('demo_'),
                'needs to start with demo_'
            ),
        fields__is_staff__label__template='tweak_label_tag.html',
        # show only for staff
        fields__is_staff__include=lambda request, **_: request.user.is_staff,
    )

Install like this:

.. code-block:: python

    urlpatterns = [
        path('users/<user_pk>/edit/', edit_user_form.as_view()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('208ba307-af56-48d7-8e42-49a5536b1cc4', this)">▼ Hide result</div>
    <iframe id="208ba307-af56-48d7-8e42-49a5536b1cc4" src="doc_includes/forms/test_fully_automatic_forms1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

In this case the default behavior for the post handler for `Form.edit` is a save function like the one we had to define ourselves in the previous example.

Declarative forms
-----------------

You can create forms declaratively, similar to Django forms. There are some important differences between iommi forms and Django forms in this mode, maybe the most important being that in iommi you can pass a callable as a parameter to late evaluate what the value of something is. This is used to restrict a field for staff users in this example:

.. code-block:: python

    class UserForm(Form):
        first_name = Field.text()
        username = Field.text(
            is_valid=lambda parsed_data, **_: (
                parsed_data.startswith('demo_'),
                'needs to start with demo_'
            )
        )
        is_staff = Field.boolean(
            # show only for staff
            include=lambda request, **_: request.user.is_staff,
            label__template='tweak_label_tag.html',
        )

        class Meta:
            instance = lambda params, **_: User.objects.get(pk=params.user_pk)

            @staticmethod
            def actions__submit__post_handler(user, form, **_):
                if not form.is_valid():
                    return  # pragma: no cover

                form.apply(user)
                user.save()
                return HttpResponseRedirect('..')

Install like this:

.. code-block:: python

    urlpatterns = [
        # Note `UserForm()`, not `UserForm`!
        path('users/<user_pk>/edit/', UserForm().as_view()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('a580a99b-61aa-47a5-be3e-3f716b22b600', this)">▼ Hide result</div>
    <iframe id="a580a99b-61aa-47a5-be3e-3f716b22b600" src="doc_includes/forms/test_declarative_forms.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Note that we don't need any template here.

Programmatic forms
------------------

The declarative style is very readable, but sometimes you don't know until runtime what the form should look like. Creating forms programmatically in iommi is easy (and equivalent to doing it the declarative way):

.. code-block:: python

    def edit_user_save_post_handler(form, **_):
        if not form.is_valid():
            return  # pragma: no cover

        form.apply(form.instance)
        form.instance.save()
        return HttpResponseRedirect('..')

    def edit_user_view(request, username):
        return Form(
            instance=User.objects.get(username=username),
            fields=dict(
                first_name=Field.text(),
                username=Field.text(
                    is_valid=lambda parsed_data, **_: (
                        parsed_data.startswith('demo_'),
                        'needs to start with demo_'
                    ),
                ),
                is_staff=Field.boolean(
                    # show only for staff
                    include=lambda request, **_: request.user.is_staff,
                    label__template='tweak_label_tag.html',
                ),
            ),
            actions__submit__post_handler=edit_user_save_post_handler,
        )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('b415da77-d1aa-443f-bc2e-8505aa20c54d', this)">▼ Hide result</div>
    <iframe id="b415da77-d1aa-443f-bc2e-8505aa20c54d" src="doc_includes/forms/test_programmatic_forms.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Post handlers
-------------

In the simplest cases, like in a create form, you only have one post handler.
You can do this yourself in the classic Django way:

.. code-block:: python

    if form.is_valid() and request.method == 'POST':
        do_your_thing()

This is fine. But what if you have two buttons? What if you have two forms?
What if there are two forms, one with two submit buttons, and a table with a
bulk action? Suddenly writing the if statement above becomes very difficult.
Post handlers in iommi handle this for you. iommi makes sure that the parts
compose cleanly and the right action is called.

By default for create/edit/delete forms you get one post handler by the name
`submit`. Adding more is easy:

.. code-block:: python

    def disable_action(form, **_):
        form.instance.disabled = True
        form.instance.save()
        return HttpResponseRedirect('.')

    form = Form.edit(
        auto__instance=instance,
        actions__disable__post_handler=disable_action,
    )

Post handlers can return a few different things:

- a `HttpResponse` object which will get returned all the way up the stack
- a *bound* `Part` of some kind. This could be a `Table`, `Form`, `Page`, etc. This is rendered into a `HttpResponse`
- `None` will result in the page being rendered like normal
- everything else iommi will attempt to json encode and return as a json response

.. _Field-hardcoded:

Customization of save behavior on `Form.create`/`edit`
------------------------------------------------------

There are some useful hooks for customizing the save behavior on `Form.create` and `Form.edit`. The most common use case
is to set some hardcoded value for a field that is not in the form. This is best done by using `Field.hardcoded`, so
that should be your first option.

Saving a model in Django models SQL quite closely and iommi have hooks for all the steps in a multi-step commit.

The callbacks are executed in this order:

- `extra__new_instance`: This is called to create a new instance of the model. By default it just calls `form.model()`.
- `extra__pre_save_all_but_related_fields` (only called for `Form.create`)
- `extra__on_save_all_but_related_fields` (only called for `Form.create`)
- `extra__pre_save` (before `instance.save()`)
- `extra__on_save` (after `instance.save()`)

After a POST is completed, the `extra__redirect` callback is executed if present, otherwise `extra__redirect_to`
is used to determine where to redirect to.

