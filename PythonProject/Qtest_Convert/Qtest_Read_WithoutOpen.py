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

        case_headline = pty[4].field_value

        case_status = pty[0].field_value_name

        case_WhenToRun = pty[18].field_value_name

        case_AutoDevStatus = pty[9].field_value_name

        case_type = pty[1].field_value_name

        case_CVBProducts = pty[7].field_value_name

        case_FeatureTest = pty[11].field_value_name

        case_Fucntion_Area = pty[12].field_value_name

        case_Tags = pty[15].field_value

        case_controllertype = pty[28].field_value_name

        case_mode = pty[29].field_value_name

        case_testwarelocation = pty[30].field_value

        case_description = pty[5].field_value

        case_Notes = pty[14].field_value

        case_Precondition = pty[34].field_value

        # define test case name
        f.write('<table class="smallerbordered" border="1" width="100%" style="table-layout:fixed;">\n<tbody>')
        f.write('<tr class="header"><td bgcolor="#add8e6" colspan="4">\n')
        f.write('<span class="finbsp;eldLabel">Test Case Name:&</span>')

        print(case_name)

        f.write(case_name+'</td></tr>')
        # define Qtest id
        f.write('<tr class="header"><td bgcolor="#add8e6" colspan="4">\n')
        f.write('<span class="fieldLabel">Test Case ID:&nbsp;</span>')

        print(qcase_id)

        f.write(qcase_id + '</td></tr>')
        # define test case headline
        f.write('<tr><td colspan="4">\n')
        f.write('<span class="fieldLabel">Headline:&nbsp;</span>\n')
        f.write('<span class="TYPE_tc_text plain">'+case_headline+'</span>')
        f.write('</td>\n')
        f.write('</tr>\n')

        # define test case state
        print(case_status)

        f.write('<tr>\n')
        f.write('<td>\n')
        f.write('<span class="fieldLabel">Test Case State:&nbsp;</span>\n')
        f.write('<span class="TYPE_tc_menu">'+case_status+'</span>')
        f.write('</td>\n')

        # define test case when to run state

        print(case_WhenToRun)
        f.write('<td>\n')
        f.write('<span class="fieldLabel">When to Run:&nbsp;</span>\n')
        f.write('<span class="TYPE_tc_menu">'+case_WhenToRun+'</span>')
        f.write('</td>\n')

        # define test case auto status

        print(case_AutoDevStatus)
        f.write('<td>\n')
        f.write('<span class="fieldLabel">Automation Development Status:&nbsp;</span>\n')
        f.write('<span class="TYPE_tc_menu">'+case_AutoDevStatus+'</span>')
        f.write('</td>\n')

        # define test case type
        print(case_type)

        f.write('<td>\n')
        f.write('<span class="fieldLabel">Execution Type:&nbsp;</span>\n')
        f.write('<span class="TYPE_tc_menu">'+case_type+'</span>')
        f.write('</td>\n')

        f.write('</tr>\n')

        # define CVB Products
        print(case_CVBProducts)

        f.write('<tr>\n')
        f.write('<td>\n')
        f.write('<span class="fieldLabel">CVB Products:&nbsp;</span>\n')
        f.write('<span class="TYPE_tc_menu">'+case_CVBProducts+'</span>')
        f.write('</td>\n')
        # define Feature Test
        print(case_FeatureTest)
        f.write('<td>\n')
        f.write('<span class="fieldLabel">Feature Test:&nbsp;</span>\n')
        f.write('<span class="TYPE_tc_menu">'+case_FeatureTest+'</span>')
        f.write('</td>\n')
        # define Function area

        print(case_Fucntion_Area)

        f.write('<td>\n')
        f.write('<span class="fieldLabel">Function Area:&nbsp;</span>\n')
        f.write('<span class="TYPE_tc_menu">'+case_Fucntion_Area+'</span>')
        f.write('</td>\n')
        # define tags

        print(case_Tags)
        f.write('<td>\n')
        f.write('<span class="fieldLabel">Tag:&nbsp;</span>\n')
        f.write('<span class="TYPE_tc_menu">'+case_Tags+'</span>')
        f.write('</td>\n')
        f.write('</tr>\n')
        # define controller type

        print(case_controllertype)
        f.write('<tr>\n')
        f.write('<td colspan="2">\n')
        f.write('<span class="fieldLabel">Controller Type:&nbsp;</span>\n')
        f.write('<span class="TYPE_tc_menu">' + case_controllertype + '</span>')
        f.write('</td>\n')

        # define mode
        print(case_mode)
        f.write('<td colspan="2">\n')
        f.write('<span class="fieldLabel">Mode:&nbsp;</span>\n')
        f.write('<span class="TYPE_tc_menu">' + case_mode + '</span>')
        f.write('</td>\n')
        f.write('</tr>\n')

        # define testware location

        print(case_testwarelocation)

        f.write('<tr>\n')
        f.write('<td colspan="4" style="word-break: break-word;overflow:hidden;">\n')
        f.write('<span class="fieldLabel">Testware Location:&nbsp;</span>\n<br>')
        f.write('<span class="TYPE_tc_menu">' + case_testwarelocation + '</span>')
        f.write('</td>\n')
        f.write('</tr>\n')
        # define descriptions

        print(case_description)
        f.write('<tr>\n')
        f.write('<td colspan="4" style="word-break: break-word;overflow:hidden;">\n')
        f.write('<span class="fieldLabel">Test Case Description:&nbsp;</span>\n<br>')
        f.write('<span class="TYPE_tc_menu">'+case_description+'</span>')
        f.write('</td>\n')
        f.write('</tr>\n')

        # define notes

        print(case_Notes)

        f.write('<tr>\n')
        f.write('<td colspan="4" style="word-break: break-word;overflow:hidden;">\n')
        f.write('<span class="fieldLabel">Notes:&nbsp;</span>\n<br>')
        f.write('<span class="TYPE_tc_menu">'+case_Notes+'</span>')
        f.write('</td>\n')
        f.write('</tr>\n')

        # define case Precondition

        print(case_Precondition)

        f.write('<tr>\n')
        f.write('<td colspan="4" style="word-break: break-word;overflow:hidden;">\n')
        f.write('<span class="fieldLabel">Precondition:&nbsp;</span>\n<br>')
        f.write('<span class="TYPE_tc_menu">'+case_Precondition+'</span>')
        f.write('</td>\n')
        f.write('</tr>\n')

        # define test case step
        # prepare the list srcs and downloaded picture

        f.write('<tr>\n')
        f.write('<td colspan="4" style="word-break: break-word;overflow:hidden;" id="ProcessTable" valign="top">\n')
        f.write('<table style="width:98%" border="1" class="TYPE_tc_table">\n')
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
        f.write('</tbody>\n</table>\n')
        f.write('</tbody>\n</table>\n')
        f.write('</body>\n')
        # f.close()
        subprocess.call([pname, current_dir+'\\'+'NewTest.html'])
