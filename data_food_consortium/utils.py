from djangoldp.serializers import LDPSerializer


def get_serializer_class(model, depth=2, extra_fields=None):
    if extra_fields is None:
        extra_fields = []
    try:
        serializer_class = model.serializer_class()
    except AttributeError:
        serializer_class = LDPSerializer

    # NOTE: LDPSerializer cannot be used without meta args:
    #   https://git.startinblox.com/djangoldp-packages/djangoldp/-/issues/277
    meta_args = {
        "model": model,
        "depth": depth,
        "fields": "__all__",
        "extra_fields": extra_fields,
    }
    meta_class = type("Meta", (), meta_args)
    return type(serializer_class)(
        serializer_class.__class__.__name__,
        (serializer_class,),
        {"Meta": meta_class},
    )
