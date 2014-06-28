JPyMAD
------

JPyMAD is a python wrapper for MAD-X_ (Methodical Accelerator Design). It
uses uses JMad_ via Py4J_ which then accesses the MAD-X_ library.

There is also cpymad_ uses Cython_ to access the MAD-X_ library directly.

.. _MAD-X: http://madx.web.cern.ch/madx/
.. _Cython: http://cython.org/
.. _JMad: http://jmad.web.cern.ch/jmad/
.. _Py4J: http://py4j.sourceforge.net/
.. _cpymad: http://cern.ch/cpymad

Prerequisites
~~~~~~~~~~~~~

- JMad_
- numpy
- Py4J_

Installation
~~~~~~~~~~~~

Installation might be as easy as running

.. code-block:: bash

    python setup.py install

from the source repository.


Further instructions are available at http://cern.ch/jpymad/installation.


Usage
~~~~~

.. code-block:: python

    # Once installed this is a nice example showing current
    # usability (run from examples folder):
    from cern.jpymad import JPyMadService

    # the service object is responsible for locating and instanciating models
    pms = JPyMadService()

    # Create a model:
    pm = pms.create_model('lhc')

    # Run twiss:
    # This returns a "lookup dictionary" containing
    # numpy arrays. Lowercase keys.
    twiss,summary = pm.twiss()

    # Your own analysis below:
    import matplotlib.pyplot as plt
    plt.plot(twiss.s, twiss.betx)


See http://cern.ch/jpymad/ for further documentation.


Development guidelines
~~~~~~~~~~~~~~~~~~~~~~

**Coding:**

Try to be consistent with the PEP8_ guidelines as far as you are familiar
with it. Add `unit tests`_ for all non-trivial functionality.
`Dependency injection`_ is a great pattern to keep modules testable.

.. _PEP8: http://www.python.org/dev/peps/pep-0008/
.. _`unit tests`: http://docs.python.org/2/library/unittest.html
.. _`Dependency injection`: http://www.youtube.com/watch?v=RlfLCWKxHJ0

**Version control:**

Commits should be reversible, independent units if possible. Use descriptive
titles and also add an explaining commit message unless the modification is
trivial. See also: `A Note About Git Commit Messages`_.

.. _`A Note About Git Commit Messages`: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html

**Tests:**

Currently, two major test services are used:

- The tests on CDash_ are run on a daily basis on the ``master`` branch and
  on update of the ``testing`` branch. It ensures that the integration
  tests for the LHC models are working correctly on all tested platforms.
  The tests are run only on specific python versions.

- The `Travis CI`_ service is mainly used to check that the unit tests for
  pymad itself execute on several python versions. Python{2.6,2.7,3.3} are
  supported. The tests are executed on any update of an upstream branch.

.. _CDash: http://abp-cdash.web.cern.ch/abp-cdash/index.php?project=pymad
.. _`Travis CI`: https://travis-ci.org/pymad/pymad


**Contribution work flow:**

This motivates the following work flow when performing any changes:

All changes are reviewed via pull-requests. Before merging to master the
pull-request must reside aliased by the ``testing`` branch long enough to
be confirmed as stable.  Any issues are discussed in the associated issue
thread.  Concrete suggestions for changes are best posed as pull-requests
onto the feature branch.

