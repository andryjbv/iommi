

Queries
-------

.. _override-operator:

How do I override what operator is used for a query?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Filter.query_operator_to_q_operator

The member `query_operator_to_q_operator` for `Filter` is used to convert from e.g. `:`
to `icontains`. You can specify another callable here:

.. code-block:: python

    Table(
        auto__model=Track,
        columns__album__filter__query_operator_to_q_operator=lambda op: 'exact',
    )

The above will force the album name to always be looked up with case
sensitive match even if the user types `album<Paranoid` in the
advanced query language. Use this feature with caution!

See also `How do I control what Q is produced?`_

.. _control-q:

How do I control what Q is produced?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. uses Filter.value_to_q

For more advanced customization you can use `value_to_q`. It is a
callable that takes `filter, op, value_string_or_f` and returns a
`Q` object. The default handles `__`, different operators, negation
and special handling of when the user searches for `null`.

.. code-block:: python

    class AlbumTable(Table):
        class Meta:
            auto__model = Album

            query__form__fields__eighties = Field.boolean(
                display_name="the '80s",
            )

            @staticmethod
            def query__filters__eighties__value_to_q(value_string_or_f, **_):
                if value_string_or_f == "1":
                    return Q(year__gte=1980) & Q(year__lte=1989)
                return Q()

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('2d80f1f3-dd0b-41c2-b8fe-4668a045790a', this)">▼ Hide result</div>
    <iframe id="2d80f1f3-dd0b-41c2-b8fe-4668a045790a" src="doc_includes/cookbook_queries/test_how_do_i_control_what_q_is_produced.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

Without the filter selected:

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('bae164ed-2cdb-4b2b-a1cd-2997d829721a', this)">► Show result</div>
    <iframe id="bae164ed-2cdb-4b2b-a1cd-2997d829721a" src="doc_includes/cookbook_queries/test_how_do_i_control_what_q_is_produced1.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

How do I control the name used in the advanced query?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. uses Filter.query_name

By default the name of filters are derived from the name you specify or from the model field name
For deeply nested names double underscores are replaced with single underscores, and those names
can become a bit unwieldy. You can then override this with `query_name`:

.. code-block:: python

    track_table = Table(
        auto__model=Track,
        auto__include=['name', 'album', 'album__artist__name'],
        columns__album_artist_name__filter=dict(
            include=True,
            query_name='artist',
        ),
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('26940c04-4ef6-41c1-98bd-7be394b285c7', this)">▼ Hide result</div>
    <iframe id="26940c04-4ef6-41c1-98bd-7be394b285c7" src="doc_includes/cookbook_queries/test_how_do_I_set_the_name_for_a_filter.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

