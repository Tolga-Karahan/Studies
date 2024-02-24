## Security
- We can encrypt the data at rest for both RDS and Aurora in launch time.
- If master is not encrypted, read replicas can't be encrypted either.
- Unencrypted database can be encrypted via snapshots.
- TLS by default for data in-flight.
- No SSH access except RDS custom.
