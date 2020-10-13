# Name: Ahsan Khan
# Date: 10/12/20
# Description: Write a function called make_album() that builds a dictionary describing a music album.

def make_album(artist_name, album_title, num_of_songs=None):
	if num_of_songs:
		info = {'artist':artist_name, 'title':album_title, 'number of songs':num_of_songs}
	else:
		info = {'artist':artist_name, 'title':album_title}
	return info

album = make_album('ahsan', 'python')
print(f"{album}\n")

album = make_album('ahmed', 'iOS')
print(f"{album}\n")

album = make_album('khan', 'python')
print(f"{album}\n")

album = make_album('ahsan', 'python', 20)
print(f"{album}\n")

while True:
	print("Enter the artist name and album:")
	print("Enter 'q' at any time to quit")

	artist_name = input("Artist Name: ")
	if artist_name == 'q':
		break

	album = input("Album Name: ")
	if album == 'q':
		break

	info = make_album(artist_name, album)
	print(f"{info}\n")