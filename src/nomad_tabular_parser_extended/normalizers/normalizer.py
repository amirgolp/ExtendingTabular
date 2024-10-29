from typing import (
    TYPE_CHECKING,
)

from nomad.metainfo import Section, Quantity
from nomad.parsing.tabular import TableData

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config
from nomad.normalizing import Normalizer

configuration = config.get_plugin_entry_point(
    'nomad_tabular_parser_extended.normalizers:normalizer_entry_point'
)


class TestTabularPlugin(TableData, Normalizer):
    m_def = Section(
        extends_base_section=True,
        more={
            "label_quantity": "short_name"
        }
    )
    data_file = Quantity(
        type=str,
        a_tabular_parser=dict(
            parsing_options=dict(comment='#'),
            mapping_options=[
                dict(mapping_mode='column', file_mode='current_entry', section=['#root'])
            ]
        ),
        a_browser={
            "adaptor": "RawFileAdaptor"
        },
        a_eln={
            "component": "FileEditQuantity"
        },
        default="test.csv",
    )
    short_name = Quantity(type=str, a_tabular=dict(name='header_1'))
    test_name = Quantity(type=str)

    def normalize(self, archive: EntryArchive, logger: BoundLogger):
        super(TestTabularPlugin, self).normalize(archive, logger)

        self.test_name = "this is written inside TestTabularPlugin normalizer"
