import subprocess


def open_app():
    subprocess.call(
        ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Github Desktop.app"]
    )


open_app()
