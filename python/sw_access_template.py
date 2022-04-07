
#!First Way :


access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access_intf = {
    tuple(range(1,11)):10,(11,13,15):20,
    tuple( range(16,23)):30
}

for int,vlan in access_intf.items():
    for i in int:
        print(f'interface gi 0/{i}')
        for command in access_template:
            if command.endswith("vlan"):
                print(f' {command} {vlan}')
            else:
                print(f' {command}')
            
#!Second Way:


def cmd_gen(template,vlan = 1,*intf):
    for interface in intf:
            print(f'int gi 0/{interface}')
            for command in template:
                if command.endswith("vlan") :
                    print(f' {command} {vlan}')
                else :
                    print(f' {command}')



