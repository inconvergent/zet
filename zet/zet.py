import requests

TZ_BASE_URL = 'https://api.better-call.dev/v1/tokens/mainnet/'
CONTRACT = 'KT1RJ6PbjHpwc3M5rw5s2Nbmefwbuwbdxton'
CONTRACT_TOKEN_URL = f'https://api.better-call.dev/v1/contract/mainnet/{CONTRACT}/tokens'


def _bcd(url):
  r = requests.get(url)
  while True:
    jsn = r.json()
    for o in jsn['transfers']:
      yield o
    if last_id := jsn.get('last_id', None):
      r = requests.get(url, params={'last_id': last_id})
    else:
      return

def contract_token_info(token_id):
  r = requests.get(CONTRACT_TOKEN_URL, params={'token_id': token_id})
  return r.json()

def get_cids(info):
  #  res = [
  #    info.get('thumbnail_uri'),
  #  ] thumbnail is the hic logo
  res = []
  #  TODO: assert artifact_uri is in formats
  res.extend(map(lambda o: o.get('uri', None), info['formats']))
  return list(filter(bool, res))


class Zet:
  def __init__(self, adr):
    self.adr = adr

  def transfers(self):
    #  TODO: filter by contract?
    return _bcd(TZ_BASE_URL + f'transfers/{self.adr}')

  def adr_tokens(self):
    for o in self.transfers():
      token_id = o['token']['token_id']
      info = contract_token_info(token_id)
      assert len(info) == 1, 'len is not 1. why?'
      info = info.pop()
      title = info['name']
      print(f'objkt# {token_id}: {title}')
      for url in get_cids(info):
        yield url

