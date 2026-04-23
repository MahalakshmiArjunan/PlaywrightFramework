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

def test_get_all_bookings(playwright: Playwright):
    request = playwright.request.new_context()
    response = request.get("https://restful-booker.herokuapp.com/booking")
    print(response.json())
    assert response.status == 200
    request.dispose()

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


def test_assert_get_booking_by_Id(playwright: Playwright, booking_id):
    request = playwright.request.new_context()
    fileInput = open("C:/Users/mahal/PycharmProjects/PlaywrightFramework/API/postData.json", "r")
    outputData = json.load(fileInput)
    response = request.get(f"https://restful-booker.herokuapp.com/booking/{booking_id}")
    print("STATUS CODE =====", response.status)
    responseBody = response.json()
    assert responseBody == outputData
    request.dispose()

def test_assert_get_booking_by_Name(playwright: Playwright, booking_id):
    request = playwright.request.new_context()
    response = request.get("https://restful-booker.herokuapp.com/booking?firstname=Ashwin&lastname=Bharati")
    allBookings = response.json()
    for booking in allBookings:
        if booking["bookingid"] == booking_id:
            print("Booking Id=======", booking["bookingid"])
            assert booking in allBookings
    request.dispose()

def test_create_token(playwright: Playwright):
    request = playwright.request.new_context()
    fileInput = open("C:/Users/mahal/PycharmProjects/PlaywrightFramework/API/auth.json", "r")
    inputData = json.load(fileInput)
    response = request.post("https://restful-booker.herokuapp.com/auth", data=inputData)
    print(response.status)
    responseBody = response.json()
    print(responseBody)
    assert response.status == 200
    assert "token" in responseBody
    global token
    token = responseBody["token"]
    request.dispose()
    return token

def test_update_booking(playwright: Playwright):
    token = test_create_token(playwright)
    print(token)
    request = playwright.request.new_context()
    fileInput = open("C:/Users/mahal/PycharmProjects/PlaywrightFramework/API/updatePostData.json", "r")
    inputData = json.load(fileInput)
    headers = {"Cookie":f"token={token}"}
    response = request.put("https://restful-booker.herokuapp.com/booking/1", data=inputData, headers=headers)
    responseBody = response.json()
    print(response.status)
    print(responseBody)
    request.dispose()
