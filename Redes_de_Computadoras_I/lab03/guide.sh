

 
    # Crear un bridge
    sudo ip link add name br0 type bridge
    # Acrivar el bridge
    sudo ip link set br0 up
    # Añadir la interfaz de red física 'eno1' al bridge
    sudo ip link set eno1 master br0
    # Obtener una dirección IP para el bridge 
    sudo dhclient br0  
    # Crear una interfaz de red Ethernet virtual para la máquina virtual
    sudo ip tuntap add dev tap0 mode tap
    # Añadir la interfaz virtual 'tap0' al bridge 'br0'
    sudo ip link set tap0 master br0
    # Activar la interfaz 'tap0'
    sudo ip link set tap0 up




    qemu-system-x86_64 -m 2G -smp 2 --enable-kvm -name 'windows' --boot d -hda HDD \
        -netdev tap,id=net0,ifname=tap0,script=no,downscript=no \
        -device virtio-net-pci,netdev=net0



     sudo ip addr add 128.0.0.3/16 dev br0



     sudo ip addr add 192.168.1.1/24 dev br0



