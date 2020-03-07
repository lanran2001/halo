import os
import re
#import nltk
def part(x):
    vec ={}
    for line in x[0]:
        data=re.split(r'[\s\r\n!@#$%^&*(|)<>/\\,.;:\'"[\]{\}0123456789+=\-_]',line)
        for word in data:
            if vec.get(word)==None:
                vec[word]=1
            else: vec[word]+=1
    ans=[]
    words=vec.keys()
    for key in words:
        ans.append([key,vec[key],x[1]])
    return ans

def operate(txt,total):
    for key in txt:
        if key[0]=='':continue
        if total.get(key[0])==None:
            total[key[0]]=[]
        total[key[0]].append([key[1], key[2]])

def printOut(total_dir):
    list=total_dir.keys()
    for words in list:
        tuple=total_dir[words]
        print("The word is "+words)
        for x in tuple:
            print("<frequency=",x[0],"  article=",x[1],">")
if __name__=='__main__':
    file_dir="20_newsgroups"
    num=1
    valid_text=[]
    for tuples in os.walk(file_dir,topdown=True):
        for file in tuples[2]:
            file_name=tuples[0]+os.sep+file
            flow =open(file_name,'r',encoding='utf-8',errors='ignore')
            lines =[]
            flag=0
            for line in flow:
                if flag==1:
                    lines.append(line)
                result1=re.match(r'Lines:',line)
                if result1!=None:
                   result1.group()
                if flag==0 and result1!=None:
                    flag=1
            valid_text.append([lines,num])
            num+=1
    #finish the valid text extraction
    total_list=[]
    for txt in valid_text:
        total_list.append(part(txt))
    total_dir={}
    for txt in total_list:
        operate(txt,total_dir)
    total_keys=total_dir.keys()
    printOut(total_dir)