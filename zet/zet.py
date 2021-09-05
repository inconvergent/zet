import requests
from zet.pinata import Pinata

TZ_BASE_URL = 'https://api.better-call.dev/v1/tokens/mainnet/'
CONTRACT = 'KT1RJ6PbjHpwc3M5rw5s2Nbmefwbuwbdxton'
CONTRACT_TOKEN_URL = f'https://api.better-call.dev/v1/contract/mainnet/{CONTRACT}/tokens'


def _bcd(url):
  r = requests.get(url, params={'sort': 'asc'})
  while True:
    jsn = r.json()
    for o in jsn['transfers']:
      yield o
    if last_id := jsn.get('last_id', None):
      r = requests.get(url, params={'last_id': last_id, 'sort': 'asc'})
    else:
      return

def contract_token_info(token_id):
  r = requests.get(CONTRACT_TOKEN_URL, params={'token_id': token_id})
  return r.json()

def strip_protocol(uri):
  if uri is None:
    return None
  assert uri.startswith('ipfs://'), 'not a valid ipfs uri??'
  return uri[7:]

def get_cids(info):
  return list(filter(bool,
                     map(lambda o: strip_protocol(o.get('uri', None)),
                         info['formats'])))


class Zet:
  def __init__(self, adr):
    self.adr = adr
    self.pinata = Pinata()

  def transfers(self):
    '''all tokens transferred to or from adr(?)'''
    #  TODO: filter by contract?
    return _bcd(TZ_BASE_URL + f'transfers/{self.adr}')

  def cids(self):
    for o in self.transfers():
      token_id = o['token']['token_id']
      info = contract_token_info(token_id)
      assert len(info) == 1, 'len is not 1. why?'
      info = info.pop()
      title = info['name']
      print(f'objkt# {token_id}: {title}')
      for cid in get_cids(info):
        yield cid

  def pin_all(self):
    for o in self.transfers():
      token_id = o['token']['token_id']
      info = contract_token_info(token_id)
      assert len(info) == 1, 'len is not 1. why?'
      info = info.pop()
      title = info['name']
      print(f'objkt# {token_id}: {title}')
      for cid in get_cids(info):
        yield self.pinata.pin(cid, title)


