import sys
import utime
from . import utils

import log

_new_layout = None
_current_layout = None

def change(layout):
    global _new_layout

    log.debug(__name__, "Changing layout to %s", layout)
    _new_layout = layout

    yield _current_layout.throw(StopIteration())

def set_main(main_layout):
    global _new_layout
    global _current_layout

    _current_layout = main_layout()
    while True:
        try:
            _current_layout = yield from _current_layout
        except Exception as e:
            sys.print_exception(e)
            utime.sleep(1)  # Don't produce wall of exceptions
            # if _current_layout == main_layout:
            #    # Main layout thrown exception, what to do?
            #    sys.exit()
            _current_layout = main_layout()
            continue

        if _new_layout != None:
            log.info(__name__, "Switching to new layout %s", _new_layout)
            _current_layout = _new_layout
            _new_layout = None

        elif type(_current_layout) != utils.type_gen:
            log.info(__name__, "Switching to main layout %s", main_layout)
            _current_layout = main_layout()
        else:
            log.info(__name__, "Switching to proposed layout %s", _current_layout)
