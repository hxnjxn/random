import sys, webbrowser

url = str(sys.argv[1])

print "[*] Generate a list of Google Dork search terms for an organization"

dorks = "site:{0} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini \n \
site:{0} ext:sql | ext:dbf | ext:mdb \n \
site:{0} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup | ext:log \n \
site:{0} ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv \n \
site:{0} intext:\"sql syntax near\" | intext:\"syntax error has occurred\" | intext:\"incorrect syntax near\" | intext:\"unexpected end of SQL command\" | intext:\"Warning: mysql_connect()\" | intext:\"Warning: mysql_query()\" | intext:\"Warning: pg_connect()\" \n \
site:{0} type:php | type:asp \n \
site:{0} inurl:admin | inurl:uploads".format(url)

print dorks

d = open('urls.txt', 'w')
d.write("http://%s" % dorks)


dorks_2 = d.readlines()

webbrowser.open_new_tab(dorks_2)
