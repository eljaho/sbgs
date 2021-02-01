# Seed Box Germination Script
This script collects all magnet links on a specified web page and populates your default torrent client with the collected magnets.
I created this script as a quick means to populate machines dedicated for seeding torrents.

## Running The Script
Clone the repository.
  ```
  hg clone https://hg.sr.ht/~snarftop/sbgs
  ```
Change directory.
  ```
  cd sbgs
  ```
Run the install script (Debian, Fedora, Arch) or install the prerequisites manually.
  ```
  sh install.sh
  ```  
Run the germination script.
  ```
  python3 germination.py
  ```
