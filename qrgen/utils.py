#!.env/bin/python
# -*- coding: utf-8 -*-
"""
Utils
"""

from os import path
import json


def from_json(file_src, json_filename):
    "Get configuration"
    json_path = get_path(file_src, json_filename)
    with open(json_path, encoding='utf-8') as json_file:
        return json.loads(json_file.read())


def get_path(file_src, file_path, filename=None):
    "Get full path"
    project_path = path.dirname(path.realpath(file_src))
    real_path = path.realpath(path.join(project_path, file_path))
    if filename:
        real_path = path.join(real_path, filename)
    return real_path
