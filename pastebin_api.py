

from requests import request


def post_new_paste(title, body_text, expiration='N', listed=True):
    """
    Posts a new paste to PasteBin
    :param title: Paste title
    :param body_text: Paste body text
    :param expiration: Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
    :param listed: Whether paste is publicly listed (True) or not (False)
    :returns: URL of new paste, if successful. Otherwise None.
    """
    print('Posting a new paste to PasteBin...', ends='')
    
    p = {
        'api_dev_key': 'tlgUMLkNyc405flks_VKoFttR91Qa8jv',
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_past_name': title,
        'api_paste_private': 0 if listed else 1,
        'api_paste_expire_date': expiration,
    }

    paste_url = 'https://pastebin.com/api/api_post.php'
    resp_msg = request.post(paste_url, data=p)

    if resp_msg.status_code == requests.cdoes.ok:
        print('success')
        return resp_msg.json()
    else:
        print('failure')
        print(f'Status code: {resp_msg.status_code}, Error reason: {resp_msg.reason}')
        return None
