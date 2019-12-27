from hashlib import md5
from json import dump, load
from os import curdir, listdir, path, mkdir


blockchain_dir = curdir + '/blockchain/'


def get_hash(path_to_file):
	text = open(path_to_file, 'rb').read()

	return md5(text).hexdigest()


def check_integrity():

	result = []

	if path.exists(blockchain_dir) == False:
		mkdir(blockchain_dir)

	files = listdir(blockchain_dir)

	if files == []:
		return None

	files = sorted([element for element in files if element.isdigit() if int(element) > 0], key=int)

	for filename in files:

		text = load(open(blockchain_dir + filename))

		try:
			file_hash = text['hash']

		except KeyError:
			return None

		if str(file_hash).replace(" ", "") == "":
			continue

		prev_file = int(filename) - 1

		actual_hash = get_hash(blockchain_dir + str(prev_file))

		if file_hash == actual_hash:
			state = "Ok"
		else:
			state = "Corrapted"

		result.append(
						{
							'name': "Block " + filename,
							'state': state
						}
					)
		
	return result


def write_block(name, amount, to_whom):

	if path.exists(blockchain_dir) == False:
		mkdir(blockchain_dir)

	files = listdir(blockchain_dir)

	if files != []:
		files = sorted([int(element) for element in files if element.isdigit() if int(element) > 0], key=int)

		last_file = files[-1]

		filename = str(last_file + 1)

		path_to_file = blockchain_dir + str(last_file)

		prev_hash = get_hash(path_to_file)

	else:
		filename = '1'
		prev_hash=''

	data = {
		'from': name,
		'amount': amount,
		'to_whom': to_whom,
		'hash': prev_hash
	}

	with open(blockchain_dir + filename, 'w') as file:
		dump(data, file, indent=4, ensure_ascii=False)
