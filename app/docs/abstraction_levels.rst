

We’ll start with using iommi declarative tables to create a list of albums:

.. code-block:: python

    class AlbumTable(Table):
        name = Column()
        artist = Column()
        year = Column()

    def index(request):
        return AlbumTable(
            title='Albums',
            rows=Album.objects.all(),
        )

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('fc546ed4-30a6-4bc5-9af3-fe9845367192', this)">▼ Hide result</div>
    <iframe id="fc546ed4-30a6-4bc5-9af3-fe9845367192" src="doc_includes/abstraction_levels/test_foo.html" style="background: white; display: ; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

The iommi middleware will handle if you return an iommi type and render it properly.

At this point you might think "Hold on! Where is the template?". There isn't one. We don't need a template. iommi works at a higher level of abstraction. Don't worry, you can drop down to templates if you need to though. This will be covered later.


You get sorting and pagination by default, and we're using the default bootstrap 5 style. iommi ships with `more styles <style>`_ that you can switch to, or you can `implement your own custom style <style>`_.

class Meta
==========

The `class Meta` concept in iommi is slightly different from how it's used in Django. In iommi any argument to the constructor of a class can be put into `Meta`. In fact, ONLY valid arguments to the constructor can be set in `Meta`. In our example above we set `title` and `rows`. We can also instead set them via `Meta`:

.. code-block:: python

    class AlbumTable(Table):
        name = Column()
        artist = Column()
        year = Column()

        class Meta:
            title = 'Albums'
            rows = Album.objects.all()

    def index(request):
        return AlbumTable()

This will do the same thing! But with a slight twist: parameters set in `Meta` are just defaults, meaning you can still override them later in the constructor call (or in subclasses).

Using as_view
=============

The view we have so far doesn't use the `request` argument. We can simplify it by doing this instead:

.. code-block:: python

    urlpatterns = [
        path('', AlbumTable().as_view()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('d43a9ee2-a814-4e7d-9e26-aa73e17559d1', this)">► Show result</div>
    <iframe id="d43a9ee2-a814-4e7d-9e26-aa73e17559d1" src="doc_includes/abstraction_levels/test_class_meta.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

This looks superficially similar to class based views, but they are very different! Notice the parenthesis after the class name for example. And Django CBVs can't be combined with iommi classes because they are radically different concepts. 

That an instance of `AlbumTable` is created here means we can pass arguments here:

.. code-block:: python

    urlpatterns = [
        path('', AlbumTable(title='Other title', page_size=2).as_view()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('32b99106-1f7a-4ad3-863e-eed3b883149f', this)">► Show result</div>
    <iframe id="32b99106-1f7a-4ad3-863e-eed3b883149f" src="doc_includes/abstraction_levels/test_class_meta1.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

auto__model
===========

The next step in the simplification is to realize that this table is trivially derived from the model definition. iommi has features to do this for you so we can simplify even further! We delete the entire `AlbumTable` class and replace the url definition with this single line:

.. code-block:: python

    urlpatterns = [
        path('', Table(auto__model=Album).as_view()),
    ]

.. raw:: html

    <div class="iframe_collapse" onclick="toggle('30a3d540-8629-4085-9fa1-56987b68f604', this)">► Show result</div>
    <iframe id="30a3d540-8629-4085-9fa1-56987b68f604" src="doc_includes/abstraction_levels/test_class_meta2.html" style="background: white; display: none; width: 100%; min-height: 100px; border: 1px solid gray;"></iframe>

You don't even need to specify the title of the table, as we use the plural verbose name of the model. These are all defaults, not hard coded values, so you can pass parameters to the `Table` constructor here to override anything you want.

