iter('Sarah')                        # String
iter(['Sarah', 'Roark'])             # List
iter(('Sarah', 'Roark'))             # Tuple
iter({'Sarah': 26, 'Roark': 25}      # Dict
# Where iteration doesn't work
#iter(30)                                 # Integer
#TypeError: 'int' object is not iterable
#iter(22.6)                               # Float
#TypeError: 'float' object is not iterable

l = ['Sarah', 'Roark']
itr = iter(l)
itr
next(itr)
#'Sarah'
next(itr)
#'Roark'
# when we create an iterator, it doesn’t generate all the items it can yield just then.
# It waits until we ask for them with next(). Items are not created until they are requested.