class Book:
    def __init__(self, cin: str, publication_type: str, quantity_sold: int):
        self.cin = cin
        self.publication_type = publication_type
        self.quantity_sold = quantity_sold
        self.is_bestseller = False


class BestSeller(Book):
    def __init__(self, cin: str, publication_type: str, quantity_sold: int):
        super().__init__(cin, publication_type, quantity_sold)
        self.is_bestseller = True
