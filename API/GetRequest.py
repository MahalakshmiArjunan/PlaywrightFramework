import json

from playwright.sync_api import Playwright
import  pytest

@pytest.mark.regression
def test_get_request(playwright: Playwright):
    request = playwright.request.new_context()
    response = request.get("https://api.restful-api.dev/objects/7")
    print("STATUS CODE =====" , response.status)
    responseBody = response.json()
    print("RESPONSE BODY =====" , responseBody)
    print(responseBody ["data"] ["price"])
    request.dispose()

def test_assert_get_request(playwright: Playwright):
    request = playwright.request.new_context()
    fileInput = open("C:/Users/mahal/PycharmProjects/PlaywrightFramework/API/inputFile.json", "r")
    outputData = json.load(fileInput)
    response = request.get("https://api.restful-api.dev/objects/7")
    print("STATUS CODE =====", response.status)
    responseBody = response.json()
    assert responseBody == outputData
    request.dispose()

