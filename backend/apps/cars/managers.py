from django.db.models import Manager


class CarManager(Manager):
    def get_by_price_gt(self, price=4000):
        return self.filter(price__gt=price)
