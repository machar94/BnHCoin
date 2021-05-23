import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    os.remove(os.path.join(os.path.dirname(__file__), '../bnhcoin/site.db'))
    print('Removing existing database...')
except:
    pass

from bnhcoin import db
db.create_all()
print('Created database site.db')
