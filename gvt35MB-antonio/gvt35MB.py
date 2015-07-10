import os

def file_is_empty(path):
    return os.stat(path).st_size==0

def write_in_f_resp(file_name, from_line, to_line, 
					file_resp_name):
	
	f = open(file_name, "r")
	f_resp = open(file_resp_name, "a")
	if file_is_empty(file_resp_name):
		f_resp.write("ip, bytes, time, TTL\n")

	f_lines = f.readlines()
	for i in range(from_line,to_line):
	
		line = f_lines[i].split(" ")
		if len(line) == 8:
			ip = line[3].replace(":","")
			package_bytes = line[0]
			time_ms = line[6].replace("time=", "")
			TTL = line[5].replace("ttl=","")
		else:
			ip = "NA"
			package_bytes = "NA"
			time_ms = "NA"
			TTL = "NA"

		f_resp.write(ip + "," + package_bytes + "," + time_ms + "," +
	 				 TTL +"\n")

	f.close()
	f_resp.close()

file_names = ["velox35MB-2jul-6pm.txt", "velox35MB-2jul-605pm.txt", "velox35MB-2jul-630pm.txt",
		"velox35MB-3jul-00am.txt", "gvtCarol.txt", "gvtCarol2.txt", "gvtCarol3.txt", "gvtCarol4.txt",
		"gvtCarol5.txt", "gvtCarol6.txt", "gvtCarol7.txt", "gvtCarol8.txt"]

for name in file_names:
	write_in_f_resp(name, 1,101,"GVT35MB-antonio.txt")