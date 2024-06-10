``` bash
# Crear un bridge
sudo ip link add name br0 type bridge
# Acrivar el bridge
sudo ip link set br0 up
# Añadir la interfaz de red física 'eno1' al bridge
sudo ip link set eno1 master br0
# Obtener una dirección IP para el bridge 
sudo dhclient br0  # o asignar una IP estática
# Crear una interfaz de red Ethernet virtual para la maáquina virtual
sudo ip tuntap add dev tap0 mode tap
# Añadir la interfaz virtual 'tap0' al bridge 'br0'
sudo ip link set tap0 master br0
# Activar la interfaz 'tap0'
sudo ip link set tap0 up
```
