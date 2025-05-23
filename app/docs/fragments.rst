.. _fragments:

Fragments
---------

If you are just using iommi's built in components like `Form` and `Table`, you won't need to use `Fragment` directly. `Fragment` is a class that is used to compose HTML tags in a way that is later :ref:`refinable`. The most basic example of this is the :ref:`h_tag <h_tag>` of a form or table. A `Fragment` has :ref:`attrs <attributes>`, :ref:`template` and :ref:`tag` configuration:



.. code-block:: python

    table = Table(
        auto__model=Artist,
        h_tag__attrs__style__background='blue',
    )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('97790766-908b-4a2c-b340-ff9e174d62f9', this)">▼ Hide result</div>
    <iframe id="97790766-908b-4a2c-b340-ff9e174d62f9" src="doc_includes/fragments/test_fragment.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

See the API reference for :doc:`Fragment` for more details.

