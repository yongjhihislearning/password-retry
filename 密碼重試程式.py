# 密碼重試程式
# 先在程式碼中 設定好密碼 password = 'a123456'
# 讓使用者[最多輸入3次密碼]
# 不對的話，就印出"密碼錯誤! 還有＿次機會"
# 對的話，就印出"登入成功!"
i = 2
while True:
    password = input('請輸入密碼: ')
    if password == 'a123456':
         print('登入成功')
         break
    elif i == 0:
         break
    else:
    	print('密碼錯誤! 還有', i, '次機會')
    	i = i - 1