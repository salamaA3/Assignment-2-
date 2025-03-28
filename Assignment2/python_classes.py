from datetime import date


class Room:
    """Represents a hotel room with details like room number, type, amenities, price, and availability."""

    def __init__(self, room_number, room_type, amenities, price, availability=True):
        # Private attributes for encapsulation
        self.__room_number = room_number  # Unique identifier for the room
        self.__room_type = room_type  # Type of room (Single, Double, Suite, etc.)
        self.__amenities = amenities  # List of amenities available in the room
        self.__price = price  # Price per night
        self.__availability = availability  # Room availability status (True/False)

    def get_room_number(self):
        """Returns the room number."""
        return self.__room_number

    def get_details(self):
        """Returns room details as a formatted string."""
        return f"Room {self.__room_number}: {self.__room_type}, Amenities: {self.__amenities}, Price: ${self.__price}, Available: {self.__availability}"

    def is_available(self):
        """Checks if the room is available for booking."""
        return self.__availability

    def book_room(self):
        """Marks the room as booked if available."""
        if self.__availability:
            self.__availability = False
            return True
        return False

    def cancel_booking(self):
        """Marks the room as available after cancellation."""
        self.__availability = True


class Guest:
    """Represents a guest with personal details and loyalty status."""

    def __init__(self, name, email, contact, loyalty_points=0):
        # Private attributes for guest details
        self.__name = name  # Guest's full name
        self.__email = email  # Email address
        self.__contact = contact  # Contact number
        self.__loyalty_points = loyalty_points  # Loyalty points earned
        self.__reservations = []  # List to store guest's reservations

    def add_reservation(self, booking):
        """Adds a booking to the guest's reservation history."""
        self.__reservations.append(booking)

    def get_details(self):
        """Returns guest details as a formatted string."""
        return f"Guest: {self.__name}, Email: {self.__email}, Contact: {self.__contact}, Loyalty Points: {self.__loyalty_points}"

    def get_reservations(self):
        """Returns all reservations of the guest."""
        return self.__reservations


class Booking:
    """Handles room reservations, including check-in/out dates and booking confirmation."""

    def __init__(self, guest, room, check_in, check_out):
        # Ensure the room is available before proceeding with booking
        if room.is_available():
            self.__guest = guest  # Guest making the booking
            self.__room = room  # Room being booked
            self.__check_in = check_in  # Check-in date
            self.__check_out = check_out  # Check-out date
            self.__status = "Confirmed"  # Booking status
            room.book_room()  # Mark room as booked
            guest.add_reservation(self)  # Add booking to guest's history
        else:
            raise ValueError("Room is not available")

    def cancel_booking(self):
        """Cancels the booking and marks the room as available."""
        self.__room.cancel_booking()
        self.__status = "Cancelled"

    def get_details(self):
        """Returns booking details as a formatted string."""
        return f"Booking for {self.__guest.get_details()} in {self.__room.get_details()} from {self.__check_in} to {self.__check_out}. Status: {self.__status}"


class Invoice:
    """Generates an invoice for a booking, including room price and additional charges."""

    def __init__(self, booking, extra_charges=0, discount=0):
        self.__booking = booking  # Booking associated with the invoice
        self.__extra_charges = extra_charges  # Additional charges (e.g., room service)
        self.__discount = discount  # Discount applied
        # Example calculation (modify based on real pricing)
        self.__total = (booking._Booking__room.get_room_number() * 100) + extra_charges - discount

    def get_invoice_details(self):
        """Returns invoice details as a formatted string."""
        return f"Invoice: {self.__booking.get_details()}, Extra Charges: ${self.__extra_charges}, Discount: ${self.__discount}, Total: ${self.__total}"


class Payment:
    """Handles different payment methods for hotel bookings."""

    def __init__(self, invoice, payment_method):
        self.__invoice = invoice  # Invoice associated with the payment
        self.__payment_method = payment_method  # Payment method used (e.g., Credit Card)
        self.__status = "Pending"  # Payment status (Pending/Paid)

    def process_payment(self):
        """Processes the payment and updates the status."""
        if self.__payment_method in ["Credit Card", "Debit Card", "Mobile Wallet"]:
            self.__status = "Paid"
            return f"Payment of ${self.__invoice.get_invoice_details().split()[-1]} via {self.__payment_method} is successful."
        else:
            return "Invalid payment method."

    def get_payment_status(self):
        """Returns the current status of the payment."""
        return self.__status


class Feedback:
    """Allows guests to leave reviews and ratings."""

    def __init__(self, guest, rating, comment):
        self.__guest = guest  # Guest leaving feedback
        self.__rating = rating  # Rating given (out of 5)
        self.__comment = comment  # Guest's review comment

    def get_feedback(self):
        """Returns the feedback as a formatted string."""
        return f"{self.__guest.get_details()} rated {self.__rating}/5: {self.__comment}"
