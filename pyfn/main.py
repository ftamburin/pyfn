"""Welcome to pyfn.

This is the entry point of the application.
"""

import logging
import argparse

from pyfn.exceptions.parameter import InvalidParameterError

logger = logging.getLogger(__name__)


def _get_fn_splits_dict(splits_dirpath, with_exemplars=False):
    return {}


def _convert(args):
    if args.source_format == args.target_format:
        raise InvalidParameterError(
            'Source and Target formats are the same! Please specify different '
            'source/target formats')
    if args.source_path == args.target_path:
        raise InvalidParameterError(
            'Source and Target paths are the same! Please specify different '
            'source/target paths')
    if args.source_format == 'fnxml':
        # TODO: check input directory structure: should contain only
        # train/dev/test dir (other keywords not allowed) and each dir should
        # contain either fulltext, either lu dir, nothing else
        with_exemplars = args.with_exemplars == 'true'
        fn_splits_dict = _get_fn_splits_dict(args.source_path, with_exemplars)


def main():
    """Launch the pyfn application."""
    parser = argparse.ArgumentParser(prog='pyfn')
    subparsers = parser.add_subparsers()
    parser_convert = subparsers.add_parser(
        'convert', formatter_class=argparse.RawTextHelpFormatter,
        help='Convert source file from given format to target file in given '
             'format')
    parser_convert.set_defaults(func=_convert)
    parser_convert.add_argument('--source', required=True,
                                dest='source_path',
                                help='Absolute filepath to source file')
    parser_convert.add_argument('--target', required=True,
                                dest='target_path',
                                help='Absolute filepath to target file')
    parser_convert.add_argument('--from', required=True,
                                dest='source_format',
                                choices=['conll', 'bios', 'semeval', 'fnxml'],
                                help='''Source format. Choose between:
    - conll: the CoNLL format used by the semafor parser
    - bios: the BIOS format used by the open-sesame parser
    - semeval: the SEMEVAL 2008 XML format
    - fnxml: the standard FrameNet XML format
    ''')
    parser_convert.add_argument('--to', required=True,
                                dest='target_format',
                                choices=['conll', 'bios', 'semeval', 'fnxml'],
                                help='''Target format. Choose between:
    - conll: the CoNLL format used by the semafor parser
    - bios: the BIOS format used by the open-sesame parser
    - semeval: the SEMEVAL 2008 XML format
    - fnxml: the standard FrameNet XML format
    ''')
    parser_convert.add_argument('--with_exemplars',
                                choices=['true', 'false'],
                                default='false',
                                help='Whether or not to use exemplars in '
                                     'splits. Default to false')
    args = parser.parse_args()
    args.func(args)