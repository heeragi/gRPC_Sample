from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloReply(_message.Message):
    __slots__ = ["result", "status_code"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    result: str
    status_code: int
    def __init__(self, result: _Optional[str] = ..., status_code: _Optional[int] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ["data", "status_code"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    data: str
    status_code: int
    def __init__(self, data: _Optional[str] = ..., status_code: _Optional[int] = ...) -> None: ...
