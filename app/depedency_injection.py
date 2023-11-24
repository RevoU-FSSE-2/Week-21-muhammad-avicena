from infrastructure.auth.modules import AuthModule
from infrastructure.user.modules import UserModule
from injector import Injector

injector = Injector([
    UserModule,
    AuthModule
])