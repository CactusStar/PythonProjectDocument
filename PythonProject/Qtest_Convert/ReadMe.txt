0. Python 3 needed
1. Need Chrome installed
2. Need Related Chrome webdriver installed
3. Need update Account_data.json file: 
      token: should be your personal token
	How to find your token:
	  1. login Qtest
          2. click the Resoure button at the top right corner
          3. expand API & SDK item 
          4. copy the string after Bearer Token, note no need to contain the "Bearer" 
      Product_id: the number in qtest url after ra.qtestnet.com/p/
4. Right click on ReadQtest.cmd, click Run as Administrator

Note: if you set value "self_login" to "False" in Account_Data.json, means you want to click the login button by yourself(This is for SDE zone sometimes login on Qtest have issue)