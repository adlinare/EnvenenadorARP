# EnvenenadorARP
Es necesario antes de ejecutar, cambiar las politicas para aceptar las recepciones
sudo iptables --policy FORWARD ACCEPT


cat /proc/sys/net/ipv4/ip_forward 
nos debe dar 1 si no debemos introducirlo a mano, para podernos comunicar de vuelta con la maquina

si no lo hacemos cuando interceptemos la maquina atacada no podra navegar


router : 192.168.20.1 

Es necesario cambiar nuestra mac temporalmente a la mac del scrip

aa:bb:cc:44:55:66

sudo ip link set dev INTERFAZ down
sudo macchanger -m 00:11:22:33:44:55 INTERFAZ
sudo ip link set dev INTERFAZ up

# EnvenenadorARP
