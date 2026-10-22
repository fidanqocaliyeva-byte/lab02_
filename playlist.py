class SongNode:
    def __init__(self, song_id, name, artist, duration):
        self.song_id = song_id
        self.name = name
        self.artist = artist
        self.duration = duration
        self.next = None  

class Playlist:
    def __init__(self):
        self.head = None  
        self.current = None  

    def add_song(self, song_id, name, artist, duration):
        new_node = SongNode(song_id, name, artist, duration)
        if not self.head:
            self.head = new_node
            self.current = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"'{name}' mahnısı uğurla əlavə olundu!")

    def delete_song(self, song_id):
        current = self.head
        prev = None
        while current:
            if current.song_id == song_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"ID {song_id} olan mahnı silindi.")
                return
            prev = current
            current = current.next
        print("Mahnı tapılmadı.")

    def search_song(self, name):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                print(f"Tapıldı -> ID: {current.song_id} | Ad: {current.name} | İfaçı: {current.artist}")
                return current
            current = current.next
        print("Mahnı tapılmadı.")
        return None

    def display_playlist(self):
        current = self.head
        if not self.head:
            print("Playlist boşdur.")
            return
        print("\n--- İNDİKİ PLAYLİST ---")
        while current:
            print(f"[ID: {current.song_id}] {current.name} - {current.artist} ({current.duration} dəq)")
            current = current.next
        print("-" * 25)

    def count_songs(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"Playlstdə cəmi {count} mahnı var.")
        return count

    def play_next_song(self):
        if not self.current:
            print("Playlist boşdur.")
            return
        print(f"İndi çalınır: {self.current.name} - {self.current.artist}")
        if self.current.next:
            self.current = self.current.next
        else:
            print("Playlistenin sonuna çatıldı, başa qayıdılır.")
            self.current = self.head


if __name__ == "__main__":
    my_playlist = Playlist()
    
    while True:
        print("\n--- Spotify Playlist Menyu ---")
        print("1. Add Song")
        print("2. Delete Song")
        print("3. Search Song")
        print("4. Display Playlist")
        print("5. Play Next Song")
        print("6. Count Songs")
        print("7. Exit")
        
        choice = input("Seçiminizi daxil edin (1-7): ")
        
        if choice == "1":
            s_id = int(input("Mahnı ID: "))
            s_name = input("Mahnı Adı: ")
            s_artist = input("İfaçı: ")
            s_duration = float(input("Müddət (dəq): "))
            my_playlist.add_song(s_id, s_name, s_artist, s_duration)
        elif choice == "2":
            s_id = int(input("Silinəcək Mahnı ID: "))
            my_playlist.delete_song(s_id)
        elif choice == "3":
            s_name = input("Axtarılan Mahnı Adı: ")
            my_playlist.search_song(s_name)
        elif choice == "4":
            my_playlist.display_playlist()
        elif choice == "5":
            my_playlist.play_next_song()
        elif choice == "6":
            my_playlist.count_songs()
        elif choice == "7":
            print("Proqramdan çıxılır...")
            break
        else:
            print("Yanlış seçim, yenidən sınayın.")


            import time

if __name__ == "__main__":
  for n in [100, 1000, 10000]:
    pl = Playlist()

   