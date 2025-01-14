class SongsManagementSystem:
    
    def __init__(self):
        
        self.song_list = []
        
        
    def display_menu(self):
        
        print("\n Song Management System")
        print("1. Add Song")
        print("2. View Songs")
        print("3. Delete Song")
        print("4. Sort Song")  
        print("5. Exit")
        
    def add_songs(self):
        
        song = input("Enter the name of the song to add: ")
        
        self.song_list.append(song)
        
        print(f'Song "{song}" added to the playlist.')
        
    
    def view_songs(self):
        
        if not self.song_list:
            
            print("No songs in the playlist.")
            
        else:
            
            print("\n Current Playlist: ")
        
            for index, song in enumerate(self.song_list, start=1):
                
                print(f"{index}. {song}")
                
    def delete_songs(self):
        
        self.view_songs()
        
        if self.song_list:
            
            try:
                
                index = int(input("Enter the number of the song to delete: ")) - 1
                
                if 0 <= index < len(self.song_list):
                    
                    removed_song = self.song_list.pop(index)
                                    
                    print(f'song "{removed_song}" removed from the playlist. ')
                    
                else: 
                    
                    print("invalid number. Please try again!")
                    
            except ValueError:
                
                print("Invalid Input. PLease enter a number!")
                
    def sort_songs(self):
        
        if not self.song_list:
            
            print("No songs to sort")
                
        else:
            
            print("Sort options:")
            print("1. Ascending")
            print("2. Descending")
            
            choice = input("Enter your choice (1 or 2): ")
            
            if choice == "1":
                
                self.song_list.sort()
                print("Songs sorted in ascending order.")
                
            elif choice == "2":
                
                self.song_list.sort(reverse=True)
                print("Songs sorted in descending order.")
                
            else:
                
                print("Invalid choice. Please enter 1 or 2.")
                
    def run(self):
        
        while True:
            
            self.display_menu()
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                
                self.add_songs()
                
            elif choice == "2":
                
                self.view_songs()
                
            elif choice == "3":
                
                 self.delete_songs()
                 
            elif choice == "4":
                
                self.sort_songs()
                
            elif choice == "5":
                
                print("exiting the system!")
                break
                
            else:
                
                print("invalid choice. Please enter a number between 1 and 5! ")
                
                
                
if __name__ == "__main__":
        manager = SongsManagementSystem()
        manager.run()