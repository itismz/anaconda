
# Copyright (C) 2012-2016 - Oscar Campos <oscar.campos@member.fsf.org>
# This program is Free Software see LICENSE file for details

import sys
sys.path.insert(0, '../anaconda_server')
sys.path.append('../anaconda_lib')

import jedi

from commands.autocomplete import AutoComplete
from handlers.jedi_handler import JediHandler


class TestAutoCompletion(object):
    """Auto completion test suite
    """

    def test_autocomplete_command(self):
        AutoComplete(self._check, 0, jedi.Script('import os; os.'))

    def test_autocomplete_handler(self):
        data = {'source': 'import os; os.', 'line': 1, 'offset': 14}
        handler = JediHandler('autocomplete', data, 0, 0, self._check)
        handler.run()

    def _check(self, kwrgs):
        assert kwrgs['success'] is True
        assert len(kwrgs['completions']) > 0
        assert kwrgs['completions'][0] == ('abort\tfunction', 'abort')
        assert kwrgs['uid'] == 0
