ACTIVATE_THIS = r'..\new_env\Scripts\activate_this.py'
with open(ACTIVATE_THIS, 'r') as f:
    exec(f.read(), dict(__file__=ACTIVATE_THIS))
# navigate to Chrome.exe location
# cmd execute 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"'
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time
import subprocess
import os

env_dist = os.environ

user_profile = env_dist.get('USERPROFILE')
pic_path = user_profile + '\\' + 'Downloads'

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# chrome_options.add_argument('--headless')
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)


def write_css_file():

    f1 = open(r'mystyle.css', 'w', encoding='utf-8')
    f1.write('table.smallerbordered {\npage-break-before: auto;\nborder-collapse: collapse;\nborder: 1px solid #3d3f3d;\nfont-size: 1em;\nfont-family: Arial;\n}\n')
    f1.write('.fieldLabel {font-weight: bold;\nvertical-align: top;\n}\n')
    f1.write('.TYPE_tc_table {border-collapse: collapse;\nborder: 1px solid #3d3f3d;\nfont-size: 1em;\n}\n')
    f1.write('.TYPE_tc_table tr.header {white-space: nowrap;\nbackground-color: #3d3f3d;\nborder: 1px solid #3d3f3d !important;\nborder-spacing: 2px;\npadding: 2px;\ncolor: white;\n}\n')
    f1.write('.TYPE_tc_table tr.header th.right {border-right: 1px solid #3d3f3d !important;\n}\n')
    f1.write('.TYPE_tc_table tr.header th.left {border-left: 1px solid #3d3f3d !important;\nwidth: 20px;\n}\n')
    f1.close()


def log_in():

    try:
        driver.get('https://ra.qtestnet.com/portal/loginform')
        driver.find_element_by_class_name('btn-primary').click()
    except:
        print('Already login')
    time.sleep(5)
    try:
        remove_cycles = driver.find_elements_by_class_name("glyphicon-remove-circle")
        for remove_cycle in remove_cycles:
            remove_cycle.click()
        driver.find_element_by_id("reloginBtn").click()
    except:
        print("not reach the maximam login account")


write_css_file()

pname = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

log_in()

log_in_url = driver.current_url

counter = True

while 1:
    # Based on user input test case id to covert

    # TestCaseID = input("Please Enter the test case id: ")
    # if TestCaseID == 'exit':
    #     break
    # driver.get('https://ra.qtestnet.com/p/86751/portal/project#tab=testdesign&object=1&id='+TestCaseID)
    # time.sleep(1)

    # Based on url change and user confirm need convert
    url = driver.current_url
    if (counter in vars()):
        print("This is the first time")
        url = "This is for the first time login test case convert"
        del counter

    time.sleep(5)

    url_after = driver.current_url
    if url == url_after:
        # print("Before url: "+url)
        # print("After url: " + url_after)
        continue
    else:
        print('#############################################################################')
        user_input = input("if you accept to convert the page: ")
        if user_input == 'y':

            f = open(r'NewTest.html', 'w', encoding='utf-8')
            # define css file
            f.write('<head>\n<link rel="stylesheet" type="text/css" href="mystyle.css" />\n</head>')
            f.write('<body id="tinymce" class="mce-content-body" data-id="propCf6414639_editorNode" contenteditable="false">')
            # define test case name
            f.write('<table class="smallerbordered" border="1" width="100%" style="table-layout:fixed;">\n<tbody>')
            f.write('<tr class="header"><td bgcolor="#add8e6" colspan="4">\n')
            f.write('<span class="fieldLabel">Test Case Name:&nbsp;</span>')

            case_name = driver.find_element_by_id('testcaseContentPane_innerEditor')\
                .find_element_by_class_name('dijitInlineEditBoxDisplayMode').get_attribute("innerHTML")
            print(case_name)

            f.write(case_name+'</td></tr>')
            # define Qtest id
            temp_id = driver.current_url
            case_id = temp_id.split("id=")[1]
            f.write('<tr class="header"><td bgcolor="#add8e6" colspan="4">\n')
            f.write('<span class="fieldLabel">Test Case ID:&nbsp;</span>')

            print(case_id)

            f.write(case_id + '</td></tr>')
            # define test case headline
            case_headline = driver.find_element_by_id('widget_propCf6414627')\
                .find_element_by_class_name('dijitInputContainer')\
                .find_element_by_tag_name('input').get_attribute('value')
            print(case_headline)

            f.write('<tr><td colspan="4">\n')
            f.write('<span class="fieldLabel">Headline:&nbsp;</span>\n')
            f.write('<span class="TYPE_tc_text plain">'+case_headline+'</span>')
            f.write('</td>\n')
            f.write('</tr>\n')

            # define test case state
            case_status = driver.find_element_by_id('widget_propStatusId_selectNode')\
                .find_element_by_class_name('dijitInputContainer')\
                .find_element_by_tag_name('input').get_attribute('value')
            print(case_status)

            f.write('<tr>\n')
            f.write('<td>\n')
            f.write('<span class="fieldLabel">Test Case State:&nbsp;</span>\n')
            f.write('<span class="TYPE_tc_menu">'+case_status+'</span>')
            f.write('</td>\n')

            # define test case when to run state
            case_WhenToRun = driver.find_element_by_id('widget_propCf6411938')\
                .find_element_by_class_name('dijitInputContainer')\
                .find_element_by_tag_name('input').get_attribute('value')
            print(case_WhenToRun)
            f.write('<td>\n')
            f.write('<span class="fieldLabel">When to Run:&nbsp;</span>\n')
            f.write('<span class="TYPE_tc_menu">'+case_WhenToRun+'</span>')
            f.write('</td>\n')

            # define test case auto status
            case_AutoDevStatus = driver.find_element_by_id('widget_propCf6411933_selectNode')\
                .find_element_by_class_name('dijitInputContainer')\
                .find_element_by_tag_name('input').get_attribute('value')
            print(case_AutoDevStatus)
            f.write('<td>\n')
            f.write('<span class="fieldLabel">Automation Development Status:&nbsp;</span>\n')
            f.write('<span class="TYPE_tc_menu">'+case_AutoDevStatus+'</span>')
            f.write('</td>\n')

            # define test case type
            case_type = driver.find_element_by_id('widget_propTypeId_selectNode')\
                .find_element_by_class_name('dijitInputContainer')\
                .find_element_by_tag_name('input').get_attribute('value')
            print(case_type)

            f.write('<td>\n')
            f.write('<span class="fieldLabel">Execution Type:&nbsp;</span>\n')
            f.write('<span class="TYPE_tc_menu">'+case_type+'</span>')
            f.write('</td>\n')

            f.write('</tr>\n')

            # define CVB Products
            case_CVBProducts = driver.find_element_by_id('widget_propCf6451893')\
                .find_element_by_class_name('dijitInputContainer')\
                .find_element_by_tag_name('input').get_attribute('value')
            print(case_CVBProducts)

            f.write('<tr>\n')
            f.write('<td>\n')
            f.write('<span class="fieldLabel">CVB Products:&nbsp;</span>\n')
            f.write('<span class="TYPE_tc_menu">'+case_CVBProducts+'</span>')
            f.write('</td>\n')
            # define Feature Test
            case_FeatureTest = driver.find_element_by_id('widget_propCf6411935')\
                .find_element_by_class_name('dijitInputContainer')\
                .find_element_by_tag_name('input').get_attribute('value')
            print(case_FeatureTest)
            f.write('<td>\n')
            f.write('<span class="fieldLabel">Feature Test:&nbsp;</span>\n')
            f.write('<span class="TYPE_tc_menu">'+case_FeatureTest+'</span>')
            f.write('</td>\n')
            # define Function area
            case_Fucntion_Area = driver.find_element_by_id('widget_propCf6447701')\
                .find_element_by_class_name('dijitInputContainer')\
                .find_element_by_tag_name('input').get_attribute('value')
            print(case_Fucntion_Area)

            f.write('<td>\n')
            f.write('<span class="fieldLabel">Function Area:&nbsp;</span>\n')
            f.write('<span class="TYPE_tc_menu">'+case_Fucntion_Area+'</span>')
            f.write('</td>\n')
            # define tags
            case_Tags = driver.find_element_by_id('propCf6414640').text
            print(case_Tags)
            f.write('<td>\n')
            f.write('<span class="fieldLabel">Tag:&nbsp;</span>\n')
            f.write('<span class="TYPE_tc_menu">'+case_Tags+'</span>')
            f.write('</td>\n')
            f.write('</tr>\n')
            # define controller type
            case_controllertype = driver.find_element_by_id('widget_propCf6585581').\
                find_element_by_class_name('dijitInputContainer').\
                find_element_by_tag_name('input').get_attribute('value')
            print(case_controllertype)
            f.write('<tr>\n')
            f.write('<td colspan="2">\n')
            f.write('<span class="fieldLabel">Controller Type:&nbsp;</span>\n')
            f.write('<span class="TYPE_tc_menu">' + case_controllertype + '</span>')
            f.write('</td>\n')

            # define mode
            case_mode = driver.find_element_by_id('widget_propCf6585583'). \
                find_element_by_class_name('dijitInputContainer'). \
                find_element_by_tag_name('input').get_attribute('value')
            print(case_mode)
            f.write('<td colspan="2">\n')
            f.write('<span class="fieldLabel">Mode:&nbsp;</span>\n')
            f.write('<span class="TYPE_tc_menu">' + case_mode + '</span>')
            f.write('</td>\n')
            f.write('</tr>\n')
            # define testware location
            case_testwarelocation = driver.find_element_by_id('widget_propCf6414630'). \
                find_element_by_class_name('dijitInputContainer'). \
                find_element_by_tag_name('input').get_attribute('value')
            print(case_testwarelocation)

            f.write('<tr>\n')
            f.write('<td colspan="4" style="word-break: break-word;overflow:hidden;">\n')
            f.write('<span class="fieldLabel">Testware Location:&nbsp;</span>\n<br>')
            f.write('<span class="TYPE_tc_menu">' + case_testwarelocation + '</span>')
            f.write('</td>\n')
            f.write('</tr>\n')
            # define descriptions
            driver.switch_to.frame('propDescriptionId_editorNode_ifr')

            case_description = driver.find_element_by_id('tinymce')\
                .find_element_by_tag_name('p').get_attribute("outerHTML")
            print(case_description)
            f.write('<tr>\n')
            f.write('<td colspan="4" style="word-break: break-word;overflow:hidden;">\n')
            f.write('<span class="fieldLabel">Test Case Description:&nbsp;</span>\n<br>')
            f.write('<span class="TYPE_tc_menu">'+case_description+'</span>')
            f.write('</td>\n')
            f.write('</tr>\n')

            # define notes
            driver.switch_to.default_content()

            driver.switch_to.frame('propCf6414639_editorNode_ifr')

            case_Notes = driver.find_element_by_id('tinymce').get_attribute("outerHTML")
            print(case_Notes)

            f.write('<tr>\n')
            f.write('<td colspan="4" style="word-break: break-word;overflow:hidden;">\n')
            f.write('<span class="fieldLabel">Notes:&nbsp;</span>\n<br>')
            f.write('<span class="TYPE_tc_menu">'+case_Notes+'</span>')
            f.write('</td>\n')
            f.write('</tr>\n')

            # define case Precondition
            driver.switch_to.default_content()

            driver.switch_to.frame('propPreconditionId_editorNode_ifr')

            case_Precondition = driver.find_element_by_id('tinymce').get_attribute("outerHTML")
            print(case_Precondition)

            f.write('<tr>\n')
            f.write('<td colspan="4" style="word-break: break-word;overflow:hidden;">\n')
            f.write('<span class="fieldLabel">Precondition:&nbsp;</span>\n<br>')
            f.write('<span class="TYPE_tc_menu">'+case_Precondition+'</span>')
            f.write('</td>\n')
            f.write('</tr>\n')

            # define test case step
            driver.switch_to.default_content()
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

            steps = driver.find_elements_by_class_name('gridxRow')

            print(len(steps))
            for i in range(len(steps)):
                z = i+1
                print(steps[i].get_attribute('innerHTML'))
                f.write('<tr>\n')
                f.write('<td align="left">\n')
                f.write('<b>'+str(z)+'</b>')
                f.write('</td>\n')
                cellvalues = steps[i].find_elements_by_class_name('gridxCell')
                print(cellvalues)
                print(len(cellvalues))
                count = len(cellvalues)
                for j in range(len(cellvalues)):
                    if count == j + 1:
                        continue
                    colid = cellvalues[j].get_attribute('colid')
                    colid_num = int(colid)
                    if 2 < colid_num < 5:
                        temp_str = cellvalues[j].get_attribute('outerHTML')
                        print('previous')
                        print(temp_str)
                        final_str = re.sub(r'class="gridxCell    " style="width: 350px; min-width: 350px; max-width: 350px;"', 'class="gridxCell"', temp_str, count=1)
                        loopcount = len(srcs)
                        for pic_count in range(loopcount):
                            final_str = final_str.replace(srcs[pic_count], add_pics[pic_count])
                        print('after modify with style')
                        print(final_str)
                        f.write(final_str)
            f.write('</tr>\n')
            f.write('</tbody>\n</table>\n')
            f.write('</tbody>\n</table>\n')
            f.write('</body>\n')
            f.close()

            subprocess.call([pname, 'NewTest.html'])
