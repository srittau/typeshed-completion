# typeshed-completion

This repository is supposed to document how complete the Python stubs of
[typeshed](https://github.com/python/typeshed) are in comparison to Python 3.7's
standard library.

## Find problems

The `find-problems.py` script can be used to spot potential problems
in typeshed. By default it will check the modules marked as *unchecked*
in `COMPLETION.md`. It can also be called with a single stub file or a
directory of stub files as argument.

The following flags are supported:

* `-a` - Warn about `Any` annotations.
* `-c` - Warn about type comments.
* `-M` - Suppress warnings about missing annotations.
