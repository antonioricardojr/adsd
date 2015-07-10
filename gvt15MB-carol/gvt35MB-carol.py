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
		if len(line) == 6 and not line[0] == "Esgotado":
			ip = line[2].replace(":","")
			package_bytes = line[3].replace("bytes=", "")
			time_ms = line[4].replace("tempo=", "").replace("ms", "")
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

file_names = ["arquivo4.txt", "arquivo5.txt", "arquivo6.txt", "arquivo7.txt", "arquivo8.txt", 
			  "arquivo9.txt", "arquivo10.txt", "arquivo11.txt", "arquivo12.txt", "arquivo13.txt",
			  "arquivo14.txt", "arquivo15.txt"]

for name in file_names:
	write_in_f_resp(name, 1,101,"GVT35MB-carol.txt")