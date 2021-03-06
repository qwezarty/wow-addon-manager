# -*- coding: utf-8 -*-

"""
    wow_addon_manager.config
    ~~~~~~~~~~~~~~~~~~~~~

    Implements the config from file to object.
    A component that can read apis(or other configs) from json file
        and pass it to main app.

    :author: qwezarty
    :date: 4:47 pm Nov 14 2017
    :email: qwezarty@gmail.com
"""

import os
import json

class Config(dict):
    def __init__(self, root_path, defaults=None):
        dict.__init__(self, defaults or {})
        self.root_path = root_path

    def from_mapping(self, *mapping, **kwargs):
        """add a mapping or mapping list to self"""
        mappings = []
        if len(mapping) == 1:
            if hasattr(mapping[0], 'items'):
                mappings.append(mapping[0].items())
            else: mappings.append(mapping[0])
        elif len(mapping) > 1:
            raise TypeError(
                'expected at most 1 positional argument, got %d' % len(mapping)
            )
        mappings.append(kwargs.items())
        for mapping in mappings:
            for (key, value) in mapping:
                self[key] = value
        return True

    def from_rel_json(self, file_name):
        """load a relative json file and add them to self"""
        abs_path = os.path.join(self.root_path, file_name)
        self.from_abs_json(abs_path)

    def from_abs_json(self, abs_path):
        """load a absolute json file and add them to self"""
        try:
            with open(abs_path, encoding='utf-8') as json_file:
                obj = json.loads(json_file.read())
        except IOError as error:
            error.strerror = 'unable to load json file, (%s)' % error.strerror
            raise
        return self.from_mapping(obj)



if __name__ == "__main__":
    # foo = Config()
    #foo.from_mapping(
    #    SECRET_KEY = 'devkey',
    #    TEST_KEY = 'foo'
    #    )
    # foo.from_mapping({
    #     'SECRET_KEY': 'devkey',
    #     'TEST_KEY': 'foo'
    #     })
    pass
