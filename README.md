# CipherCheck
Weak cipher checking tool for nmap `--script ssl-enum-ciphers` results

- Uses database of https://ciphersuite.info (07-2023)
- Local / offline database (no api request needed for each cipher suite)
- Assumes nmap output containing ssl-enum-ciphers script output



### ciphercheck_download.py (download db)
- Downloads latest cipher suite database (including security rating) from ciphersuite.info API  
- To copy into a file just run `$ ciphercheck_download.py > db.txt`  

### nmap_parser.py (check for vuln ciphers in nmap results)
- Parses nmap output for cipher suites
- Compares them to ciphersuite.info's database (locally)
- Pretty-prints out weak ciphers
