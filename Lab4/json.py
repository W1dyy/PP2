import json


file_path = "/mnt/data/sample-data.json"
with open(file_path, "r") as file:
    data = json.load(file)

interfaces = data["imdata"]


print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 80)


for interface in interfaces:
    attributes = interface["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "")
    print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")