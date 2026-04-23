import json

import pytest
from openpyxl.formatting.rule import DataBar
from playwright.sync_api import Playwright


# ─── Fixture: shared request context across all tests ────────────────────────
@pytest.fixture(scope="session")
def request_context(playwright: Playwright):
    request = playwright.request.new_context(extra_http_headers={"Content-Type": "application/json"})
    yield request
    request.dispose()

# ─── Fixture: reads the json file ────────────────────────
@pytest.fixture(scope="session")
def read_json_file():
    def _read(filepath):           # Inner function accepts the filepath
        with open(filepath, "r") as f:
            return json.load(f)
    return _read

# ─── Fixture: POST booking once, share booking_id with other tests ────────────
@pytest.fixture(scope="session")
def booking_id(request_context, read_json_file):
    inputData = read_json_file("C:/Users/mahal/PycharmProjects/PlaywrightFramework/API/postData.json")
    response = request_context.post("https://restful-booker.herokuapp.com/booking", data=json.dumps(inputData))

    assert response.ok, f"POST failed [{response.status}]: {response.text()}"
    responseBody = response.json()
    print("\nPOST Response:", responseBody)

    assert "bookingid" in responseBody
    return responseBody["bookingid"]  # Shared via fixture, no globals needed

# ─── Fixture: shares token across the tests ────────────────────────
@pytest.fixture(scope="session")
def access_token(request_context, read_json_file):
    inputData = read_json_file("C:/Users/mahal/PycharmProjects/PlaywrightFramework/API/auth.json")
    response = request_context.post("https://restful-booker.herokuapp.com/auth", data=json.dumps(inputData))
    assert response.ok, f"POST failed [{response.status}]: {response.text()}"
    responseBody = response.json()
    print(responseBody)
    return responseBody["token"]

def test_postData(request_context, read_json_file, booking_id):
    inputData = read_json_file("C:/Users/mahal/PycharmProjects/PlaywrightFramework/API/postData.json")
    response = request_context.post(
        "https://restful-booker.herokuapp.com/booking", data=json.dumps(inputData))
    assert response.ok, f"POST failed [{response.status}]: {response.text()}"
    responseBody = response.json()
    print(responseBody)
    assert "bookingid" in responseBody
    assert responseBody["booking"]["firstname"] == inputData["firstname"]
    assert responseBody["booking"]["lastname"] == inputData["lastname"]
    assert responseBody["booking"]["totalprice"] == inputData["totalprice"]
    assert responseBody["booking"]["depositpaid"] == inputData["depositpaid"]
    assert responseBody["booking"]["bookingdates"]["checkin"] == inputData["bookingdates"]["checkin"]
    assert responseBody["booking"]["bookingdates"]["checkout"] == inputData["bookingdates"]["checkout"]
    assert responseBody["booking"]["additionalneeds"] == inputData["additionalneeds"]

def test_getData(request_context, read_json_file, booking_id):
    inputData = read_json_file("C:/Users/mahal/PycharmProjects/PlaywrightFramework/API/postData.json")
    response = request_context.get(f"https://restful-booker.herokuapp.com/booking/{booking_id}")
    assert response.ok, f"GET failed [{response.status}]: {response.text()}"
    responseBody = response.json()
    print(responseBody)
    assert responseBody["firstname"] == inputData["firstname"]
    assert responseBody["lastname"] == inputData["lastname"]
    assert responseBody["totalprice"] == inputData["totalprice"]
    assert responseBody["depositpaid"] == inputData["depositpaid"]
    assert responseBody["bookingdates"]["checkin"] == inputData["bookingdates"]["checkin"]
    assert responseBody["bookingdates"]["checkout"] == inputData["bookingdates"]["checkout"]
    assert responseBody["additionalneeds"] == inputData["additionalneeds"]

def test_putData(request_context, read_json_file, booking_id, access_token):
    updatedData = read_json_file("C:/Users/mahal/PycharmProjects/PlaywrightFramework/API/updatePostData.json")
    response = request_context.put(
        f"https://restful-booker.herokuapp.com/booking/{booking_id}",
        data=json.dumps(updatedData),
        headers={"Cookie": f"token={access_token}"}
    )
    assert response.ok, f"PUT failed [{response.status}]: {response.text()}"
    responseBody = response.json()
    print(responseBody)
    assert responseBody["firstname"] == updatedData["firstname"]
    assert responseBody["lastname"] == updatedData["lastname"]
    assert responseBody["totalprice"] == updatedData["totalprice"]
    assert responseBody["depositpaid"] == updatedData["depositpaid"]
    assert responseBody["bookingdates"]["checkin"] == updatedData["bookingdates"]["checkin"]
    assert responseBody["bookingdates"]["checkout"] == updatedData["bookingdates"]["checkout"]
    assert responseBody["additionalneeds"] == updatedData["additionalneeds"]

def test_patchData(request_context, read_json_file, booking_id, access_token):
    partialData = read_json_file("C:/Users/mahal/PycharmProjects/PlaywrightFramework/API/partialUpdateData.json")
    response = request_context.patch(
        f"https://restful-booker.herokuapp.com/booking/{booking_id}",
        data=json.dumps(partialData),
        headers={"Cookie": f"token={access_token}"}  # ✅ Auth required for PATCH
    )
    assert response.ok, f"PATCH failed [{response.status}]: {response.text()}"
    responseBody = response.json()
    print(responseBody)
    assert responseBody["additionalneeds"] == partialData["additionalneeds"]

def test_deleteData(request_context, booking_id, access_token):
    response = request_context.delete(
        f"https://restful-booker.herokuapp.com/booking/{booking_id}",
        headers={"Cookie": f"token={access_token}"}  
    )
    # API returns 201 (not 200) on successful delete
    assert response.status == 201, f"DELETE failed [{response.status}]: {response.text()}"
    print(f"\n✅ Booking {booking_id} deleted successfully!")

    # ─── Verify booking no longer exists ─────────────────────────────────────
    verifyResponse = request_context.get(
        f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    )
    assert verifyResponse.status == 404, (
        f"Booking {booking_id} still exists after DELETE! Status: {verifyResponse.status}"
    )
    print(f"✅ Verified booking {booking_id} no longer exists (404)!")


