class UI(dict):
    """
    Custom dictionary class for UI metadata.

    **Keys:**
    - `width`: Width of the UI.
    - `height`: Height of the UI.
    - `count`: Number of objects in the UI.
    - `objects`: List of objects in the UI.
    """
    def __init__(self):
        super().__init__()
        self['count'] = 0
        self['objects'] = []

    def verify_objects(self):
        """
        **Raises**:
        - `KeyError` If any object is missing a required key.

        Verify that all objects have the required keys.
        """
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