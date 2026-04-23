import json

import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="module")             # booking_id variable is globally accessible for all the tests
def booking_id(playwright: Playwright):
    request = playwright.request.new_context()
    fileInput = open("C:/Users/mahal/PycharmProjects/PlaywrightFramework/API/postData.json", "r")
    inputData = json.load(fileInput)
    response = request.post("https://restful-booker.herokuapp.com/booking", data=inputData)
    print("STATUS CODE =====", response.status)
    responseBody = response.json()
    print(responseBody)
    assert "bookingid" in responseBody
    booking_id = responseBody["bookingid"]
    request.dispose()
    yield booking_id


def test_assert_post_request(playwright: Playwright, booking_id):
    request = playwright.request.new_context()
    fileInput = open("C:/Users/mahal/PycharmProjects/PlaywrightFramework/API/postData.json", "r")
    inputData = json.load(fileInput)
    response = request.post("https://restful-booker.herokuapp.com/booking", data=inputData )
    responseBody = response.json()
    assert responseBody["booking"]["firstname"] == inputData["firstname"]
    assert responseBody["booking"]["lastname"] == inputData["lastname"]
    assert responseBody["booking"]["totalprice"] == inputData["totalprice"]
    assert responseBody["booking"]["depositpaid"] == inputData["depositpaid"]
    assert responseBody["booking"]["bookingdates"]["checkin"] == inputData["bookingdates"]["checkin"]
    assert responseBody["booking"]["bookingdates"]["checkout"] == inputData["bookingdates"]["checkout"]
    assert responseBody["booking"]["additionalneeds"] == inputData["additionalneeds"]
    request.dispose()


def test_get_data(playwright: Playwright, booking_id):
    request = playwright.request.new_context()
    fileInput = open("C:/Users/mahal/PycharmProjects/PlaywrightFramework/API/postData.json", "r")
    outputData = json.load(fileInput)
    response = request.get(f"https://restful-booker.herokuapp.com/booking/{booking_id}")
    print("STATUS CODE =====", response.status)
    responseBody = response.json()
    assert responseBody == outputData
    request.dispose()

