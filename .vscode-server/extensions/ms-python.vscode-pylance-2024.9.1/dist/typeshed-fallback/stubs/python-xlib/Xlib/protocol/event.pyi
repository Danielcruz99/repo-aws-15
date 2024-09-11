from typing import Final
from typing_extensions import TypeAlias

from Xlib.protocol import rq

class AnyEvent(rq.Event): ...
class KeyButtonPointer(rq.Event): ...
class KeyPress(KeyButtonPointer): ...
class KeyRelease(KeyButtonPointer): ...
class ButtonPress(KeyButtonPointer): ...
class ButtonRelease(KeyButtonPointer): ...
class MotionNotify(KeyButtonPointer): ...
class EnterLeave(rq.Event): ...
class EnterNotify(EnterLeave): ...
class LeaveNotify(EnterLeave): ...
class Focus(rq.Event): ...
class FocusIn(Focus): ...
class FocusOut(Focus): ...
class Expose(rq.Event): ...
class GraphicsExpose(rq.Event): ...
class NoExpose(rq.Event): ...
class VisibilityNotify(rq.Event): ...
class CreateNotify(rq.Event): ...
class DestroyNotify(rq.Event): ...
class UnmapNotify(rq.Event): ...
class MapNotify(rq.Event): ...
class MapRequest(rq.Event): ...
class ReparentNotify(rq.Event): ...
class ConfigureNotify(rq.Event): ...
class ConfigureRequest(rq.Event): ...
class GravityNotify(rq.Event): ...
class ResizeRequest(rq.Event): ...
class Circulate(rq.Event): ...
class CirculateNotify(Circulate): ...
class CirculateRequest(Circulate): ...
class PropertyNotify(rq.Event): ...
class SelectionClear(rq.Event): ...
class SelectionRequest(rq.Event): ...
class SelectionNotify(rq.Event): ...
class ColormapNotify(rq.Event): ...
class MappingNotify(rq.Event): ...
class ClientMessage(rq.Event): ...
class KeymapNotify(rq.Event): ...

_EventClass: TypeAlias = dict[
    int,
    type[
        KeyPress
        | KeyRelease
        | ButtonPress
        | ButtonRelease
        | MotionNotify
        | EnterNotify
        | LeaveNotify
        | FocusIn
        | FocusOut
        | KeymapNotify
        | Expose
        | GraphicsExpose
        | NoExpose
        | VisibilityNotify
        | CreateNotify
        | DestroyNotify
        | UnmapNotify
        | MapNotify
        | MapRequest
        | ReparentNotify
        | ConfigureNotify
        | ConfigureRequest
        | GravityNotify
        | ResizeRequest
        | CirculateNotify
        | CirculateRequest
        | PropertyNotify
        | SelectionClear
        | SelectionRequest
        | SelectionNotify
        | ColormapNotify
        | ClientMessage
        | MappingNotify
    ],
]
event_class: Final[_EventClass]
