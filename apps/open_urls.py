import webbrowser



url = [
    'https://www.icloud.com/#mail',
    'https://mail.google.com/mail/u/0/#inbox',
    'https://app.zeplin.io/project/5c82cb40af86007b4377b013',
    'https://calendar.google.com/calendar/r?tab=mc',
    'https://stockx-services.atlassian.net/secure/RapidBoard.jspa?rapidView=71&projectKey=WEB&selectedIssue=BS-19&sprint=553',
    'https://stockx-services.atlassian.net/secure/RapidBoard.jspa?rapidView=71&projectKey=WEB&sprint=557',
    'https://www.youtube.com/',
    'https://github.com/stockx/iron'
]


def open_url(urls):
    for u in urls:
        webbrowser.open_new_tab(u)


open_url(url)
