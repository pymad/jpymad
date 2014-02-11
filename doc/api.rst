PyMad API
*********

Module jpymad
=============

The jpymad package contains a lightweight python wrapper for JMad. In
additions we have some tools which may be used more generally, found in
:py:mod:`cern.jpymad.tools`


=============================
Module cern.pymad.abc.service
=============================
.. automodule:: cern.jpymad.service
    :members:

========================
Module cern.jpymad.model
========================
.. automodule:: cern.jpymad.model
    :members:

===========================
Module cern.jpymad.modeldef
===========================
.. automodule:: cern.jpymad.modeldef
    :members:

============================
Module cern.jpymad.tools.tfs
============================
.. automodule:: cern.jpymad.tools.tfs
    :members:



Additional tools
================

A collection of tools which can be useful to the end user are documented here.


Module cern.jpymad.tools.tfs
----------------------------

Simple function which loads a tfs file

.. code-block:: python

    from cern.jpymad.tools.tfs import tfs
    table,summary = tfs('file.tfs')

You can then access e.g. the horizontal beta in several equivalent ways

.. code-block:: python

    table.betx
    table.BETX
    table['betx']
    table['BETX']

All these four methods will return the same object. Naming scheme follows
the convention from Mad-X.

It is possible to get the list of available keys:

.. code-block:: python

    table.keys()
    summary.keys()
