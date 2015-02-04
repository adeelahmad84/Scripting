#
# GET Command Generator
#
# Send a SNMP GET request
#     with SNMPv3 with user 'usr-sha-aes', SHA auth and AES128 privacy protocols
#     using Twisted framework for network transport
#     over IPv4/UDP
#     to an Agent at 195.218.195.228:161
#     for an OID in tuple form
#
# This script performs similar to the following Net-SNMP command:
#
# $ snmpget -v3 -l authPriv -u usr-sha-aes -a SHA -A authkey1 -x AES -X privkey1 -ObentU 195.218.195.228:161  1.3.6.1.2.1.1.1.0
#
from twisted.internet import reactor, defer
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413.twisted import cmdgen
from pysnmp.carrier.twisted.dgram import udp

# Create SNMP engine instance
snmpEngine = engine.SnmpEngine()

#
# SNMPv3/USM setup
#

# user: usr-sha-aes, auth: SHA, priv AES
config.addV3User(
    snmpEngine, 'usr-sha-aes',
        config.usmHMACSHAAuthProtocol, 'authkey1',
            config.usmAesCfb128Protocol, 'privkey1'
            )
config.addTargetParams(snmpEngine, 'my-creds', 'usr-sha-aes', 'authPriv')

#
# Setup transport endpoint and bind it with security settings yielding
# a target name
#

# UDP/IPv4
config.addTransport(
    snmpEngine,
    udp.domainName,
    udp.UdpTwistedTransport().openClientMode()
)
config.addTargetAddr(
    snmpEngine, 'my-router',
    udp.domainName, ('195.218.195.228', 161),
    'my-creds'
)

# Error/response receiver
def cbFun(cbCtx):
    (errorIndication, errorStatus, errorIndex, varBinds) = cbCtx
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex)-1][0] or '?'
            )
        )
    else:
        for oid, val in varBinds:
            print('%s = %s' % (oid.prettyPrint(), val.prettyPrint()))

    reactor.stop()

# Prepare request to be sent yielding Twisted deferred object
df = cmdgen.GetCommandGenerator().sendReq(
    snmpEngine,
    'my-router',
    ( ('1.3.6.1.2.1.1.1.0', None), ),
)

# Register error/response receiver function at deferred
df.addCallback(cbFun)

# Run Twisted main loop
reactor.run()