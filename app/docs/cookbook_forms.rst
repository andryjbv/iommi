

.. _cookbook-forms:

Forms
-----

.. _show-fields:

How do I specify which fields to show?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Field.include
.. uses FormAutoConfig.model
.. uses FormAutoConfig.include
.. uses FormAutoConfig.exclude
.. uses FormAutoConfig.default_included

Pass `include=False` to hide the field or `include=True` to show it. By default fields are shown, except the primary key field that is by default hidden. You can also pass a callable here like so:

.. code-block:: python

    Form.create(
        auto__model=Album,
        fields__name__include=
            lambda request, **_: request.GET.get('some_parameter') == 'hello!',
    )

This will show the field `name` only if the GET parameter `some_parameter` is set to `hello!`.

To be more precise, `include` turns off the entire field. See  :ref:`field-non-editable` and :ref:`field-hidden`

Use `auto__include`, to specify the complete list of fields you want:

.. code-block:: python

    form = Form.create(
        auto__model=Album,
        auto__include=['name', 'artist'],
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('fd54e153-8e3b-41cd-bc07-a3b53b15eb34', this)">▼ Hide result</div>
    <iframe id="fd54e153-8e3b-41cd-bc07-a3b53b15eb34" src="doc_includes/cookbook_forms/test_how_do_i_specify_which_fields_to_show.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Instead of using `auto__include`, you can also use `auto__exclude` to just exclude the fields you don't want:

.. code-block:: python

    form = Form.create(
        auto__model=Album,
        auto__exclude=['year'],
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('2bef2b0d-3783-46c9-beb3-7f6d6d1052d2', this)">▼ Hide result</div>
    <iframe id="2bef2b0d-3783-46c9-beb3-7f6d6d1052d2" src="doc_includes/cookbook_forms/test_how_do_i_specify_which_fields_to_show1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

There is also a config option `default_included` which is by default `True`, which is where iommi's default behavior of showing all fields comes from. If you set it to `False` fields are now opt-in:

.. code-block:: python

    form = Form.create(
        auto__model=Album,
        auto__default_included=False,
        # Turn on only the name field
        fields__name__include=True,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('25c000b4-32a4-40ad-ba70-8a196b3e666f', this)">▼ Hide result</div>
    <iframe id="25c000b4-32a4-40ad-ba70-8a196b3e666f" src="doc_includes/cookbook_forms/test_how_do_i_specify_which_fields_to_show2.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _supply-custom-parser-field:

How do I supply a custom parser for a field?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Field.parse

Pass a callable to the `parse` member of the field:

.. code-block:: python

    form = Form(
        auto__model=Track,
        fields__index__parse=lambda field, string_value, **_: int(string_value[:-3]),
    )

.. _field-non-editable:

How do I make a field non-editable?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Field.editable
.. uses Field.parsed_data

There are two cases: A) non-editable and you want to show the value to the
user, or B) non-editable but do not show it ("hardcoded").

A) Show the value
=================

Pass a callable or `bool` to the `editable` member of the field:

.. code-block:: python

    form = Form(
        auto__model=Album,
        fields__name__editable=lambda request, **_: request.user.is_staff,
        fields__artist__editable=False,
    )

For a normal user:

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('38dae2c0-84f3-4026-9bb5-8c45993b53b5', this)">▼ Hide result</div>
    <iframe id="38dae2c0-84f3-4026-9bb5-8c45993b53b5" src="doc_includes/cookbook_forms/test_how_do_i_make_a_field_non_editable.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

For a staff user:

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('c6c96418-a193-4827-906d-fc7715a42dc1', this)">▼ Hide result</div>
    <iframe id="c6c96418-a193-4827-906d-fc7715a42dc1" src="doc_includes/cookbook_forms/test_how_do_i_make_a_field_non_editable1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

B) Hardcode the value
=====================

A common use case is to navigate to some object, then create a sub-object.
In this example we have a url like `/artists/Black Sabbath/`, where the
artist name is parsed into an `Artist` instance by an iommi path decoder.

Then under that we have `/artists/Black Sabbath/create_album/`, and in this
form, we don't want to make the user choose Black Sabbath again. We
accomplish this with the `hardcoded` shortcut:

.. code-block:: python

    form = Form.create(
        auto__model=Album,
        fields__artist=Field.hardcoded(
            parsed_data=lambda params, **_: params.artist,
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('014ea7e7-0464-43b4-a186-958228b78035', this)">▼ Hide result</div>
    <iframe id="014ea7e7-0464-43b4-a186-958228b78035" src="doc_includes/cookbook_forms/test_how_do_i_make_a_field_non_editable2.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _form-non-editable:

How do I make an entire form non-editable?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Form.editable
.. uses FormAutoConfig.instance

This is a very common case so there's a special syntax for this: pass a `bool` to the form:

.. code-block:: python

    form = Form.edit(
        auto__instance=album,
        editable=False,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('11472d59-c727-4daa-8686-2820c27a779f', this)">▼ Hide result</div>
    <iframe id="11472d59-c727-4daa-8686-2820c27a779f" src="doc_includes/cookbook_forms/test_how_do_i_make_an_entire_form_non_editable.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _custom-validator:

How do I supply a custom validator?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Field.is_valid

Pass a callable that has the arguments `form`, `field`, and `parsed_data`. Return a tuple `(is_valid, 'error message if not valid')`.

.. code-block:: python

    form = Form.create(
        auto__model=Album,
        auto__include=['name'],
        fields__name__is_valid=lambda form, field, parsed_data, **_: (
            parsed_data == 'only this value is valid',
            'invalid!',
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('069a2f10-0b49-4eeb-bcec-4c21aa5b18b9', this)">▼ Hide result</div>
    <iframe id="069a2f10-0b49-4eeb-bcec-4c21aa5b18b9" src="doc_includes/cookbook_forms/test_how_do_i_supply_a_custom_validator.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

You can also raise `ValidationError`:

.. code-block:: python

    def name_is_valid(form, field, parsed_data, **_):
        if parsed_data != 'only this value is valid':
            raise ValidationError('invalid!')

    form = Form.create(
        auto__model=Album,
        auto__include=['name'],
        fields__name__is_valid=name_is_valid,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('a31a0998-e70c-499c-bbca-ce7d110e6ec5', this)">▼ Hide result</div>
    <iframe id="a31a0998-e70c-499c-bbca-ce7d110e6ec5" src="doc_includes/cookbook_forms/test_how_do_i_supply_a_custom_validator1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _validate-multiple-fields-together:

How do I validate multiple fields together?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Field.is_valid

Refine the `post_validation` hook on the `form`. It is run after all the individual fields validation
has run. But note that it is run even if the individual fields validation was not successful.

How do I exclude a field?
~~~~~~~~~~~~~~~~~~~~~~~~~

See `How do I say which fields to include when creating a form from a model?`_

.. _include-exclude-fields:

How do I say which fields to include when creating a form from a model?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Form.auto
.. uses Field.include

`Form()` has four methods to select which fields are included in the final form:

1. the `auto__include` parameter: this is a list of strings for members of the model to use to generate the form.
2. the `auto__exclude` parameter: the inverse of `include`. If you use this the form gets all the fields from the model excluding the ones with names you supply in `exclude`.
3. for more advanced usages you can also pass the `include` parameter to a specific field like `fields__my_field__include=True`. Here you can supply either a `bool` or a callable like `fields__my_field__include=lambda request, **_: request.user.is_staff`.
4. you can also add fields that are not present in the model by passing configuration like `fields__foo__attr='bar__baz'` (this means create a `Field` called `foo` that reads its data from `bar.baz`). You can either pass configuration data like that, or pass an entire `Field` instance.

.. _field-initial-value:

How do I supply a custom initial value?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Field.initial

Pass a value or callable to the `initial` member:

.. code-block:: python

    form = Form(
        auto__model=Album,
        fields__name__initial='Paranoid',
        fields__year__initial=lambda field, form, **_: 1970,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('3f42505b-4158-42e2-bf33-6f88ac3c53bd', this)">▼ Hide result</div>
    <iframe id="3f42505b-4158-42e2-bf33-6f88ac3c53bd" src="doc_includes/cookbook_forms/test_how_do_i_supply_a_custom_initial_value.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

If there are `GET` parameters in the request, iommi will use them to fill in the appropriate fields. This is very handy for supplying links with partially filled in forms from just a link on another part of the site.

.. _field-required:

How do I set if a field is required?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Field.required

Normally this will be handled automatically by looking at the model definition, but sometimes you want a form to be more strict than the model. Pass a `bool` or a callable to the `required` member:

.. code-block:: python

    form = Form.create(
        auto__model=Album,
        fields__name__required=True,
        fields__year__required=lambda field, form, **_: True,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('04fb9810-1b11-4dd4-8076-31e4b94f5dd9', this)">▼ Hide result</div>
    <iframe id="04fb9810-1b11-4dd4-8076-31e4b94f5dd9" src="doc_includes/cookbook_forms/test_how_do_i_set_if_a_field_is_required.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

To show the field as required before posting, you can add a CSS class rendering to your style definition:

.. code-block:: python

    IOMMI_DEFAULT_STYLE = Style(
        bootstrap,
        Field__attrs__class__required=lambda field, **_: field.required,
    )

...and this CSS added to your sites custom style sheet:

.. code-block:: css

    .required label:after {
        content: " *";
        color: red;
    }

For the following result:

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('c45e5679-ec5c-4f34-add0-5851bb99eca3', this)">▼ Hide result</div>
    <iframe id="c45e5679-ec5c-4f34-add0-5851bb99eca3" src="doc_includes/cookbook_forms/test_how_do_i_set_if_a_field_is_required1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

See the style docs for more information on defining a custom style for your project.

.. _field-order:

How do I change the order of the fields?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Field.after

You can change the order in your model definitions as this is what iommi uses. If that's not practical you can use the `after` member. It's either the name of a field or an index. There is a special value `LAST` to put a field last.

.. code-block:: python

    from iommi import LAST

    form = Form(
        auto__model=Album,
        fields__name__after=LAST,
        fields__year__after='artist',
        fields__artist__after=0,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('2cfebf3b-bd6e-4828-a509-ee37716c154a', this)">▼ Hide result</div>
    <iframe id="2cfebf3b-bd6e-4828-a509-ee37716c154a" src="doc_includes/cookbook_forms/test_how_do_i_change_the_order_of_the_fields.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

This will make the field order `artist`, `year`, `name`.

If there are multiple fields with the same index or name the order of the fields will be used to disambiguate.

.. _field-search-fields:

How do I specify which model fields the search of a choice_queryset use?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Field.search_fields

`Form.choice_queryset` uses the registered search fields for filtering and ordering.
See `Registrations <registrations>`_ for how to register one. If present it will default
to a model field `name`.


In special cases you can override which attributes it uses for
searching by specifying `search_fields`:

.. code-block:: python

    form = Form(
        auto__model=Album,
        fields__name__search_fields=('name', 'year'),
    )

This last method is discouraged though, because it will mean searching behaves
differently in different parts of your application for the same data.

How do I insert a CSS class or HTML attribute?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See :doc:`Attrs`.

.. _field-template:

How do I override rendering of an entire field?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Field.template

Pass a template name:

.. code-block:: python

    form = Form(
        auto__model=Album,
        fields__year__template='my_template.html',
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('f2cacc2f-f73c-48af-aec9-f1a95b41af57', this)">▼ Hide result</div>
    <iframe id="f2cacc2f-f73c-48af-aec9-f1a95b41af57" src="doc_includes/cookbook_forms/test_how_do_i_override_rendering_of_an_entire_field.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

or a `Template` object:

.. code-block:: python

    form = Form(
        auto__model=Album,
        fields__year__template=Template('This is from the inline template'),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('ec0a4d3a-ad77-4ef3-aa22-9892bf256e17', this)">▼ Hide result</div>
    <iframe id="ec0a4d3a-ad77-4ef3-aa22-9892bf256e17" src="doc_includes/cookbook_forms/test_how_do_i_override_rendering_of_an_entire_field1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _field-input-template:

How do I override rendering of the input field?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Field.input
.. uses Fragment.template

Pass a template name or a `Template` object to the `input` namespace:

.. code-block:: python

    form = Form(
        auto__model=Album,
        fields__year__input__template='my_template.html',
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('6e463571-ded2-4dbc-bd98-7c39e1484f19', this)">▼ Hide result</div>
    <iframe id="6e463571-ded2-4dbc-bd98-7c39e1484f19" src="doc_includes/cookbook_forms/test_how_do_i_override_rendering_of_the_input_field.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. code-block:: python

    form = Form(
        auto__model=Album,
        fields__year__input__template=Template('This is from the inline template'),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('d4f65423-ae7f-4f0f-bf2a-fa3038b62ac0', this)">▼ Hide result</div>
    <iframe id="d4f65423-ae7f-4f0f-bf2a-fa3038b62ac0" src="doc_includes/cookbook_forms/test_how_do_i_override_rendering_of_the_input_field1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _project-wide-field-rendering:

How do I change how fields are rendered everywhere in my project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Style

Define a custom style and override the appropriate fields. For
example here is how you could change `Field.date` to use a text
based input control (as opposed to the date picker that `input type='date'`
uses).

.. code-block:: python

    my_style = Style(bootstrap, Field__shortcuts__date__input__attrs__type='text')

When you do that you will get English language relative date parsing
(e.g. "yesterday", "3 days ago") for free, because iommi used to use a
text based input control and the parser is applied no matter what
(its just that when using the default date picker control it will
always only see ISO-8601 dates).

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('86ebf5e8-c995-4b3b-bf1b-cfc348ac7583', this)">▼ Hide result</div>
    <iframe id="86ebf5e8-c995-4b3b-bf1b-cfc348ac7583" src="doc_includes/cookbook_forms/test_how_do_i_change_how_fields_are_rendered_everywhere_in_my_project.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _form-redirect:

How do I change where the form redirects to after completion?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses FormAutoConfig.instance
.. uses Form.extra

iommi by default redirects to `..` after edit/create/delete. You can
override this via two methods:

- `extra__redirect_to`: a string with the url to redirect to. Relative URLs also work.
- `extra__redirect`: a callable that gets at least the keyword arguments `request`, `redirect_to`, `form`.

Form that after create redirects to the edit page of the object:

.. code-block:: python

    form = Form.create(
        auto__model=Album,
        extra__redirect=lambda form, **_: HttpResponseRedirect(form.instance.get_absolute_url() + 'edit/'),
    )

Form that after edit stays on the edit page:

.. code-block:: python

    form = Form.edit(
        auto__instance=album,
        extra__redirect_to='.',
    )

.. _dependent-fields:

How do I make a fields choices depend on another field?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Field.choices
.. uses Form.fields

The contents of the form is sent with any AJAX requests, so we can
access the value of the other fields to do the filtering:

.. code-block:: python

    def album_choices(form, **_):
        if form.fields.artist.value:
            return Album.objects.filter(artist=form.fields.artist.value)
        else:
            return Album.objects.all()

.. code-block:: python

    Form(
        auto__model=Track,
        fields__artist=Field.choice_queryset(
            attr=None,
            choices=Artist.objects.all(),
            after=0,
        ),
        fields__album__choices=album_choices,
    )

.. _reverse-fk-form:

How do I enable a reverse foreign key relationship?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Form.auto
.. uses FormAutoConfig.instance

By default reverse foreign key relationships are hidden. To turn it on, pass `include=True` to the field. Note that these are read only, because the semantics of hijacking another models foreign keys would be quite weird.

.. code-block:: python

    f = Form(
        auto__instance=black_sabbath,
        fields__albums__include=True,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('b2b65226-d38e-48c3-806c-d94f31086c25', this)">▼ Hide result</div>
    <iframe id="b2b65226-d38e-48c3-806c-d94f31086c25" src="doc_includes/cookbook_forms/test_form_with_foreign_key_reverse.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _non-rendered-field:

How do I set an initial value on a field that is not in the form?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Field.non_rendered
.. uses Field.editable
.. uses Field.initial

You do have to include the field, but you can make it not rendered by using
the `non_rendered` shortcut and setting `initial`.

.. code-block:: python

    f = Form.create(
        auto__model=Album,
        fields__artist=Field.non_rendered(initial=black_sabbath),
        fields__year=Field.non_rendered(initial='1980'),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('b115f489-65aa-4481-a535-82799c1d7d12', this)">▼ Hide result</div>
    <iframe id="b115f489-65aa-4481-a535-82799c1d7d12" src="doc_includes/cookbook_forms/test_non_rendered.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

If you post this form you will get this object:

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('d3da3125-9c04-4c8c-8917-9447b7a6bafb', this)">▼ Hide result</div>
    <iframe id="d3da3125-9c04-4c8c-8917-9447b7a6bafb" src="doc_includes/cookbook_forms/test_non_rendered1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

By default this will be non-editable, but you can allow editing (via the
URL `GET` parameters) by setting `editable=True`.

.. code-block:: python

    f = Form.create(
        auto__model=Album,
        fields__artist=Field.non_rendered(initial=black_sabbath),
        fields__year=Field.non_rendered(
            initial='1980',
            editable=True,
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('825d2ff7-86bd-4ded-a4f9-c8d21910bfff', this)">► Show result</div>
    <iframe id="825d2ff7-86bd-4ded-a4f9-c8d21910bfff" src="doc_includes/cookbook_forms/test_non_rendered2.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Accessing this create form with `?year=1999` in the title will create this object on submit:

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('4223d3a3-753d-49b5-937d-a375984f1204', this)">▼ Hide result</div>
    <iframe id="4223d3a3-753d-49b5-937d-a375984f1204" src="doc_includes/cookbook_forms/test_non_rendered3.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _group-fields:

How do I group fields?
~~~~~~~~~~~~~~~~~~~~~~

.. uses Field.group

Use the `group` field:

.. code-block:: python

    form = Form(
        auto__model=Album,
        fields__year__group='metadata',
        fields__artist__group='metadata',
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('a60ab350-68b1-447e-8a17-f7a27d855639', this)">▼ Hide result</div>
    <iframe id="a60ab350-68b1-447e-8a17-f7a27d855639" src="doc_includes/cookbook_forms/test_grouped_fields.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _field-reverse-m2m:

How do I show a reverse many-to-many relationship?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Field.include

By default reverse many-to-many relationships are hidden. To turn it on, pass `include=True` to the field:

.. code-block:: python

    form = Form(
        auto__model=Genre,
        instance=heavy_metal,
        fields__albums__include=True,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('5e754e84-3432-4e8d-aa38-145f56ced634', this)">▼ Hide result</div>
    <iframe id="5e754e84-3432-4e8d-aa38-145f56ced634" src="doc_includes/cookbook_forms/test_form_with_m2m_key_reverse.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _nested-forms:

How do I nest multiple forms?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Form.fields
.. uses save_nested_forms
.. uses Action.post_handler

You need to use the ``save_nested_forms`` post handler to have a single save button for all the nested forms and edit tables:

.. code-block:: python

    class MyNestedForm(Form):
        edit_ozzy = Form.edit(
            auto__model=Artist,
            instance=lambda **_: Artist.objects.get(name='Ozzy Osbourne'),
        )
        create_artist = Form.create(auto__model=Artist)
        edit_albums = EditTable(
            auto__model=Album,
            auto__include=['name', 'year'],
            columns__name__field__include=True,
        )

        class Meta:
            actions__submit__post_handler = save_nested_forms

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('2f049fb3-05a8-4223-a217-b099e2426384', this)">▼ Hide result</div>
    <iframe id="2f049fb3-05a8-4223-a217-b099e2426384" src="doc_includes/cookbook_forms/test_nested_forms.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _fields-templates:

How do I use templates for fields?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Form.fields_template

Sometimes field groups just aren't enough and you may want to use a template to make your forms pretty:

.. code-block:: python

    class CommentForm(Form):
        class Meta:
            # language=html
            fields_template = Template(
                {{ fields.album.input }}
                <div class="row">
                    <div class="col">
                        {{ fields.name }}
                    </div>
                    <div class="col">
                        {{ fields.email }}
                    </div>
                </div>
                {{ fields.comment }}
            )

        name = Field()
        email = Field()
        comment = Field.textarea()
        album = Field.hardcoded(parsed_data=lambda **_: Album.objects.get(name='Heaven & Hell'))

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('2a54e747-0879-4c55-bd35-f12636710ae4', this)">▼ Hide result</div>
    <iframe id="2a54e747-0879-4c55-bd35-f12636710ae4" src="doc_includes/cookbook_forms/test_fields_template.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _dependent-fields2:

How do I make a field that depends on the choice in another field?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Field.choices

This only works for cases when the choices are fetched via ajax, but this is also the common case:

.. code-block:: python

    def album_choices(form, **_):
        if form.fields.artist.value:
            return Album.objects.filter(artist=form.fields.artist.value)
        else:
            return Album.objects.all()

    form = Form(
        auto__model=Track,
        # First choose an artist
        fields__artist=Field.choice_queryset(
            attr=None,
            choices=Artist.objects.all(),
            after=0,
        ),
        # Then choose an album
        fields__album__choices=album_choices,
    )

.. _create-or-edit-forms:

How do I make a create or edit form?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Field.editable
.. uses Form.create_or_edit

If you don't know until runtime if you want `Form.create` or `Form.edit`,
you can use the `Form.create_or_edit` shortcut. Ff the `instance` is `None`
it will become a create form, otherwise an edit form:

.. code-block:: python

    form = Form.create_or_edit(
        auto__model=Album,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('e33040e2-d223-423a-9d12-38025374bdce', this)">▼ Hide result</div>
    <iframe id="e33040e2-d223-423a-9d12-38025374bdce" src="doc_includes/cookbook_forms/test_how_do_i_make_a_form_to_create_or_edit.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Using a lambda for a create form:

.. code-block:: python

    form = Form.create_or_edit(
        auto__model=Album,
        instance=lambda **_: None,
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('02da32d8-5f94-4581-911c-12b79ba7217f', this)">▼ Hide result</div>
    <iframe id="02da32d8-5f94-4581-911c-12b79ba7217f" src="doc_includes/cookbook_forms/test_how_do_i_make_a_form_to_create_or_edit1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Now an edit form:

.. code-block:: python

    form = Form.create_or_edit(
        auto__model=Album,
        instance=lambda **_: Album.objects.first(),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('9ff65304-aca1-4ee0-adb4-20d8d039515f', this)">▼ Hide result</div>
    <iframe id="9ff65304-aca1-4ee0-adb4-20d8d039515f" src="doc_includes/cookbook_forms/test_how_do_i_make_a_form_to_create_or_edit2.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. _field-hidden:

How do I create a hidden field?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Field.hidden

Use the `Field.hidden` shortcut:

.. code-block:: python

    form = Form.create(
        auto__model=Album,
        fields__artist=Field.hidden(),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('7b886f78-370a-411f-81ff-142d001ae63a', this)">▼ Hide result</div>
    <iframe id="7b886f78-370a-411f-81ff-142d001ae63a" src="doc_includes/cookbook_forms/test_how_do_i_create_a_hidden_field.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

