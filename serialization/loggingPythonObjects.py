class Player:

    def __init__(self, _id, team, name):
        self._id = _id
        self.team = team
        self.name = name

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}({self._id!r}, {self.team!r}, {self.name!r})"


if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.INFO, filename='game.log')
    p1 = Player(1, 'India', {'Virat', 'Kohli'})
    logging.info('p1 is %r', p1)
