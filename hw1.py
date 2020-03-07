import os
import re

if  __name__=='__main__':
    #f="C:\\Users\\Amayama_Haru\\OneDrive\\大三下\\信息检索\\codes\\lab1\\20_newsgroups"
    counts = {}
    #f="C:\\Users\\Amayama_Haru\\OneDrive\\code\\20_newsgroups"
    f="20_newsgroups"
    for tuples in os.walk(f,topdown=True):
        for file in tuples[2]:
            data = open(tuples[0]+os.sep+file,'r',encoding='utf-8',errors='ignore')
            text =data.read()
            ans = re.split(r'[ \s\r\n*&%$#:@"!;,./?1234567890^=+`~><()}{|\]\'\\\-[_]',text)
            for words in ans:
                now =words.lower()
                if counts.get(now) == None:
                    counts[now]=1
                else:
                    counts[now]+=1
            data.close()
    print("finish")
    sol = counts.keys()
    for x in sol:
        y=x.lower()
        print(y+" ")
        print(counts[y])