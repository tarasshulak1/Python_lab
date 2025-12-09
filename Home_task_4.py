import datetime

OUTPUT_FILE = "news_feed.txt"


class Publication:
    """Base class for all publication types."""

    def __init__(self, text):
        self.text = text

    def format(self):
        """Override in child classes."""
        raise NotImplementedError("format() must be implemented in subclasses")

    def publish(self):
        """Writes formatted record to file."""
        with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
            file.write(self.format() + "\n\n")
        print("Record saved.")


class News(Publication):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city
        self.publish_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def format(self):
        return (
            "News -----------------------------\n"
            f"{self.text}\n"
            f"{self.city}, {self.publish_date}"
        )


class PrivateAd(Publication):
    def __init__(self, text, expiration_date):
        super().__init__(text)
        self.expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d")
        self.days_left = (self.expiration_date - datetime.datetime.now()).days

    def format(self):
        return (
            "Private Ad -----------------------\n"
            f"{self.text}\n"
            f"Expires: {self.expiration_date.date()}, "
            f"Days left: {self.days_left}"
        )


class WeatherForecast(Publication):
    """
    Unique custom publication type:
    Inputs: city, temperature
    Adds: mood-based weather interpretation rule
    """

    def __init__(self, city, temperature):
        super().__init__(text=None)
        self.city = city
        self.temperature = temperature
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")

    def _interpret(self):
        if self.temperature > 25:
            return "Hot and sunny"
        elif 10 <= self.temperature <= 25:
            return "Mild and pleasant"
        else:
            return "Cold weather ahead"

    def format(self):
        return (
            "Weather Forecast -----------------\n"
            f"City: {self.city}\n"
            f"Temperature: {self.temperature}°C\n"
            f"Forecast: {self._interpret()}\n"
            f"Date: {self.date}"
        )


class PublicationFactory:
    """Handles creation of publications based on user selection."""

    @staticmethod
    def create_publication():
        print("\nChoose publication type:")
        print("1 – News")
        print("2 – Private Ad")
        print("3 – Weather Forecast (unique type)")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            text = input("Enter news text: ")
            city = input("Enter city: ")
            return News(text, city)

        elif choice == "2":
            text = input("Enter ad text: ")
            expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
            return PrivateAd(text, expiration_date)

        elif choice == "3":
            city = input("Enter city: ")
            temp = float(input("Enter temperature (°C): "))
            return WeatherForecast(city, temp)

        else:
            print("Invalid option.")
            return None


def main():
    print("=== USER GENERATED NEWS FEED TOOL ===")
    while True:
        record = PublicationFactory.create_publication()
        if record:
            record.publish()

        again = input("Add another record? (y/n): ").lower()
        if again != "y":
            print("Program finished. File saved:", OUTPUT_FILE)
            break


if __name__ == "__main__":
    main()
