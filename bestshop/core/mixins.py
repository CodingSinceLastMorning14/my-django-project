class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_fields()

    def _init_bootstrap_fields(self):
        for (_, field) in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'


class FormTableMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_margin_fields()

    def _init_margin_fields(self):
        for (_, field) in self.fields.items():
            if 'style' not in field.widget.attrs:
                field.widget.attrs['style'] = ''
            field.widget.attrs['style'] += ' margin-left: 9%;'
