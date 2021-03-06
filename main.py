from netmiko import ConnectHandler
import dispaly
junipersw88_2 = {
	'device_type': 'juniper',
	'host':   '192.168.88.2',
	'username': 'root',
	'password': 'juniper123',
	'port' : 22,
}
net_connect = ConnectHandler(**junipersw88_2)
#config_commands = ['set system services telnet']
dispaly.displayset('show configuration | display set | find protocols')
config_commands = ['delete protocols']
ouput = net_connect.send_config_set(config_commands, exit_config_mode=False)
net_connect.commit()
exit_config_mode = ['exit']
net_connect.send_config_set(exit_config_mode, exit_config_mode=False)
print()
print("Shows the protocols section is gone with patterno not fournd")
dispaly.displayset('show configuration | display set | find protocols')
print("ROll back to Original")
rollback_res = ["rollback rescue"]
net_connect.send_config_set(rollback_res, exit_config_mode=False)
net_connect.commit()
exit_config_mode = ['exit']
net_connect.send_config_set(exit_config_mode, exit_config_mode=False)
dispaly.displayset('show configuration | display set | find protocols')
print("done")