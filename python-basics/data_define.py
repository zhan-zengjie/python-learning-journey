class Record:
    def __init__(self, date, product, quantity, price, region):
        self.date = date
        self.product = product
        self.quantity = int(quantity)
        self.price = int(price)
        self.region = region

    def amount(self):
        return self.quantity * self.price


if __name__ == "__main__":
    r = Record("2026-01-01", "手机", "3", "2999", "广州")
    print(r.product)
    print(r.quantity)
    print(r.amount())