class VocabCard(object):
    def __init__(self, name, definition=None):
        self.name = name
        self.definition = definition

    def set_definition(self, definition):
        if self.definition:
            self.definition = definition

    def get_definition(self):
        if self.has_definition():
            print(self.definition)
            return self.definition

    def has_definition(self):
        return self.definition
    def __str__(self):
        return self.name()

