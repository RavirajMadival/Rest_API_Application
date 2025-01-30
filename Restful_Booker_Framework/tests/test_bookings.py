import pytest
import random
from datetime import datetime, timedelta
from utils.logger import logger

new_booking_ids = []


def generate_test_booking(total_price, deposit_paid, additional_needs, **kwargs):
    """
    Generates a random test booking with the specified parameters.
    Args:
        total_price (int): The total price of the booking.
        deposit_paid (bool): Whether the deposit is paid or not.
        additional_needs (str): Any additional needs for the booking.
    Returns:
        dict: A dictionary representing the booking data.
    """
    checkin = (datetime.today() + timedelta(days=random.randint(1, 10))).strftime('%Y-%m-%d')
    checkout = (datetime.today() + timedelta(days=random.randint(11, 20))).strftime('%Y-%m-%d')
    return {
        "firstname": "Test" if not kwargs['firstname'] else kwargs['firstname'],
        "lastname": "User" if not kwargs['lastname'] else kwargs['lastname'],
        "totalprice": total_price,
        "depositpaid": deposit_paid,
        "bookingdates": {"checkin": checkin, "checkout": checkout},
        "additionalneeds": additional_needs
    }


@pytest.mark.parametrize('num_of_booking', [3])
def test_create_booking(client, num_of_booking):
    """
    Test case for creating a booking.
    Verifies that a booking is created successfully and that the response contains a booking ID.
    """
    for num in range(1, num_of_booking + 1):
        total_price = 1000 if num == 2 else 500
        deposit_paid = False if total_price == 1000 else True
        additional_needs = "Lunch" if deposit_paid else ""
        booking = client.create_booking(generate_test_booking(total_price, deposit_paid, additional_needs,
                                                              firstname=f"Test_{num}", lastname=F"User_{num}"))
        assert "bookingid" in booking, f"BookingID is not present in response"
        new_booking_ids.append(booking['bookingid'])
        logger.info(f"Created New Booking: {booking}")


def test_get_all_booking_ids(client):
    """
    Test case for retrieving al booking_ids.
    Verifies that all available booking ids are fetched or not.
    """
    all_booking_ids = client.get_booking()
    logger.info(f"All available booking ids: {all_booking_ids}")


def test_get_new_booking_details(client):
    for i, booking_id in enumerate(new_booking_ids):
        booking_details = client.get_booking(booking_id=booking_id)
        logger.info(f"Details of New Booking{i + 1}: {booking_details}")


def test_update_booking(client):
    """
    Test case for updating a booking.
    Verifies that a booking is updated correctly, particularly the total price.
    """
    for i, booking_id in enumerate(new_booking_ids[0:2]):
        booking_details = client.get_booking(booking_id=booking_id)
        data_to_update = {**booking_details, "totalprice": 1000 if i == 0 else 1500}
        logger.info(f"Updating total price of booking_id {booking_id} to {data_to_update['totalprice']}")
        client.update_booking(booking_id, data_to_update)
        data_after_update = client.get_booking(booking_id=booking_id)
        assert data_after_update["totalprice"] == data_to_update['totalprice'], "New price is not updated"
        logger.info(f"Fetched Details of Booking{i + 1} after updating total price is: {data_after_update}")


def test_delete_booking(client):
    """
    Test case for deleting a booking.
    Verifies that a booking is deleted successfully and that the correct status code is returned.
    """
    delete_status = client.delete_booking(new_booking_ids[-1])
    logger.info(f"Deleted booking ID {new_booking_ids[-1]}, status_code:{delete_status}")
