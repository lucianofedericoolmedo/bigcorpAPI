import importlib


class StringSearchMixin(object):
    # Creating custom import serialize class because of error with imports in library not solved by PR:
    # https://github.com/rsinger86/drf-flex-fields/pull/34/

    def _import_serializer_class(self, location: str):
        pieces = location.split(".")
        class_name = pieces.pop()
        module = importlib.import_module(".".join(pieces))
        return getattr(module, class_name)
