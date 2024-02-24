## Route 53
- Managed, highly-available, scalable, authoritative DNS service.
- Authoritative because customer can update DNS records.
- It is also a domain registrar.
- Provides 100% availability SLA.
- We can set TTL so that clients cache responses from Route 53 and makes less requests.
- High TTL causes outdated records on client side, but causes less traffic.
- TTL is required for each record except alias records.
- Allows setting records for domains provided by other registrars.

## Records
- Records define how traffic will be routed for a specific domain.
- Each record has domain/subdomain name, record type, value, routing policy and TTL.

## Record Types
- A: maps a hostname to a IPv4.
- AAAA: maps a hostname to a IPv6.
- CNAME: maps a hostname to a hostname.

## Alias
- We can use alias to point a hostname to a AWS resource. A CNAME also can be used, but CNAMEs don't work for root domains.
- Only A or AAAA type record can be created as alias.
- TTL can't be set on alias, it is set by Route 53.

## Hosted Zones
- A container for records controlling routing to a domain/subdomain.
- Maybe public or private. Private one is for routing in VPCs.

## Routing Policies
- It is how Route 53 responds to DNS queries, not routing traffic.
- Simple Policy:
    - For translating names to a single resource.
    - Multiple values can be returned in the same record in which case client randomly picks one.
    - One AWS resource can be specified in case alias enabled.
    - Health check is not allowed.
- Weighted Policy:
    - Allows controlling percentage of requests that goes to each resource.
    - Each record is assigned a weight.
    - Records must have same name and type.
    - Supports health checks.
- Latency-based:
    - Purpose is resolving to the resource that has least latency.
    - Supports health check.
- Failover(Active-Passive) Policy:
    - Imagine that there are two EC2 instances. One primary and one secondary. In case health check of  
primary fails, Route 53 automatically failover to secondary instance.
- Geolocation Policy:
    - Location based policy.
    - Requests are handled based on their location.
- Geoproximity Policy:
    - Requests are handled based on their location.
    - Each region gets a bias value which specifies how frequent traffic will be routed.
    - Range is 1-99 to expand traffic and -1--99 to shrink the traffic.
    - Resources can be AWS resources as well as non-AWS resources.
    - Require using Route 53 traffic flow.
- IP-Based Policy:
    - Based on client's IP addresses.
    - A list of CIDRs and corresponding locations are specified.
- Multi-value Policy:
    - Used to route traffic to multiple resources.
    - Supports health checks.
    - Up to 8 healthy resources can be returned by each query.
    - Not a substitute for ELB, it can be used as client-side load balancer.

## Health Checks
- Useful to not resolve names to resources that aren't healthy.
- Health checks may monitor endpoints, other health checks(calculated health checks) or CloudWatch Alarms.
- 15 global health checkers monitors an endpoint.
- They can't directly access to private endpoints, but we can set up CloudWatch metrics and alarms so that  
it can check private endpoints indirectly.