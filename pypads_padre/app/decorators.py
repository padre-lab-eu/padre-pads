from pypads.app.decorators import IDecorators, decorator

from pypads_padre.util import get_class_that_defined_method


class PadrePadsDecorators(IDecorators):
    def __init__(self):
        super().__init__()

    @property
    def pypads(self):
        from pypads.app.pypads import get_current_pads
        return get_current_pads()

    # ------------------------------------------- decorators --------------------------------
    @decorator
    def dataset(self, mappings=None, name=None, metadata=None, **kwargs):
        def track_decorator(fn):
            ctx = get_class_that_defined_method(fn)
            return self.pypads.api.track_dataset(ctx=ctx, fn=fn, name=name, metadata=metadata, mappings=mapping,
                                                  **kwargs)

        return track_decorator

    @decorator
    def splitter(self, mappings=None):
        def track_decorator(fn):
            ctx = get_class_that_defined_method(fn)
            return self.pypads.api.track_splits(ctx=ctx, fn=fn, mappings=mapping)

        return track_decorator

    @decorator
    def hyperparameters(self, mappings=None):
        def track_decorator(fn):
            ctx = get_class_that_defined_method(fn)
            return self.pypads.api.track_parameters(ctx=ctx, fn=fn, mappings=mapping)

        return track_decorator

    @decorator
    def parameter_search(self, mappings=None):
        def track_decorator(fn):
            ctx = get_class_that_defined_method(fn)
            return self.pypads.api.track_parameter_search(ctx=ctx, fn=fn, mappings=mapping)

        return track_decorator