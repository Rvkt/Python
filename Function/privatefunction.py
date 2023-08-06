class SeeMee:
    def youcanseeme(self):
        return 'you can see me'

    def __youcannotseeme(self):
        return 'you cannot see me'


Check = SeeMee()
print(Check.youcanseeme())
print(Check._SeeMee__youcannotseeme())
