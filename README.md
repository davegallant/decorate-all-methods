# decorate-all-methods

Decorator that applies a decorator to all methods of a class.

## Installing

```bash
pip install decorate-all-methods
```

## Example Usage

```python
from decorate_all_methods import decorate_all_methods
from tenacity import retry, stop_after_attempt, wait_fixed


@decorate_all_methods(retry(stop=stop_after_attempt(3), wait=wait_fixed(1)), exclude=['__init__'])
class MyClass(object):

    def __init__(self, object):
        """Will not be retried."""
        pass

    def force_error(self):
        """Will be retried 3 times."""
        assert False

    def force_another_error(self):
        """Will also be retried 3 times."""
        assert False
```

_Note: It is not necessary to exclude any methods._

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## License

This project is licensed under the Apache License, Version 2.0.

## Acknowledgments

* https://stackoverflow.com/a/6307868/1191286
