from dependency_injector import containers, providers
from app.services.sms_service import SmsService
from app.services.push_service import PushService
from app.services.email_service import EmailService

class ContainerService(containers.DeclarativeContainer):
    sms_service = providers.Singleton( SmsService )
    push_service = providers.Singleton( PushService )
    email_service = providers.Singleton( EmailService )