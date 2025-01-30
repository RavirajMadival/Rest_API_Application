import pytest
from datetime import datetime
from utils.api_client import RestfulBookerClient


@pytest.fixture(scope="module")
def client():
    """
    Pytest fixture that provides the RestfulBookerClient instance.
    This client will be used by the test functions to interact with the RESTful Booker API.
    Returns:
       RestfulBookerClient: The client for interacting with the API.
    """
    return RestfulBookerClient()


def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"logs/test_report_{timestamp}.html"
    config.option.htmlpath = report_filename


def pytest_html_report_title(report):
    report.title = f"Test Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


def pytest_html_results_summary(summary):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    summary.append(f"Report generated at: {timestamp}")
