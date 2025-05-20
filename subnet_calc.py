import ipaddress

def calculate_subnet_info(ip_with_mask):
    try:
        network = ipaddress.ip_network(ip_with_mask, strict=False)
        wildcard_mask = get_wildcard_mask(network.netmask)

        print("\n=== Subnet Information ===")
        print(f"IP Address        : {network.network_address}")
        print(f"Subnet Mask       : {network.netmask}")
        print(f"Wildcard Mask     : {wildcard_mask}")
        print(f"Broadcast Address : {network.broadcast_address}")
        print(f"Total Hosts       : {network.num_addresses}")
        print(f"Usable Hosts      : {max(network.num_addresses - 2, 0)}")
        print(f"First Host        : {list(network.hosts())[0] if network.num_addresses > 2 else 'N/A'}")
        print(f"Last Host         : {list(network.hosts())[-1] if network.num_addresses > 2 else 'N/A'}")
        print(f"Network Bits      : /{network.prefixlen}")
        print(f"Binary Netmask    : {'.'.join(format(o, '08b') for o in network.netmask.packed)}")
    except ValueError as e:
        print(f"Error: {e}")

def get_wildcard_mask(netmask):
    # Convert netmask to its 4 octets
    mask_octets = [int(octet) for octet in str(netmask).split('.')]
    # Invert bits to get wildcard
    wildcard_octets = [str(255 - octet) for octet in mask_octets]
    return '.'.join(wildcard_octets)

if __name__ == "__main__":
    print("=== Subnet Calculator ===")
    ip_input = input("Enter IP address with subnet (e.g. 192.168.1.10/24): ")
    calculate_subnet_info(ip_input)
