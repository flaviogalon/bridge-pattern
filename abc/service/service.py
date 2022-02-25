from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

from data import Buffer, BufferData


@dataclass
class StreamingService(ABC):

    devices: List[Buffer] = field(default_factory=list)

    def add_device(self, device: Buffer) -> None:
        self.devices.append(device)

    def retrieve_buffer_data(self) -> List[BufferData]:
        return [buffer() for buffer in self.devices]

    @abstractmethod
    def start_stream(self) -> str:
        pass

    @abstractmethod
    def fill_buffer(self, stream_reference: str) -> None:
        pass

    @abstractmethod
    def stop_stream(self, stream_reference: str) -> None:
        pass
