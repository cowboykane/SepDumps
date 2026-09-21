# SIGHHHH

"""
server = {
    "hostname": "web-prod-01",
    "ip": "192.168.1.50",
    "status": "active"
}

# Change "status" to "maintenance"

server.update({"status": "maintenance"})

print(server)

try:
    port = server.get("port", 80)
    print(port)
except ValueError:
    print("Port not found.")
    
"""

user = {
    "username": "alex99",
    "role": "admin",
    "login_count": 5
}

# Drills

user["login_count"] = 6

user["email"] = "alex@example.com"

print(user.get("last_login", "Never"))

del user["role"]


player = {
    "name": "Knight",
    "hp": 100,
    "level": 1
}

player["hp"] = 120

print(user.get("stamina", 100))

player["class"] = "Warrior"

print(player)