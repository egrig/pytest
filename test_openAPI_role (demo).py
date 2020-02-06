import requests
import jsondiff
import pytest
import json


def test_positive_test_get_roles(test_get_token):
	response = requests.get(
		"https://api.abc123.io/management_open_api/roles",
		headers={
		"Client-Id": "7v0vldgiht807umb3iht2d5psn",
		"Accept": "application/json",
		"Content-Type": "application/json",
		"x-api-key": "QUdFTkNZX0lERU5USUZJRVI6NTcwOTM4OQ",
		"Authorization": test_get_token
		})
	prod_agency_users = response.json()
	# inject an error
	# prod_agency_users = {"abc": "123"}
	qa_agency_users = response.json()
	print(qa_agency_users)
	res = jsondiff.diff(qa_agency_users, prod_agency_users)
	assert res == {}
	assert response.status_code == 200