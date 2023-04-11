import logging
from io import BytesIO
from datetime import datetime
from time import sleep

import requests
import pandas as pd

from conf import GROUP_ID, TG_URL, text, SHEET_URL
from mycelery.celery import app


logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('mailing.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

params = {
    'chat_id': GROUP_ID
}


def get_bbs(now=datetime.now().strftime('%d.%m')) -> list:
    res = []
    req = requests.get(SHEET_URL)
    data = req.content
    df = pd.read_csv(BytesIO(data), names=['dt', 'name', 'job'])
    for d in df.itertuples():
        if d.dt == now:
            res.append(d.name)
    return res


@app.task(ignore_result=True)
def congrat():
    bbs = get_bbs()
    for bb in bbs:
        sleep(1)
        params['text'] = text.format(bb)
        res = requests.get(TG_URL, params)
        if res.status_code != 200:
            logger.error(res.text)
