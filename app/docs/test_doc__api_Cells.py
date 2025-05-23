
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
    
Cells
=====

Base class: :doc:`Traversable`

"""
def test_base():
    # language=rst
    """
Internal class used in row rendering.

You can access the current row via `.row` and the current row index via `.row_index`.

    """

    # language=rst
    """

Refinable members
-----------------


`attrs`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: :doc:`Attrs`

    See :ref:`attributes <attributes>`


`cell_class`
^^^^^^^^^^^^

Type: `Type[iommi.table.Cell]`


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


`iommi_style`
^^^^^^^^^^^^^

Type: `str`

    See :ref:`iommi_style <iommi_style>`


`tag`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `str`

    See :ref:`tag <tag>`


`template`       (:ref:`evaluated <evaluate>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type: `Union[str, iommi._web_compat.Template]`

    See :ref:`template <template>`


Methods
-------

`column_count`
^^^^^^^^^^^^^^

`get_table`
^^^^^^^^^^^

`own_evaluate_parameters`
^^^^^^^^^^^^^^^^^^^^^^^^^

`render`
^^^^^^^^

    """
