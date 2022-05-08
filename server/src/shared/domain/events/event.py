import ulid
import datetime


class Event(object):
    def __init__(
        self,
        aggregate_id,
        event_name,
        event_id=ulid.new(),
        ocurred_on=datetime.datetime.now()
    ):
        self.aggregate_id = aggregate_id
        self.event_name = event_name
        self.event_id = event_id
        self.ocurred_on = ocurred_on
