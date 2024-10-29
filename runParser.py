# from nomad.cli.parse import _parse
#
# if __name__ == "__main__":
#     _parse(
#         mainfile='./tests/data/test_tabular.archive.yaml --show-archive',
#         show_archive=True,
#         archive_with_meta=False,
#         show_metadata=False,
#         preview_plots=False,
#         skip_normalizers=False,
#         not_strict=False,
#         server_context=False,
#         username=None,
#         password=None,
#         save_plot_dir=False,
#     )

from nomad.datamodel import EntryArchive
from nomad_tabular_parser_extended.normalizers.normalizer import TestTabularPlugin
import logging

p = TestTabularPlugin()
a = EntryArchive()
p.normalize(a, logger=logging.getLogger())

print(a.m_to_dict())
