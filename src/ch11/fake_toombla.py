from src.ch11.tombla import Tombla


class FakeTombla(Tombla):

    def pick(self):
        return 13

    def load(self, iter):
        pass


fake = FakeTombla()