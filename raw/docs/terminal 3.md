E840-5CG3384SN8+firstuser@E840-5CG3384SN8 MINGW64 ~/.ssh
$ ssh -v -i ~/.ssh/claude-synology firstuser@192.168.1.99
debug1: OpenSSH_10.0p2, OpenSSL 3.2.4 11 Feb 2025
debug1: Reading configuration data /c/Users/firstuser/.ssh/config
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: Connecting to 192.168.1.99 [192.168.1.99] port 22.
debug1: Connection established.
debug1: identity file /c/Users/firstuser/.ssh/claude-synology type 3
debug1: identity file /c/Users/firstuser/.ssh/claude-synology-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_10.0
debug1: Remote protocol version 2.0, remote software version OpenSSH_6.8p1-hpn14v6
debug1: compat_banner: match: OpenSSH_6.8p1-hpn14v6 pat OpenSSH* compat 0x04000000
debug1: Authenticating to 192.168.1.99:22 as 'star'
debug1: load_hostkeys: fopen /c/Users/firstuser/.ssh/known_hosts2: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256@libssh.org
debug1: kex: host key algorithm: ssh-ed25519
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: SSH2_MSG_KEX_ECDH_REPLY received
debug1: Server host key: ssh-ed25519 SHA256:iOki/McmfxwUzITQ3Mlr8CiyXeYrUTBwmh0yO26fGfk
debug1: load_hostkeys: fopen /c/Users/firstuser/.ssh/known_hosts2: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
debug1: Host '192.168.1.99' is known and matches the ED25519 host key.
debug1: Found key in /c/Users/firstuser/.ssh/known_hosts:21
debug1: rekey out after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey in after 134217728 blocks
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Will attempt key: /c/Users/firstuser/.ssh/claude-synology ED25519 SHA256:R9EP0Q0aKchVLQs8mlUFsOkjMafzK+p4WUIrlu9/SvU explicit
debug1: Offering public key: /c/Users/firstuser/.ssh/claude-synology ED25519 SHA256:R9EP0Q0aKchVLQs8mlUFsOkjMafzK+p4WUIrlu9/SvU explicit
debug1: Server accepts key: /c/Users/firstuser/.ssh/claude-synology ED25519 SHA256:R9EP0Q0aKchVLQs8mlUFsOkjMafzK+p4WUIrlu9/SvU explicit
Authenticated to 192.168.1.99 ([192.168.1.99]:22) using "publickey".
debug1: channel 0: new session [client-session] (inactive timeout: 0)
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: pledge: filesystem
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: client_input_hostkeys: convert key: unknown or unsupported key type
debug1: client_input_hostkeys: searching /c/Users/firstuser/.ssh/known_hosts for 192.168.1.99 / (none)
debug1: client_input_hostkeys: searching /c/Users/firstuser/.ssh/known_hosts2 for 192.168.1.99 / (none)
debug1: client_input_hostkeys: hostkeys file /c/Users/firstuser/.ssh/known_hosts2 does not exist
debug1: client_input_hostkeys: host key found matching a different name/address, skipping UserKnownHostsFile update
debug1: pledge: fork
firstuser@DiskStation:~$ sudo kill $(ps aux | grep syno_hibernation_debug | grep -v grep | awk '{print $2}')
Password:
firstuser@DiskStation:~$ ps aux | grep hibernation | grep -v grep
firstuser@DiskStation:~$ sudo synosetkeyvalue /etc/synoinfo.conf enable_hibernation_debug no
firstuser@DiskStation:~$
Broadcast message from root@DiskStation
        (unknown) at 23:38 ...

The system is going down for reboot NOW!
Connection to 192.168.1.99 closed by remote host.
Connection to 192.168.1.99 closed.
debug1: channel 0: free: client-session, nchannels 1
Transferred: sent 3008, received 3332 bytes, in 723.6 seconds
Bytes per second: sent 4.2, received 4.6
debug1: Exit status -1

E840-5CG3384SN8+firstuser@E840-5CG3384SN8 MINGW64 ~/.ssh
$ ssh -v -i ~/.ssh/claude-synology firstuser@192.168.1.99
debug1: OpenSSH_10.0p2, OpenSSL 3.2.4 11 Feb 2025
debug1: Reading configuration data /c/Users/firstuser/.ssh/config
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: Connecting to 192.168.1.99 [192.168.1.99] port 22.
debug1: Connection established.
debug1: identity file /c/Users/firstuser/.ssh/claude-synology type 3
debug1: identity file /c/Users/firstuser/.ssh/claude-synology-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_10.0
debug1: Remote protocol version 2.0, remote software version OpenSSH_6.8p1-hpn14v6
debug1: compat_banner: match: OpenSSH_6.8p1-hpn14v6 pat OpenSSH* compat 0x04000000
debug1: Authenticating to 192.168.1.99:22 as 'star'
debug1: load_hostkeys: fopen /c/Users/firstuser/.ssh/known_hosts2: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256@libssh.org
debug1: kex: host key algorithm: ssh-ed25519
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: SSH2_MSG_KEX_ECDH_REPLY received
debug1: Server host key: ssh-ed25519 SHA256:iOki/McmfxwUzITQ3Mlr8CiyXeYrUTBwmh0yO26fGfk
debug1: load_hostkeys: fopen /c/Users/firstuser/.ssh/known_hosts2: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
debug1: Host '192.168.1.99' is known and matches the ED25519 host key.
debug1: Found key in /c/Users/firstuser/.ssh/known_hosts:21
debug1: rekey out after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey in after 134217728 blocks
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Will attempt key: /c/Users/firstuser/.ssh/claude-synology ED25519 SHA256:R9EP0Q0aKchVLQs8mlUFsOkjMafzK+p4WUIrlu9/SvU explicit
debug1: Offering public key: /c/Users/firstuser/.ssh/claude-synology ED25519 SHA256:R9EP0Q0aKchVLQs8mlUFsOkjMafzK+p4WUIrlu9/SvU explicit
debug1: Server accepts key: /c/Users/firstuser/.ssh/claude-synology ED25519 SHA256:R9EP0Q0aKchVLQs8mlUFsOkjMafzK+p4WUIrlu9/SvU explicit
Authenticated to 192.168.1.99 ([192.168.1.99]:22) using "publickey".
debug1: channel 0: new session [client-session] (inactive timeout: 0)
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: pledge: filesystem
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: client_input_hostkeys: convert key: unknown or unsupported key type
debug1: client_input_hostkeys: searching /c/Users/firstuser/.ssh/known_hosts for 192.168.1.99 / (none)
debug1: client_input_hostkeys: searching /c/Users/firstuser/.ssh/known_hosts2 for 192.168.1.99 / (none)
debug1: client_input_hostkeys: hostkeys file /c/Users/firstuser/.ssh/known_hosts2 does not exist
debug1: client_input_hostkeys: host key found matching a different name/address, skipping UserKnownHostsFile update
debug1: pledge: fork
firstuser@DiskStation:~$ ps aux | grep hibernation | grep -v grep
firstuser@DiskStation:~$ date && cat /proc/diskstats | grep sda1
Fri May  8 23:42:43 CEST 2026
   8       1 sda1 22368 1971 455338 10660 7164 4948 96896 7640 0 9820 18290
firstuser@DiskStation:~$ date && cat /proc/diskstats | grep sda1
Fri May  8 23:56:16 CEST 2026
   8       1 sda1 24084 1978 478330 11080 7653 4956 100872 8770 0 11060 19840
firstuser@DiskStation:~$ date && cat /proc/diskstats | grep sda1
Fri May  8 23:56:20 CEST 2026
   8       1 sda1 24369 1978 480610 11090 7717 4957 101392 9100 0 11400 20180
firstuser@DiskStation:~$ sudo synosetkeyvalue /etc/synoinfo.conf enable_hibernation_debug yes
Password:
Sorry, try again.
Password:
firstuser@DiskStation:~$ sudo synosetkeyvalue /etc/synoinfo.conf enable_hibernation_debug yes
firstuser@DiskStation:~$ ps aux | grep syno_hibernation_debug | grep -v grep || echo "процесс не запущен"
процесс не запущен
firstuser@DiskStation:~$ grep enable_hibernation_debug /etc/synoinfo.conf
enable_hibernation_debug="yes"
firstuser@DiskStation:~$ ps aux | grep syno_hibernation_debug | grep -v grep
firstuser@DiskStation:~$ sudo synosetkeyvalue /etc/synoinfo.conf enable_hibernation_debug yes
firstuser@DiskStation:~$ sudo /bin/sh /usr/syno/sbin/syno_hibernation_debug &
[1] 7873
firstuser@DiskStation:~$ ps aux | grep hibernation | grep -v grep
root      7882  0.1  0.4   5252  1020 pts/1    S    00:00   0:00 /bin/sh /usr/syno/sbin/syno_hibernation_debug
[1]+  Done                    sudo /bin/sh /usr/syno/sbin/syno_hibernation_debug
firstuser@DiskStation:~$ ps aux | grep hibernation | grep -v grep
root      7882  0.0  0.4   5252  1020 pts/1    S    00:00   0:00 /bin/sh /usr/syno/sbin/syno_hibernation_debug
firstuser@DiskStation:~$
firstuser@DiskStation:~$
firstuser@DiskStation:~$
firstuser@DiskStation:~$
firstuser@DiskStation:~$ date && cat /proc/diskstats | grep sda1|sda2
Sat May  9 00:02:04 CEST 2026
-sh: sda2: command not found
firstuser@DiskStation:~$ date && cat /proc/diskstats
Sat May  9 00:02:10 CEST 2026
   1       0 ram0 0 0 0 0 0 0 0 0 0 0 0
   1       1 ram1 0 0 0 0 0 0 0 0 0 0 0
   1       2 ram2 0 0 0 0 0 0 0 0 0 0 0
   1       3 ram3 0 0 0 0 0 0 0 0 0 0 0
   1       4 ram4 0 0 0 0 0 0 0 0 0 0 0
   1       5 ram5 0 0 0 0 0 0 0 0 0 0 0
   1       6 ram6 0 0 0 0 0 0 0 0 0 0 0
   1       7 ram7 0 0 0 0 0 0 0 0 0 0 0
   1       8 ram8 0 0 0 0 0 0 0 0 0 0 0
   1       9 ram9 0 0 0 0 0 0 0 0 0 0 0
   1      10 ram10 0 0 0 0 0 0 0 0 0 0 0
   1      11 ram11 0 0 0 0 0 0 0 0 0 0 0
   1      12 ram12 0 0 0 0 0 0 0 0 0 0 0
   1      13 ram13 0 0 0 0 0 0 0 0 0 0 0
   1      14 ram14 0 0 0 0 0 0 0 0 0 0 0
   1      15 ram15 0 0 0 0 0 0 0 0 0 0 0
   8       0 sda 27893 2149 521352 12420 8908 4999 111052 13870 0 16040 26280
   8       1 sda1 24465 1978 483434 11120 8195 4987 105456 12330 0 14600 23440
   8       2 sda2 111 0 870 30 38 0 304 240 0 270 270
   8       3 sda3 3091 165 35192 1260 674 12 5284 1300 0 1970 2560
   8      16 sdb 6175 8383 335664 39020 2125 11253 106880 61160 0 32630 100170
   8      17 sdb1 5458 7044 270348 30840 2023 11159 105456 58750 0 29350 89580
   8      18 sdb2 34 182 1728 270 25 13 304 760 0 1030 1030
   8      19 sdb3 3 0 18 30 0 0 0 0 0 30 30
   8      21 sdb5 658 946 61706 7670 76 81 1112 1630 0 4960 9300
  31       0 mtdblock0 0 0 0 0 0 0 0 0 0 0 0
  31       1 mtdblock1 0 0 0 0 0 0 0 0 0 0 0
  31       2 mtdblock2 0 0 0 0 0 0 0 0 0 0 0
  31       3 mtdblock3 0 0 0 0 0 0 0 0 0 0 0
  31       4 mtdblock4 0 0 0 0 0 0 0 0 0 0 0
  31       5 mtdblock5 0 0 0 0 0 0 0 0 0 0 0
   9       0 md0 77868 0 1507376 164970 25724 0 205792 803450 37 1338280 49122450
   9       1 md1 634 0 5072 1440 60 0 480 900 0 730 2040
   9       2 md2 6416 0 70068 3060 1304 0 10432 3690 4 1293220 5130660
   9       3 md3 3108 0 123028 19930 266 0 2128 2720 0 3920 22220
 253       0 dm-0 1242 0 59018 19590 133 0 1064 2720 0 4230 22310
   7       0 loop0 0 0 0 0 0 0 0 0 0 0 0
   7       1 loop1 0 0 0 0 0 0 0 0 0 0 0
   7       2 loop2 0 0 0 0 0 0 0 0 0 0 0
   7       3 loop3 0 0 0 0 0 0 0 0 0 0 0
   7       4 loop4 0 0 0 0 0 0 0 0 0 0 0
   7       5 loop5 0 0 0 0 0 0 0 0 0 0 0
   7       6 loop6 0 0 0 0 0 0 0 0 0 0 0
   7       7 loop7 0 0 0 0 0 0 0 0 0 0 0
   7       8 loop8 0 0 0 0 0 0 0 0 0 0 0
   7       9 loop9 0 0 0 0 0 0 0 0 0 0 0
   7      10 loop10 0 0 0 0 0 0 0 0 0 0 0
   7      11 loop11 0 0 0 0 0 0 0 0 0 0 0
   7      12 loop12 0 0 0 0 0 0 0 0 0 0 0
   7      13 loop13 0 0 0 0 0 0 0 0 0 0 0
   7      14 loop14 0 0 0 0 0 0 0 0 0 0 0
   7      15 loop15 0 0 0 0 0 0 0 0 0 0 0
firstuser@DiskStation:~$ date && cat /proc/diskstats | grep sda
Sat May  9 00:02:27 CEST 2026
   8       0 sda 27893 2149 521352 12420 8913 5000 111100 13950 0 16120 26360
   8       1 sda1 24465 1978 483434 11120 8200 4988 105504 12410 0 14680 23520
   8       2 sda2 111 0 870 30 38 0 304 240 0 270 270
   8       3 sda3 3091 165 35192 1260 674 12 5284 1300 0 1970 2560
firstuser@DiskStation:~$ # network cable off
firstuser@DiskStation:~$ Read from remote host 192.168.1.99: Connection reset by peer
Connection to 192.168.1.99 closed.
client_loop: send disconnect: Connection reset by peer

E840-5CG3384SN8+firstuser@E840-5CG3384SN8 MINGW64 ~/.ssh
$ ssh -v -i ~/.ssh/claude-synology firstuser@192.168.1.99
debug1: OpenSSH_10.0p2, OpenSSL 3.2.4 11 Feb 2025
debug1: Reading configuration data /c/Users/firstuser/.ssh/config
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: Connecting to 192.168.1.99 [192.168.1.99] port 22.
debug1: Connection established.
debug1: identity file /c/Users/firstuser/.ssh/claude-synology type 3
debug1: identity file /c/Users/firstuser/.ssh/claude-synology-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_10.0
debug1: Remote protocol version 2.0, remote software version OpenSSH_6.8p1-hpn14v6
debug1: compat_banner: match: OpenSSH_6.8p1-hpn14v6 pat OpenSSH* compat 0x04000000
debug1: Authenticating to 192.168.1.99:22 as 'star'
debug1: load_hostkeys: fopen /c/Users/firstuser/.ssh/known_hosts2: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256@libssh.org
debug1: kex: host key algorithm: ssh-ed25519
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: SSH2_MSG_KEX_ECDH_REPLY received
debug1: Server host key: ssh-ed25519 SHA256:iOki/McmfxwUzITQ3Mlr8CiyXeYrUTBwmh0yO26fGfk
debug1: load_hostkeys: fopen /c/Users/firstuser/.ssh/known_hosts2: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
debug1: Host '192.168.1.99' is known and matches the ED25519 host key.
debug1: Found key in /c/Users/firstuser/.ssh/known_hosts:21
debug1: rekey out after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey in after 134217728 blocks
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Will attempt key: /c/Users/firstuser/.ssh/claude-synology ED25519 SHA256:R9EP0Q0aKchVLQs8mlUFsOkjMafzK+p4WUIrlu9/SvU explicit
debug1: Offering public key: /c/Users/firstuser/.ssh/claude-synology ED25519 SHA256:R9EP0Q0aKchVLQs8mlUFsOkjMafzK+p4WUIrlu9/SvU explicit
debug1: Server accepts key: /c/Users/firstuser/.ssh/claude-synology ED25519 SHA256:R9EP0Q0aKchVLQs8mlUFsOkjMafzK+p4WUIrlu9/SvU explicit
Authenticated to 192.168.1.99 ([192.168.1.99]:22) using "publickey".
debug1: channel 0: new session [client-session] (inactive timeout: 0)
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: pledge: filesystem
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: client_input_hostkeys: convert key: unknown or unsupported key type
debug1: client_input_hostkeys: searching /c/Users/firstuser/.ssh/known_hosts for 192.168.1.99 / (none)
debug1: client_input_hostkeys: searching /c/Users/firstuser/.ssh/known_hosts2 for 192.168.1.99 / (none)
debug1: client_input_hostkeys: hostkeys file /c/Users/firstuser/.ssh/known_hosts2 does not exist
debug1: client_input_hostkeys: host key found matching a different name/address, skipping UserKnownHostsFile update
debug1: pledge: fork
firstuser@DiskStation:~$ # network cable on
firstuser@DiskStation:~$ date && cat /proc/diskstats | grep sda
Sat May  9 00:12:33 CEST 2026
   8       0 sda 27967 2149 523056 12560 9735 5068 118202 17170 0 18530 29720
   8       1 sda1 24539 1978 485138 11260 9008 5047 112440 15460 0 17080 26710
   8       2 sda2 111 0 870 30 38 0 304 240 0 270 270
   8       3 sda3 3091 165 35192 1260 688 21 5450 1470 0 2140 2730
firstuser@DiskStation:~$ exitdebug1: client_input_channel_req: channel 0 rtype exit-status reply 0
debug1: client_input_channel_req: channel 0 rtype eow@openssh.com reply 0

logout
debug1: channel 0: free: client-session, nchannels 1
Connection to 192.168.1.99 closed.
Transferred: sent 2880, received 3396 bytes, in 67.4 seconds
Bytes per second: sent 42.7, received 50.4
debug1: Exit status 0

E840-5CG3384SN8+firstuser@E840-5CG3384SN8 MINGW64 ~/.ssh
$ ssh -i ~/.ssh/claude-synology firstuser@192.168.1.99
firstuser@DiskStation:~$ ls /volume1/Backup
dump  @eaDir  HomeAssistant  #recycle  vmSynology_Data.hbk  vmSynology_MyScan.hbk  vmSynology_Obsidian.hbk
firstuser@DiskStation:~$ sudo synosetkeyvalue /etc/synoinfo.conf enable_hibernation_debug no
Password:
firstuser@DiskStation:~$ sudo kill $(ps aux | grep syno_hibernation_debug | grep -v grep | awk '{print $2}')
firstuser@DiskStation:~$ ps aux | grep hibernation | grep -v grep
firstuser@DiskStation:~$