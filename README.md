# Seed Box Germination Script
This script collects all magnet links on a specified web page and populates your default torrent client with the collected magnets.
I created this script as a quick means to populate remote machines dedicated for seeding torrents.

## Working Websites
* https://thepiratebay10.org/
* https://www.nyaa.net/

## Example Arguments
* https://www.nyaa.net/search?c=_&q=ergo+proxy
* https://thepiratebay10.org/top/100

## Running The Script
Clone
  ```
  hg clone https://hg.sr.ht/~snarftop/sbgs
  ```
Change Directory
  ```
  cd sbgs
  ```
Run Install Script
  ```
  sh install.sh
  ```  
Run Germination Script
  ```
  python3 germination.py
  ```
