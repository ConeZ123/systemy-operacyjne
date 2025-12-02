#!/bin/bash

cpu() {
       # na vm nie ma odpowiedniego wpisu w /proc/cpuinfo zeby pobrac info o procesorze
       echo "CPU: " $(cat /proc/cpuinfo | grep processor | cut -d ':' -f 2)
}

ram() {
       echo "RAM:" $(free -m | grep Mem | awk '{printf "%s/%s MiB (%.0f%% used)\n, $3, $2, ($3/$2*100)}')
}

load() {
       echo "Load:" $(uptime | awk -F, '{print $3",",$4",", $5}' | sed 's/load average//g') 
}

kernel() {
       echo "Kernel:" $(uname -a | awk '{print $1, $3}')
}

gpu() {
       echo "GPU:" $(lspci | grep -i 'vga' | sed 's/.*: //')
}

user() {
       echo "User:" $(echo "$USER")
}

shell() {
       echo "Shell:" $(basename "$SHELL")
}

processes() {
       echo "Processes:" $(ps -aux | wc -l)
}

threads() {
       echo "Threads:" $(ps -eLf | wc -l)
}

ip() {
       echo "IP:" $(ip -o -4 address | awk '{print $4}')
}

dns() {
       echo "DNS:" $(grep nameserver /etc/resolve.conf | awk '{print $2}')
}

internet() {
       echo $(timeout 1 ping -c1 8.8.8.8 >/dev/null && echo "Internet: OK" || echo "Internet: Fail")        
}

if [ "$#" -eq 0 ]; then
    cpu
    ram
    load
    kernel
    gpu
    user
    shell
    processes
    threads
    ip
    dns
    internet
    exit 0
fi

for arg in "$@"; do
    case ${arg,,} in
        cpu) cpu ;;
        ram) ram ;;
        load) load ;;
        kernel) kernel ;;
        gpu) gpu ;;
        user) user ;;
        shell) shell ;;
        processes) processes ;;
        threads) threads ;;
        up) ip ;;
        dns) dns ;;
        internet) internet ;;
        *)
            echo "Invalid argument: $arg"
            exit 1
            ;;
    esac
done

exit 0