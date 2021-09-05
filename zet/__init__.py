"""fn

Description:
  `zet` is a mess

  use `fn` to generate a file name.
  use `fn -r [dir]` to get the most recent file (in dir).
  more options listed below.


Usage:
  zet hen list <adr>


Options:
  --hen-list  list all tokesn
  -h --help   show this screen.
  --version   show version.

"""


from sys import exit as pexit
from sys import stderr
from traceback import print_exc
from pprint import pprint as pp

from docopt import docopt

from zet.zet import Zet


#  def handle_path_args(args):
#    path_style = 'rel' # relative path style: dir/file.ext
#    if args['-a']: # file name only: file.ext
#      path_style = 'file'
#    elif args['-A']: # absolute path style: /a/b/file.ext
#      path_style = 'abs'
#    return overlay(args, path_style=path_style)

def handle_args(fn, args):
  if args['-l']:
    return fn.lst(d=args['DIR'],
                  path_style=args['path_style'],
                  ext=not args['-f'])
  if args['-L']:
    return fn.lst_recent(d=args['DIR'],
                         path_style=args['path_style'],
                         ext=not args['-f'])
  if args['-r']:
    return fn.recent(d=args['DIR'],
                     path_style=args['path_style'],
                     ext=not args['-f'])
  if args['-s']:
    return fn.recent_prochash(d=args['DIR'])
  if args['-p']:
    return [fn.get_pid_sha()]
  if args['-g']:
    return [fn.get_sha()]
  return [fn.name(milli=args['-m'])]


def main():
  args = docopt(__doc__, version='zet 0.0.1')
  print(args)

  #  try:

  zet = Zet(args['<adr>'])
  #  for o in zet.transfers():
  #    pp(o)
  for o in zet.adr_tokens():
    pp(o)


    #  print(zet)
    #  res = filter(bool, handle_args(fn, args))
    #  for r in head_tail(res, head=args['-N'], tail=args['-n'],
    #                     reverse=args['-i']):
    #    print(r)
  #  except ValueError as e:
  #    print('err: ' + str(e), file=stderr)
  #    pexit(1)
  #  except Exception as e:
  #    print_exc(file=stderr)
  #    pexit(2)


if __name__ == '__main__':
  main()

