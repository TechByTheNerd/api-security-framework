# Actions

Below is a table of contents for help navigating this page:

- [Actions](#actions)
  - [Sysadmins and Automation Engineers](#sysadmins-and-automation-engineers)
    - [Configuration Management](#configuration-management)
    - [Encryption](#encryption)
    - [Incident Response](#incident-response)
  - [Software Architects](#software-architects)
    - [Access Control](#access-control)
    - [Authentication and Authorization](#authentication-and-authorization)
    - [Configuration Management](#configuration-management-1)
    - [Data Protection](#data-protection)
    - [Incident Response](#incident-response-1)
  - [Developers](#developers)
    - [Cryptographic Controls](#cryptographic-controls)
    - [Error Handling](#error-handling)
    - [Input Validation](#input-validation)
    - [Logging and Monitoring](#logging-and-monitoring)
    - [Access Controls](#access-controls)
    - [Authentication and Authorization](#authentication-and-authorization-1)
    - [Secure Coding Practices](#secure-coding-practices)

---

## Sysadmins and Automation Engineers

Below are the items to address, sorted by category.

### Configuration Management

- CCPA - Data Security: Implement and maintain reasonable security procedures and practices to protect personal data from unauthorized access, destruction, use, modification, or disclosure: CCPA §1798.150(a)(1) - [Link](https://oag.ca.gov/privacy/ccpa)

- CPRA - Data Security: Maintain reasonable security procedures and practices appropriate to the nature of the personal data to protect against unauthorized access and disclosure: CPRA §1798.185(a)(1) - [Link](https://www.caprivacy.org/)

- FDA 21 CFR Part 11 - Record Retention: Ensure electronic records are retained for the required period and are retrievable: 21 CFR §11.10(c) - [Link](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/21-cfr-part-11-electronic-records-electronic-signatures-scope-and-application)

- FISMA - Continuous Monitoring: Implement continuous monitoring of information systems to detect and respond to security incidents: FISMA §3544(b)(7)(C) - [Link](https://www.nist.gov/programs-projects/federal-information-security-management-act-fisma-implementation-project)

- FedRAMP - Configuration Management: Apply secure configuration management practices to ensure cloud systems are maintained in a secure state: FedRAMP Configuration Management - [Link](https://www.fedramp.gov/)

- GLBA - Access Controls: Limit access to customer information to those who need it to perform their job duties: GLBA Safeguards Rule §314.4(c) - [Link](https://www.ftc.gov/tips-advice/business-center/privacy-and-security/gramm-leach-bliley-act)

- HiTRUST - Data Protection: Implement controls to protect the confidentiality, integrity, and availability of healthcare data: HiTRUST CSF 01.b - [Link](https://hitrustalliance.net/)

- HIPAA - Access Controls: Implement technical policies and procedures to limit access to electronic protected health information (ePHI) to authorized persons: HIPAA 45 CFR 164.312(a)(1) - [Link](https://www.hhs.gov/hipaa/index.html)

- NAIC - Data Security Program: Implement a comprehensive information security program based on an assessment of risks: NAIC Model Law §4 - [Link](https://www.naic.org/)

- NYS DFS - Cybersecurity Program: Implement a cybersecurity program to protect the confidentiality, integrity, and availability of information systems: 23 NYCRR 500.02 - [Link](https://www.dfs.ny.gov/industry_guidance/cybersecurity)

- PCI-DSS - Network Security: Install and maintain a firewall configuration to protect cardholder data: PCI-DSS Requirement 1 - [Link](https://www.pcisecuritystandards.org/)

- ISO/IEC 27001 - Configuration Management: Apply secure configuration management practices: ISO/IEC 27001:2013 A.12.1 - [Link](https://www.iso.org/isoiec-27001-information-security.html)

- NIST SP 800-128 - Configuration Management Policy: Develop and implement a configuration management policy: NIST SP 800-128 Section 2.1 - [Link](https://csrc.nist.gov/publications/detail/sp/800-128/final)

- OWASP API Security Top 10 - Secure API Gateway setup: OWASP API Security Top 10: API9:2019 - [Link](https://owasp.org/www-project-api-security/)

### Encryption

- CCPA - Encryption: Encrypt personal data both at rest and in transit to protect against unauthorized access: CCPA §1798.81.5 - [Link](https://oag.ca.gov/privacy/ccpa)

- CPRA - Data Security: Encrypt personal data both at rest and in transit: CPRA §1798.185(a)(1) - [Link](https://www.caprivacy.org/)

- FDA 21 CFR Part 11 - Encryption: Encrypt electronic records to protect against unauthorized access: 21 CFR §11.30 - [Link](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/21-cfr-part-11-electronic-records-electronic-signatures-scope-and-application)

- FISMA - Data Encryption: Encrypt sensitive data to protect it during transmission and storage: FISMA §3544(a)(1)(A)(ii)(II) - [Link](https://www.nist.gov/programs-projects/federal-information-security-management-act-fisma-implementation-project)

- FedRAMP - Encryption: Encrypt data at rest and in transit to protect sensitive information: FedRAMP Encryption Requirements - [Link](https://www.fedramp.gov/)

- GLBA - Encryption: Encrypt customer information to protect it during transmission and storage: GLBA Safeguards Rule §314.4(b)(2) - [Link](https://www.ftc.gov/tips-advice/business-center/privacy-and-security/gramm-leach-bliley-act)

- HiTRUST - Encryption: Encrypt healthcare data both at rest and in transit to protect against unauthorized access: HiTRUST CSF 10.1.1 - [Link](https://hitrustalliance.net/)

- HIPAA - Encryption: Encrypt ePHI to protect it during transmission and storage: HIPAA 45 CFR 164.312(a)(2)(iv) - [Link](https://www.hhs.gov/hipaa/index.html)

- NAIC - Encryption: Encrypt non-public information both in transit and at rest: NAIC Model Law §4 - [Link](https://www.naic.org/)

- NYS DFS - Encryption: Encrypt non-public information both in transit and at rest: 23 NYCRR 500.15 - [Link](https://www.dfs.ny.gov/industry_guidance/cybersecurity)

- PCI-DSS - Encryption: Encrypt transmission of cardholder data across open, public networks: PCI-DSS Requirement 4 - [Link](https://www.pcisecuritystandards.org/)

- ISO/IEC 27001 - Cryptographic Controls: Use cryptographic controls to protect the confidentiality, integrity, and availability of information: ISO/IEC 27001:2013 A.10.1.1 - [Link](https://www.iso.org/isoiec-27001-information-security.html)

- NIST SP 800-53 - System and Communications Protection: Encrypt data transmitted through APIs to protect its confidentiality and integrity: NIST SP 800-53 SC-1 - [Link](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)

- NIST SP 800-94 - Cryptographic Controls: Encrypt sensitive data transmitted and stored by information systems: NIST SP 800-94 Section 4.2 - [Link](https://csrc.nist.gov/publications/detail/sp/800-94/final)

- OWASP API Security Top 10 - API Encryption: Encrypt sensitive data transmitted through APIs: OWASP API Security Top 10: API7:2019 - [Link](https://owasp.org/www-project-api-security/)

### Incident Response

- CCPA - Data Breach Notification: Establish procedures for promptly notifying affected individuals in the event of a data breach: CCPA §1798.82 - [Link](https://oag.ca.gov/privacy/ccpa)

- CPRA - Data Protection Impact Assessments: Conduct assessments to identify and mitigate risks related to data processing activities: CPRA §1798.185(a)(15) - [Link](https://www.caprivacy.org/)

- FDA 21 CFR Part 11 - Incident Response: Develop and test incident response plans for healthcare data breaches: HiTRUST CSF 12.1.1 - [Link](https://hitrustalliance.net/)

- FISMA - Incident Response: Establish incident response procedures and conduct regular testing: FISMA §3544(b)(7)(D) - [Link](https://www.nist.gov/programs-projects/federal-information-security-management-act-fisma-implementation-project)

- FedRAMP - Incident Response: Develop and test incident response plans for cloud systems: FedRAMP Incident Response Requirements - [Link](https://www.fedramp.gov/)

- GLBA - Incident Response: Develop and implement an incident response plan to respond to security incidents: GLBA Safeguards Rule §314.4(e) - [Link](https://www.ftc.gov/tips-advice/business-center/privacy-and-security/gramm-leach-bliley-act)

- HiTRUST - Incident Response: Develop and test incident response plans for healthcare data breaches: HiTRUST CSF 12.1.1 - [Link](https://hitrustalliance.net/)

- HIPAA - Incident Response: Establish procedures for responding to security incidents involving ePHI: HIPAA 45 CFR 164.308(a)(6) - [Link](https://www.hhs.gov/hipaa/index.html)

- NAIC - Incident Response: Develop and maintain a written incident response plan to promptly respond to data breaches: NAIC Model Law §4 - [Link](https://www.naic.org/)

- NYS DFS - Incident Response: Develop and maintain a written incident response plan to promptly respond to data breaches: 23 NYCRR 500.16 - [Link](https://www.dfs.ny.gov/industry_guidance/cybersecurity)

- PCI-DSS - Regular Testing: Regularly test security systems and processes: PCI-DSS Requirement 11 - [Link](https://www.pcisecuritystandards.org/)

- ISO/IEC 27001 - Information Security Incident Management: Establish an incident management process to respond to and manage security incidents: ISO/IEC 27001:2013 A.16.1.1 - [Link](https://www.iso.org/isoiec-27001-information-security.html)

- NIST SP 800-61 - Incident Response Policy: Develop and implement an incident response policy: NIST SP 800-61 Section 2.2 - [Link](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)

- OWASP API Security Top 10 - Logging and Monitoring: Log and monitor API activities to detect and respond to security incidents: OWASP API Security Top 10: API10:2019 - [Link](https://owasp.org/www-project-api-security/)

---

## Software Architects

Below are the items to address, sorted by category.

### Access Control

- CPRA - Data Classification: Classify personal data based on sensitivity and apply appropriate security measures: CPRA §1798.185(a)(15) - [Link](https://www.caprivacy.org/)

- FISMA - Access Controls: Ensure only authorized individuals have access to information systems: FISMA §3544(a)(1)(A)(ii)(I) - [Link](https://www.nist.gov/programs-projects/federal-information-security-management-act-fisma-implementation-project)

- GLBA - Access Controls: Limit access to customer information to those who need it to perform their job duties: GLBA Safeguards Rule §314.4(c) - [Link](https://www.ftc.gov/tips-advice/business-center/privacy-and-security/gramm-leach-bliley-act)

- HIPAA - Access Controls: Implement technical policies and procedures to limit access to electronic protected health information (ePHI) to authorized persons: HIPAA 45 CFR 164.312(a)(1) - [Link](https://www.hhs.gov/hipaa/index.html)

- ISO/IEC 27001 - Access Control: Implement access control policies to ensure only authorized access to information systems: ISO/IEC 27001:2013 A.9.1.1 - [Link](https://www.iso.org/isoiec-27001-information-security.html)

- ISO/IEC 27017 - Access Control: Implement access control measures specific to cloud environments: ISO/IEC 27017:2015 9.1.1 - [Link](https://www.iso.org/standard/43757.html)

- ISO/IEC 27018 - Access Control: Restrict access to personal data to authorized individuals: ISO/IEC 27018:2019 8.2 - [Link](https://www.iso.org/standard/61498.html)

- ISO/IEC 27701 - Access Controls: Implement access controls to protect personal data: ISO/IEC 27701:2019 6.4 - [Link](https://www.iso.org/standard/71670.html)

- ISO/IEC 29100 - Access Controls: Implement access controls to restrict access to PII: ISO/IEC 29100:2011 Clause 4.3 - [Link](https://www.iso.org/standard/45123.html)

- NIST SP 800-53 - Access Control: Implement access control policies to restrict access to information systems: NIST SP 800-53 AC-1 - [Link](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)

- OWASP ASVS - Access Control Verification: Enforce proper access control measures: OWASP ASVS V4 - [Link](https://owasp.org/www-project-application-security-verification-standard/)

- OWASP Cheat Sheet - Access Control Enforcement: Consistently enforce access control checks on both the server and client sides: Access Control Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)

### Authentication and Authorization

- HIPAA - Authentication and Authorization: Implement technical policies and procedures for user authentication and authorization: HIPAA 45 CFR 164.312(d) - [Link](https://www.hhs.gov/hipaa/index.html)

- ISO/IEC 27001 - Identification and Authentication: Ensure proper identification and authentication mechanisms: ISO/IEC 27001:2013 A.9.2.1 - [Link](https://www.iso.org/isoiec-27001-information-security.html)

- NIST Digital Identity Guidelines - Authentication Assurance Levels: Use appropriate authentication mechanisms to achieve required assurance levels: NIST SP 800-63B Section 4.1 - [Link](https://pages.nist.gov/800-63-3/)

- OWASP ASVS - Authentication Verification: Ensure robust authentication mechanisms are in place: OWASP ASVS V1 - [Link](https://owasp.org/www-project-application-security-verification-standard/)

- OWASP Cheat Sheet - Multi-Factor Authentication: Implement multi-factor authentication to enhance security: Authentication Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

- RFC 6749 - Client Authentication: Ensure clients are authenticated securely when requesting tokens, using mechanisms such as client secrets or public/private key pairs: RFC 6749 Section 2.3.1 - [Link](https://tools.ietf.org/html/rfc6749)

### Configuration Management

- CPRA - Data Protection Impact Assessments: Conduct assessments to identify and mitigate risks related to data processing activities: CPRA §1798.185(a)(15) - [Link](https://www.caprivacy.org/)

- FISMA - Configuration Management: Apply secure configuration management practices: FISMA §3544(a)(1)(A)(ii)(III) - [Link](https://www.nist.gov/programs-projects/federal-information-security-management-act-fisma-implementation-project)

- FedRAMP - Configuration Management: Apply secure configuration management practices to ensure cloud systems are maintained in a secure state: FedRAMP Configuration Management - [Link](https://www.fedramp.gov/)

- ISO/IEC 27001 - Configuration Management: Apply secure configuration management practices: ISO/IEC 27001:2013 A.12.1 - [Link](https://www.iso.org/isoiec-27001-information-security.html)

- NIST SP 800-128 - Configuration Management Policy: Develop and implement a configuration management policy: NIST SP 800-128 Section 2.1 - [Link](https://csrc.nist.gov/publications/detail/sp/800-128/final)

- OWASP Cheat Sheet - Secure Configuration Management: Follow best practices for secure configuration management: Configuration Management Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Configuration_Management_Cheat_Sheet.html)

### Data Protection

- CCPA - Data Minimization: Collect and retain only as much personal data as needed for processing purposes: CCPA §1798.100(b) - [Link](https://oag.ca.gov/privacy/ccpa)

- CPRA - Data Minimization: Ensure that the collection, usage, retention, and sharing of personal data is limited to what is necessary: CPRA §1798.100(c) - [Link](https://www.caprivacy.org/)

- FDA 21 CFR Part 11 - Data Integrity: Ensure the integrity of electronic records through the use of validated systems: 21 CFR §11.10(a) - [Link](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/21-cfr-part-11-electronic-records-electronic-signatures-scope-and-application)

- FISMA - Data Encryption: Encrypt sensitive data to protect it during transmission and storage: FISMA §3544(a)(1)(A)(ii)(II) - [Link](https://www.nist.gov/programs-projects/federal-information-security-management-act-fisma-implementation-project)

- FedRAMP - Data Protection: Protect data in transit and at rest using encryption and data masking: FedRAMP Encryption Requirements - [Link](https://www.fedramp.gov/)

- GDPR - Data Protection by Design: Integrate data protection into the development and operation of information systems: GDPR Article 25(1) - [Link](https://gdpr.eu/)

- HiTRUST - Data Protection: Implement controls to protect the confidentiality, integrity, and availability of healthcare data: HiTRUST CSF 01.b - [Link](https://hitrustalliance.net/)

- HIPAA - Data Encryption: Encrypt ePHI to protect it during transmission and storage: HIPAA 45 CFR 164.312(a)(2)(iv) - [Link](https://www.hhs.gov/hipaa/index.html)

- ISO/IEC 27001 - Cryptographic Controls: Use cryptographic controls to protect the confidentiality, integrity, and availability of information: ISO/IEC 27001:2013 A.10.1.1 - [Link](https://www.iso.org/isoiec-27001-information-security.html)

- ISO/IEC 27018 - Data Encryption: Encrypt personal data both at rest and in transit: ISO/IEC 27018:2019 8.3 - [Link](https://www.iso.org/standard/61498.html)

- ISO/IEC 27701 - Data Minimization: Ensure only necessary personal data is collected and processed: ISO/IEC 27701:2019 6.5 - [Link](https://www.iso.org/standard/71670.html)

- ISO/IEC 29100 - Data Minimization: Ensure PII collection and processing is limited to what is necessary: ISO/IEC 29100:2011 Clause 4.4 - [Link](https://www.iso.org/standard/45123.html)

- NIST SP 800-53 - System and Communications Protection: Encrypt data transmitted through APIs to protect its confidentiality and integrity: NIST SP 800-53 SC-1 - [Link](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)

- OWASP ASVS - Data Protection: Ensure sensitive data is properly protected: OWASP ASVS V8 - [Link](https://owasp.org/www-project-application-security-verification-standard/)

- OWASP Cheat Sheet - Data at Rest: Encrypt sensitive data at rest to protect it from unauthorized access: Cryptographic Storage Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)

### Incident Response

- FISMA - Incident Response: Establish incident response procedures and conduct regular testing: FISMA §3544(b)(7)(D) - [Link](https://www.nist.gov/programs-projects/federal-information-security-management-act-fisma-implementation-project)

- GLBA - Incident Response: Develop and implement an incident response plan to respond to security incidents: GLBA Safeguards Rule §314.4(e) - [Link](https://www.ftc.gov/tips-advice/business-center/privacy-and-security/gramm-leach-bliley-act)

- HIPAA - Incident Response: Establish procedures for responding to security incidents involving ePHI: HIPAA 45 CFR 164.308(a)(6) - [Link](https://www.hhs.gov/hipaa/index.html)

- NIST SP 800-61 - Incident Response Policy: Develop and implement an incident response policy: NIST SP 800-61 Section 2.2 - [Link](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)

- OWASP API Security Top 10 - Logging and Monitoring: Log and monitor API activities to detect and respond to security incidents: OWASP API Security Top 10: API10:2019 - [Link](https://owasp.org/www-project-api-security/)

- ISO/IEC 27035 - Incident Detection: Implement mechanisms for detecting information security incidents: ISO/IEC 27035-1:2016 Clause 7 - [Link](https://www.iso.org/standard/44379.html)

- ISO/IEC 27035 - Incident Response: Develop and maintain an incident response plan to handle information security incidents: ISO/IEC 27035-1:2016 Clause 9 - [Link](https://www.iso.org/standard/44379.html)

- ISO/IEC 27035 - Root Cause Analysis: Conduct root cause analysis to prevent recurrence of incidents: ISO/IEC 27035-1:2016 Clause 10 - [Link](https://www.iso.org/standard/44379.html)

- ISO/IEC 27035 - Post-Incident Review: Perform post-incident reviews to improve the incident management process: ISO/IEC 27035-1:2016 Clause 11 - [Link](https://www.iso.org/standard/44379.html)

---

## Developers

Below are the items to address, sorted by category.

### Cryptographic Controls

- ISO/IEC 27001 - Cryptographic Controls: Use cryptographic controls to protect the confidentiality, integrity, and availability of information: ISO/IEC 27001:2013 A.10.1.1 - [Link](https://www.iso.org/isoiec-27001-information-security.html)

- HIPAA - Encryption: Encrypt ePHI to protect it during transmission and storage: HIPAA 45 CFR 164.312(a)(2)(iv) - [Link](https://www.hhs.gov/hipaa/index.html)

- GLBA - Encryption: Encrypt customer information to protect it during transmission and storage: GLBA Safeguards Rule §314.4(b)(2) - [Link](https://www.ftc.gov/tips-advice/business-center/privacy-and-security/gramm-leach-bliley-act)

- ISO/IEC 27018 - Data Encryption: Encrypt personal data both at rest and in transit: ISO/IEC 27018:2019 8.3 - [Link](https://www.iso.org/standard/61498.html)

- PCI-DSS - Encryption: Encrypt transmission of cardholder data across open, public networks: PCI-DSS Requirement 4 - [Link](https://www.pcisecuritystandards.org/)

- OWASP ASVS - Cryptographic Controls: Use strong cryptographic controls to protect data: OWASP ASVS V6 - [Link](https://owasp.org/www-project-application-security-verification-standard/)

- OWASP Cheat Sheet - Encryption Algorithms: Use strong encryption algorithms, such as AES, for data encryption: Cryptographic Storage Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)

- OWASP Cheat Sheet - Data in Transit: Encrypt data in transit using protocols such as TLS: Cryptographic Storage Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)

- OAuth 2.0 Security Best Current Practice - Access Token Binding: Bind access tokens to client identifiers to prevent token misuse: OAuth 2.0 Security BCP Section 3.3 - [Link](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics)

- RFC 7525 - TLS Configuration: Configure TLS securely to protect data in transit: RFC 7525 Section 3.1 - [Link](https://tools.ietf.org/html/rfc7525)

- RFC 7636 - PKCE Support: Implement PKCE to enhance the security of the authorization code flow: RFC 7636 Section 4 - [Link](https://tools.ietf.org/html/rfc7636)

- RFC 8725 - Algorithm Selection: Use secure algorithms for signing and encryption: RFC 8725 Section 3 - [Link](https://tools.ietf.org/html/rfc8725)

### Error Handling

- OWASP Cheat Sheet - Generic Error Messages: Display generic error messages to users to avoid revealing sensitive information: Error Handling Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html)

- OWASP Cheat Sheet - Detailed Logging: Log detailed error information for debugging and auditing purposes: Error Handling Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html)

- OWASP Cheat Sheet - Exception Handling: Use structured exception handling to manage errors gracefully: Error Handling Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html)

- OWASP Cheat Sheet - API Error Messages: Ensure API error responses do not reveal sensitive information: Error Handling Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html)

- OWASP Cheat Sheet - API Error Logging: Log detailed error information for API requests: Error Handling Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html)

- OWASP Cheat Sheet - API Exception Handling: Use structured exception handling in APIs to manage errors gracefully: Error Handling Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html)

- OWASP API Security Top 10 - Error Handling: Implement proper error handling to avoid exposing sensitive information: OWASP API Security Top 10: API8:2019 - [Link](https://owasp.org/www-project-api-security/)

- ISO/IEC 27002 - Error Handling: Implement proper error handling to prevent information leakage: ISO/IEC 27002:2013 A.14.2.7 - [Link](https://www.iso.org/standard/54533.html)

- SANS CWE Top 25 - Error Handling: Implement proper error handling to prevent information leakage: CWE-209 - [Link](https://cwe.mitre.org/top25/)

### Input Validation

- OWASP Cheat Sheet - Whitelist Input Validation: Use whitelist validation to allow only known good inputs: Input Validation Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)

- OWASP Cheat Sheet - Input Sanitization: Sanitize inputs to remove or neutralize potentially harmful data: Input Validation Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)

- OWASP Cheat Sheet - Regular Expressions: Use regular expressions carefully to validate input formats: Input Validation Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)

- OWASP Cheat Sheet - Input Length Checks: Validate input lengths to prevent buffer overflow and other attacks: Input Validation Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)

- OWASP API Security Top 10 - Input Validation: Validate all inputs to APIs to prevent injection attacks: OWASP API Security Top 10: API5:2019 - [Link](https://owasp.org/www-project-api-security/)

- ISO/IEC 27001 - Input Validation: Validate inputs to prevent common vulnerabilities: ISO/IEC 27001:2013 A.14.2.4 - [Link](https://www.iso.org/isoiec-27001-information-security.html)

- SANS CWE Top 25 - Input Validation: Ensure proper validation of inputs to prevent common vulnerabilities such as SQL injection and buffer overflow: CWE-20, CWE-79 - [Link](https://cwe.mitre.org/top25/)

### Logging and Monitoring

- FISMA - Audit Trails: Maintain audit logs to monitor and record system activity: FISMA §3544(a)(1)(A)(ii)(III) - [Link](https://www.nist.gov/programs-projects/federal-information-security-management-act-fisma-implementation-project)

- GLBA - Audit Trails: Maintain logs to monitor and record access to customer information: GLBA Safeguards Rule §314.4(b)(3) - [Link](https://www.ftc.gov/tips-advice/business-center/privacy-and-security/gramm-leach-bliley-act)

- HIPAA - Audit Controls: Implement hardware, software, and/or procedural mechanisms to record and examine access and other activity in information systems that contain or use ePHI: HIPAA 45 CFR 164.312(b) - [Link](https://www.hhs.gov/hipaa/index.html)

- ISO/IEC 27001 - Logging and Monitoring: Implement logging and monitoring controls to detect and respond to security incidents: ISO/IEC 27001:2013 A.12.4.1 - [Link](https://www.iso.org/isoiec-27001-information-security.html)

- NIST SP 800-92 - Log Management Policy: Develop and implement a log management policy: NIST SP 800-92 Section 2 - [Link](https://csrc.nist.gov/publications/detail/sp/800-92/final)

- OWASP API Security Top 10 - Logging and Monitoring: Log and monitor API activities to detect and respond to security incidents: OWASP API Security Top 10: API10:2019 - [Link](https://owasp.org/www-project-api-security/)

- OWASP Cheat Sheet - Log Sensitive Data: Avoid logging sensitive data such as passwords and credit card numbers: Logging Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

- OWASP Cheat Sheet - Log Integrity: Protect logs from tampering by implementing integrity controls: Logging Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

- OWASP Cheat Sheet - Log Access Controls: Restrict access to logs to authorized personnel only: Logging Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

- OWASP Cheat Sheet - Log Retention: Define and implement log retention policies to comply with legal and operational requirements: Logging Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

- OWASP Cheat Sheet - Log Analysis: Regularly analyze logs to detect and respond to security incidents: Logging Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

- PCI-DSS - Audit Trails: Track and monitor all access to network resources and cardholder data: PCI-DSS Requirement 10 - [Link](https://www.pcisecuritystandards.org/)

- SANS CWE Top 25 - Logging and Monitoring: Maintain logs and monitor activities to detect and respond to security incidents: CWE-778 - [Link](https://cwe.mitre.org/top25/)

### Access Controls

- ISO/IEC 27001 - Access Control: Implement access control policies to ensure only authorized access to information systems: ISO/IEC 27001:2013 A.9.1.1 - [Link](https://www.iso.org/isoiec-27001-information-security.html)

- HIPAA - Access Controls: Implement technical policies and procedures to limit access to electronic protected health information (ePHI) to authorized persons: HIPAA 45 CFR 164.312(a)(1) - [Link](https://www.hhs.gov/hipaa/index.html)

- GLBA - Access Controls: Limit access to customer information to those who need it to perform their job duties: GLBA Safeguards Rule §314.4(c) - [Link](https://www.ftc.gov/tips-advice/business-center/privacy-and-security/gramm-leach-bliley-act)

- NIST SP 800-53 - Access Control: Implement access control policies to restrict access to information systems: NIST SP 800-53 AC-1 - [Link](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)

- NIST SP 800-63 - Identity Proofing: Implement identity proofing processes to validate the identity of users: NIST SP 800-63A Section 4.2 - [Link](https://pages.nist.gov/800-63-3/)

- PCI-DSS - Access Controls: Restrict access to cardholder data by business need to know: PCI-DSS Requirement 7 - [Link](https://www.pcisecuritystandards.org/)

- OWASP ASVS - Access Control Verification: Enforce proper access control measures: OWASP ASVS V4 - [Link](https://owasp.org/www-project-application-security-verification-standard/)

- OWASP Cheat Sheet - Role-Based Access Control (RBAC): Implement RBAC to restrict access to resources based on user roles: Access Control Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)

- OWASP Cheat Sheet - Least Privilege: Apply the principle of least privilege to limit user access rights: Access Control Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)

- OWASP Cheat Sheet - Access Control Lists (ACLs): Use ACLs to define and enforce access policies: Access Control Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)

- OWASP Cheat Sheet - Segregation of Duties: Ensure that critical tasks require multiple users to prevent fraud and abuse: Access Control Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)

### Authentication and Authorization

- ISO/IEC 27001 - Identification and Authentication: Ensure proper identification and authentication mechanisms: ISO/IEC 27001:2013 A.9.2.1 - [Link](https://www.iso.org/isoiec-27001-information-security.html)

- HIPAA - Access Controls: Implement technical policies and procedures to limit access to electronic protected health information (ePHI) to authorized persons: HIPAA 45 CFR 164.312(a)(1) - [Link](https://www.hhs.gov/hipaa/index.html)

- PCI-DSS - Authentication: Assign a unique ID to each person with computer access to cardholder data: PCI-DSS Requirement 8 - [Link](https://www.pcisecuritystandards.org/)

- OWASP ASVS - Authentication Verification: Ensure robust authentication mechanisms are in place: OWASP ASVS V1 - [Link](https://owasp.org/www-project-application-security-verification-standard/)

- OWASP Cheat Sheet - Password Storage: Use strong, one-way hashing algorithms with a salt for storing passwords: Authentication Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

- OWASP Cheat Sheet - Multi-Factor Authentication: Implement multi-factor authentication to enhance security: Authentication Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

- OWASP Cheat Sheet - Account Lockout: Implement account lockout mechanisms to prevent brute force attacks: Authentication Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

- OWASP Cheat Sheet - Password Complexity: Enforce password complexity requirements to ensure strong passwords: Authentication Cheat Sheet - [Link](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

- OAuth 2.0 Security Best Current Practice - Client Authentication: Ensure confidential clients are registered with secrets or other credentials: OAuth 2.0 Security BCP Section 3.5 - [Link](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics)

- RFC 6749 - Authorization Code Grant: Implement the authorization code grant for obtaining access tokens securely: RFC 6749 Section 4.1 - [Link](https://tools.ietf.org/html/rfc6749)

- RFC 6749 - Implicit Grant: Use the implicit grant with caution for public clients: RFC 6749 Section 4.2 - [Link](https://tools.ietf.org/html/rfc6749)

- RFC 6749 - Resource Owner Password Credentials Grant: Use this grant type for highly trusted clients only: RFC 6749 Section 4.3 - [Link](https://tools.ietf.org/html/rfc6749)

- RFC 6749 - Client Credentials Grant: Use the client credentials grant for machine-to-machine authentication: RFC 6749 Section 4.4 - [Link](https://tools.ietf.org/html/rfc6749)

- RFC 6749 - Access Token Security: Protect access tokens using secure storage mechanisms: RFC 6749 Section 10.3 - [Link](https://tools.ietf.org/html/rfc6749)

- RFC 6749 - Refresh Tokens: Use refresh tokens to obtain new access tokens: RFC 6749 Section 10.4 - [Link](https://tools.ietf.org/html/rfc6749)

- RFC 6749 - Client Authentication: Ensure clients are authenticated securely when requesting tokens: RFC 6749 Section 2.3.1 - [Link](https://tools.ietf.org/html/rfc6749)

- RFC 6749 - Scope Management: Define and enforce scopes for access tokens: RFC 6749 Section 3.3 - [Link](https://tools.ietf.org/html/rfc6749)

- RFC 6749 - State Parameter: Use the state parameter to prevent CSRF attacks: RFC 6749 Section 10.12 - [Link](https://tools.ietf.org/html/rfc6749)

- RFC 7009 - Token Revocation: Implement token revocation endpoints to invalidate access and refresh tokens: RFC 7009 Section 2.1 - [Link](https://tools.ietf.org/html/rfc7009)

- RFC 7636 - PKCE Support: Implement PKCE to enhance the security of the authorization code flow: RFC 7636 Section 4 - [Link](https://tools.ietf.org/html/rfc7636)

### Secure Coding Practices

- OWASP ASVS - Secure Development: Ensure secure development practices are followed throughout the software development lifecycle: OWASP ASVS V14 - [Link](https://owasp.org/www-project-application-security-verification-standard/)

- ISO/IEC 27002 - Secure Development: Follow secure development practices for software development and maintenance: ISO/IEC 27002:2013 A.14.2.1 - [Link](https://www.iso.org/standard/54533.html)

- ISO/IEC 27035 - Secure Development: Implement secure development practices to prevent vulnerabilities: ISO/IEC 27035:2016 A.14.2.1 - [Link](https://www.iso.org/standard/44379.html)

- OWASP Cheat Sheet - Secure Development Lifecycle: Follow a secure development lifecycle (SDLC) to incorporate security at each stage of software development: SANS Whitepaper - [Link](https://www.sans.org/reading-room/whitepapers/securecode/secure-software-development-code-analysis-tools-36697)

- OWASP Cheat Sheet - Static Code Analysis: Use static code analysis tools to identify vulnerabilities early in the development process: SANS Whitepaper - [Link](https://www.sans.org/reading-room/whitepapers/securecode/secure-software-development-code-analysis-tools-36697)

- OWASP Cheat Sheet - Dynamic Code Analysis: Use dynamic code analysis tools to detect runtime vulnerabilities: SANS Whitepaper - [Link](https://www.sans.org/reading-room/whitepapers/securecode/secure-software-development-code-analysis-tools-36697)

- OWASP Cheat Sheet - Manual Code Review: Conduct manual code reviews to complement automated analysis: SANS Whitepaper - [Link](https://www.sans.org/reading-room/whitepapers/securecode/secure-software-development-code-analysis-tools-36697)

- OWASP Cheat Sheet - Secure Coding Training: Provide secure coding training for developers: SANS Whitepaper - [Link](https://www.sans.org/reading-room/whitepapers/securecode/secure-software-development-code-analysis-tools-36697)

