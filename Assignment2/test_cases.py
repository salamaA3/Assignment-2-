# test_cases.py

from python_classes import Room, Guest, Booking, Invoice, Payment, Feedback


# Test Case: Guest Account Creation
def test_guest_creation():
    # Creating two guest accounts with sample data
    guest1 = Guest("John Doe", "john@example.com", "1234567890", 50)
    guest2 = Guest("Jane Smith", "jane@example.com", "0987654321", 20)

    # Verifying that guest details are correctly stored and retrieved
    assert guest1.get_details() == "Guest: John Doe, Email: john@example.com, Contact: 1234567890, Loyalty Points: 50"
    assert guest2.get_details() == "Guest: Jane Smith, Email: jane@example.com, Contact: 0987654321, Loyalty Points: 20"
    print("Guest Creation Test Passed")


# Test Case: Searching for Available Rooms
def test_room_search():
    # Creating two room instances with different types and amenities
    room1 = Room(101, "Single", ["WiFi", "TV"], 100)
    room2 = Room(102, "Double", ["WiFi", "TV", "Mini-bar"], 150)

    # Checking if the rooms are available upon creation
    assert room1.is_available() is True
    assert room2.is_available() is True
    print("Room Search Test Passed")


# Test Case: Making a Room Reservation
def test_booking():
    # Creating a guest and a room for the booking
    guest = Guest("Alice Johnson", "alice@example.com", "1234567890")
    room = Room(103, "Suite", ["WiFi", "TV", "Mini-bar", "Balcony"], 200)

    # Creating a booking instance with check-in and check-out dates
    booking = Booking(guest, room, "2025-04-01", "2025-04-05")

    # Verifying that the booking details are correctly stored
    assert booking.get_details().startswith("Booking for Guest: Alice Johnson")
    print("Booking Test Passed")


# Test Case: Invoice Generation
def test_invoice():
    # Creating guest, room, and booking instances
    guest = Guest("Bob Brown", "bob@example.com", "5555555555")
    room = Room(104, "Double", ["WiFi", "TV"], 120)
    booking = Booking(guest, room, "2025-05-01", "2025-05-03")

    # Generating an invoice with discounts and additional charges
    invoice = Invoice(booking, 50, 10)

    # Verifying that the invoice details contain the correct information
    assert "Invoice:" in invoice.get_invoice_details()
    print("Invoice Test Passed")


# Test Case: Payment Processing
def test_payment():
    # Creating guest, room, booking, and invoice instances
    guest = Guest("Charlie White", "charlie@example.com", "4444444444")
    room = Room(105, "Single", ["WiFi"], 80)
    booking = Booking(guest, room, "2025-06-01", "2025-06-04")
    invoice = Invoice(booking, 30, 5)

    # Processing a payment using a credit card
    payment = Payment(invoice, "Credit Card")

    # Verifying that the payment process runs successfully
    assert payment.process_payment().startswith("Payment of")
    print("Payment Test Passed")


# Test Case: Guest Feedback Submission
def test_feedback():
    # Creating a guest instance and submitting feedback
    guest = Guest("David Black", "david@example.com", "3333333333")
    feedback = Feedback(guest, 5, "Amazing stay!")

    # Verifying that the feedback contains the correct text
    assert "Amazing stay!" in feedback.get_feedback()
    print("Feedback Test Passed")


# Running all tests
if __name__ == "__main__":
    test_guest_creation()  # Test guest account creation
    test_room_search()  # Test searching for available rooms
    test_booking()  # Test making a room reservation
    test_invoice()  # Test generating an invoice
    test_payment()  # Test processing payments
    test_feedback()  # Test guest feedback submission

    print("All Tests Passed Successfully!")
