import models


class LambdaFunction:

    @staticmethod
    def search_by_price_contain():
        return lambda k: models.Car.price.contains(k)


# search_by_price_contain = lambda keyword: models.Car.price.contains(keyword)
# search_by_name_contain = lambda keyword: models.Car.name.contains(keyword)
