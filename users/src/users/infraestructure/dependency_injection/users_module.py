from dependency_injector import providers


def setCommands(container):
    from users.application.commands.register_user_handler import RegisterUserHandler
    container.RegisterUserCommand = providers.Factory(
        RegisterUserHandler,
    )


def setQueries(container):
    from users.application.queries.user_login_handler import UserLoginHandler
    container.UserLoginQuery = providers.Factory(
        UserLoginHandler,
    )


def setEvents(container):
    from users.application.events.user_registered_handler import UserRegisteredHandler
    container.UserRegisteredEvent = providers.Factory(
        UserRegisteredHandler,
    )


def setApplication(container):
    setCommands(container)
    setQueries(container)
    setEvents(container)


def setInfraestructure(container):
    from users.infraestructure.repositories.user_respository import UserRepository
    container.UserRepository = providers.Singleton(
        UserRepository,
    )

    from users.infraestructure.tokens.user_token_service import UserTokenService
    container.UserTokenService = providers.Factory(
        UserTokenService,
    )


def setUsersModule(container):
    setInfraestructure(container)
    setApplication(container)

