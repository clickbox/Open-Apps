import subprocess


def open_app():
    subprocess.call(
        ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Slack.app"]
    )


open_app()
