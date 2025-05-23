

Philosophy
==========

iommi follows a design philosophy that has evolved over several
years. It might feel a bit strange in the beginning but we believe
it's well worth it.

We want it to always be possible to create higher abstractions where
you can reuse those abstractions with small tweaks *without having to
change the abstraction to enable this*. If you have code that creates
a complex page with tables, forms, and help text fragments in several places,
then you should be able to reuse that but with a single line of code
make a change to a single small detail of that page, like adding a CSS
class somewhere.

In standard APIs you often have to copy paste the entire page and make
a small change. This hides the difference between the two pages because you
spend 99% of the code to say the same thing. Or alternatively you have to
pollute the definition of the first page with some super specific option
that makes that code worse. We want to avoid both these scenarios.

In short we want to be able to have code that reads like:

    It's like that one, but different like this.

The philosophy has these main parts:

No silent mistakes
---------------------

Systems that fail silently are the worst. Like when you try to render a
value in a django template and you just get silence instead of an error telling
you that you misspelled the variable name. Or when you define a `clean_albumm` method
that never gets called because you misspelled "album" (or worse if you renamed
album to record!). Or silent changes to behavior because you upgraded a library
and your overridden method isn't called because they renamed the function in
the class you inherited from.

In iommi we have an explicit design goal that all mistakes made by the
programmer should (if at all possible) be an error with a very good
error message telling them how to fix the problem.

To accomplish this we:

- don't override using standard object oriented overriding, instead preferring `refining <https://kodare.net/2018/06/25/refinableobject-object-orientation-refined.html>`_
- show you the valid values when you supply an invalid one, one per line and in alphabetical order
- detect common mistakes we've made and have helpful error messages telling you what to do or why you can't do that thing

We love Django, but it does silently fail in many places. In iommi we try our hardest to never let you get stuck with silence as your only company.

Everything has a name
---------------------

We like to think of GUIs as a tree of items like tables, buttons, links
and pages. We want it to be easy to reference an item in this tree so we
can change some property of it, ask it about its configuration, or its state,
and more. This is why iommi requires names for everything. This might seem
overly verbose in the beginning but this is what enables many of the powerful
features of iommi and the robust error handling and error messages.

This philosophy is what enables `Single point customization with no boilerplate`_ via :ref:`dispatching`.

Traversing a namespace is done with `__` when `.` can't be used in normal python syntax
---------------------------------------------------------------------------------------

If you have a class `Car` that has a member `engine` of type `Engine`. Now
let's say you want to create a `Car` with an electric engine. In standard
OOP the `Car` constructor might take an `engine` parameter so you'll end up
with something like:

.. code-block:: python

    car = Car(engine=ElectricEngine())

which is fine if you want to replace the entire engine, but if you just wanted
to configure a small thing but keep all the defaults this can become noisy:

.. code-block:: python

    car = Car(
        engine=InternalCombustionEngine(
            turbo=True,
            cylinders=6,
            gearbox=SequentialGearbox(
                clutch_type='double',
            ),
            color='blue',
            doors=4,
            make='toyota'
            # ...and on and on!...
        )
    )

Now it's impossible to see the intent of the programmer: which of all those
options was the single thing they wanted to change and which are copy paste
of the defaults? Turns out in this case it was just the `clutch_type`! We
would like to write:

.. code-block:: python

    car = Car(engine.gearbox.clutch_type='double')

but pythons syntax doesn't allow this. So instead we use `__`:

.. code-block:: python

    car = Car(engine__gearbox__clutch_type='double')

this is an elegant solution to this problem, one we've stolen from Django's ORM.

Callables for advanced usage, values for the simple cases
---------------------------------------------------------

We want the simple cases to be obvious and simple and the complex cases to
be possible. To enable this we aim to make it so that every place you can
place a value, you can use a lambda. So for example the simple case could be:

.. code-block:: python

    form = Form(
        auto__model=Musician,
        fields__instrument__initial='guitar',
    )

but for the more dynamic case we can write:

.. code-block:: python

    form = Form(
        auto__model=Musician,
        fields__instrument__initial=
            lambda request, **_: 'guitar' if request.user.is_staff else 'tambourine',
    )

In this case you have e.g. `form`, and `field` accessible. If you don't
know which arguments you can use, you can write whatever and you will get an
error message telling you what arguments are available.

Late binding
------------

Late binding allows us to sometimes avoid doing work, but more importantly
it enables us to build more flexible customizations. A concrete example can
be to show a column in a table for only staff users even though the table is
defined in the module scope, long before there even is a request object.

Late binding is accomplished by two mechanisms:

- not creating object structures until the :ref:`bind` phase
- and `Callables for advanced usage, values for the simple cases`_

.. _philosophy_hybrid_api:

Declarative/programmatic hybrid API
-----------------------------------

The ``@declarative`` and ``@with_meta``
decorators enables us to very easily write an API
that can look both like a normal simple python API:

.. code-block:: python

    my_table = Table(
        columns=dict(
            foo=Column(),
            bar=Column(),
        ),
        sortable=False)

This code is hopefully pretty self explanatory. But the cool thing is
that we can do the exact same thing with a declarative style:

.. code-block:: python

    class MyTable(Table):
        foo = Column()
        bar = Column()

        class Meta:
            sortable = False

    my_table = MyTable()

This style can be much more readable. There's a subtle different though
between the first and second styles: the second is really a way to
declare defaults, not hard coding values. This means we can create
instances of the class and set the values in the call to the
constructor:

.. code-block:: python

    my_table = MyTable(
        columns__foo__include=False,  # <- hides the column foo
        sortable=True,                # <- turns on sorting again
    )

...without having to create a new class inheriting from ``MyTable``. So
the API keeps all the power of the simple style and also getting the
nice syntax of a declarative API.

Prepackaged commonly used patterns (that can still be customized!)
------------------------------------------------------------------

A pattern you'll see often in iommi is that we have class methods instead of
classes. We call these "shortcuts". We don't need to have classes in order to
share functionality and in fact we think this hinders composability and hides
lack of customizability.

A shortcut is a bunch of config (and sometimes a tiny bit of code) that also
has a name. We use these instead of writing e.g. `Field` subclasses. The names of
these shortcuts are also used by the style system to determine what rules to
apply.

An important difference between a traditional class and a shortcut is that the
config in a shortcut are defaults, not hard behavior. That means we can start
with a shortcut that does mostly what we want and then pass one or more
arguments to further refine. Again without writing a class.

Single point customization with no boilerplate
----------------------------------------------

GUIs consists of layers of abstraction like a form containing fields,
fields containing input tags, and a button. But in traditional APIs, to customize the input tag of
a form field row you must subclass several classes even for very trivial
things. Often trivial things also requires copy pasting a template and making
a minor change. This leads to lots of code that basically does nothing and it
*hides* the unique and relevant code in the noise of the other cruft around
it that is just copy paste or boilerplate.

In iommi we strive to avoid this by enabling one-off customizations with
*no boilerplate*. To set a CSS style on a specific input field inside a form
that was automatically generated we can write:

.. code-block:: python

    Form(
        auto__model=Album,
        fields__year__input__attrs__style__font='helvetica')

See also `Everything has a name`_

.. _escape-hatches:

Escape hatches included
-----------------------

It's frustrating when a library can't do what you want. But if the library
can't be *extended* to do what you want it's even worse. We aim to include escape
hatches for when you reach the limits of iommi. You should be able to add your
own logic and data without having to subclass or patch the code.

Read the documentation on :doc:`extra` for more information.

