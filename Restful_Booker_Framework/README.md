# Restful Booker API Test Framework

## 📦 Setup Instructions

### 1. **Clone the repository**
Clone the repository to your local machine using the following command:
```sh
git clone https://github.com/RavirajMadival/Rest_API_Application.git
```
### 2. Install Dependencies
Navigate to the project directory and set up a Python virtual environment:

```sh
cd Restful_Booker_Framework
```
For Windows OS:
```sh
py -m venv venv 
.\venv\Scripts\activate
```
For Linux/MacOs: 
```sh
python3 -m venv venv
source venv/bin/activate
```
#
Once the virtual environment is activated, install the required dependencies from requirements.txt:
```sh
pip install -r requirements.txt
```
### 3. 🧪 Run the Tests
To execute the tests, simply run the following command:

```sh
pytest
```

### 4. 📄 Notes
Status code validations are handled in api_client.py after sending requests to the API.
Data validations (e.g., checking booking details) are implemented in the individual test cases within test_bookings.py.

### 5. Project Structure
```graphql
restful_booker_framework/
│-- configs/
│   ├── config.py                # Configuration for API and authentication
│-- tests/
│   ├── test_bookings.py         # Test cases for creating, updating, fetching, and deleting bookings
│   ├── conftest.py              # Pytest fixtures for the framework
│-- utils/
│   ├── api_client.py            # API client for making requests
│   ├── logger.py                # Logging setup and utility
│-- logs/
│   ├── test_log.log             # Log file for requests and responses
│   ├── test_log.html            # HTML Log file for requests and responses
│-- requirements.txt             # List of dependencies
│-- pytest.ini                   # Pytest configuration
│-- README.md                    # This file
```