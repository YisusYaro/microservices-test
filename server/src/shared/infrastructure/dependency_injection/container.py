from dependency_injector import containers, providers
from shared.infrastructure.tokens.token_service import TokenService

from ..command_bus.command_bus import CommandBus
from ..event_bus.event_bus import EventBus
from ..query_bus.query_bus import QueryBus
from ..filter.filter import Filter


class Container(containers.DeclarativeContainer):

    CommandBus = providers.Factory(
        CommandBus,
    )

    QueryBus = providers.Factory(
        QueryBus,
    )

    EventBus = providers.Factory(
        EventBus,
    )

    TokenService = providers.Factory(
        TokenService
    )

    Filter = providers.Factory(
        Filter
    )
