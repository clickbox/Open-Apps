import subprocess


def open_app():
    subprocess.call(
        ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Webstorm.app"]
    )


open_app()
