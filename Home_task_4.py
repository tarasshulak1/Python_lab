import datetime
import os

OUTPUT_FILE = "news_feed.txt"
DEFAULT_INPUT_FOLDER = "input/"


# ==========================================================
#                     BASE PUBLICATION
# ==========================================================
class Publication:
    def __init__(self, text):
        self.text = text

    def format(self):
        raise NotImplementedError

    def publish(self):
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(self.format() + "\n\n")
        print("✔ Record saved.")


# ==========================================================
#                          NEWS
# ==========================================================
class News(Publication):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def format(self):
        return (f"News -----------------------------\n"
                f"{self.text}\n"
                f"{self.city}, {self.date}")


# ==========================================================
#                      PRIVATE AD
# ==========================================================
class PrivateAd(Publication):
    def __init__(self, text, expiration_date):
        super().__init__(text)
        self.expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d")
        self.days_left = (self.expiration_date - datetime.datetime.now()).days

    def format(self):
        return (f"Private Ad -----------------------\n"
                f"{self.text}\n"
                f"Expires: {self.expiration_date.date()}, "
                f"Days left: {self.days_left}")


# ==========================================================
#                   CUSTOM: WEATHER FORECAST
# ==========================================================
class WeatherForecast(Publication):
    def __init__(self, city, temp):
        super().__init__(text=None)
        self.city = city
        self.temp = float(temp)
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")

    def _interpret(self):
        if self.temp > 25:
            return "Hot and sunny"
        if 10 <= self.temp <= 25:
            return "Mild and pleasant"
        return "Cold weather ahead"

    def format(self):
        return (f"Weather Forecast -----------------\n"
                f"City: {self.city}\n"
                f"Temperature: {self.temp}°C\n"
                f"Forecast: {self._interpret()}\n"
                f"Date: {self.date}")


# ==========================================================
#                   FACTORY FOR PUBLICATIONS
# ==========================================================
class PublicationFactory:
    @staticmethod
    def create_manual():
        print("\nChoose publication type:")
        print("1 – News")
        print("2 – Private Ad")
        print("3 – Weather Forecast")

        option = input("Enter choice (1/2/3): ")

        if option == "1":
            return News(input("Text: "), input("City: "))
        elif option == "2":
            return PrivateAd(input("Text: "), input("Expiration date YYYY-MM-DD: "))
        elif option == "3":
            return WeatherForecast(input("City: "), input("Temperature: "))
        else:
            print("Invalid choice.")
            return None

    @staticmethod
    def create_from_file(tokens):
        """Tokens is the list split by '|'."""
        record_type = tokens[0].strip().lower()

        if record_type == "news":
            return News(tokens[1].strip(), tokens[2].strip())

        elif record_type == "ad":
            return PrivateAd(tokens[1].strip(), tokens[2].strip())

        elif record_type == "weather":
            return WeatherForecast(tokens[1].strip(), tokens[2].strip())

        else:
            raise ValueError(f"Unknown record type: {record_type}")


# ==========================================================
#                   FILE PROCESSOR CLASS
# ==========================================================
class FileProcessor:
    def __init__(self, path=None):
        self.path = path or self._get_default_file()
        print(f"Processing file: {self.path}")

    @staticmethod
    def _get_default_file():
        files = os.listdir(DEFAULT_INPUT_FOLDER)
        if not files:
            raise FileNotFoundError("No files in input folder.")
        return os.path.join(DEFAULT_INPUT_FOLDER, files[0])

    def process(self):
        records = []

        with open(self.path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    tokens = line.split("|")
                    pub = PublicationFactory.create_from_file(tokens)
                    records.append(pub)

        # Publish all parsed records
        for record in records:
            record.publish()

        # Remove the file after processing
        os.remove(self.path)
        print(f"✔ File processed and removed: {self.path}")


# ==========================================================
#                           MAIN
# ==========================================================
def main():
    print("=== News Feed Tool Extended ===")

    while True:
        print("\nSelect input mode:")
        print("1 – Manual input")
        print("2 – Load from file")

        choice = input("Enter 1 or 2: ")

        if choice == "1":
            record = PublicationFactory.create_manual()
            if record:
                record.publish()

        elif choice == "2":
            try:
                custom_path = input("Enter file path or press Enter for default: ")
                fp = FileProcessor(custom_path if custom_path else None)
                fp.process()
            except Exception as e:
                print("Error:", e)

        else:
            print("Invalid option.")

        again = input("Add more? (y/n): ").lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()
