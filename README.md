# Seed Box Germination Script
This script collects all magnet links on a specified web page and populates your default torrent client with the collected magnets.
I created this script as a quick means to populate machines dedicated for seeding torrents.

## Running The Script
1. Clone the repository.
  ```
  hg clone https://hg.sr.ht/~snarftop/sbgs
  ```
2. Change directory.
  ```
  cd sbgs
  ```
3. Run the install script (Debian, Fedora, Arch) or install the prerequisites manually.
  ```
  sh install.sh
  ```  
4. Run the germination script.
  ```
  python3 germination.py
  ```
