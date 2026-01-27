# Networking Issues 🌐

Common symptoms
- Cannot reach public internet from private subnet
- Service-to-service timeouts
- DNS resolution failures

Checks & fixes
1. **Routing**: public subnet needs IGW; private subnet needs NAT GW/instance for egress. Verify route tables.
2. **Security groups**: allow inbound on correct ports; ensure outbound not blocked; match source SGs.
3. **NACLs**: ensure not denying ephemeral ports; keep stateless rules symmetric.
4. **DNS**: VPC DNS enabled? Check `/etc/resolv.conf`; use Route 53 resolver endpoints for hybrid.
5. **Endpoints**: add VPC Interface/Gateway Endpoints to avoid NAT/data-transfer costs.
6. **Firewalls**: check NLB/ALB target SGs and health checks; verify health check paths.

Tools
- VPC Reachability Analyzer, `traceroute`, `dig`, Flow Logs (accept/deny), ALB/NLB target health.