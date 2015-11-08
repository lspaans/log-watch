#!/usr/bin/env python
# encoding: UTF-8
###############################################################################
#
#   Module:     log-watch.py
#   Author:     L. Spaans
#   Date:       8 November 2015
#   Purpose:    
#
#   Version:    0.1
#   Date/Time:  2015-11-08 19:48:00
#
#   Amendment history:
#   20151108    LS      Initial version
#
###############################################################################

"""<description placeholder>"""

__author__ = "Léon Spaans"

import ConfigParser

import argparse
import datetime
import json
import math
import operator
import os
import re
import sys
import time
import urllib2

DEF_SCRIPT_NAME = os.path.basename(sys.argv[0])
DEF_SCRIPT_NAME_NO_EXT = os.path.splitext(DEF_SCRIPT_NAME)[0]
DEF_SCRIPT_VERSION = 0.1

DEF_PATH_ROOT = os.environ.get('ROOT', os.path.join(
    '/opt', DEF_SCRIPT_NAME_NO_EXT
))
print(DEF_PATH_ROOT)
DEF_PATH_CFG = os.environ.get('CFG', os.path.join(DEF_PATH_ROOT, 'etc'))
DEF_PATH_DATA = os.environ.get('DATA', os.path.join(DEF_PATH_ROOT, 'var'))

DEF_FILE_CONFIG = os.path.join(DEF_PATH_CFG, '.'.join(
    [DEF_SCRIPT_NAME_NO_EXT,'conf'])
)

DEF_CONFIG = {
}


def get_arguments(
    script_name=DEF_SCRIPT_NAME,
    script_version=DEF_SCRIPT_VERSION
):
    """
    Parses the command-line parameters.

    Arguments:
        script_name    - str(): name of this script
        script_version - str(): version of this script

    Returns argparse.ArgumentParser() with parsed command-line.
    """
    parser = argparse.ArgumentParser(
        prog=script_name,
        description='<description placeholder>'
    )
    parser.add_argument(
        '-c', '--config-file',
        metavar='FILE', nargs='?', default=DEF_FILE_CONFIG,
        dest='file_cfg', help='a non-default ' +
            '(i.e. {0}) configuration file'.format(DEF_FILE_CONFIG)
    )
    parser.add_argument(
        '-v', '--version', action='version',
        version='%(prog)s v{0}'.format(script_version)
    )
    arguments = parser.parse_args()
    return(arguments)


def get_config(arguments, default_config=DEF_CONFIG):
    """
    Parses script configuration file.

    Arguments:
        arguments      - argparse.ArgumentParser(): arguments parsed by
                         get_arguments()
        default_config - dict(): default configuration values

    Returns ConfigParser.RawConfigParser() with parsed configuration values.
    """
    config = ConfigParser.RawConfigParser()
    for section in default_config:
        config.add_section(section)
        for option in default_config[section]:
            config.set(section, option, default_config[section][option])
    files_parsed = config.read(os.path.expandvars(arguments.file_cfg))
    if len(files_parsed) < 1:
        show_result(
            '* WARNING: cannot parse configuration file "{0}"\n'.format(
                arguments.file_cfg
        ))
    return(config)


def show_result(result, flush=False):
    """
    Generic function for screen output (STDOUT), optionally with forced flush.

    Arguments:
        result - str(): printable string
    """
    sys.stdout.write(result)
    if flush is True:
        sys.stdout.flush()


def main(config):
    """
    The script's main()-function which is automatically executed when the
    script is started natively.

    Arguments:
        config - ConfigParser.RawConfigParser(): configuration
    """
    pass

if __name__ == '__main__':
    main(get_config(get_arguments()))
