import os

# Each website to be crawled is a separate folder/dir
def create_website_dir(directory):
	if not os.path.exists(directory):
		print ('Creating directory ... ' + directory)
		os.makedirs(directory)


# create crawled files and queue
def create_data_files(dir_name, base_url):
	queue = dir_name + '\queue.txt'      #links to be crawled
	crawled = dir_name + '\crawled.txt'	 #links that have been crawled
	if not os.path.isfile(queue):
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled, '')


#create new file
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()


#Add data to file
def append_to_file(path, data):
	with open(path, 'a') as file:  #file opened in append mode
		file.write(data + '\n')


#delete file data
def delete_file_data(path):
	open(path, 'w').close()


# Read file and convert data to set items
def file_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', '')) #removing new line from file data
	return results


# Adds data from set to file
def set_to_file(set_data, file):
	with open(file,"w") as f:
		for link in sorted(set_data):
			f.write(link+"\n")




