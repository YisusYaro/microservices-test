from comics.domain.comic import Comic


class Factory(object):
    @staticmethod
    def create(id, title, image, on_sale_date):
        return Comic(id=id, title=title, image=image, on_sale_date=on_sale_date)

    @staticmethod
    def reconstitute(id, title, image, on_sale_date):
        return Comic(id=id, title=title, image=image, on_sale_date=on_sale_date)
