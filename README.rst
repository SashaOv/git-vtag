git vtag
========

Simple and straightforward version tagging with Git. Version tags are
tags in the following format:

::

      v<major>.<release>.<build>
     

(actually, the number of the components can be variable, we are only
dealing with the last component)

Installing
----------

To install the released version:

::

      > pip install gitvtag

Running
-------

The command has built-in help:

::

      > git vtag

Development version
-------------------

The code is hosted on Github: `https://github.com/SashaOv/git-vtag`_. To install the code in development mode:

::

      > git clone https://github.com/SashaOv/git-vtag.git
      > cd git-vtag
      > python setup.py develop

**Tip**: if you are using virtual environment and autoenv, you may want
to set up the .env file, for example:

::

    env_dir=./.venv
    echo activate $env_dir
    source $env_dir/bin/activate`

Apache License
--------------

Copyright (C) 2016 Sasha Ovsankin.
Licensed under the `Apache License v2.0 http://www.apache.org/licenses/LICENSE-2.0`_.
See the file `'LICENSE' https://github.com/SashaOv/git-vtag/LICENSE`_ for details.
