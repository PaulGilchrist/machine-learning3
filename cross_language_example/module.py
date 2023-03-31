import sys
# input_data = sys.stdin.read()
args = sys.argv[1:]
sys.stdout.write(f'Hello {args[0]} from Python module')
sys.stdout.flush() # Data is not sent until flushed allowing multiple lines to be returned at once
exit(0)