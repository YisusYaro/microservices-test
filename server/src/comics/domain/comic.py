from shared.domain.aggregate_root import AggregateRoot


class Comic(AggregateRoot):
    def __init__(self, id, title, image, on_sale_date):
        super().__init__()
        self.__id = id
        self.__title = title
        self.__image = image
        self.__on_sale_date = on_sale_date

    def to_properties(self):
        return dict(
            id=self.__id,
            title=self.__title,
            image=self.__image,
            on_sale_date=self.__on_sale_date,
        )
