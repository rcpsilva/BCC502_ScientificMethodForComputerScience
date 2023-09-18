
    def method(self, action):
        """
            For a given action, return a percept
        """
        averageConsumption = [30, 80, 100, 80, 10, 2, 1]
        day = self.clock % 7

        self.number += action["to-buy"]
        self.number = min(self.number, self.max)
        demand = (averageConsumption[day] +
                        np.random.randn() * averageConsumption[day] / 10)
        self.number -= demand
        if (self.number < self.min):
            self.number = self.min

        self.price = 1 + (0.0005 * self.clock + np.random.randn()/10)
        self.price = abs(self.price)
        self.clock += 1

        return {
            "number": self.number,
            "number": self.number,
            "max": self.max,
            "min": self.min,
            "price": self.price,
        }