http_basic_auth_passwd_scanner.py
=======================================
a simple multi-thread http_basic_auth_passwd_scanner 

how to use 
---------------
1,the scanner use requests ,so if it not in your system install it
    pip install requests
2,modily the config.py
    #set Number of concurrent threads
    threadsNo = 5
    #set the scan url
    url = 'http://192.168.1.1'
    #set username list,must be a list
    usernameList = ['admin','root','administrator']
    #set retry geturl times 
    trytimes= 3
    #set every scan sleep time
    sleep_time=0.02
3,if you have a big password_dict cover passwddict.txt

4,run it
    python http_basic_auth_passwd_scanner.py
    

    
in chinese
-----------------
���߳�·�������Ƿ�����������֤����̽�⹤��
============================================

ʹ�÷���
-------------
1,�����õ���rqeuestsģ��,�����ϵͳ��û��,��Ҫ��װ
    pip install requests
2,���������ļ�config.py
     #set Number of concurrent threads �����߳���,���������10
    threadsNo = 5
    #set the scan url      ���÷�������·�ɵ�ַ
    url = 'http://192.168.1.1'
    #set username list,must be a list �����û����б�
    usernameList = ['admin','root','administrator']
    #set retry geturl times     ��������url���ִ���ʱ�����Դ���
    trytimes= 3
    #set every scan sleep time   ����ÿ��̽��ʱ��
    sleep_time=0.02
3,�Ҹ�����ֵ��滻�ֵ��ļ� password_dict.txt

4,����
    python http_basic_auth_passwd_scanner.py
