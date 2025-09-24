# andro-privacy-hub

A modular privacy toolkit for rooted Android (Termux) integrating Tor, I2P, DNS spoofing, GPS spoofing (Magisk/Xposed), IP rotation, file/data transfer, random port/proxy generation, web dashboard, and peer analytics.

## Features

- Random port/proxy generation (Tor, I2P, proxychains)
- Masked IP support (192.0.0.2)
- Peer-to-peer decentralized encrypted network (I2P)
- DNS spoofing (dnsspoof/dnsmasq)
- GPS spoofing (Magisk/Xposed, automation hooks)
- Socket transfer via Tor/I2P hidden services
- Real-time IP rotation
- Web dashboard (Flask + SocketIO)
- Peer analytics

## Quick Install

```bash
pkg update
pkg install python tor i2pd proxychains dnsspoof dnsmasq git
pip install -r requirements.txt
python3 portgen.py
cp proxychains.conf $PREFIX/etc/proxychains.conf
# Edit your Tor and I2PD config files to use generated ports
```

## GPS Spoofing

- Install [Fake Location Magisk Module](https://github.com/Lerist/FakeLocation) or Xposed [Fake Location](https://repo.xposed.info/module/com.lerist.fakelocation)
- Use `gps_spoofing.py` for automation (see file for details)
