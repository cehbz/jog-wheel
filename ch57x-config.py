#!/usr/bin/env python3
"""Diagnostic tool for CH57x-based USB mini keyboards (VID 0x514C, PID 0x8850).

Lists matching HID devices and queries device status via the 0xFB command.
"""

import sys
import hid

VID = 0x514C
PID = 0x8850
USAGE_PAGE = 0xFF00
REPORT_ID = 0x03


def make_msg(payload):
    """Build a 65-byte HID output report (Report ID + 64 bytes)."""
    msg = [REPORT_ID] + payload
    msg += [0x00] * (65 - len(msg))
    return bytes(msg)


def open_device():
    for info in hid.enumerate(VID, PID):
        if info["usage_page"] == USAGE_PAGE:
            dev = hid.device()
            dev.open_path(info["path"])
            print(f"Opened: {info['product_string']} (usage_page=0x{USAGE_PAGE:04X})")
            return dev
    print("ERROR: device not found. Is it plugged in?")
    print(f"Looking for VID=0x{VID:04X} PID=0x{PID:04X} usage_page=0x{USAGE_PAGE:04X}")
    print("\nAll matching VID/PID devices:")
    for info in hid.enumerate(VID, PID):
        print(f"  usage_page=0x{info['usage_page']:04X} usage=0x{info['usage']:04X} path={info['path']}")
    sys.exit(1)


def cmd_list():
    """List all HID devices matching VID/PID."""
    print(f"Devices matching VID=0x{VID:04X} PID=0x{PID:04X}:")
    for info in hid.enumerate(VID, PID):
        print(f"  usage_page=0x{info['usage_page']:04X} "
              f"usage=0x{info['usage']:04X} "
              f"interface={info.get('interface_number', '?')} "
              f"product='{info.get('product_string', '')}'")


def cmd_status():
    """Send 0xFB status query and display the response."""
    dev = open_device()
    dev.write(make_msg([0xFB, 0xFB, 0xFB]))
    data = dev.read(64, timeout_ms=1000)
    if data:
        print(f"Response: {' '.join(f'{b:02x}' for b in data)}")
    else:
        print("No response.")
    dev.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  ch57x-config.py list    — list matching HID devices")
        print("  ch57x-config.py status  — query device status via 0xFB")
        sys.exit(0)

    cmd = sys.argv[1]
    if cmd == "list":
        cmd_list()
    elif cmd == "status":
        cmd_status()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
