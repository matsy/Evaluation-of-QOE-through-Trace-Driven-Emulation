/*
 * make a 256kbit/s TBF on eth0
 *
 */

dev eth1 {
    egress {
        tbf( rate 256 kbps, burst 20 kB, limit 20 kB, mtu 1514 B );
    }
}
