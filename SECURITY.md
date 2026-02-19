# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 2.2.x   | Yes       |
| < 2.2   | No        |

## Reporting a Vulnerability

If you discover a security vulnerability in MW-Omega, including but not limited to:

- Exposed credentials or secrets in any file
- Cryptographic implementation weaknesses
- Hash verification bypass possibilities
- IP protection gaps

**Do not open a public issue.**

Instead, email **abrahamkolo@gmail.com** with:

1. Description of the vulnerability
2. Steps to reproduce
3. Potential impact assessment

You will receive acknowledgment within 48 hours and a substantive response within 7 business days.

## Cryptographic Standards

MW-Omega uses the following cryptographic standards for document sealing and verification:

**Implemented:**
- **Hashing**: SHA3-512 (see `scripts/hash-verify.py`)

**Planned (Stack Deployment Phase 1):**
- **Signing**: Ed25519
- **Timestamping**: OpenTimestamps (Bitcoin-backed) + notarization for foundational documents
- **Encryption at rest**: git-crypt or GPG

## Scope

This security policy covers the MW-Omega repository and all associated skill modules, scripts, and documentation. It does not cover external platforms (Amazon KDP, Substack, etc.) where MW-Omega outputs are published.
