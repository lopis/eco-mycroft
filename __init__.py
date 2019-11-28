from mycroft import MycroftSkill, intent_file_handler


class Ecosia(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ecosia.intent')
    def handle_ecosia(self, message):
        self.speak_dialog('ecosia')


def create_skill():
    return Ecosia()

