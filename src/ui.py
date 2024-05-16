class UI(dict):
    """Custom dictionary class for UI metadata."""
    def __init__(self):
        super().__init__()
        self['count'] = 0
        self['objects'] = []

    def verify_objects(self):
        for obj in self['objects']:
            if 'x' not in obj:
                raise KeyError(f'"x" not found in object: {obj}')
            if 'y' not in obj:
                raise KeyError(f'"y" not found in object: {obj}')
            if 'width' not in obj:
                raise KeyError(f'"width" not found in object: {obj}')
            if 'height' not in obj:
                raise KeyError(f'"height" not found in object: {obj}')
            if 'class' not in obj:
                raise KeyError(f'"class" not found in object: {obj}')