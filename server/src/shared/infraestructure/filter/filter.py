class Filter(object):
    def __init__(self):
        self.__options = {"=": self.__is_equal, "<": self.__is_minor,
                          ">": self.__is_greater, "<>": self.__is_different}

    def filter_by_criteria(self, filters, aggregate_root):
        for query_filter in filters:
            try:
                return self.__options[query_filter["operator"]](field=query_filter["field"], value=query_filter["value"], aggregate_root=aggregate_root)
            except KeyError:
                return False

    def __is_equal(self, field, value, aggregate_root):
        return aggregate_root.to_properties()[field] == value

    def __is_minor(self, field, value, aggregate_root):
        return aggregate_root.to_properties()[field] < value

    def __is_greater(self, field, value, aggregate_root):
        return aggregate_root.to_properties()[field] > value

    def __is_different(self, field, value, aggregate_root):
        return aggregate_root.to_properties()[field] != value
