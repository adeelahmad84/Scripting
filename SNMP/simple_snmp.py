#!/usr/bin/env python
# -- coding: utf-8 --

"""
File:   class1_ex3.py
Author: Adeel Ahmad
Email:  adeelahmad84@me.com
Github: https://github.com/adeelahmad84
Description: Determine network configuration with this script
"""

from snmp_helper import snmp_get_oid,snmp_extract

def main():
    """TODO: Docstring for main.
    including the below script within the main function.

    """
    COMMUNITY_STRING = 'galileo'
    SNMP_PORT = 7961
    IP = '50.242.94.227'

    a_device = (IP, COMMUNITY_STRING, SNMP_PORT)

    UPTIME_OID = '1.3.6.1.2.1.1.3.0'
    RUNNING_CFG_LST_CHNGE_OID = '1.3.6.1.4.1.9.9.43.1.1.1.0'

    snmp_data = snmp_get_oid(a_device, oid=UPTIME_OID)
    snmp_data2 = snmp_get_oid(a_device, oid=RUNNING_CFG_LST_CHNGE_OID)

    output = snmp_extract(snmp_data)
    output2 = snmp_extract(snmp_data2)

    print (output,output2)

if __name__ == '__main__':
    main()
