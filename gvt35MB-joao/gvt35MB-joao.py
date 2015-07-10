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
		if len(line) == 6:
			ip = line[2].replace(":","")
			package_bytes = line[3].replace("bytes=", "")
			time_ms = line[4].replace("time=", "").replace("ms", "")
			TTL = line[5].replace("TTL=","")
		else:
			ip = "NA"
			package_bytes = "NA"
			time_ms = "NA"
			TTL = "NA\n"

		f_resp.write(ip + "," + package_bytes + "," + time_ms + "," +
	 				 TTL)

	f.close()
	f_resp.close()

file_names = ["carol.txt", "chuva.txt", "domingo.txt", "domingo_dedicado.txt","domingo_noite.txt",
			  "domingoteste.txt", "exp.txt", "joaoonzeedezessete.txt", "joaoseisemeiapm.txt",
			  "joaoseishorascincominutospm.txt", "joaoseispm.txt", "joaowireless.txt"]

for name in file_names:
	write_in_f_resp(name, 1,101,"GVT35MB-joao.txt")