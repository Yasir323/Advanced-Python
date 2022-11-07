import datetime
import shelve
from danceMoves import Move

if __name__ == '__main__':
    second = datetime.timedelta(seconds=1)
    now = datetime.datetime.now()
    move1 = Move(now + 1 * second, 'jump', 'to the left')
    move2 = Move(now + 2 * second, 'step', 'to the right')
    move3 = Move(now + 3 * second, 'hands', 'on your hips')
    move4 = Move(now + 4 * second, 'knees', 'bring in tight')

    db = shelve.open('dance.db')
    db['1'] = move1
    db['2'] = move2
    db['3'] = move3
    db['4'] = move4
    db.close()

    db = shelve.open('dance.db')
    print(db['1'])
