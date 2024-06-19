Installation
============
The installation of this package can either be done by cloning the git repository and installing it or by using pip. Also this package can be installed in user oder developer mode.

User Installation
-----------------

.. code-block:: bash

   $ git clone https://github.com/sogno-platform/cimpy.git
   $ cd cimpy
   $ python3 -m pip install .

or

.. code-block:: bash

   $ python3 -m pip install cimpy

Developer Installation
----------------------

.. code-block:: bash

   $ git clone https://github.com/sogno-platform/cimpy.git
   $ cd cimpy
   $ python3 -m pip install -e .[dev]

or

.. code-block:: bash

   $ python3 -m pip install --pre cimpy


Building a distributable package
--------------------------------

.. code-block:: bash

   $ python3 -m pip install --upgrade build
   $ python3 -m build
