"""fn

Description:
  `zet` is a mess

  use `fn` to generate a file name.
  use `fn -r [dir]` to get the most recent file (in dir).
  more options listed below.


Usage:
  zet hen list <adr>


Options:
  -h --help   show this screen.
  --version   show version.

"""


from sys import exit as pexit
from sys import stderr
from traceback import print_exc
from pprint import pprint as pp

from docopt import docopt

from zet.zet import Zet


def main():
  args = docopt(__doc__, version='zet 0.0.1')
  zet = Zet(args['<adr>'])

  try:
    for o in zet.pin_all():
      pp(o)
  except ValueError as e:
    print('err: ' + str(e), file=stderr)
    pexit(1)
  except Exception as e:
    print_exc(file=stderr)
    pexit(2)


if __name__ == '__main__':
  main()

