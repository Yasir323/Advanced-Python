import datetime
import pickle
import socket
from danceMoves import Move

if __name__ == '__main__':
    second = datetime.timedelta(seconds=1)
    now = datetime.datetime.now()
    move1 = Move(now + 1 * second, 'jump', 'to the left')
    move2 = Move(now + 2 * second, 'step', 'to the right')
    move3 = Move(now + 3 * second, 'hands', 'on your hips')
    move4 = Move(now + 4 * second, 'knees', 'bring in tight')

    ws, rs = socket.socketpair()
    w, r = ws.makefile('wb'), rs.makefile('rb')

    # Serialize
    pickle.dump(move1, w)
    pickle.dump(move2, w)
    pickle.dump(move3, w)
    pickle.dump(move4, w)
    w.flush()

    # De-serialize
    for _ in range(4):
        move = pickle.load(r)
        print(f"{move.limb} {move.what}")
