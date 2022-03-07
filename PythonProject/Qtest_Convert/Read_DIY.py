ACTIVATE_THIS = r'..\new_env\Scripts\activate_this.py'
with open(ACTIVATE_THIS, 'r') as f:
    exec(f.read(), dict(__file__=ACTIVATE_THIS))

import os
import qtest_swagger_client
import json
import subprocess

# Get browser
json_file = open('Account_Data.json', 'rb')
json_data = json.load(json_file)

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

product_id = json_data['Product_id']

token = json_data['token']

browser = json_data['browser']

Displayed_item = json_data['Displayed_item']

if browser == 'chrome':
    pname = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
elif browser == 'firefox':
    pname = "C:\Program Files\Mozilla Firefox\\firefox.exe"
elif browser == 'ie':
    pname = "C:\Program Files\Internet Explorer\iexplore.exe"

current_dir = os.path.abspath(os.path.dirname(__file__))
while 1:
    # Based on url change and user confirm need convert
    print('#############################################################################')
    user_input = input("Put enter test case id: ")

    with open(r'NewTest.html', 'w', encoding='utf-8') as f:
        # define css file
        f.write('<head>\n<link rel="stylesheet" type="text/css" href="mystyle.css" />\n</head>')
        f.write('<body id="tinymce" class="mce-content-body" data-id="propCf6414639_editorNode" contenteditable="false">')
        # get qtest id
        qcase_id = user_input

        # Get all info by the API
        Qtest = QtestUtilsLgx(token)
        Qtest.generate_api_inst()

        tcase = Qtest.get_testcase(product_id, qcase_id)
        # Get all properties except test steps
        pty = tcase.properties

        case_name = tcase.name

        # define test case name
        f.write('<table class="smallerbordered" border="1" width="100%" style="table-layout:fixed;">\n<tbody>')
        f.write('<table class="smallerbordered" width="100%">')
        f.write('<tr class="header"><td bgcolor="#add8e6" colspan="4">\n')
        f.write('<span class="finbsp;eldLabel">Test Case Name:&</span>')

        print(case_name)

        f.write(case_name+'</td></tr></table>')
        # define Qtest id
        f.write('<table class="smallerbordered" width="100%">')
        f.write('<tr class="header"><td bgcolor="#add8e6" colspan="4">\n')
        f.write('<span class="fieldLabel">Test Case ID:&nbsp;</span>')
        f.write(qcase_id + '</td></tr></table>')
        print(qcase_id)

        itemCount = len(Displayed_item)
        detail_dic = {}
        long_dic = {}
        long_list = ['Description', 'Test Case Design', 'Notes', 'Automation Metadata: Script Options',
                     'Hardware Needed', 'Testware Location', 'Precondition', 'Pass-Fail Criteria', 'Post Conditions']
        for eachItem in Displayed_item:
            for each_pty in pty:
                if each_pty.field_name == eachItem['name']:
                    if each_pty.field_name in long_list:
                        if each_pty.field_value_name is None or each_pty.field_value_name == '':
                            long_dic[eachItem['name']] = each_pty.field_value
                        else:
                            long_dic[eachItem['name']] = each_pty.field_value_name
                    else:
                        if each_pty.field_value_name is None or each_pty.field_value_name == '':
                            detail_dic[eachItem['name']] = each_pty.field_value
                        else:
                            detail_dic[eachItem['name']] = each_pty.field_value_name
        if 'Headline' in detail_dic.keys():
            f.write('<table class="smallerbordered" width="100%">')
            f.write('<tr><td colspan="4">\n')
            f.write('<span class="fieldLabel">Headline:&nbsp;</span>\n')
            f.write('<span class="TYPE_tc_text plain">' + detail_dic['Headline'] + '</span>')
            f.write('</td>\n')
            f.write('</tr>\n')
            f.write('</table>\n')
            del detail_dic['Headline']

        shortCount = len(detail_dic)
        rowCount = shortCount//4
        remainCellCount = shortCount%4

        print('short countt is: ' + str(shortCount))

        print('row count is: ' + str(rowCount))

        print('remain Cell countt is: ' + str(remainCellCount))
        counter = 0
        set_count = 0
        reach_count = 0
        not_type = 0
        for key, value in detail_dic.items():

            if not_type == 0:
                counter += 1
                if counter == 1:
                    f.write('<table class="smallerbordered" width="100%">')
                    f.write('<tr>\n')
                f.write('<td>\n')
                f.write('<span class="fieldLabel">' + key + ': ' + '</span>\n')
                f.write('<span class="TYPE_tc_menu">' + value + '</span>')
                f.write('</td>\n')
            if counter == 4:
                f.write('</tr>\n')
                f.write('</table>\n')
                counter = 0
                set_count += 1
            if set_count == rowCount:
                not_type += 1
                if not_type == 1:
                    continue
                reach_count += 1
                if reach_count == 1:
                    f.write('<table class="smallerbordered" width="100%">')
                    f.write('<tr>\n')
                if remainCellCount == 1:
                    f.write('<td colspan="1">\n')
                    f.write('<span class="fieldLabel">' + key + ': ' + '</span>\n')
                    f.write('<span class="TYPE_tc_menu">' + value + '</span>')
                    f.write('</td>\n')
                    f.write('</tr>\n')
                    f.write('</table>\n')
                elif remainCellCount == 2:
                    f.write('<td colspan="2">\n')
                    f.write('<span class="fieldLabel">' + key + ': ' + '</span>\n')
                    f.write('<span class="TYPE_tc_menu">' + value + '</span>')
                    f.write('</td>\n')
                    if reach_count == 2:
                        f.write('</tr>\n')
                        f.write('</table>\n')
                elif remainCellCount == 3:
                    f.write('<td colspan="3">\n')
                    f.write('<span class="fieldLabel">' + key + ': ' + '</span>\n')
                    f.write('<span class="TYPE_tc_menu">' + value + '</span>')
                    f.write('</td>\n')
                    if reach_count == 3:
                        f.write('</tr>\n')
                        f.write('</table>\n')
        for key, value in long_dic.items():
            f.write('<table class="smallerbordered" width="100%">')
            f.write('<tr>\n')
            f.write('<td colspan="4" style="word-break: break-word;overflow:hidden;">\n')
            f.write('<span class="fieldLabel">' + key + ': ' + '</span>\n<br>')
            if value is None:
                value = 'None'
            f.write('<span class="TYPE_tc_menu">' + value + '</span>')
            f.write('</td>\n')
            f.write('</tr>\n')
            f.write('</table>\n')

        # define test case step
        f.write('<table class="smallerbordered" width="100%">')
        f.write('<tr>\n')
        f.write('<td colspan="4" style="word-break: break-word;overflow:hidden;" id="ProcessTable" valign="top">\n')
        f.write('<table style="width:100%" border="1" class="TYPE_tc_table">\n')
        f.write('<tbody>\n')
        f.write('<tr class="header">\n')
        f.write('<th class="left right" border="1" colspan="3" >Test Process</th>\n')
        f.write('</tr>\n')
        f.write('<tr class="header">\n')
        f.write('<th class="left">#</th>\n')
        f.write('<th class="right">Procedure</th>\n')
        f.write('<th class="right">Verification Procedure</th>\n')
        f.write('</td>\n')
        f.write('</tr>\n')

        steps = tcase.test_steps
        print(len(steps))
        for i in range(len(steps)):
            z = i+1
            f.write('<tr>\n')
            f.write('<td align="left">\n')
            f.write('<b>'+str(z)+'</b>')
            f.write('</td>\n')
            for j in range(2):
                if j == 0:
                    input_step = steps[i].description
                elif j == 1:
                    input_step = steps[i].expected

                f.write('<td align="left">\n')
                f.write(input_step)
                f.write('</td>\n')
        f.write('</tr>\n')
        f.write('</table>\n')
        f.write('</tbody>\n</table>\n')
        f.write('</tbody>\n</table>\n')
        f.write('</body>\n')
        f.close()
        subprocess.call([pname, current_dir+'\\'+'NewTest.html'])
