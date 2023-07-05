##
#
# Usage: $ nmap_parser.py
# 
# 1. Parses nmap output for ports/tls versions/cipher suites
# 2. Compares them to ciphersuite.info's database (locally)
# 3. Pretty-prints weak ciphers
#
##

import json

nmap_results_file = "output.txt"
cipherdb = "db.txt"

with open(nmap_results_file) as nmap_results:
    with open(cipherdb) as cipherdb:
        cipherdict = json.loads(cipherdb.read())
        
        # Split output for ports
        for line in nmap_results:
            line = line.rstrip()
            if "/tcp" in line:
                line = line.split("/")[0]
                print("-"*100+"\n Port " + line)
                
            # Split output for TLS versions
            if "|" in line:
                if "TLSv" in line:
                    line = line.split("   ")[1]
                    print("\n[+] TLS Version " + line)
                    
                # Compare found cipher suites to database
                elif "TLS_" in line:
                    line = line.split("       ")[1].split(" ")[0]
                    for entry in cipherdict['ciphersuites']:
                        for key in entry:
                            if key == line and entry[key]['security'] == 'weak' and not "GCM" in line:
                                print(f"{line}")
