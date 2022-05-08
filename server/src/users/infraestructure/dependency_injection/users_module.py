from dependency_injector import providers


def set_commands(container):
    from users.application.commands.register_user_handler import RegisterUserHandler
    container.RegisterUserCommand = providers.Factory(
        RegisterUserHandler,
    )


def set_queries(container):
    from users.application.queries.user_login_handler import UserLoginHandler
    container.UserLoginQuery = providers.Factory(
        UserLoginHandler,
    )

    from users.application.queries.get_user_handler import GetUserHandler
    container.GetUserQuery = providers.Factory(
        GetUserHandler
    )


def set_events(container):
    from users.application.events.user_registered_handler import UserRegisteredHandler
    container.UserRegisteredEvent = providers.Factory(
        UserRegisteredHandler,
    )


def set_application(container):
    set_commands(container)
    set_queries(container)
    set_events(container)


def set_infraestructure(container):
    from users.infraestructure.repositories.user_respository import UserRepository
    container.UserRepository = providers.Singleton(
        UserRepository,
    )

    from users.infraestructure.tokens.user_token_service import UserTokenService
    container.UserTokenService = providers.Factory(
        UserTokenService,
    )


def set_interface(container):
    from users.interface.middlewares.get_user_approver import GetUserApprover
    container.GetUserApprover = providers.Factory(
        GetUserApprover,
    )


def set_users_module(container):
    set_infraestructure(container)
    set_interface(container)
    set_application(container)
