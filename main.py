import nmap
import json

scanNmap = nmap.PortScanner()

scanNmap.scan('127.0.0.1', '22-443')

scanResult = scanNmap.all_hosts()

with open('nmap_result.json','w') as file:
    json.dump(scanResult, file)