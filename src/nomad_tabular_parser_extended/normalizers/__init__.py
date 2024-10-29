from nomad.config.models.plugins import NormalizerEntryPoint


class ExtendedTabularParser(NormalizerEntryPoint):

    def load(self):
        from nomad_tabular_parser_extended.normalizers.normalizer import TestTabularPlugin

        return TestTabularPlugin(**self.dict())


extended_tabular = ExtendedTabularParser(
    name='ExtendedTabularParser',
    description='ExtendedTabularParser entry point configuration.',
)
