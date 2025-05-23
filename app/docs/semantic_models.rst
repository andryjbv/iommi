

.. _semantic-models:

Semantic models
===============


The standard way in Django to define models is something like this:

.. code-block:: python

    class User(Model):
        name = CharField()
        person_number = CharField()
        birth_place = ForeignKey(Location, on_delete=CASCADE)
        manager = ForeignKey('self', on_delete=CASCADE)

The issue with that is that the semantic meaning of each field is hidden behind the name, and not in the type. The `name` 
and `person_number` fields have the same type but should be handled differently. Since iommi shortcut registrations are 
based on the type, you can't customize the parsing or rendering of the `person_number` or `birth_place` fields on 
the project level via the :ref:`style`.

Moreover in this example the type information alone is not enough for other customization. For `ForeignKey`, by default
in iommi you'll get a select2 drop-down to select from all items in that table. This is not good UX for a location, and
it's probably not good UX for a manager field either as that should most likely exclude non-active users, and/or limited
to users with a certain role.

For `CharField`, the default is to present a text field, but in the above model we want a Swedish "person number", which
has a specific storage format, can accept a variety of input formats that can be unambiguously parsed, and even has a
checksum that can be used to validate that the user input is correct.

A solution to this is to create additional specialized types to specify semantic model fields:

.. code-block:: python

    class PersonNumberField(CharField):
        pass


    class LocationField(ForeignKey):
        def __init__(self, to=None, *args, **kwargs):
            assert to is None
            to = Location
            super().__init__(to=to, *args, **kwargs)


    class UserField(ForeignKey):
        def __init__(self, to=None, *args, **kwargs):
            assert to is None
            to = User
            super().__init__(to=to, *args, **kwargs)

These fields can then be registered in iommi:

.. code-block:: python

    register_factory(PersonNumberField, shortcut_name='person_number')
    register_factory(LocationField, shortcut_name='location')
    register_factory(UserField, shortcut_name='user')

You will then need to add shortcuts for these in your subclasses of `Column`, `Field`, and `Filter`. These can start out empty, and configuration can be done in the style definition:

.. code-block:: python

    your_style = Style(
        bootstrap5,
        Field=dict(
            shortcuts=dict(
                person_number__parse=person_number__parse,
            ),
        ),
    )

It requires a little bit more initial setup, but for commonly used field types, it will make new views correct by default and super easy to setup.

