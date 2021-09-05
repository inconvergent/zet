import requests
from itertools import chain

BASE_URL = 'https://api.better-call.dev/v1/tokens/mainnet/'


def bcd_call(url):
  r = requests.get(url)
  print(r.url)
  while True:
    jsn = r.json()
    for o in jsn['transfers']:
      yield o
    if last_id := jsn.get('last_id', None):
      r = requests.get(url, params={'last_id': last_id})
    else:
      return

class Zet:
  def __init__(self, adr):
    self.adr = adr

  def transfers(self):
    return bcd_call(BASE_URL + f'transfers/{self.adr}')



  # def __enter__(self):
  #   return self

  # def __exit__(self, t, value, traceback):
  #   return False



