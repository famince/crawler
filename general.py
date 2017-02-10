import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('createing project ' + directory) 
        os.makedirs(directory)

create_project_dir('xiami')

# Create queue and crwaled files (if not created)
def create_data_files(project_name, base_url):
    queue   = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Create a nwe file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

create_data_files('xiami', 'http://www.xiami.com/')

# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete the contents of a file
def delete_file_content(path):
  with open(path, 'w'):
      pass

# Read a file and convert eachto set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:    
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a new line to the file
def set_to_file(links, file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file, link)

