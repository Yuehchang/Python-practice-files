#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:27:02 2017

@author: changyueh
"""
import unicodedata as unicd
"""
在unicodedata裡面
lookup() => 接收一個不分大小寫的名稱，回傳一個Unicode字元
name() => 接收一個Unicode字元，回傳一個大寫名稱
"""
#逼寫測試函數：接收Python Unicode字元，查看名稱並用該名稱再次查看字元 p159
def unicode_test(value):
    import unicodedata as unicd
    name = unicd.name(value)
    value2 = unicd.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))
#test
#ASCII字母
unicode_test('A')  # output => value="A", name="LATIN CAPITAL LETTER A", value2="A"
#ASCII標點符號
unicode_test('$')  # output => value="$", name="DOLLAR SIGN", value2="$" 
#Unicode貨幣字元
unicode_test('\u00a2')
unicode_test('\u20ac')

#不一定想顯示的一定有Unicode字元圖像，所以可能會顯示一些預留字元 page159
unicode_test('\u2603')

#從網上複製字元
place = 'café'
place # output => café 成功

# é => E WITH ACUTE, LATIN SMALL LETTER = 00e9
unicode_test('\u00e9')
unicd.name('\u00e9')
unicd.lookup('E WITH ACUTE, LATIN SMALL LETTER') # get error, correct answer is down below
unicd.lookup('LATIN SMALL LETTER E WITH ACUTE') # correct sequence

place2 = 'caf\u00e9'
place2
place3 = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
place3

#也可以用附加的方式建立字串
u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
print (u_umlaut)
drink = 'Gew' + u_umlaut + 'rztraminer'
print (drink)
print ('Now I can finally have my', drink, 'in a', place2 + '.')

#len()會計算Unicode字元的數目，不是byte數
len('$') #output = 1
len('\U0001f47b') #output = 1 
unicd.name('\U0001f47b') # '\U0001f47b' = 'GHOST'

"""
以UTF-8編碼與解碼
與外界交換資料時，就須要 
1. 一種將字元字串編碼成byte的方式
2. 一種將byte解碼成字元字串的方式
"""
#字串編碼成byte => encode() // 表7-1
snowman = '\u2603'
len(snowman) # output = 1 
ds = snowman.encode('utf-8')
len(ds) # output = 3 這邊是回傳byte的數量
print (ds) # output => b'\xe2\x98\x83'

ds1 = snowman.encode('ascii') #ASCII無法encode"\u2603"
#encode的第二個引數可以幫助排除避免編碼例外
snowman.encode('ascii', 'ignore') # output => b''引號內為空
snowman.encode('ascii', 'replace') # output => b'?'引號內為問號
#使用backslashreplace來產生Python Unicode，跟unicode-escape一樣
snowman.encode('ascii', 'backslashreplace')
#列印轉義序列版本，會產生字元實體字串，可在網頁中使用 page163：
snowman.encode('ascii', 'xmlcharrefreplace')

#解碼page163
place = 'caf\u00e9'
place
type(place) # output => str
#用UTF-8格式，將place編碼成byte變數
place_bytes = place.encode('utf-8')
place_bytes #output => b'caf\xc3\xa9'
type(place_bytes) #output => bytes, 有五個byte
#解碼回Unicode字串
place2 = place_bytes.decode('utf-8')
place2
place3 = place_bytes.decode('ascii') #error
#ASCII會丟出例外，但其他不一定會
place4 = place_bytes.decode('latin-1') # place4 = 'cafÃ©'
place5 = place_bytes.decode('windows-1252') #place5 = 'cafÃ©'

#格式
#以％來表示的舊方式
"""
%s 字串 / %d 十進位 / %x 十六進位 / %o 八進位
%f 十進位浮點數 / %e 指數浮點數 / %g 十進位或指數浮點數
%% 字面%
example = page165
在%s之後的多個項目、必須放入tuple裡面
"""

#practice ％與類型之間添加其他值
n = 42 
f = 7.03 
s = 'string cheese'

'%d %f %s' % (n, f, s)#預設寬度
'%10d %10f %10s' % (n, f, s)#每個變數最小欄位寬度=10、向右對齊、用空格填充左邊
'%-10d %-10f %-10s' % (n, f, s)#同上、但是向左對齊
'%10.4d %10.4f %10.4s' % (n, f, s) #同上上、但會截斷字串、並將浮點數限制為小數點後四位
'%.4d %.4f %.4s' % (n, f, s) #同上、但向右對齊、沒有欄位寬度
'%*.*d %*.*f %*.*s' % (10, 4 , n, 10, 4, f, 10, 4, s)#用引數取得欄位寬度

#使用{}與format的新格式化方式
'{} {} {}'.format(n, f, s)#最簡單的方法
'{2} {0} {1}'.format(f, s, n)#新方法中可以指定順序，效果等同上面
'{n} {f} {s}'.format(n=42, f=7.03, s='string cheese')#可以用字典或具名引數在指定符加入他們的名稱

d = {'n' : 42, 'f' : 7.03, 's' : 'string cheese'}
'{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other') #使用字典，有指定位置所以不用**

'{0:n} {1:f} {2:s}'.format(n, f, s) #新方式用位置引數
'{n:d} {f:f} {s:s}'.format(n=42, f=7.03, s='string cheese')#新方式用具名引數

#一樣可以提供其他選項（最小欄位、最大字元寬度、對齊）
'{0:10d} {1:10f} {2:10s}'.format(n, f, s)#最小寬度＝10、右對齊
'{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s)#最小寬度＝10、右對齊，但更明顯
'{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s)#最小寬度＝10、左對齊
'{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s)#最小寬度＝10、置中
'{0:>10d} {1:>10.4f} {2:>10.4s}'.format(n, f, s)#一樣可以使用精度值（小數點後幾位）、但是新版的整數不能用會報錯

#填充字元，讓空格填充你選定的值或符號
'{0:!^20s}'.format('BIG SALE')#選定的東西必須在(>, <, ^之前)，20為要展現多少格子數

#用正規表達式來匹配 page169 用來找東西！
#example 
result = re.match('You', 'Young Frankenstein')#You是模式、Young Frankenstein是來源（也就是需要檢查的字段）
#example2
youpattern = re.compile('You')#先編譯模式
result2 = youpattern.match('Young Frankenstein')
"""
match()會檢查來源是否以該模式開頭
search()會檢查第一個匹配項目，如果有的話
findall()會回傳所有不重疊的匹配，如果有的話
spilt()會使用模式，在匹配處分割來，並回傳一串字串片段
sub()會使用另一個取代引數，並將來源內所有匹配模式的項目換成取代引數
"""
#match()
import re
source = 'Young Frankenstein'
m = re.match('You', source) 
if m: #match 回傳一個物件，以查看有沒有匹配項目
    print(m.group())

m1 = re.match('^You', source)
if m1:
    print(m1.group())

m2 = re.match('Frank', source)
if m2:
    print(m2.group())#match是查看開頭

m3 = re.search('Frank', source)
if m3:
    print("search", m3.group(), "return:", source)

m4 = re.match('.*Frank', source)
if m4:
    print(m4.group()) #.代表任何單一字元、*代表在他前面的東西（or任何數量）、.*一起用代表任何數量的字元
#因此上述會回傳，我們匹配目標：Frank之前的全部字元

#search() m3

#findall()
find_n = re.findall('n', source)
find_n #source裡面有4個n => output = ['n','n','n','n']

find_behind_n = re.findall('n.', source)
find_behind_n #只有返回三個n

find_all_behind_n = re.findall('n.?', source)
find_all_behind_n #加上?代表無論n後面有無字元都是需要回傳的

#split()
split_up = re.split('n', source)
split_up #用n分段點

#sub()
replace_n_to_qmark = re.sub('n', '?', source)
replace_n_to_qmark #有點類似replace()但是供模式使用，而不是原字串

#模式：特殊字元
"""
\d => number
\D => non-number
\w => english & number
\W => non-english & number
\s => space
\S => non-space
\b => 一個單字範圍
\B => 一個非單字範圍
"""
import string
printable = string.printable
len(printable) #length = 100            
printable[0:50]
printable[50:]

re.findall('\d', printable) #找數字
re.findall('\w', printable) #找數字、英字母、底線（這個算英數的成員）
re.findall('\s', printable) #空白

#正規表達式並非只限於ASCII
x = 'abc' + '-/*' + '\u00ea' + '\u0115'             
re.findall('\w', x) # => 也有找出來後兩個unicode字元

#模式：使用指定符 page174有很多指定符範例
#practice1
source1 = """I wish I may, I wish I might
Have a dish of fish tonight."""

re.findall('wish', source1) #找出任何地方的wish
re.findall('wish|fish', source1) #找出任何地方的wish & fish
re.findall('^wish', source1) #找出開頭的wish => 回傳[]空白list
re.findall('^I wish', source1) #找出開頭的I wish
re.findall('fish$', source1) #找出結尾的的fish => 回傳[]空白list
re.findall('fish tonight.$', source1) #找出結尾的fish tonight.
#Anchor錨點 => ^會找到收尋字段的開頭；＄會錨定至結尾；.$會匹配任何在行爲的字元（包括句點）
re.findall('fish tonight\.$', source1) #因為有真的.$用法所以轉義句點成\.
re.findall('[wf]ish', source1) #用ish找出wish & fish
re.findall('[wsh]+', source1) #找一個或多個w、s、h、ws、wh、sh
re.findall('ght\W', source1) #找後面沒有英數字元的ght
re.findall('I (?=wish)', source1) #找出wish之前的I
re.findall('(?<=I) wish', source1) #找出I之後的wish，I前面不能有空格，如果空格會視為收尋空格配I的字串
#有時候python會因為轉義字元與正則表達式產生衝突，此時要加上r
re.findall(r'\bfish', source1) #\b再轉義等於“倒退”，在正則表達式中等於一個單字範圍

#模式：指定匹配輸出
m = re.search(r'(. \bdish).*(\bfish)', source1)#Q1 為何兩個\b在不同地方
m.group()
m.groups()

#(?P< name > expr)晦匹配expr，將匹配像存入name
m1 = re.search(r'(?P<DISH>. \bdish).*(?P<FISH>\bfish)', source1)
m1.group() 
m1.groups() 
m1.group('DISH') 
m1.group('FISH')

#二進位資料 byte不可變、bytearray是可變的
blist = [1, 2, 3, 255] 
the_bytes = bytes(blist)
the_bytes_array = bytearray(blist) 
the_bytes[1] = 127 #不可變
the_bytes_array[1] = 127 #可變

#使用struct來轉換二進位資料
import struct 
valid_png_header = b'\x89PNG\r\n\x1a\n' 

data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
 
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width:', width, 'height:', height)
else:
    print('Not a valid PNG')

#想要反過來將python資料轉成byte => struct.pack()
struct.pack('>L', 154)
struct.pack('>L', 141)

#endian指定符 page180 // 格式指定符 page 181 表7-6

#用數量來取代 ">LL"
struct.unpack('>2L', data[16:24])

#用 "x" 跳過沒有興趣的
struct.unpack('>16x2L6x', data) #output同上

#用binascii()來轉換Byte / 字串
import binascii
valid_png_header = b'\x89PNG\r\n\x1a\n'
print(binascii.hexlify(valid_png_header))
print(binascii.unhexlify(b'89504e470d0a1a0a')) #也可以互相轉換

"""
Practice page183
"""
#Q1 
import unicodedata
mystery = '\U0001f4a9'
print (unicodedata.name(mystery)) # output PILE OF POO 大便emoji

#Q2 
pop_bytes = mystery.encode('UTF-8')
print (pop_bytes)             

#Q3 
pop_string = pop_bytes.decode('UTF-8')
print (pop_string) #output => 不等於Q1//這邊直接印出emoji 

if mystery == pop_string:
    print ('OMG, there is no different!!') #但是本質一樣
    
#Q4 
"""My kitty cat likes %s, 
My kiity cat likes %s, 
My kitty cat fell on his %s
And now thinks he's a %s""" % ('roast beef', 'ham', 'head', 'clam') #這個辦法會讓句子中間出現\n換行符號

poem = """
My kitty cat likes %s, 
My kiity cat likes %s, 
My kitty cat fell on his %s
And now thinks he's a %s
"""
args = ('roast beef', 'ham', 'head', 'clam')
print (poem % args) 

#Q5 
letter = """
Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially 
near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send 
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.

Thank you for your support.

Sincerely, 
{spokesman}
{job_title} """

#Q6 
reponse = {'salutation' : 'Mr.', 'name' : 'Chang', 'product' : 'Laptop', 'verbed' : 'exploded',
           'room' : 'Lab', 'animals' : 'kitty', 'amount' : '$10', 'percent' : '50', 'spokesman' : 'Yi-Tang',
           'job_title' : 'CEO'}

print(letter.format(**reponse))

#Q7
mammoth = """ 
We have seen the Queen of cheese,
Laying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial Show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled Queen of Cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great World's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek; then songs or glees
We could not sing o' Queen of Cheese. 

We'rt thou suspended from baloon,
You'd cast a shade, even at noon;
Folks would think it was the moon
About to fall and crush them soon. """

#Q8
import re 
re.findall('\bc.*', mammoth) # 回傳空list => 因為要在前面加個r
re.findall(r'\bc.*', mammoth) # 回傳c為開頭的所有東西
re.findall(r'\bc\w', mammoth) #回傳以c開頭的c與後一個字母
start_with_c = r'\bc\w*'
re.findall(start_with_c, mammoth) # 正解

#Q9 c開頭四字母單字
re.findall(r'\bc...\s', mammoth) #收尋到都是最後有個空格
re.findall(r'\bc...\b', mammoth) #沒有空格但是不實用
start_with_c4 = r'\bc\w{3}\b'
re.findall(start_with_c4, mammoth)

#Q10 r結尾的單字
end_with_r = r'\b\w.*r\b' #回傳r之前所有的值
end_with_r2 = r'\b\w*r\b'
re.findall(end_with_r2, mammoth)
"""
找r比較簡單，但是找l就會遇見困難
find_l_wrong = r'\b\w\*'l\b' => output = 'll'
find_l_wrong2 = r'\b[\w']*l\b' => 也是錯的，原因在p446
find_l = r'\b[\w\']*l\b' => 有中括號才是對的，代表可以放入任一中括號內的單字
"""

#Q11找出三母音連著的單字
pat = r'\b\w*[aeiou]{3}[^aeiou]\b' #回傳的只有三母音之後一個單字的
pat2 = r'\b\w*[aeiou]{3}[^aeiou]\w*\b' #回傳有beau\nIn
pat3 = r'\b\w*[aeiou]{3}[^aeiou\s]\w*\b' #但沒有找到beau
pat4 = r'\b\w*[aeiou]{3}[^aeiou\s]*\b' #這樣之後有母音的都不會出現
pat5 = r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b'
re.findall(pat5, mammoth)

#Q12
import binascii
gif = '47494638396101000010080000000000ffffff21f9' + '0401000000002c000000000100010000020144003b'
gif1 = binascii.unhexlify(gif)
print(gif1) #output => b'GIF89a\x01\x00\x00\x10\x08\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00;'

#Q13 yes
gif1[:6] == b'GIF89a' #True, 是byte
gif[:6] == 'GIF89a' #Flase, 是str

#Q14 
import struct
width, height = struct.unpack('<HH', gif1[6:10])  
print (width, height) #output應該是(1, 1) => 我的是(1, 4096)