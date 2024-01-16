## Route 53
- Managed, highly-available, scalable, authoritative DNS service.
- Authoritative because customer can update DNS records.
- It is also a domain registrar.
- Provides 100% availability SLA.

## Records
- Records define how traffic will be routed for a specific domain.
- Each record has domain/subdomain name, record type, value, routing policy and TTL.

## Record Types
- A: maps a hostname to a IPv4.
- AAAA: maps a hostname to a IPv6.
- CNAME: maps a hostname to a hostname.

## Hosted Zones
- A container for records controlling routing to a domain/subdomain.
- Maybe public or private. Private one is for routing in VPCs.
