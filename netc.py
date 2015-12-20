import sys
import socket
import getopt
import threading
import subprocess

#define some global variables
listen		= False
command		= False
upload		= False
execute		= " "
target		= " "
upload_destination		= " "
port		= 0

def usage():
	print "net tool"
	print
	print "usage: netc.py -t target_host -p port"
	print "-l --listen  -l listen on [host]:[port] for incoming connections"
	print "-e --execute=file_to_rn - execute the give file upon receiving connection"
	print "-c --comand initailize a command shell"
	print "-u --upload=destination - upon reveiving connection upload"
	sys.exit(0)


def client_sender(buffer):

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
			#connect to target
			client.connect((target_host))

			if len(buffer):
					client.send(buffer)

			while True:
					recv_len = 1
					response = " "

					while recv_len:
						data = client.recv(4096)
						recv_len = len(data)
						response+= data

						if recv_len < 4096:
							break
					print response,

					buffer = raw_input("")
					buffer += "\n"

					client.send(buffer)

	except:
			print"[*] Exception. Exiting"
			client.close()

def server_loop():
		global target

		if not len(target):
				target = "0.0.0.0"

		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((target,port))
		server.listen(5)

		while True:
				client_socket, addr = server.accept()

				client_thread = threading.Thread(target=client_handler, 
					args=(client_socket,))
					client_thread.start()


def run_command(command):
		command = command.rstrip()

		try:
			output = subprocess.check_output(comand,stderr=subprocess.
			STDOUT, shell=True)
		except:
			output = "Failed to execute command. \r\n"

		return output

def client_handler(client_socket):
	global	upload
	global execute
	global command

	if len(upload_destination):
		file_buffer = ""

		while True:
			data = client_socket.recv(1024)

			if not data:
				break
			else:
				file_buffer += data

		try:
			file_descriptor = open(upload_destination, "wb")
			file_descriptor.write(file_buffer)
			file_descriptor.close()

			client_socket.send("successfully saved file")
		except
			client_socket.send("failed to save file")

	if len(execute):
		output = run_command(execute)
		client.socket.send(output)

	if command:
		while True:
			client.socket.send("netc:#> ")

			cmd_buffer = ""
			while "\n" not in cmd_buffer:
				cmd_buffer += client_socket.recv(1024)
			response = run_command(cmd_buffer)
			client.socket.send(response)
			

def main():
	global listen
	global port
	global execute
	global command
	global upload_destination
	global target

	if not len(sys.argv[1:]):
		usage()

	#read the commandline options
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:"
		["help","listen","execute","target","port","command","upload"])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o,a in opts:
		if o in ("-h","--help"):
			usage()
		elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e","--execute"):
            execute = a
        elif o in ("-c","--comandshell"):
            command = True
        elif o in ("-u","--uplaod"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = init(a)
        else:
            assert	False, "Unhandled Option"

    #are we going to listen or just send data from stdin"
    if not listen and len(target) and port > 0:
    		#read in the buffer from the commandline 
    		#this will block so send crtl -d if not sending input
    		#to stdin
    		buffer = sys.stdin.read()

    		#send data off
    		client_sender(buffer)

    #we are going to listen dand potentially upload things, execute commands, etc
    if listen:
    		server_loop()




main()



