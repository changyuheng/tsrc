.. image:: https://img.shields.io/github/license/your-tools/tsrc.svg
   :target: https://github.com/your-tools/tsrc/blob/main/LICENSE

.. image:: https://github.com/your-tools/tsrc/workflows/tests/badge.svg
   :target: https://github.com/your-tools/tsrc/actions

.. image:: https://github.com/your-tools/tsrc/workflows/linters/badge.svg
   :target: https://github.com/your-tools/tsrc/actions

.. image:: https://img.shields.io/pypi/v/tsrc.svg
   :target: https://pypi.org/project/tsrc/

.. image:: https://img.shields.io/badge/deps%20scanning-pyup.io-green
     :target: https://github.com/your-tools/tsrc/actions

tsrc: manage groups of git repositories
=======================================

`Overview`_ · `Installation`_ · `Usage example`_ · `Documentation`_ · `Release notes`_ · `Contributing`_ · `License`_

Note
----

This project was originally hosted on the `TankerHQ
<https://github.com/TankerHQ>`_ organization, which was my employer from 2016
to 2021. They kindly agreed to give back ownership of this project to
me. Thanks!

Overview
---------

tsrc is a command-line tool that helps you manage groups of several git repositories.

It can be `seen in action on asciinema.org <https://asciinema.org/a/131625>`_.

Note
-----

`tsrc` does not adhere strictly to the `semver specification <https://semver.org/>`_. So before upgrading to a new version, please take the time to read the `Changelog <https://your-tools.github.io/tsrc/changelog/>`_ first!

Installation
-------------

The recommended way to install ``tsrc`` is to use `pipx <https://pipxproject.github.io/pipx/>`_

* Make sure to have Python **3.7** or later installed.
* Install ``pipx``
* Run ``pipx install tsrc``.


Usage Example
-------------


* Create a *manifest* repository. (``git@example.org/manifest``)

* Push a file named ``manifest.yml`` looking like:

.. code-block:: yaml

    repos:
      - url: git@example.com/foo.git
        dest: foo

     -  url: git@example.com/bar.git
        dest: bar


* Create a new workspace with all the repositories listed in the manifest:

.. code-block:: console

    $ tsrc init git@git.local/manifest.git

    :: Configuring workspace in /path/to/work
    ...
    => Cloning missing repos
    * (1/2) foo
    ...
    * (2/2) bar
    ...
    : Configuring remotes
    Done ✓


* Synchronize all the repositories in the workspace:

.. code-block:: console

    $ tsrc sync
    => Updating manifest
    ...
    :: Configuring remotes
    :: Synchronizing workspace
    * (1/2) foo
    => Fetching origin
    => Updating branch
    Already up to date
    * (2/2) bar
    => Updating branch
    Updating 29ac0e1..b635a43
    Fast-forward
     bar.txt | 1 +
     1 file changed, 1 insertion(+)
     create mode 100644 bar.txt
    Done ✓


Documentation
--------------

For more details and examples, please refer to `tsrc documentation <https://your-tools.github.io/tsrc/>`_.

Release notes
-------------

Detailed changes for each release are documented in the `changelog <https://your-tools.github.io/tsrc/changelog/>`_.

Contributing
------------

We welcome feedback, `bug reports <https://github.com/your-tools/tsrc/issues>`_, and bug fixes in the form of `pull requests <https://github.com/your-tools/tsrc/pulls>`_.

Detailed instructions can be found `in the documentation <https://your-tools.github.io/tsrc>`_.

License
-------

tsrc is licensed under a `BSD 3-Clause license <https://github.com/your-tools/tsrc/blob/main/LICENSE>`_.
