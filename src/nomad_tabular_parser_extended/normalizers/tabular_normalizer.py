from nomad.metainfo import Section, Quantity
from nomad.parsing.tabular import TableData


from nomad.config import config

configuration = config.get_plugin_entry_point(
    'nomad_tabular_parser_extended.normalizers:tabular_normalizer'
)


class TestTabularPlugin(TableData):
    m_def = Section(more={'label_quantity': 'short_name'})
    data_file = Quantity(
        type=str,
        a_tabular_parser=dict(
            parsing_options=dict(comment='#'),
            mapping_options=[
                dict(
                    mapping_mode='column', file_mode='current_entry', section=['#root']
                )
            ],
        ),
        a_browser={'adaptor': 'RawFileAdaptor'},
        a_eln={'component': 'FileEditQuantity'},
        default='test.xlsx',
    )
    test_if_tabular_parser_is_called = Quantity(
        type=str, shape=['*'], a_tabular=dict(name='header_1')
    )
    test_tabular_plugin = Quantity(type=str)

    def normalize(self, archive, logger):
        super(TestTabularPlugin, self).normalize(archive, logger)

        self.test_tabular_plugin = 'this is written by TestTabularPlugin normalizer'
