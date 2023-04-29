# Implementing Rule modification

## Introduction

The objective of this exercise is to write a P4 program that
implements basic forwarding. To keep things simple, we will just
implement forwarding for IPv4.

With IPv4 forwarding, the switch must perform the following actions
for every packet: (i) update the source and destination MAC addresses,
(ii) decrement the time-to-live (TTL) in the IP header, and (iii)
forward the packet out the appropriate port.

Your switch will have a single table, which the control plane will
populate with static rules. Each rule will map an IP address to the
MAC address and output port for the next hop. We have already defined
the control plane rules, so you only need to implement the data plane
logic of your P4 program.


## How to run

Run the topology:

```
sudo p4run
```


Try to ping from one host to another:

```
mininet> h1 ping h2
```

Ping from all host pairs to test for connectivity:

```
mininet> pingall
```
Now run the attack file in the terminal which is drop.py

```
sudo python drop.py
```
Now check the switch 1 and switch 5 commands ,action should be changed to drop from forward.

Now run the sudo p4run command to act the necessary changes.
```
sudo p4run
```
check in the xterm or by pingall ,communication should be stopped between desired hosts.

```
mininet> pingall
```
or

```
mininet> xterm h1 h2
```
send the traffic fromm h1 to h2 and verify that communication is topped between the hosts
run the command on receiver host
```
sudo python receive.py
```
run the following command on sender host

```
sudo python send.py 10.0.2.2
```
communication should be stopped between h1 to h2.


Till now Attcak has been done on the switch.



