from nomad.config.models.plugins import NormalizerEntryPoint


class ExtendedTabularParser(NormalizerEntryPoint):
    def load(self):
        from nomad_tabular_parser_extended.normalizers.tabular_normalizer import (
            TestTabularPlugin,
        )

        return TestTabularPlugin(**self.dict())


tabular_normalizer = ExtendedTabularParser(
    name='ExtendedTabularParser test',
    description='ExtendedTabularParser entry point configuration.',
)
