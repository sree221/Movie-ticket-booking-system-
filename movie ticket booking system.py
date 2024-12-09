class Movie:
    def __init__(self, title, available_seat):
        self.title = title
        self.available_seat = available_seat

    def show_details(self):
        print(f"Movie Name: {self.title}\nAvailable Seats: {self.available_seat}")

    def book_ticket(self, number, price=10):
        total_price = price * number
        if self.available_seat < number:
            print(f"Only {self.available_seat} seats are available. Please try again.")
        else:
            self._available_seat -= number
            print(f"{number} tickets are booked for {self.title}.\nTotal Price: ${total_price}")


class PremiumMovie(Movie):
    def __init__(self, extra_charge, title, available_seat):
        self.extra_charge = extra_charge
        super().__init__(title, available_seat)

    def show_details(self):
        print(f"Movie Name: {self.title}\nAvailable Seats: {self.available_seat}\nExtra Charges: ${self.extra_charge}")

    def book_ticket(self, number, price=10):
        base_price = price * number
        extra_charge = self.extra_charge * number
        total_price = base_price + extra_charge

        if self._available_seat < number:
            print(f"Only {self.available_seat} seats are available. Please try again.")
        else:
            self._available_seat -= number
            print(f"{number} tickets are booked for {self.title}.\nBase Price: ${base_price}\nExtra Charge: ${extra_charge}\nTotal Price: ${total_price}")


def c(d):
    d.show_details()

b = PremiumMovie(10, "Kali", 10)
a = Movie("Kali", 10)

# Test show_details
c(b)
