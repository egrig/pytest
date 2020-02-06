import pytest
import requests

# common variables
get_prod_token_header_values={
		"Accept": "application/json", 
		"Cache-Control": "no-cache",
		"Content-Type": "application/x-www-form-urlencoded",
		"x-api-key": "QUdFTkNZX0lERU5USUZJRVI6NTcwOTM4OQ",
		"Authorization": "Basic N3YwdmxkZ2lodDgwN3VtYjNpaHQyZDVwc246bTJkODBkaDBhcjc3OTVkZWdnMzJjczFrNGJzam9uaWllbWhma2RodGJ0dnFmazk2dHQ4"
		}

get_devcat_token_header_values={
		"Accept": "application/json", 
		"Cache-Control": "no-cache",
		"Content-Type": "application/x-www-form-urlencoded",
		"x-api-key": "QUdFTkNZX0lERU5USUZJRVI6NTcwOTM4OQ",
		"Authorization": "Basic M2UxaGtpNmdqM3A2dmhqdDIzNDFnczRocDg6MTFucWpiYnVwZGExYjdqcmcwOWdodTFtcDlrdGM4bzFhdmJwOHE2YWtjMDQzNHFyc21zaQ=="
		}

# set prod base URL
@pytest.fixture
def supply_prod_base_url():
	return "https://api.abc123.io"

# set devcat base URL
@pytest.fixture
def supply_devcat_base_url():
	return "https://api.abc123.test"

# build prod token
@pytest.fixture
def get_prod_token(supply_prod_base_url):
	response = requests.post(supply_prod_base_url+"/oauth2/token", headers=get_prod_token_header_values)
	# assemble auth token
	print(response.status_code, response)
	prod_token = "Bearer " + response.json()["access_token"]
	return prod_token

# build devcat token
@pytest.fixture
def get_devcat_token(supply_test_base_url):
	response = requests.post(supply_test_base_url+"/oauth2/token", headers=get_test_token_header_values)
	# assemble auth token
	print(response.status_code, response)
	devcat_token = "Bearer " + response.json()["access_token"]
	return test_token

# declaring custom markers
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "test_set_AgencyUsers_AddUser: test_set_AgencyUsers_AddUser"
    )
    config.addinivalue_line(
        "markers", "test_set_AgencyUsers: test_set_AgencyUsers"
    )
