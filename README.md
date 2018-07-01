# typeshed-completion

This repository is supposed to document how complete the Python stubs of
[typeshed](https://github.com/python/typeshed) are in comparison to Python 3.7's
standard library.

## Find problems

The `find-problems.py` script can be used to spot potential problems
in typeshed. By default it will check the modules marked as *unchecked*
in `COMPLETION.md`. It can also be called with a single stub file or a
directory of stub files as argument.

The script does not support type comments, and will warn about missing
annotations in those cases. Suppress these warnings with `-M`. To warn
about `Any` annotations, supply `-a`.

