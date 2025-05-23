

Views
=====

iommi ships with some views for some common use cases:

Authorization
~~~~~~~~~~~~~
We have `login`, `logout`, and `change_password` views, and there's a function to get all patterns:

.. code-block:: python

    urlpatterns = [
        path('', auth_views()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('f6d4f77a-8004-433c-a417-618cfd223a79', this)">▼ Hide result</div>
    <iframe id="f6d4f77a-8004-433c-a417-618cfd223a79" src="doc_includes/views/test_auth.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('1801bf8e-d342-4b67-9190-9f26dd165c40', this)">▼ Hide result</div>
    <iframe id="1801bf8e-d342-4b67-9190-9f26dd165c40" src="doc_includes/views/test_auth1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('433495f5-c6f3-4266-ab84-90aad63e143b', this)">▼ Hide result</div>
    <iframe id="433495f5-c6f3-4266-ab84-90aad63e143b" src="doc_includes/views/test_auth2.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

CRUD views
~~~~~~~~~~

Create a full CRUD set of views:

.. code-block:: python

    urlpatterns = [
        path('', crud_views(model=Album)),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('1f7a8d49-1bf4-46ca-99e7-6dd68f8526e8', this)">▼ Hide result</div>
    <iframe id="1f7a8d49-1bf4-46ca-99e7-6dd68f8526e8" src="doc_includes/views/test_crud_view.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('90575edb-623e-4edf-b6c2-d93c10f5ee7f', this)">▼ Hide result</div>
    <iframe id="90575edb-623e-4edf-b6c2-d93c10f5ee7f" src="doc_includes/views/test_crud_view1.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('621cbc7e-f713-4469-a213-d429666842e3', this)">▼ Hide result</div>
    <iframe id="621cbc7e-f713-4469-a213-d429666842e3" src="doc_includes/views/test_crud_view2.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('a0190017-d931-48f4-936c-4c25b23437ec', this)">▼ Hide result</div>
    <iframe id="a0190017-d931-48f4-936c-4c25b23437ec" src="doc_includes/views/test_crud_view3.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('84cb5d6a-fe9b-460b-a8d6-83af1ca9afe5', this)">▼ Hide result</div>
    <iframe id="84cb5d6a-fe9b-460b-a8d6-83af1ca9afe5" src="doc_includes/views/test_crud_view4.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

