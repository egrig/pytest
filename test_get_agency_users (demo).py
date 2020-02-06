import requests
import jsondiff
import pytest
import json

@pytest.mark.test_set_AgencyUsers_AddUser
@pytest.mark.parametrize("in_username, in_email, in_name, in_password, in_all_groups, in_roleIds, in_GroupIds, in_is_visible",
	[
	(None, None, None, None, None, None, None, None),
	("edward1", None, None, None, None, None, None, None),
	("edward2", "edward1@abc123.io", None, None, None, None, None, None),
	("edward3", "edward2@abc123.io", "edward grigorovich", None, None, None, None, None),
	("edward4", "edward3@abc123.io", "edward grigorovich", "12345678", None, None, None, None),
	("edward5", "edward4@abc123.io", "edward grigorovich", "12345678", True, None, None, None),
	("edward6", "edward5@abc123.io", "edward grigorovich", "12345678", True, [642, 1665], None, None),
	("edward7", "edward6@abc123.io", "edward grigorovich", "12345678", True, [642, 1665], [10038979], None),
	("edward8", "edward7@abc123.io", "edward grigorovich", "12345678", True, [642, 1665], [10038979], True),
	("edward8", "edward7@abc123.io", "edward grigorovich", "12345678", True, [642, 1665], [10038979], True)
	])

@pytest.mark.test_set_AgencyUsers_AddUser
def test_negative_test_add_agency_user_with_user_data(in_username, in_email, in_name, in_password, in_all_groups, in_roleIds,
 in_advertiserIds, in_is_visible, get_prod_token, get_test_token):
	payload_prod = json.dumps({
		"username": in_username,
		"email": in_email,
		"name": in_name,
		"password": in_password,
		"all_groups" : in_all_groups,
		"roleIds" : in_roleIds,
		"advertiserIds" : in_advertiserIds,
		"is_visible" : in_is_visible
		})
	res_prod = requests.post(
		"https://api.abc123.io/management_open_api/agency_user",
		headers={
		"Client-Id": "7v0vldgiht807umb3iht2d5psn",
		"Accept": "application/json",
		"Content-Type": "application/json",
		"x-api-key": "QUdFTkNZX0lERU5USUZJRVI6NTcwOTM4OQ",
		"Authorization": get_prod_token
		},
		data=res_prod)

	payload_test = json.dumps({
		"username": in_username,
		"email": in_email,
		"name": in_name,
		"password": in_password,
		"all_groups" : in_all_groups,
		"roleIds" : in_roleIds,
		"GroupIds" : in_advertiserIds,
		"is_visible" : in_is_visible
		})
	res_test = requests.post(
		"https://api.abc123.io/management_open_api/agency_user",
		headers={
		"Client-Id": "3e1hki6gj3p6vhjt2341gs4hp8",
		"Accept": "application/json",
		"Content-Type": "application/json",
		"x-api-key": "QUdFTkNZX0lERU5USUZJRVI6NTcwOTM4OQ",
		"Authorization": get_test_token
		},
		data=payload_test)

	prod_agency_users = res_prod.json()
	test_agency_users = res_test.json()
	res_diff = jsondiff.diff(test_agency_users, prod_agency_users)

	# assertions
	assert res_prod.status_code == 200
	assert res_test.status_code == 200
	assert res_diff == {}

@pytest.mark.test_set_AgencyUsers
def test_get_all_agency_users(test_get_token):
	response = requests.get("https://api.abc123.io/management_open_api/agency_users", 
		headers={
		"Client-Id": "7v0vldgiht807umb3iht2d5psn",
		"Accept": "application/json",
		"Content-Type": "application/json",
		"x-api-key": "QUdFTkNZX0lERU5USUZJRVI6NTcwOTM4OQ",
		"Authorization": test_get_prod_token
		})
	prod_agency_users = response.json()
	qa_agency_users = response.json()
	print(qa_agency_users)
	res = jsondiff.diff(qa_agency_users, prod_agency_users)
	assert res == {}
	assert response.status_code == 200