# Secure Development Requirements Backbone

This is a comprehensive list of all regulatory and best practice standards which might apply to your organization.

- [Secure Development Requirements Backbone](#secure-development-requirements-backbone)
  - [Regulatory](#regulatory)
    - [CCPA (California Consumer Privacy Act)](#ccpa-california-consumer-privacy-act)
    - [CPRA (California Privacy Rights Act)](#cpra-california-privacy-rights-act)
    - [FDA 21 CFR Part 11](#fda-21-cfr-part-11)
    - [FISMA (Federal Information Security Management Act)](#fisma-federal-information-security-management-act)
    - [FedRAMP (Federal Risk and Authorization Management Program)](#fedramp-federal-risk-and-authorization-management-program)
    - [GDPR (General Data Protection Regulation)](#gdpr-general-data-protection-regulation)
    - [GLBA (Gramm-Leach-Bliley Act)](#glba-gramm-leach-bliley-act)
    - [HiTRUST (Health Information Trust Alliance Common Security Framework)](#hitrust-health-information-trust-alliance-common-security-framework)
    - [HIPAA (Health Insurance Portability and Accountability Act)](#hipaa-health-insurance-portability-and-accountability-act)
    - [NAIC (National Association of Insurance Commissioners) Insurance Data Security Model Law](#naic-national-association-of-insurance-commissioners-insurance-data-security-model-law)
    - [NIST CSF (Cybersecurity Framework)](#nist-csf-cybersecurity-framework)
    - [NYS DFS Cybersecurity Regulation (23 NYCRR 500)](#nys-dfs-cybersecurity-regulation-23-nycrr-500)
    - [PCI-DSS (Payment Card Industry Data Security Standard)](#pci-dss-payment-card-industry-data-security-standard)
    - [SOX (Sarbanes-Oxley Act)](#sox-sarbanes-oxley-act)
  - [Best Practice](#best-practice)
    - [CSA CCM (Cloud Security Alliance Cloud Controls Matrix)](#csa-ccm-cloud-security-alliance-cloud-controls-matrix)
    - [ISO 22301 (Security and Resilience / Business Continuity)](#iso-22301-security-and-resilience--business-continuity)
    - [ISO/IEC 27001 (Information Security Management)](#isoiec-27001-information-security-management)
    - [ISO/IEC 27002 (Guidelines for Internet Security)](#isoiec-27002-guidelines-for-internet-security)
    - [ISO/IEC 27017 (Security Techniques for Cloud Services)](#isoiec-27017-security-techniques-for-cloud-services)
    - [ISO/IEC 27018 (Security Techniques for PII in Public Cloud)](#isoiec-27018-security-techniques-for-pii-in-public-cloud)
    - [ISO/IEC 27035 (Information Security Incident Management)](#isoiec-27035-information-security-incident-management)
    - [ISO/IEC 27701 (Security Techniques for Privacy Information Management)](#isoiec-27701-security-techniques-for-privacy-information-management)
    - [ISO/IEC 29100 (Information Technology Privacy Framework)](#isoiec-29100-information-technology-privacy-framework)
    - [MITRE ATT\&CK Framework](#mitre-attck-framework)
    - [NIST CSF (Cybersecurity Framework)](#nist-csf-cybersecurity-framework-1)
    - [NIST Digital Identity Guidelines (SP 800-63\*)](#nist-digital-identity-guidelines-sp-800-63)
    - [NIST SP 800-34 (Contingency Planning Guide for Federal Information Systems)](#nist-sp-800-34-contingency-planning-guide-for-federal-information-systems)
    - [NIST SP 800-40 (Enterprise Patch Management)](#nist-sp-800-40-enterprise-patch-management)
    - [NIST SP 800-41 (Guidelines on Firewalls and Firewall Policy)](#nist-sp-800-41-guidelines-on-firewalls-and-firewall-policy)
    - [NIST SP 800-53 (Security and Privacy Controls)](#nist-sp-800-53-security-and-privacy-controls)
    - [NIST SP 800-61 (Computer Security Incident Handling Guide)](#nist-sp-800-61-computer-security-incident-handling-guide)
    - [NIST SP 800-92 (Guide to Computer Security Log Management)](#nist-sp-800-92-guide-to-computer-security-log-management)
    - [NIST SP 800-94 (Guide to Intrusion Detection and Prevention Systems (IDPS))](#nist-sp-800-94-guide-to-intrusion-detection-and-prevention-systems-idps)
    - [NIST SP 800-128 (Guide for Security-Focused Configuration Management of Information Systems)](#nist-sp-800-128-guide-for-security-focused-configuration-management-of-information-systems)
    - [NIST SP 800-137 (ISCM for Federal Information Systems and Organizations)](#nist-sp-800-137-iscm-for-federal-information-systems-and-organizations)
    - [NIST SP 800-150 (Guide to Cyber Threat Intelligence Sharing)](#nist-sp-800-150-guide-to-cyber-threat-intelligence-sharing)
    - [OWASP API Security Top 10](#owasp-api-security-top-10)
    - [OWASP ASVS (Application Security Verification Standard)](#owasp-asvs-application-security-verification-standard)
    - [OWASP Cheat Sheet Series](#owasp-cheat-sheet-series)
    - [OWASP Source Analysis Tools](#owasp-source-analysis-tools)
    - [OWASP Top 10](#owasp-top-10)
    - [RFC 5424 (The Syslog Protocol)](#rfc-5424-the-syslog-protocol)
    - [RFC 6749 (OAuth 2.0 Authorization Framework)](#rfc-6749-oauth-20-authorization-framework)
    - [RFC 6811 (BGP Prefix Origin Validation)](#rfc-6811-bgp-prefix-origin-validation)
    - [RFC 7525 (Recommendations for TLS and DTLS)](#rfc-7525-recommendations-for-tls-and-dtls)
    - [RFC 8725 (JWT Best Current Practices)](#rfc-8725-jwt-best-current-practices)
    - [RFC 9110 (HTTP Semantics)](#rfc-9110-http-semantics)
    - [SANS CWE Top 25 Software Errors](#sans-cwe-top-25-software-errors)
    - [SANS Secure Software Development and Code Analysis Tools Whitepaper](#sans-secure-software-development-and-code-analysis-tools-whitepaper)

---

## Regulatory

Below are organizations that provide specifications for compliance.

### CCPA (California Consumer Privacy Act)

> https://oag.ca.gov/privacy/ccpa

Enhances privacy rights and consumer protection for residents of California.

### CPRA (California Privacy Rights Act)

> https://www.caprivacy.org/

Amends and enhances CCPA with additional privacy protections.

### FDA 21 CFR Part 11

> https://www.fda.gov/regulatory-information/search-fda-guidance-documents/21-cfr-part-11-electronic-records-electronic-signatures-scope-and-application

Establishes criteria for acceptance of electronic records and signatures by the FDA.

### FISMA (Federal Information Security Management Act)

> https://www.nist.gov/programs-projects/federal-information-security-management-act-fisma-implementation-project

Requires federal agencies and contractors to implement information security programs.

### FedRAMP (Federal Risk and Authorization Management Program)

> https://www.fedramp.gov/

Provides a standardized approach to security assessment, authorization, and continuous monitoring for cloud products and services used by the federal government.

### GDPR (General Data Protection Regulation)

> https://gdpr.eu/

Protects personal data and privacy for individuals within the European Union.

### GLBA (Gramm-Leach-Bliley Act)

> https://www.ftc.gov/tips-advice/business-center/privacy-and-security/gramm-leach-bliley-act

Protects consumers' personal financial information held by financial institutions.

### HiTRUST (Health Information Trust Alliance Common Security Framework)

> https://hitrustalliance.net/

Provides a certifiable framework for managing regulatory compliance and risk in healthcare information security.

### HIPAA (Health Insurance Portability and Accountability Act)

> https://www.hhs.gov/hipaa/index.html

Protects patient health information and ensures data privacy and security.

### NAIC (National Association of Insurance Commissioners) Insurance Data Security Model Law

> https://www.naic.org/

Establishes standards for data security and for the investigation and notification of data breaches applicable to insurance providers.

### NIST CSF (Cybersecurity Framework)

> https://www.nist.gov/cyberframework

Provides a policy framework for cybersecurity management.

### NYS DFS Cybersecurity Regulation (23 NYCRR 500)

> https://www.dfs.ny.gov/industry_guidance/cybersecurity

Establishes cybersecurity requirements for financial services companies.

### PCI-DSS (Payment Card Industry Data Security Standard)

> https://www.pcisecuritystandards.org/

Ensures secure handling of cardholder information by merchants and service providers.

### SOX (Sarbanes-Oxley Act)

> https://www.sec.gov/spotlight/sarbanes-oxley.htm

No specific IT requirements. Ensures financial transparency and accountability, requiring stringent financial reporting and controls.

## Best Practice

Below are published, public best practices.

### CSA CCM (Cloud Security Alliance Cloud Controls Matrix)

> https://cloudsecurityalliance.org/research/cloud-controls-matrix/

Security control framework for cloud computing.

### ISO 22301 (Security and Resilience / Business Continuity)

> https://www.iso.org/iso-22301-business-continuity.html

Provides guidelines for business continuity management systems.

### ISO/IEC 27001 (Information Security Management)

> https://www.iso.org/isoiec-27001-information-security.html

Specifies requirements for establishing, implementing, maintaining, and continually improving an information security management system (ISMS).

### ISO/IEC 27002 (Guidelines for Internet Security)

> https://www.iso.org/standard/54533.html

Provides guidelines for organizational information security standards and information security management practices.

### ISO/IEC 27017 (Security Techniques for Cloud Services)

> https://www.iso.org/standard/43757.html

Provides guidelines for information security controls applicable to the provision and use of cloud services.

### ISO/IEC 27018 (Security Techniques for PII in Public Cloud)

> https://www.iso.org/standard/61498.html

Establishes controls for protecting personal data in the cloud.

### ISO/IEC 27035 (Information Security Incident Management)

> https://www.iso.org/standard/44379.html

Provides guidelines for information security incident management.

### ISO/IEC 27701 (Security Techniques for Privacy Information Management)

> https://www.iso.org/standard/71670.html

Provides guidelines for implementing a privacy information management system (PIMS) as an extension to ISO/IEC 27001 and ISO/IEC 27002.

### ISO/IEC 29100 (Information Technology Privacy Framework)

> https://www.iso.org/standard/45123.html

Provides a high-level framework for the protection of personally identifiable information (PII) within information and communication technology systems.

### MITRE ATT&CK Framework

> https://attack.mitre.org/

Knowledge base of adversary tactics and techniques.

### NIST CSF (Cybersecurity Framework)

> https://www.nist.gov/cyberframework

Provides a policy framework for cybersecurity management.

### NIST Digital Identity Guidelines (SP 800-63*)

> https://pages.nist.gov/800-63-3/

Provides technical requirements for federal agencies implementing digital identity services.

### NIST SP 800-34 (Contingency Planning Guide for Federal Information Systems)

> https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final

Provides guidance on contingency planning for federal information systems.

### NIST SP 800-40 (Enterprise Patch Management)

> https://csrc.nist.gov/publications/detail/sp/800-40/rev-3/final

Offers guidance on managing patching and vulnerability remediation.

### NIST SP 800-41 (Guidelines on Firewalls and Firewall Policy)

> https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final

Provides guidelines on configuring and managing firewalls.

### NIST SP 800-53 (Security and Privacy Controls)

> https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final

Provides a catalog of security and privacy controls for federal information systems and organizations.

### NIST SP 800-61 (Computer Security Incident Handling Guide)

> https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

Offers guidelines for incident response.

### NIST SP 800-92 (Guide to Computer Security Log Management)

> https://csrc.nist.gov/publications/detail/sp/800-92/final

Provides guidance on log management.

### NIST SP 800-94 (Guide to Intrusion Detection and Prevention Systems (IDPS))

> https://csrc.nist.gov/publications/detail/sp/800-94/final

Provides guidelines on implementing and managing IDPS.

### NIST SP 800-128 (Guide for Security-Focused Configuration Management of Information Systems)

> https://csrc.nist.gov/publications/detail/sp/800-128/final

Offers guidance on security-focused configuration management.

### NIST SP 800-137 (ISCM for Federal Information Systems and Organizations)

> https://csrc.nist.gov/publications/detail/sp/800-137/final

Offers guidance on continuous monitoring.

### NIST SP 800-150 (Guide to Cyber Threat Intelligence Sharing)

> https://csrc.nist.gov/publications/detail/sp/800-150/final

Provides guidance on sharing cyber threat intelligence.

### OWASP API Security Top 10

> https://owasp.org/www-project-api-security/

Identifies top 10 security risks for APIs.

### OWASP ASVS (Application Security Verification Standard)

> https://owasp.org/www-project-application-security-verification-standard/

A framework for testing the security of web applications and web services.

### OWASP Cheat Sheet Series

> https://cheatsheetseries.owasp.org/

Set of concise information on various application security topics.

### OWASP Source Analysis Tools

> https://owasp.org/www-community/Source_Code_Analysis_Tools

List of tools for static and dynamic code analysis.

### OWASP Top 10

> https://owasp.org/www-project-top-ten/

Identifies top 10 security risks for web applications.

### RFC 5424 (The Syslog Protocol)

> https://tools.ietf.org/html/rfc5424

Protocol for system logging.

### RFC 6749 (OAuth 2.0 Authorization Framework)

> https://tools.ietf.org/html/rfc6749

Framework for token-based authorization.

### RFC 6811 (BGP Prefix Origin Validation)

> https://tools.ietf.org/html/rfc6811

Mechanism to validate the origination of BGP announcements.

### RFC 7525 (Recommendations for TLS and DTLS)

> https://tools.ietf.org/html/rfc7525

Best practices for using TLS and DTLS securely.

### RFC 8725 (JWT Best Current Practices)

> https://tools.ietf.org/html/rfc8725

Best practices for securely using JSON Web Tokens (JWT).

### RFC 9110 (HTTP Semantics)

> https://tools.ietf.org/html/rfc9110

Defines the semantics of HTTP.

### SANS CWE Top 25 Software Errors

> https://cwe.mitre.org/top25/

Lists the top 25 most dangerous software weaknesses.

### SANS Secure Software Development and Code Analysis Tools Whitepaper

> https://www.sans.org/reading-room/whitepapers/securecode/secure-software-development-code-analysis-tools-36697

Guidelines and tools for secure software development and code analysis.