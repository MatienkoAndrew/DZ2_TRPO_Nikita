from src.TableDataGateway.RestaurantGateway import RestaurantGateway


class Restaurant:
    def __init__(self):
        pass

    # записываем ресторан в БД
    def createRestaurant(self, metro, kitchen, avg_bill):
        restaurant = RestaurantGateway()
        restaurant.metro = metro
        restaurant.kitchen = kitchen
        restaurant.avg_bill = avg_bill
        restaurant.Insert()
        pass

    # считываем все рестораны из БД
    def getAll(self):
        return RestaurantGateway().getAll()

    # считываем последний введенный ресторан
    def getLastRestaurant(self):
        restaurant = RestaurantGateway()
        lastId = restaurant.getLastId()

        restaurantInfo = restaurant.getLastRestaurant(lastId)
        return restaurantInfo
