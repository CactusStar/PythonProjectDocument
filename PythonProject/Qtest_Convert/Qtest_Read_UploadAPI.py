# navigate to Chrome.exe location
# cmd execute 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"'
ACTIVATE_THIS = r'..\new_env\Scripts\activate_this.py'
with open(ACTIVATE_THIS, 'r') as f:
    exec(f.read(), dict(__file__=ACTIVATE_THIS))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import qtest_swagger_client
import json

# Get globle variable for download path
env_dist = os.environ
user_profile = env_dist.get('USERPROFILE')
pic_path = user_profile + '\\' + 'Downloads'
# Get browser
json_file = open('Account_Data.json', 'rb')
json_data = json.load(json_file)
browser = json_data['brower']
if browser == "chrome":
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # chrome_options.add_argument('--headless')
    chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    # os.system('cd C:\Program Files (x86)\Google\Chrome\Application&&start chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"')
elif browser == "firefox":
    firefox_options = Options()
    firefox_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Firefox(executable_path="geckodriver")
    # os.system('cd C:\Program Files\Mozilla Firefox&&start firefox.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"')
class QtestUtilsLgx(object):
    def __init__(self, apikey):
        qtest_swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
        qtest_swagger_client.configuration.api_key['Authorization'] = apikey
        self._testcase_api = None


    def generate_api_inst(self):
        self._testcase_api = qtest_swagger_client.TestcaseApi()

    def a(self, p_id, testcaseid):
        cases = self._testcase_api.get_test_case(project_id=p_id, test_case_id=testcaseid)
        return cases


def write_css_file():

    f1 = open(r'mystyle.css', 'w', encoding='utf-8')
    f1.write('table.smallerbordered {\npage-break-before: auto;\nborder-collapse: collapse;\nborder: 1px solid #3d3f3d;\nfont-size: 1em;\nfont-family: Arial;\n}\n')
    f1.write('.fieldLabel {font-weight: bold;\nvertical-align: top;\n}\n')
    f1.write('.TYPE_tc_table {border-collapse: collapse;\nborder: 1px solid #3d3f3d;\nfont-size: 1em;\n}\n')
    f1.write('.TYPE_tc_table tr.header {white-space: nowrap;\nbackground-color: #3d3f3d;\nborder: 1px solid #3d3f3d !important;\nborder-spacing: 2px;\npadding: 2px;\ncolor: white;\n}\n')
    f1.write('.TYPE_tc_table tr.header th.right {border-right: 1px solid #3d3f3d !important;\n}\n')
    f1.write('.TYPE_tc_table tr.header th.left {border-left: 1px solid #3d3f3d !important;\nwidth: 20px;\n}\n')
    f1.close()


def log_in(selfLogIn):

    try:
        driver.get('https://ra.qtestnet.com/portal/loginform')
        if selfLogIn == True:
            driver.find_element_by_class_name('btn-primary').click()
    except:
        print('Already login')

    if selfLogIn == True:
        time.sleep(5)
        try:
            remove_cycles = driver.find_elements_by_class_name("glyphicon-remove-circle")
            for remove_cycle in remove_cycles:
                remove_cycle.click()
            driver.find_element_by_id("reloginBtn").click()
        except:
            print("not reach the maximam login account")

product_id = json_data['Product_id']

token = json_data['token']

self_login = json_data['self_login']

write_css_file()

pname = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

log_in(self_login)

counter = True

while 1:
    # Based on url change and user confirm need convert
    url = driver.current_url
    try:
        if counter:
            print("This is the first time")
            url = "This is for the first time login test case convert"
            del counter
    except:
        print("This is not the first time")

    time.sleep(5)

    url_after = driver.current_url
    if url == url_after:
        print("Before url: "+url)
        print("After url: " + url_after)
        continue
    else:
        print('#############################################################################')
        user_input = input("if you accept to convert the page: ")
        if user_input == 'y':

            f = open(r'NewTest.html', 'w', encoding='utf-8')
            # define css file
            f.write('<head>\n<link rel="stylesheet" type="text/css" href="mystyle.css" />\n</head>')
            f.write('<body id="tinymce" class="mce-content-body" data-id="propCf6414639_editorNode" contenteditable="false">')
            # get qtest id
            temp_id = driver.current_url
            qcase_id = temp_id.split("id=")[1]

            # Get all info by the API
            Qtest = QtestUtilsLgx(token)
            Qtest.generate_api_inst()

            tcase = Qtest.a(product_id, qcase_id)
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
            f.write('<span class="fieldLabel">Test Case Name:&nbsp;</span>')

            print(case_name)

            f.write(case_name+'</td></tr>')
            # define Qtest id
            temp_id = driver.current_url
            case_id = temp_id.split("id=")[1]
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
            try:
                image_srcs = driver.find_elements_by_tag_name('img')
            except:
                print('No image exist')
            if image_srcs:
                srcs = []
                add_pics = []
                print(len(image_srcs))
                for image in image_srcs:
                    src = image.get_attribute('src')
                    if 'attachmentId' in src:
                        srcs.append(src)
                        before = dict([(f, None) for f in os.listdir(pic_path)])
                        driver.get(src)
                        time.sleep(5)
                        after = dict([(f, None) for f in os.listdir(pic_path)])
                        added = [f for f in after if not f in before]
                        for add in added:
                            add_fullpath = pic_path + '\\' + add
                            add_pics.append(add_fullpath)
                        print(src)
                        print(added)

            f.write('<tr>\n')
            f.write('<td colspan="4" style="word-break: break-word;overflow:hidden;" id="ProcessTable" valign="top">\n')
            f.write('<table style="width:98%" border="1" class="TYPE_tc_table">\n')
            f.write('<tbody>\n')
            f.write('<tr class="header">\n')
            f.write('<th class="left right" border="1" colspan="3" >Test Process</th>\n')
            f.write('</tr>\n')
            f.write('<tr class="header">\n')
            f.write('<th class="left">#</th>\n')
            f.write('<th>Procedure</th>\n')
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
                    loopcount = len(srcs)
                    for pic_count in range(loopcount):
                        input_step = input_step.replace(srcs[pic_count], add_pics[pic_count])
                    f.write('<td align="left">\n')
                    f.write(input_step)
                    f.write('</td>\n')
            f.write('</tr>\n')
            f.write('</tbody>\n</table>\n')
            f.write('</tbody>\n</table>\n')
            f.write('</body>\n')
            f.close()

            os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" NewTest.html')
