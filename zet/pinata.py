from json import load
from pprint import pprint as pp
import requests

#  https://docs.pinata.cloud/api-pinning/pin-by-hash


BASE_URL = 'https://api.pinata.cloud'
PIN_BY_HASH = f'{BASE_URL}/pinning/pinByHash'


def pin_request_body(cid, name):
  #  TODO: skip name if missing, set creator as kv
  if not name:
    name = 'x'
  name = name.strip()
  return {
    'pinataMetadata': {
      'name': name,
      'keyvalues': {
        'zetv': 0,
        'title': name
      }
    },
    'hashToPin': cid
  }

class Pinata:
  def __init__(self):
    with open('/home/anders/.zet.json') as f:
      jsn = load(f)
    self.auth = jsn
    self.headers = {'Authorization':  f'Bearer {jsn["jwt"]}'}

  def pin(self, cid, name):
    pp(pin_request_body(cid, name))
    r = requests.post(PIN_BY_HASH,
                      json=pin_request_body(cid, name),
                      headers=self.headers)
    return r.json()

