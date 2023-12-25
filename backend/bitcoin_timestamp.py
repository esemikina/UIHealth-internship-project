class BitcoinTimestamp:
    # TODO: (5.2)
    def __init__(self, timestamp: str, price: float):
        self.timestamp = timestamp
        self.price = price

    def to_json(self):
        return {
            'timestamp': self.timestamp,
            'price': self.price
        }
