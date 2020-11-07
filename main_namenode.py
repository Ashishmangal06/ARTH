import os

def namenode_configuration():

	os.chdir("/etc/hadoop/")
	myfile1 = open("hdfs-site.xml","w")
	myfile1.write('<?xml version="1.0"?>\n')
	myfile1.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n')
	myfile1.write("<!-- Put site-specific property overrides in this file. -->\n\n")
	myfile1.write("<configuration>\n")
	myfile1.write("<property>\n")
	myfile1.write("<name>dfs.name.dir</name>\n")
	myfile1.write("<value>/namenode</value>\n")
	myfile1.write("</property>\n")
	myfile1.write("</configuration>\n")
	myfile1.close()

	os.system("ifconfig enp0s3 | grep -E 'inet.[0-9]' | grep -v '127.0.0.1' | awk '{ print $2}' > ips.txt")

	myfile = open("ips.txt")
	content = myfile.read()
	ips = content.split("\n")
	myfile.close()
	ip = ips[0]

	os.chdir("/etc/hadoop/")
	myfile2 = open("core-site.xml","w")
	myfile2.write('<?xml version="1.0"?>\n')
	myfile2.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n')
	myfile2.write("<!-- Put site-specific property overrides in this file. -->\n\n")
	myfile2.write("<configuration>\n")
	myfile2.write("<property>\n")
	myfile2.write("<name>fs.default.name</name>\n")
	myfile2.write("<value>hdfs://{ip_address}:9001</value>\n".format(ip_address = ip))
	myfile2.write("</property>\n")
	myfile2.write("</configuration>\n")
	myfile2.close()

	os.system("cd")
	os.system("hadoop namenode -format")

	os.system("hadoop-daemon.sh start namenode")
	os.system("jps")