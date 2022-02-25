import logging

from device.dslr_camera import get_dslr_buffer_data
from device.webcam import get_webcam_buffer_data
from service import TwitchStreamingService
from service.youtube import YoutubeStreamingService


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    twitch_service = TwitchStreamingService(get_webcam_buffer_data)

    twitch_service_ref = twitch_service.start_stream()
    twitch_service.fill_buffer(twitch_service_ref)
    twitch_service.stop_stream(twitch_service_ref)

    youtube_service = YoutubeStreamingService(get_dslr_buffer_data)

    youtube_service_ref = youtube_service.start_stream()
    youtube_service.fill_buffer(youtube_service_ref)
    youtube_service.stop_stream(youtube_service_ref)


if __name__ == "__main__":
    main()
