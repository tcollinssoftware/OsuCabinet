import os

folders = os.listdir('Songs/')
songs_list = []
running = True
cwd = os.getcwd()

song_count = 0

while running == True:

	for i in folders:
		if os.path.isdir(cwd + '/Songs/' + i):
			songfolder = os.listdir(cwd + '/Songs/' + i)
			for j in songfolder:
				if '.osu' in j:
					#instead of printing, read the file and get the title and artist
					filepath = str(cwd + '/Songs/' + i + '/' + j)
					f = open(filepath, 'r', errors='replace')
					contents = f.readlines()
					song_title_raw = ''
					song_artist_raw = ''
					for k in contents:
						if 'Title:' in k:
							song_title_raw = k
						if 'Artist:' in k:
							song_artist_raw = k
					song_title_new = song_title_raw.replace('Title:', '')
					song_title_new2 = song_title_new.replace('\n', '')
					song_artist_new = song_artist_raw.replace('Artist:', '')
					song_artist_new2 = song_artist_new.replace('\n', '')
					song_artist_new3 = song_artist_new2.capitalize()
					song_info = str(song_artist_new3 + ' | ' + song_title_new2)
					print(song_info)
					songs_list.append(song_info)
					song_count += 1

					#print(contents)
					#print(j)
					break

	songs_list.sort()

	song_list_file = open('Song List.txt', 'w', errors='replace')
	song_list_file.write('Song List generated by Osu Cabinet, a program written by Israphen.\n')
	song_list_file.write('####################\n')
	for i in songs_list:
		song_list_file.write(i + '\n')

	song_list_file.write('####################\n')
	song_list_file.write('You had ' + str(song_count) + ' songs, nice!')
	running = False

while running == False:
	quit()
