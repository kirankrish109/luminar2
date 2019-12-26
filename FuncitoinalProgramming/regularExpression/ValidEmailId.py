import re
str = input("enter the string:")
# x='[A-Za-z0-9 ! # $ % & , * + - / = ? ^ _ ` { |][@][gmail/yahoo][.com/.in/.co]'
x='[a-z0-9! # $ % & , * + - / = ? ^ _ ][@]gamil/yahoo .com/.in'
match=re.fullmatch(x,str)
if(match!=None):
    print("valid")
else:
    print("invalid")