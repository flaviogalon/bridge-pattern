import logging

from device import Webcam, DSLRCamera
from service.youtube import YoutubeStreamingService
from service import TwitchStreamingService


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    webcam = Webcam()
    twitch_service = TwitchStreamingService(webcam)

    twitch_service_ref = twitch_service.start_stream()
    twitch_service.fill_buffer(twitch_service_ref)
    twitch_service.stop_stream(twitch_service_ref)

    dslr_camera = DSLRCamera()
    youtube_service = YoutubeStreamingService(dslr_camera)

    youtube_service_ref = youtube_service.start_stream()
    youtube_service.fill_buffer(youtube_service_ref)
    youtube_service.stop_stream(youtube_service_ref)


if __name__ == "__main__":
    main()
