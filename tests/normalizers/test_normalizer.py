import os

from nomad.datamodel import EntryArchive, EntryData, EntryMetadata
from nomad.parsing.parsers import ParserContext

from nomad_tabular_parser_extended.normalizers.tabular_normalizer import (
    TestTabularPlugin,
)
import logging


def test_normalizer():
    directory = os.path.join(os.getcwd(), '../data')

    test_archive = TestTabularPlugin()
    entry_archive = EntryArchive(
        data=EntryData(), metadata=EntryMetadata(), m_context=ParserContext(directory)
    )
    test_archive.normalize(entry_archive, logger=logging.getLogger())
    result = test_archive.m_to_dict()
    assert result['test_if_tabular_parser_is_called'] == ['1', '2', '3', '4']
    assert (
        result['test_tabular_plugin']
        == 'this is written by TestTabularPlugin normalizer'
    )
