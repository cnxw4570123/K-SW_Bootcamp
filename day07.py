class PrettyMixin:
    def dump(self):
        import pprint
        pprint.pprint(vars(self))

    def time_print(self):
        import datetime
        print(datetime.date.today())


class Thing(PrettyMixin):
    pass


t = Thing()
t.age = 27
t.name = 'gm'
t.gender = 'male'
t.dump()
t.time_print()

