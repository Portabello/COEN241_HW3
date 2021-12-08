Task 1

1. Output of nodes & net

	The nodes command outputs the following…

	Available nodes are:
	C0 h1 h2 h3 h4 h5 h6 h7 h8 s1 s2 s3 s4 s5 s6 s7

	The net command outputs the following…
	
	h1  h1-eth0:s3-eth2
	h2  h2-eth0:s3-eth3
	h3  h3-eth0:s4-eth2
	h4  h4-eth0:s4-eth3
	h5  h5-eth0:s6-eth2
	h6  h6-eth0:s6-eth3
	h7  h7-eth0:s7-eth2
	h8  h8-eth0:s7-eth3
	s1  lo:  s1-eth1:s2-eth1  s1-eth2:s5-eth1
	s2  lo:  s2-eth1:s1-eth1  s2-eth2:s3-eth1  s2-eth3:s4-eth1
	s3  lo:  s3-eth1:s2-eth2  s3-eth2:h1-eth0  s3-eth3:h2-eth0
	s4  lo:  s4-eth1:s2-eth3  s4-eth2:h3-eth0  s4-eth3:h4-eth0
	s5  lo:  s5-eth1:s1-eth2  s5-eth2:s6-eth1  s5-eth3:s7-eth1
	s6  lo:  s6-eth1:s5-eth2  s6-eth2:h5-eth0  s6-eth3:h6-eth0
	s7  lo:  s7-eth1:s5-eth3  s7-eth2:h7-eth0  s7-eth3:h8-eth0
	c0

2. Output of h7 ifconfig
	
	H7-eth0: flags=4163<UP, BROADCAST, RUNNING, MULTICAST> mtu 1500
		Inet 10.0.0.7 netmask 255.0.0.0 broadcast 10.255.255.255
		Inet6 fe80::448b::cdff::fe51::cadf prefixlen 64 scopeid 0x20<link>
		Ether 46:8b:cd:51:ca:df txqueuelen 1000 (Ethernet)
		RX packets 57 bytes 4374 (4.3 KB)
		RX errors 0 dropped 0 overruns 0 frame 0
		TX packets 10 bytes 796 (796.0 B)
		TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0
	
	Lo: flags=73<UP, LOOPBACK, RUNNING> mtu 65536
		Inet 127.0.0.1 netmask 255.0.0.0
		Inet6 ::1 prefixlen 128 scopeid 0.10<host>
		Loop txqueuelen 1000 (Local Loopback)
		RX packets 0 bytes 0 (0.0 B)
		RX errors 0 dropped 0 overruns 0 frame 0
		TX packets 0 bytes 0 (0.0 B)
		TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0


Task 2

1. 

	a. Initially once of_tutorial is started the launch() function is called which creates a 
	Tutorial object which fist initiates the __init__ function to create connection and bind 
	packedIn event listener and create table (mac_to_port) to track which ethernet address is 
	on which switch port
	
	b. Once the code is running, once a packet comes to the controller the _handle_PacketIn()  
	function is called to parse the packet, then call the act_like_hub() function
	
	c. In the act_like_hub() function the packet is flooded to all output ports using the 
	resend_packet() function
	
	d. The resend_packet() function the packet is sent out to all output ports and a message 
	is logged to switch

2. 

	a.
	H1 ping H2 - average 8.485ms
	H1 ping H8 - average 33.654ms

	b.
	H1 ping H2 - min 2.425ms - max 32.349ms
	H1 ping H8 - min 12.002ms- max 66.359ms

	c. There is a large difference between the two results, H1 pinging H2 is much faster than H1 
	pinging H8. This is because of the relational distance between the two nodes. There are much 
	fewer switches to traverse from H1 to H2 than from H1 to H8. This is because of how the binary 
	tree topology is setup. H1 to H2 would only have to traverse 1 switch, which H1 to H8 has to 
	traverse 5 switches, which results in the increased latency when pinging.

3. 
	a. Iperf is a network performance measurement tool that creates TCP and UDP data streams and 
	measures the throughput of a network that is carrying them

	b.
	Iperf H1 H2
	[1.63 Mbits/sec , 2.23 Mbits/s]

	Iperf H1 H8
	[1.29 Mbits/sec , 1.79 Mbits/sec]

	c. There is a slight difference with the TCP bandwidth between h1 and h2 being larger than the 
	bandwidth between h1 and h8. This is most likely a slight overhead of each packet from traversing 
	through more switches between h1 and h8 which is causing a smaller bandwidth.

4. 	Every switch will observe traffic, as we are using the act_like_switch() method in the of_tutorial 
	the packets will be sent out to all switches and handled in the _handle_PacketIn() method. We can 
	modify the _handle_PacketIn() method to further examine the traffic/ examine each packet.


Task 3

1. 	In our act_like_switch() implementation, the mac_to_port table is built as packets are coming in. 
	as a packet comes in, a check is performed to see if the packet source is logged already in the 
	mac_to_port table. If it is not in the table, the method will create an entry with the key as the 
	packet source and the destination port as the value. This will allow the table mac_to_port to fill up. 
	Then the packet is sent out, if there is an entry for the destination port in the mac_to_port table, the 
	packet is sent to the destination port. Otherwise it is flooded to all switches, like in our previous 
	implementation of act_like_hub()


2. 
	a.  H1 ping H2 - average 7.161ms
		H1 ping H8 - average 32.730ms

	b.  H1 ping H2 - min 2.385ms - max 18.520ms
		H1 ping H8 - min 11.288ms - max 99.434ms

	c. here we can see lower average pings and higher maximum pings, the causes of these two changes 
	can be traced back to the changes we made in our code. I believe that due to the mac_to_port table 
	being populated so our program learns where sources are attached to which ports will result in a 
	lower average over time as the program learns more entries in the table, and allows for faster 
	direction of traffic later down the line. The increase in maximum values could be a result of early 
	pings and the overhead in our code required to create an entry in the table for those, resulting in 
	a higher latency for those ping requests


3.  
	a. Iperf H1 H2
		[10.2 Mbits/sec , 11.8 Mbits/sec]

		Iperf H1 H8
		[1.66 Mbits/sec , 2.15 Mbits/sec]

	b. Here we can see a large increase in the bandwidth between H1 and H2 and a slight increase in the 
	bandwidth between H1 and H8. I believe that this can be attributed to the ability for our program to 
	learn the mac_to_port table which results in quicker redirection of packet traffic, which would result 
	in a larger bandwidth. As more traffic through switches is introduced, such as in H1 to H8 that benefit 
	is reduced to the point where it is only a slight improvement than before. This can be due to the fact 
	that so many switches still have to be traversed and the overhead that is required for the table 
	mac_to_port to be maintained outweighing the potential bandwidth gains that it could have.
