import qtest_swagger_client
# import json
# json_file = open('Account_Data.json', 'rb')
# json_data = json.load(json_file)
#
# item = json_data['Displayed_item']
# print(item)
#
# for i in item:
#     print(i["name"])

class QtestUtilsLgx(object):
    def __init__(self, apikey):
        qtest_swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
        qtest_swagger_client.configuration.api_key['Authorization'] = apikey
        self._testcase_api = None


    def generate_api_inst(self):
        self._testcase_api = qtest_swagger_client.TestcaseApi()

    def get_testcase(self, p_id, testcaseid):
        cases = self._testcase_api.get_test_case(project_id=p_id, test_case_id=testcaseid)
        return cases


Qtest = QtestUtilsLgx('7c32ffa3-2bee-4f7c-9251-3ab9790f3ef0')

Qtest.generate_api_inst()

tcase = Qtest.get_testcase('86751', '25177394')

steps = tcase.test_steps

print(steps)

# #
# # print(pty.Headline)
# for each_item in pty:
#     print(each_item.field_name)
#
# print(pty)