**Port forwarding NAT**

1. open /etc/ssh/ssh_config
2. Enter these lines
`
#Host somename
HostName this-is-nat-host-ip
Port 22
User ec2-user
IdentityFile nat.pem

## instancedetailes
LocalForward localport private-instance-ip:remoteport
`



**Port forward from DBvisualizer**
`
Database Server : localhost
Database Port   : localport
`
