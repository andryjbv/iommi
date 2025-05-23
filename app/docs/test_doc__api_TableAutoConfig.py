
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
    
TableAutoConfig
===============

Base class: `AutoConfig`

"""
def test_base():
    # language=rst
    """
    """

    # language=rst
    """

Refinable members
-----------------


`default_included`
^^^^^^^^^^^^^^^^^^


Cookbook:
    :ref:`show-columns`


`exclude`
^^^^^^^^^

A list of attribute names to exclude, use `__` to drill down to nested attributes. Example: `['album', 'album__year']`


Cookbook:
    :ref:`show-columns`


`include`
^^^^^^^^^

A list of attribute names to include, use `__` to drill down to nested attributes. Example: `['album', 'album__year']`

    See :ref:`include <include>`


Cookbook:
    :ref:`show-columns`

    :ref:`nested-fk`


`model`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Django model class

Type: `Type[django.db.models.base.Model]`


Cookbook:
    :ref:`show-columns`

    :ref:`group-columns`

    :ref:`reorder-columns`

    :ref:`cell-link`

    :ref:`turn-off-pagination`

    :ref:`column-computed-data`

    :ref:`freetext-column`

    :ref:`filter-column`


`rows`
^^^^^^

A `QuerySet` object. If this field is specified, the `model` attribute will be automatically derived. This cannot be a callable, in that case set `model` and use `rows=lambda...` instead of `auto__rows`.


Cookbook:
    :ref:`group-rows`


    """
