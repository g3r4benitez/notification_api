from sqlmodel import Session, select
from app.models.user import Channel
from app.core.database import engine

class ChannelService:
    def __init__(self, session: Session):
        self.session = session

    def create_channel(self, channel: Channel) -> Channel:
        self.session.add(channel)
        self.session.commit()
        self.session.refresh(channel)
        return channel

    def get(self, _id):
        obj = self.session.get(Channel, _id)
        return obj

    def get_all(self):
        statement = select(Channel)
        results = self.session.exec(statement)
        return results.all()


session = Session(engine)
channel_service = ChannelService(session)

