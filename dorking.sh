me: dorks_generator.sh
# Desc: Generate a list of Google Dork syntax search terms for a given domain
#

echo ""; echo "		-= dorks_generator.sh =-"
echo "[*] Generate a list of Google Dork search terms for an organization"
read -p "[*] Enter domain to use for Google Dorking, (example.com): " baseurl
cat << EOF >> $baseurl.dorks # Will prevent output of below echo's from being displayed; can then use column to print the output from the file
[-] Search for directory listing vulnerabilities: 	site:$baseurl intitle:index.of
[-] Search for configuration files: 			site:$baseurl ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini
[-] Search for database files: 				site:$baseurl ext:sql | ext:dbf | ext:mdb
[-] Search for log files: 				site:$baseurl ext:log
[-] Search for backup and old files:			site:$baseurl ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup
[-] Search for login pages: 				site:$baseurl inurl:login
[-] Search for publicly exposed documents: 		site:$baseurl ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv
[-] Search for SQL errors: 				site:$baseurl intext:\"sql syntax near\" | intext:\"syntax error has occurred\" | intext:\"incorrect syntax near\" | intext:\"unexpected end of SQL command\" | intext:\"Warning: mysql_connect()\" | intext:\"Warning: mysql_query()\" | intext:\"Warning: pg_connect()\"

Need more dorks? https://www.exploit-db.com/google-hacking-database/
EOF
echo "[*] Done. File saved as $baseurl.dorks"
