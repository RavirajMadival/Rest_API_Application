import requests
from configs.config import BASE_URL, USERNAME, PASSWORD
from utils.logger import logger


class RestfulBookerClient:
    """
    Client class to interact with the RESTful Booker API.
    Handles authentication, making requests, and managing bookings.
    """
    def __init__(self):
        """
        Initializes the RestfulBookerClient and authenticates to get the token.
        """
        self.base_url = BASE_URL
        self.token = self._get_auth_token()
        self.headers = {"Content-Type": "application/json", "Cookie": f"token={self.token}"}

    def _get_auth_token(self):
        """
        Authenticates the client using the provided username and password,
        and retrieves an authentication token.
        Returns:
            str: The authentication token required for making API requests.
        """
        response = requests.post(f"{self.base_url}/auth", json={"username": USERNAME, "password": PASSWORD})
        response.raise_for_status()
        token = response.json().get("token")
        logger.info("Authentication successful, token received")
        return token

    def _make_request(self, method, endpoint, **kwargs):
        """
        Makes an HTTP request to the API.
        Args:
            method (str): HTTP method (GET, POST, PUT, PATCH, DELETE).
            endpoint (str): The API endpoint to make the request to.
            kwargs: Additional parameters to pass to the request.
        Returns:
            dict or int: The API response, either as a JSON object or HTTP status code.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        response.raise_for_status()
        return response.json() if response.content else response.status_code

    def create_booking(self, booking_data):
        """
        Creates a new booking with the given data.
        Args:
            booking_data (dict): The data to create a new booking.
        Returns:
            dict: The response containing the booking details, including the booking ID.
        """
        booking = self._make_request("POST", "/booking", json=booking_data)
        return booking

    def get_booking(self, booking_id=None):
        """
        Retrieves a booking by its ID.
        Args:
            booking_id (int): The ID of the booking to retrieve.
        Returns:
            dict: The details of the booking.
        """
        booking = self._make_request("GET", f"/booking/{booking_id}") if booking_id else self._make_request("GET", f"/booking")
        return booking

    def update_booking(self, booking_id, updated_data):
        """
        Updates an existing booking with new data.
        Args:
            booking_id (int): The ID of the booking to update.
            updated_data (dict): The new data to update the booking with.
        Returns:
            dict: The updated booking details.
        """
        updated_booking = self._make_request("PUT", f"/booking/{booking_id}", json=updated_data)
        return updated_booking

    def delete_booking(self, booking_id):
        """
        Deletes a booking by its ID.
        Args:
           booking_id (int): The ID of the booking to delete.
        Returns:
           int: The HTTP status code (201 for successful deletion).
        """
        url = f"{self.base_url}/booking/{booking_id}"
        response = requests.request("DELETE", url, headers=self.headers)
        response.raise_for_status()
        return response.status_code

