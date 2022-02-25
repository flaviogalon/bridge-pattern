import logging

from device import Webcam
from service import TwitchStreamingService


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    device = Webcam()
    service = TwitchStreamingService(device)

    reference = service.start_stream()
    service.fill_buffer(reference)
    service.stop_stream(reference)


if __name__ == "__main__":
    main()
