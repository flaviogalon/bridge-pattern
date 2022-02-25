from typing import Protocol

from data import BufferData


class StreamingDevice(Protocol):
    def get_buffer_data(self) -> BufferData:
        ...
