from danceMoves import Move
import datetime
import pickle

if __name__ == '__main__':
    second = datetime.timedelta(seconds=1)
    now = datetime.datetime.now()
    move1 = Move(now + 1 * second, 'jump', 'to the left')
    move2 = Move(now + 2 * second, 'step', 'to the right')
    move3 = Move(now + 3 * second, 'hands', 'on your hips')
    move4 = Move(now + 4 * second, 'knees', 'bring in tight')
    print(f"Original move:\n{move1}")
    # Serialize
    serialized_data = pickle.dumps(move1)
    print(f"Serialized move:\n{serialized_data}")
    print(type(serialized_data))
    # Deserialize
    deserialized_data = pickle.loads(serialized_data)
    print(f"Deserialized move:\n{deserialized_data}")

    # Dump to a file
    with open('move1.pkl', 'wb') as out:
        pickle.dump(move1, out)
    # Read from a file
    with open('move1.pkl', 'rb') as fp:
        move1f = pickle.load(fp)
        print(f"Deserialized move from file:\n{move1f}")

    # Sequence
    dance = [move1, move2, move3, move4]
    with open('dance.pkl', 'wb') as out:
        pickle.dump(dance, out)
