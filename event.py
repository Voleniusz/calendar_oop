class Event:
    def __init__(self, title, location, start_time, duration, owner, participants,):
        self.title = title
        self.location = location
        self.start_time = start_time
        self.duration = duration
        self.participants = participants
        self.owner = owner

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if len(str(value)):
            self._title = value
        else:
            self._title = "No title"



