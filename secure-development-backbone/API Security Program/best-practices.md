# Best Practices

Below is a table of contents for help navigating this page:

- [Best Practices](#best-practices)
	- [CSA CCM (Cloud Security Alliance - Cloud Controls Matrix)](#csa-ccm-cloud-security-alliance---cloud-controls-matrix)
		- [Security control framework for cloud computing.](#security-control-framework-for-cloud-computing)
		- [Secure Coding Requirements](#secure-coding-requirements)
		- [API Specific Requirements](#api-specific-requirements)
	- [ISO 22301 (Security and Resilience / Business Continuity)](#iso-22301-security-and-resilience--business-continuity)
		- [Provides guidelines for business continuity management systems.](#provides-guidelines-for-business-continuity-management-systems)
		- [Secure Coding Requirements](#secure-coding-requirements-1)
		- [API Specific Requirements](#api-specific-requirements-1)
	- [ISO/IEC 27001 (Information Security Management)](#isoiec-27001-information-security-management)
		- [Specifies requirements for establishing, implementing, maintaining, and continually improving an information security management system (ISMS).](#specifies-requirements-for-establishing-implementing-maintaining-and-continually-improving-an-information-security-management-system-isms)
		- [Secure Coding Requirements](#secure-coding-requirements-2)
		- [API Specific Requirements](#api-specific-requirements-2)
	- [ISO/IEC 27002 (Guidelines for Internet Security)](#isoiec-27002-guidelines-for-internet-security)
		- [Provides guidelines for organizational information security standards and information security management practices.](#provides-guidelines-for-organizational-information-security-standards-and-information-security-management-practices)
		- [Secure Coding Requirements](#secure-coding-requirements-3)
		- [API Specific Requirements](#api-specific-requirements-3)
	- [ISO/IEC 27017 (Security Techniques for Cloud Services)](#isoiec-27017-security-techniques-for-cloud-services)
		- [Provides guidelines for information security controls applicable to the provision and use of cloud services.](#provides-guidelines-for-information-security-controls-applicable-to-the-provision-and-use-of-cloud-services)
		- [Secure Coding Requirements](#secure-coding-requirements-4)
		- [API Specific Requirements](#api-specific-requirements-4)
	- [ISO/IEC 27018 (Security Techniques for PII in Public Cloud)](#isoiec-27018-security-techniques-for-pii-in-public-cloud)
		- [Establishes controls for protecting personal data in the cloud.](#establishes-controls-for-protecting-personal-data-in-the-cloud)
		- [Secure Coding Requirements](#secure-coding-requirements-5)
		- [API Specific Requirements](#api-specific-requirements-5)
	- [ISO/IEC 27035 (Information Security Incident Management)](#isoiec-27035-information-security-incident-management)
		- [Provides guidelines for information security incident management.](#provides-guidelines-for-information-security-incident-management)
		- [Secure Coding Requirements](#secure-coding-requirements-6)
		- [API Specific Requirements](#api-specific-requirements-6)
	- [ISO/IEC 27701 (Security Techniques for Privacy Information Management)](#isoiec-27701-security-techniques-for-privacy-information-management)
		- [Provides guidelines for implementing a privacy information management system (PIMS) as an extension to ISO/IEC 27001 and ISO/IEC 27002.](#provides-guidelines-for-implementing-a-privacy-information-management-system-pims-as-an-extension-to-isoiec-27001-and-isoiec-27002)
		- [Secure Coding Requirements](#secure-coding-requirements-7)
		- [API Specific Requirements](#api-specific-requirements-7)
	- [ISO/IEC 29100 (Information Technology Privacy Framework)](#isoiec-29100-information-technology-privacy-framework)
		- [Provides a high-level framework for the protection of personally identifiable information (PII) within information and communication technology systems.](#provides-a-high-level-framework-for-the-protection-of-personally-identifiable-information-pii-within-information-and-communication-technology-systems)
		- [Secure Coding Requirements](#secure-coding-requirements-8)
		- [API Specific Requirements](#api-specific-requirements-8)
	- [MITRE ATT\&CK Framework](#mitre-attck-framework)
		- [Knowledge base of adversary tactics and techniques.](#knowledge-base-of-adversary-tactics-and-techniques)
		- [Secure Coding Requirements](#secure-coding-requirements-9)
		- [API Specific Requirements](#api-specific-requirements-9)
	- [NIST CSF (Cybersecurity Framework)](#nist-csf-cybersecurity-framework)
		- [Provides a policy framework for cybersecurity management.](#provides-a-policy-framework-for-cybersecurity-management)
		- [Secure Coding Requirements](#secure-coding-requirements-10)
		- [API Specific Requirements](#api-specific-requirements-10)
	- [NIST Digital Identity Guidelines (SP 800-63\*)](#nist-digital-identity-guidelines-sp-800-63)
		- [Provides technical requirements for federal agencies implementing digital identity services.](#provides-technical-requirements-for-federal-agencies-implementing-digital-identity-services)
		- [Secure Coding Requirements](#secure-coding-requirements-11)
		- [API Specific Requirements](#api-specific-requirements-11)
	- [NIST SP 800-34 (Contingency Planning Guide for Federal Information Systems)](#nist-sp-800-34-contingency-planning-guide-for-federal-information-systems)
		- [Provides guidance on contingency planning for federal information systems.](#provides-guidance-on-contingency-planning-for-federal-information-systems)
		- [Secure Coding Requirements](#secure-coding-requirements-12)
		- [API Specific Requirements](#api-specific-requirements-12)
	- [NIST SP 800-40 (Enterprise Patch Management)](#nist-sp-800-40-enterprise-patch-management)
		- [Offers guidance on managing patching and vulnerability remediation.](#offers-guidance-on-managing-patching-and-vulnerability-remediation)
		- [Secure Coding Requirements](#secure-coding-requirements-13)
		- [API Specific Requirements](#api-specific-requirements-13)
	- [NIST SP 800-41 (Guidelines on Firewalls and Firewall Policy)](#nist-sp-800-41-guidelines-on-firewalls-and-firewall-policy)
		- [Provides guidelines on configuring and managing firewalls.](#provides-guidelines-on-configuring-and-managing-firewalls)
		- [Secure Coding Requirements](#secure-coding-requirements-14)
		- [API Specific Requirements](#api-specific-requirements-14)
	- [NIST SP 800-53 (Security and Privacy Controls)](#nist-sp-800-53-security-and-privacy-controls)
		- [Provides a catalog of security and privacy controls for federal information systems and organizations.](#provides-a-catalog-of-security-and-privacy-controls-for-federal-information-systems-and-organizations)
		- [Secure Coding Requirements](#secure-coding-requirements-15)
		- [API Specific Requirements](#api-specific-requirements-15)
	- [NIST SP 800-61 (Computer Security Incident Handling Guide)](#nist-sp-800-61-computer-security-incident-handling-guide)
		- [Offers guidelines for incident response.](#offers-guidelines-for-incident-response)
		- [Secure Coding Requirements](#secure-coding-requirements-16)
		- [API Specific Requirements](#api-specific-requirements-16)
	- [NIST SP 800-92 (Guide to Computer Security Log Management)](#nist-sp-800-92-guide-to-computer-security-log-management)
		- [Provides guidance on log management.](#provides-guidance-on-log-management)
		- [Secure Coding Requirements](#secure-coding-requirements-17)
		- [API Specific Requirements](#api-specific-requirements-17)
	- [NIST SP 800-94 (Guide to Intrusion Detection and Prevention Systems (IDPS))](#nist-sp-800-94-guide-to-intrusion-detection-and-prevention-systems-idps)
		- [Provides guidelines on implementing and managing IDPS.](#provides-guidelines-on-implementing-and-managing-idps)
		- [Secure Coding Requirements](#secure-coding-requirements-18)
		- [API Specific Requirements](#api-specific-requirements-18)
	- [NIST SP 800-128 (Guide for Security-Focused Configuration Management of Information Systems)](#nist-sp-800-128-guide-for-security-focused-configuration-management-of-information-systems)
		- [Offers guidance on security-focused configuration management.](#offers-guidance-on-security-focused-configuration-management)
		- [Secure Coding Requirements](#secure-coding-requirements-19)
		- [API Specific Requirements](#api-specific-requirements-19)
	- [NIST SP 800-137 (ISCM for Federal Information Systems and Organizations)](#nist-sp-800-137-iscm-for-federal-information-systems-and-organizations)
		- [Offers guidance on continuous monitoring.](#offers-guidance-on-continuous-monitoring)
		- [Secure Coding Requirements](#secure-coding-requirements-20)
		- [API Specific Requirements](#api-specific-requirements-20)
	- [NIST SP 800-150 (Guide to Cyber Threat Intelligence Sharing)](#nist-sp-800-150-guide-to-cyber-threat-intelligence-sharing)
		- [Provides guidance on sharing cyber threat intelligence.](#provides-guidance-on-sharing-cyber-threat-intelligence)
		- [Secure Coding Requirements](#secure-coding-requirements-21)
		- [API Specific Requirements](#api-specific-requirements-21)
	- [OWASP API Security Top 10](#owasp-api-security-top-10)
		- [Identifies top 10 security risks for APIs.](#identifies-top-10-security-risks-for-apis)
		- [Secure Coding Requirements](#secure-coding-requirements-22)
		- [API Specific Requirements](#api-specific-requirements-22)
	- [OWASP ASVS (Application Security Verification Standard)](#owasp-asvs-application-security-verification-standard)
		- [A framework for testing the security of web applications and web services.](#a-framework-for-testing-the-security-of-web-applications-and-web-services)
		- [Secure Coding Requirements](#secure-coding-requirements-23)
		- [API Specific Requirements](#api-specific-requirements-23)
	- [OWASP Cheat Sheet Series](#owasp-cheat-sheet-series)
		- [Set of concise information on various application security topics.](#set-of-concise-information-on-various-application-security-topics)
		- [Authentication Cheat Sheet](#authentication-cheat-sheet)
		- [Access Control Cheat Sheet](#access-control-cheat-sheet)
		- [Input Validation Cheat Sheet](#input-validation-cheat-sheet)
		- [Cryptographic Storage Cheat Sheet](#cryptographic-storage-cheat-sheet)
		- [Error Handling Cheat Sheet](#error-handling-cheat-sheet)
		- [Logging Cheat Sheet](#logging-cheat-sheet)
		- [REST Security Cheat Sheet](#rest-security-cheat-sheet)
		- [SQL Injection Prevention Cheat Sheet](#sql-injection-prevention-cheat-sheet)
		- [Secure File Upload Cheat Sheet](#secure-file-upload-cheat-sheet)
		- [Transport Layer Protection Cheat Sheet](#transport-layer-protection-cheat-sheet)
		- [Cross-Site Scripting (XSS) Prevention Cheat Sheet](#cross-site-scripting-xss-prevention-cheat-sheet)
		- [Security Logging Cheat Sheet](#security-logging-cheat-sheet)
		- [CSRF Prevention Cheat Sheet](#csrf-prevention-cheat-sheet)
	- [OWASP Source Analysis Tools](#owasp-source-analysis-tools)
		- [List of tools for static and dynamic code analysis.](#list-of-tools-for-static-and-dynamic-code-analysis)
		- [Secure Coding Requirements](#secure-coding-requirements-24)
		- [API Specific Requirements](#api-specific-requirements-24)
	- [OWASP Top 10](#owasp-top-10)
		- [Identifies top 10 security risks for web applications.](#identifies-top-10-security-risks-for-web-applications)
		- [Secure Coding Requirements](#secure-coding-requirements-25)
		- [API Specific Requirements](#api-specific-requirements-25)
	- [RFC 5424 (The Syslog Protocol)](#rfc-5424-the-syslog-protocol)
		- [Protocol for system logging.](#protocol-for-system-logging)
		- [Secure Coding Requirements](#secure-coding-requirements-26)
		- [API Specific Requirements](#api-specific-requirements-26)
	- [RFC 6749 (OAuth 2.0 Authorization Framework)](#rfc-6749-oauth-20-authorization-framework)
		- [Framework for token-based authorization.](#framework-for-token-based-authorization)
		- [Secure Coding Requirements](#secure-coding-requirements-27)
		- [API Specific Requirements](#api-specific-requirements-27)
	- [RFC 6811 (BGP Prefix Origin Validation)](#rfc-6811-bgp-prefix-origin-validation)
		- [Mechanism to validate the origination of BGP announcements.](#mechanism-to-validate-the-origination-of-bgp-announcements)
		- [Secure Coding Requirements](#secure-coding-requirements-28)
		- [API Specific Requirements](#api-specific-requirements-28)
	- [RFC 7009 (OAuth 2.0 Token Revocation)](#rfc-7009-oauth-20-token-revocation)
		- [Defines a mechanism for clients to revoke access and refresh tokens.](#defines-a-mechanism-for-clients-to-revoke-access-and-refresh-tokens)
		- [Secure Coding Requirements](#secure-coding-requirements-29)
		- [API Specific Requirements](#api-specific-requirements-29)
	- [OAuth 2.0 Security Best Current Practice](#oauth-20-security-best-current-practice)
		- [Provides security recommendations and best practices for OAuth 2.0 implementations.](#provides-security-recommendations-and-best-practices-for-oauth-20-implementations)
		- [Secure Coding Requirements](#secure-coding-requirements-30)
		- [API Specific Requirements](#api-specific-requirements-30)
	- [RFC 7525 (Recommendations for TLS and DTLS)](#rfc-7525-recommendations-for-tls-and-dtls)
		- [Best practices for using TLS and DTLS securely.](#best-practices-for-using-tls-and-dtls-securely)
		- [Secure Coding Requirements](#secure-coding-requirements-31)
		- [API Specific Requirements](#api-specific-requirements-31)
	- [RFC 7636 (Proof Key for Code Exchange by OAuth Public Clients)](#rfc-7636-proof-key-for-code-exchange-by-oauth-public-clients)
		- [Extends OAuth 2.0 to provide better security for public clients using the authorization code grant.](#extends-oauth-20-to-provide-better-security-for-public-clients-using-the-authorization-code-grant)
		- [Secure Coding Requirements](#secure-coding-requirements-32)
		- [API Specific Requirements](#api-specific-requirements-32)
	- [RFC 8725 (JWT Best Current Practices)](#rfc-8725-jwt-best-current-practices)
		- [Best practices for securely using JSON Web Tokens (JWT).](#best-practices-for-securely-using-json-web-tokens-jwt)
		- [Secure Coding Requirements](#secure-coding-requirements-33)
		- [API Specific Requirements](#api-specific-requirements-33)
	- [RFC 9110 (HTTP Semantics)](#rfc-9110-http-semantics)
		- [Defines the semantics of HTTP.](#defines-the-semantics-of-http)
		- [Secure Coding Requirements](#secure-coding-requirements-34)
		- [API Specific Requirements](#api-specific-requirements-34)
	- [SANS CWE Top 25 Software Errors](#sans-cwe-top-25-software-errors)
		- [Lists the top 25 most dangerous software weaknesses.](#lists-the-top-25-most-dangerous-software-weaknesses)
		- [Secure Coding Requirements](#secure-coding-requirements-35)
		- [API Specific Requirements](#api-specific-requirements-35)
	- [SANS Secure Software Development and Code Analysis Tools - Whitepaper](#sans-secure-software-development-and-code-analysis-tools---whitepaper)
		- [Guidelines and tools for secure software development and code analysis.](#guidelines-and-tools-for-secure-software-development-and-code-analysis)
		- [Secure Coding Requirements](#secure-coding-requirements-36)
		- [API Specific Requirements](#api-specific-requirements-36)

---

## CSA CCM (Cloud Security Alliance - Cloud Controls Matrix)

> **https://cloudsecurityalliance.org/research/cloud-controls-matrix/**

### Security control framework for cloud computing.

### Secure Coding Requirements

- **Application & Interface Security:** Ensure secure software development, deployment, and maintenance practices (AIS-01).

- **Data Security & Information Lifecycle Management:** Protect data in transit and at rest using encryption and data masking (DSI-02).

- **Identity & Access Management:** Implement role-based access controls and multi-factor authentication (IAM-03).

- **Audit Assurance & Compliance:** Maintain detailed audit logs to ensure accountability and traceability (AAC-02).

- **Incident Management:** Establish and maintain an incident response plan (SEF-02).

- **Risk Management:** Conduct regular risk assessments to identify and mitigate security risks (RSK-01).

### API Specific Requirements

- **Secure API Development:** Ensure APIs are developed using secure coding practices to prevent common vulnerabilities (AIS-01).

- **API Access Controls:** Implement proper authentication and authorization mechanisms for API access (IAM-03).

- **API Encryption:** Encrypt API communication to protect data in transit (DSI-02).

- **API Logging:** Maintain detailed logs of API access and activities for audit and compliance purposes (AAC-02).

## ISO 22301 (Security and Resilience / Business Continuity)

> **https://www.iso.org/iso-22301-business-continuity.html**

### Provides guidelines for business continuity management systems.

### Secure Coding Requirements

- **Business Continuity Plans:** Develop and maintain business continuity plans for critical systems (ISO 22301:2019 Clause 8.4).

- **Risk Assessment:** Conduct regular risk assessments to identify potential disruptions (ISO 22301:2019 Clause 8.2).

- **Incident Response:** Establish incident response procedures to ensure rapid recovery from disruptions (ISO 22301:2019 Clause 8.4.3).

- **Training and Awareness:** Provide regular training to ensure staff are aware of business continuity procedures (ISO 22301:2019 Clause 7.2).

### API Specific Requirements

- **Nothing API specific**

## ISO/IEC 27001 (Information Security Management)

> **https://www.iso.org/isoiec-27001-information-security.html**

### Specifies requirements for establishing, implementing, maintaining, and continually improving an information security management system (ISMS).

### Secure Coding Requirements

- **Access Control:** Implement access control policies to ensure only authorized access to information systems (ISO/IEC 27001:2013 A.9.1.1).

- **Cryptographic Controls:** Use cryptographic controls to protect the confidentiality, integrity, and availability of information (ISO/IEC 27001:2013 A.10.1.1).

- **Logging and Monitoring:** Implement logging and monitoring controls to detect and respond to security incidents (ISO/IEC 27001:2013 A.12.4.1).

- **Secure Development:** Ensure secure development practices are followed throughout the software development lifecycle (ISO/IEC 27001:2013 A.14.2.1).

- **Supplier Relationships:** Ensure that suppliers adhere to security requirements (ISO/IEC 27001:2013 A.15.1.1).

- **Information Security Incident Management:** Establish an incident management process to respond to and manage security incidents (ISO/IEC 27001:2013 A.16.1.1).

### API Specific Requirements

- **Nothing API specific**

## ISO/IEC 27002 (Guidelines for Internet Security)

> **https://www.iso.org/standard/54533.html**

### Provides guidelines for organizational information security standards and information security management practices.

### Secure Coding Requirements

- **Access Control:** Implement and manage access controls to protect information systems (ISO/IEC 27002:2013 A.9.1.1).

- **Cryptographic Controls:** Apply cryptographic controls to safeguard the confidentiality and integrity of information (ISO/IEC 27002:2013 A.10.1.1).

- **Logging and Monitoring:** Maintain and review logs of activities and events for security monitoring (ISO/IEC 27002:2013 A.12.4.1).

- **Secure Development:** Follow secure development practices for software development and maintenance (ISO/IEC 27002:2013 A.14.2.1).

- **Third-Party Service Management:** Ensure that third-party services comply with security requirements (ISO/IEC 27002:2013 A.15.1.1).

- **Incident Management:** Implement an incident management process to handle security breaches (ISO/IEC 27002:2013 A.16.1.1).

### API Specific Requirements

- **Nothing API specific**

## ISO/IEC 27017 (Security Techniques for Cloud Services)

> **https://www.iso.org/standard/43757.html**

### Provides guidelines for information security controls applicable to the provision and use of cloud services.

### Secure Coding Requirements

- **Access Control:** Implement access control measures specific to cloud environments (ISO/IEC 27017:2015 9.1.1).

- **Cloud Customer Responsibilities:** Define and communicate cloud customer responsibilities for security (ISO/IEC 27017:2015 5.1.1).

- **Cloud Provider Responsibilities:** Ensure cloud providers implement necessary security measures (ISO/IEC 27017:2015 6.1.1).

- **Encryption:** Use encryption to protect data stored in the cloud (ISO/IEC 27017:2015 10.1.1).

- **Monitoring:** Monitor cloud environments for security events and incidents (ISO/IEC 27017:2015 12.4.1).

- **Incident Management:** Implement procedures for responding to cloud-specific security incidents (ISO/IEC 27017:2015 16.1.1).

### API Specific Requirements

- **API Security:** Ensure APIs provided by cloud services are secure, with proper authentication and authorization (ISO/IEC 27017:2015 14.1.1).

- **Data Encryption in APIs:** Use encryption for data transmitted through APIs (ISO/IEC 27017:2015 10.1.1).

- **API Access Controls:** Implement role-based access controls for APIs in cloud services (ISO/IEC 27017:2015 9.1.1).

## ISO/IEC 27018 (Security Techniques for PII in Public Cloud)

> **https://www.iso.org/standard/61498.html**

### Establishes controls for protecting personal data in the cloud.

### Secure Coding Requirements

- **Personal Data Protection:** Implement measures to protect personal data in the cloud (ISO/IEC 27018:2019 8.1).

- **Access Control:** Restrict access to personal data to authorized individuals (ISO/IEC 27018:2019 8.2).

- **Encryption:** Encrypt personal data both at rest and in transit (ISO/IEC 27018:2019 8.3).

- **Data Masking:** Use data masking techniques to protect personal data (ISO/IEC 27018:2019 8.4).

- **Audit Trails:** Maintain audit trails to monitor access to personal data (ISO/IEC 27018:2019 8.5).

- **Incident Response:** Develop and test incident response plans for personal data breaches (ISO/IEC 27018:2019 8.6).

### API Specific Requirements

- **API Access Controls:** Ensure APIs that handle personal data have robust access controls (ISO/IEC 27018:2019 8.2).

- **API Encryption:** Encrypt personal data transmitted through APIs (ISO/IEC 27018:2019 8.3).

- **API Logging:** Implement logging for API access and activities involving personal data (ISO/IEC 27018:2019 8.5).

## ISO/IEC 27035 (Information Security Incident Management)

> **https://www.iso.org/standard/44379.html**

### Provides guidelines for information security incident management.

### Secure Coding Requirements

- **Incident Detection:** Implement mechanisms for detecting information security incidents (ISO/IEC 27035-1:2016 Clause 7).

- **Incident Reporting:** Establish procedures for reporting information security incidents (ISO/IEC 27035-1:2016 Clause 8).

- **Incident Response:** Develop and maintain an incident response plan to handle information security incidents (ISO/IEC 27035-1:2016 Clause 9).

- **Root Cause Analysis:** Conduct root cause analysis to prevent recurrence of incidents (ISO/IEC 27035-1:2016 Clause 10).

- **Post-Incident Review:** Perform post-incident reviews to improve the incident management process (ISO/IEC 27035-1:2016 Clause 11).

### API Specific Requirements

- **Nothing API specific**

## ISO/IEC 27701 (Security Techniques for Privacy Information Management)

> **https://www.iso.org/standard/71670.html**

### Provides guidelines for implementing a privacy information management system (PIMS) as an extension to ISO/IEC 27001 and ISO/IEC 27002.

### Secure Coding Requirements

- **Privacy Impact Assessments:** Conduct privacy impact assessments to identify and mitigate risks to personal data (ISO/IEC 27701:2019 6.3).

- **Access Controls:** Implement access controls to protect personal data (ISO/IEC 27701:2019 6.4).

- **Data Minimization:** Ensure only necessary personal data is collected and processed (ISO/IEC 27701:2019 6.5).

- **Data Subject Rights:** Implement mechanisms to support data subject rights, such as access, correction, and deletion (ISO/IEC 27701:2019 6.6).

- **Encryption:** Encrypt personal data to protect its confidentiality (ISO/IEC 27701:2019 6.7).

- **Incident Response:** Develop and implement an incident response plan for personal data breaches (ISO/IEC 27701:2019 6.8).

### API Specific Requirements

- **API Access Controls:** Ensure APIs that handle personal data have robust access controls (ISO/IEC 27701:2019 6.4).

- **API Encryption:** Encrypt personal data transmitted through APIs (ISO/IEC 27701:2019 6.7).

- **API Data Subject Rights:** Implement APIs to support data subject rights requests (ISO/IEC 27701:2019 6.6).

## ISO/IEC 29100 (Information Technology Privacy Framework)

> **https://www.iso.org/standard/45123.html**

### Provides a high-level framework for the protection of personally identifiable information (PII) within information and communication technology systems.

### Secure Coding Requirements

- **Privacy Policies:** Establish and communicate privacy policies to protect PII (ISO/IEC 29100:2011 Clause 4.1).

- **Consent Management:** Implement mechanisms for obtaining and managing consent from data subjects (ISO/IEC 29100:2011 Clause 4.2).

- **Access Controls:** Implement access controls to restrict access to PII (ISO/IEC 29100:2011 Clause 4.3).

- **Data Minimization:** Ensure PII collection and processing is limited to what is necessary (ISO/IEC 29100:2011 Clause 4.4).

- **Data Quality:** Maintain data quality by ensuring PII is accurate, complete, and up-to-date (ISO/IEC 29100:2011 Clause 4.5).

- **Security Measures:** Implement security measures to protect PII (ISO/IEC 29100:2011 Clause 4.6).

### API Specific Requirements

- **API Access Controls:** Ensure APIs that handle PII have robust access controls (ISO/IEC 29100:2011 Clause 4.3).

- **API Data Minimization:** Implement APIs to ensure data minimization principles are followed (ISO/IEC 29100:2011 Clause 4.4).

- **API Data Quality:** Ensure APIs maintain the quality of PII by verifying its accuracy and completeness (ISO/IEC 29100:2011 Clause 4.5).

## MITRE ATT&CK Framework

> **https://attack.mitre.org/**

### Knowledge base of adversary tactics and techniques.

### Secure Coding Requirements

- **Threat Modeling:** Use the framework to perform threat modeling and identify potential attack vectors (MITRE ATT&CK Framework: Threat Modeling).

- **Security Testing:** Leverage the framework for security testing and validation of defensive measures (MITRE ATT&CK Framework: Security Testing).

- **Incident Response:** Utilize the framework to enhance incident response procedures and identify attacker behavior (MITRE ATT&CK Framework: Incident Response).

- **Red Teaming:** Use the framework for red teaming exercises to simulate adversary tactics (MITRE ATT&CK Framework: Red Teaming).

### API Specific Requirements

- **Nothing API specific**

## NIST CSF (Cybersecurity Framework)

> **https://www.nist.gov/cyberframework**

### Provides a policy framework for cybersecurity management.

### Secure Coding Requirements

- **Identify:** Develop an organizational understanding to manage cybersecurity risk to systems, assets, data, and capabilities (NIST CSF ID Function).

- **Protect:** Develop and implement appropriate safeguards to ensure delivery of critical infrastructure services (NIST CSF PR Function).

- **Detect:** Develop and implement appropriate activities to identify the occurrence of a cybersecurity event (NIST CSF DE Function).

- **Respond:** Develop and implement appropriate activities to take action regarding a detected cybersecurity incident (NIST CSF RS Function).

- **Recover:** Develop and implement appropriate activities to maintain plans for resilience and to restore any capabilities or services that were impaired due to a cybersecurity incident (NIST CSF RC Function).

### API Specific Requirements

- **Nothing API specific**

## NIST Digital Identity Guidelines (SP 800-63*)

> **https://pages.nist.gov/800-63-3/**

### Provides technical requirements for federal agencies implementing digital identity services.

### Secure Coding Requirements

- **Identity Proofing:** Implement identity proofing processes to validate the identity of users (NIST SP 800-63A Section 4.2).

- **Authentication Assurance Levels:** Use appropriate authentication mechanisms to achieve required assurance levels (NIST SP 800-63B Section 4.1).

- **Federation:** Support federation protocols to allow for secure identity sharing across domains (NIST SP 800-63C Section 4.1).

- **Session Management:** Implement secure session management practices to protect active sessions (NIST SP 800-63B Section 7).

- **Credential Management:** Ensure secure issuance, use, and lifecycle management of credentials (NIST SP 800-63B Section 6).

### API Specific Requirements

- **Identity Proofing APIs:** Implement APIs to facilitate identity proofing processes (NIST SP 800-63A Section 4.2).

- **Authentication APIs:** Provide APIs to support secure authentication mechanisms (NIST SP 800-63B Section 4.1).

- **Federation APIs:** Develop APIs to enable secure federation and identity sharing (NIST SP 800-63C Section 4.1).

- **Session Management APIs:** Implement APIs for secure session management (NIST SP 800-63B Section 7).

## NIST SP 800-34 (Contingency Planning Guide for Federal Information Systems)

> **https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final**

### Provides guidance on contingency planning for federal information systems.

### Secure Coding Requirements

- **Contingency Planning:** Develop and implement contingency plans for information systems (NIST SP 800-34 Section 3.1).

- **Risk Assessment:** Conduct risk assessments to identify potential impacts of system disruptions (NIST SP 800-34 Section 3.2).

- **Backup and Recovery:** Implement backup and recovery procedures to ensure data integrity and availability (NIST SP 800-34 Section 4.2).

- **Plan Testing:** Regularly test contingency plans to ensure effectiveness (NIST SP 800-34 Section 3.3).

- **Training and Awareness:** Provide training on contingency planning and procedures (NIST SP 800-34 Section 3.4).

### API Specific Requirements

- **Nothing API specific**

## NIST SP 800-40 (Enterprise Patch Management)

> **https://csrc.nist.gov/publications/detail/sp/800-40/rev-3/final**

### Offers guidance on managing patching and vulnerability remediation.

### Secure Coding Requirements

- **Patch Management Policy:** Develop and implement a patch management policy (NIST SP 800-40 Section 2.1).

- **Vulnerability Management:** Identify, prioritize, and mitigate vulnerabilities in software (NIST SP 800-40 Section 3.1).

- **Testing Patches:** Test patches in a controlled environment before deployment (NIST SP 800-40 Section 3.2).

- **Patch Deployment:** Deploy patches to production systems in a timely manner (NIST SP 800-40 Section 3.3).

- **Monitoring:** Monitor systems for compliance with patch management policies (NIST SP 800-40 Section 4.1).

### API Specific Requirements

- **Nothing API specific**

## NIST SP 800-41 (Guidelines on Firewalls and Firewall Policy)

> **https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final**

### Provides guidelines on configuring and managing firewalls.

### Secure Coding Requirements

- **Firewall Policies:** Develop and implement firewall policies to control network traffic (NIST SP 800-41 Section 3.1).

- **Access Controls:** Implement access controls to restrict unauthorized access through firewalls (NIST SP 800-41 Section 4.2).

- **Monitoring and Logging:** Enable logging and monitoring of firewall activities (NIST SP 800-41 Section 5.3).

- **Rule Management:** Regularly review and update firewall rules to ensure compliance with security policies (NIST SP 800-41 Section 4.3).

- **Incident Response:** Establish procedures for responding to firewall-related security incidents (NIST SP 800-41 Section 5.4).

### API Specific Requirements

- **Nothing API specific**

## NIST SP 800-53 (Security and Privacy Controls)

> **https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final**

### Provides a catalog of security and privacy controls for federal information systems and organizations.

### Secure Coding Requirements

- **Access Control:** Implement access control policies to restrict access to information systems (NIST SP 800-53 AC-1).

- **Audit and Accountability:** Maintain audit logs to monitor and record system activity (NIST SP 800-53 AU-1).

- **Configuration Management:** Apply secure configuration management practices (NIST SP 800-53 CM-1).

- **Identification and Authentication:** Ensure proper identification and authentication mechanisms (NIST SP 800-53 IA-1).

- **Incident Response:** Develop and maintain incident response procedures (NIST SP 800-53 IR-1).

- **System and Communications Protection:** Implement measures to protect the confidentiality and integrity of information transmitted and received (NIST SP 800-53 SC-1).

### API Specific Requirements

- **API Access Controls:** Ensure APIs have robust access control mechanisms (NIST SP 800-53 AC-1).

- **API Logging:** Implement logging for API access and activities (NIST SP 800-53 AU-1).

- **API Encryption:** Encrypt data transmitted through APIs to protect its confidentiality and integrity (NIST SP 800-53 SC-1).

## NIST SP 800-61 (Computer Security Incident Handling Guide)

> **https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final**

### Offers guidelines for incident response.

### Secure Coding Requirements

- **Incident Response Policy:** Develop and implement an incident response policy (NIST SP 800-61 Section 2.2).

- **Incident Response Plan:** Create an incident response plan outlining procedures for detecting, reporting, and managing incidents (NIST SP 800-61 Section 3.1).

- **Training:** Provide regular training on incident response procedures (NIST SP 800-61 Section 3.2).

- **Detection and Analysis:** Implement mechanisms for detecting and analyzing security incidents (NIST SP 800-61 Section 3.3).

- **Containment, Eradication, and Recovery:** Establish procedures for containing, eradicating, and recovering from incidents (NIST SP 800-61 Section 3.4).

- **Post-Incident Activity:** Conduct post-incident reviews to improve the incident response process (NIST SP 800-61 Section 3.5).

### API Specific Requirements

- **Nothing API specific**

## NIST SP 800-92 (Guide to Computer Security Log Management)

> **https://csrc.nist.gov/publications/detail/sp/800-92/final**

### Provides guidance on log management.

### Secure Coding Requirements

- **Log Management Policy:** Develop and implement a log management policy (NIST SP 800-92 Section 2).

- **Log Generation:** Ensure that logs are generated for critical system events (NIST SP 800-92 Section 3).

- **Log Storage:** Implement secure storage for logs to prevent tampering (NIST SP 800-92 Section 4).

- **Log Analysis:** Regularly analyze logs to detect and respond to security incidents (NIST SP 800-92 Section 5).

- **Log Retention:** Maintain logs for an appropriate period to meet regulatory and operational requirements (NIST SP 800-92 Section 6).

### API Specific Requirements

- **API Logging:** Ensure APIs generate logs for critical activities and events (NIST SP 800-92 Section 3).

- **API Log Storage:** Implement secure storage for API logs (NIST SP 800-92 Section 4).

- **API Log Analysis:** Regularly analyze API logs to detect and respond to security incidents (NIST SP 800-92 Section 5).

## NIST SP 800-94 (Guide to Intrusion Detection and Prevention Systems (IDPS))

> **https://csrc.nist.gov/publications/detail/sp/800-94/final**

### Provides guidelines on implementing and managing IDPS.

### Secure Coding Requirements

- **IDPS Policy:** Develop and implement an IDPS policy (NIST SP 800-94 Section 2.2).

- **IDPS Implementation:** Deploy and configure IDPS to monitor network and system activities (NIST SP 800-94 Section 3.1).

- **Alert Management:** Establish procedures for managing and responding to IDPS alerts (NIST SP 800-94 Section 4.2).

- **Incident Response Integration:** Integrate IDPS with incident response processes (NIST SP 800-94 Section 5.1).

- **Monitoring:** Continuously monitor IDPS for signs of intrusion or anomalous behavior (NIST SP 800-94 Section 6.1).

### API Specific Requirements

- **Nothing API specific**

## NIST SP 800-128 (Guide for Security-Focused Configuration Management of Information Systems)

> **https://csrc.nist.gov/publications/detail/sp/800-128/final**

### Offers guidance on security-focused configuration management.

### Secure Coding Requirements

- **Configuration Management Policy:** Develop and implement a configuration management policy (NIST SP 800-128 Section 2.1).

- **Baseline Configurations:** Establish and maintain baseline configurations for information systems (NIST SP 800-128 Section 3.2).

- **Configuration Change Control:** Implement processes for managing configuration changes (NIST SP 800-128 Section 3.3).

- **Configuration Monitoring:** Continuously monitor configurations for compliance with security policies (NIST SP 800-128 Section 3.4).

- **Configuration Auditing:** Conduct regular audits to ensure configurations meet security requirements (NIST SP 800-128 Section 3.5).

### API Specific Requirements

- **Nothing API specific**

## NIST SP 800-137 (ISCM for Federal Information Systems and Organizations)

> **https://csrc.nist.gov/publications/detail/sp/800-137/final**

### Offers guidance on continuous monitoring.

### Secure Coding Requirements

- **Continuous Monitoring Strategy:** Develop a continuous monitoring strategy to ensure ongoing security (NIST SP 800-137 Section 2.2).

- **Monitoring Processes:** Implement processes for continuous monitoring of information systems (NIST SP 800-137 Section 3.1).

- **Security Controls:** Regularly assess the effectiveness of security controls (NIST SP 800-137 Section 4.2).

- **Risk Management:** Continuously manage risks to information systems (NIST SP 800-137 Section 5.1).

- **Reporting:** Report on the security status of information systems (NIST SP 800-137 Section 6.1).

### API Specific Requirements

- **Nothing API specific**

## NIST SP 800-150 (Guide to Cyber Threat Intelligence Sharing)

> **https://csrc.nist.gov/publications/detail/sp/800-150/final**

### Provides guidance on sharing cyber threat intelligence.

### Secure Coding Requirements

- **Intelligence Sharing Policy:** Develop and implement a policy for sharing cyber threat intelligence (NIST SP 800-150 Section 3.1).

- **Data Protection:** Ensure that shared intelligence is protected from unauthorized access (NIST SP 800-150 Section 3.2).

- **Collaboration:** Promote collaboration with external partners to enhance threat intelligence sharing (NIST SP 800-150 Section 4.1).

- **Incident Response Integration:** Integrate threat intelligence sharing with incident response processes (NIST SP 800-150 Section 4.2).

- **Data Quality:** Ensure the quality and relevance of shared intelligence (NIST SP 800-150 Section 5.1).

### API Specific Requirements

- **Nothing API specific**

## OWASP API Security Top 10

> **https://owasp.org/www-project-api-security/**

### Identifies top 10 security risks for APIs.

### Secure Coding Requirements

- **API Authentication:** Implement strong authentication mechanisms for APIs (OWASP API Security Top 10: API1:2019).

- **API Authorization:** Ensure proper authorization checks to prevent access to unauthorized data (OWASP API Security Top 10: API2:2019).

- **Data Exposure:** Avoid excessive data exposure by limiting the data returned by APIs (OWASP API Security Top 10: API3:2019).

- **Rate Limiting:** Implement rate limiting to protect APIs from abuse and Denial of Service (DoS) attacks (OWASP API Security Top 10: API4:2019).

- **Input Validation:** Validate all inputs to APIs to prevent injection attacks (OWASP API Security Top 10: API5:2019).

- **Security Misconfiguration:** Ensure APIs are configured securely to prevent common vulnerabilities (OWASP API Security Top 10: API6:2019).

- **Encryption:** Encrypt sensitive data transmitted through APIs (OWASP API Security Top 10: API7:2019).

- **Error Handling:** Implement proper error handling to avoid exposing sensitive information (OWASP API Security Top 10: API8:2019).

- **API Gateway:** Use an API gateway to enforce security policies (OWASP API Security Top 10: API9:2019).

- **Logging and Monitoring:** Log and monitor API activities to detect and respond to security incidents (OWASP API Security Top 10: API10:2019).

### API Specific Requirements

- **API Authentication:** Implement strong authentication mechanisms for APIs (OWASP API Security Top 10: API1:2019).

- **API Authorization:** Ensure proper authorization checks to prevent access to unauthorized data (OWASP API Security Top 10: API2:2019).

- **Data Exposure:** Avoid excessive data exposure by limiting the data returned by APIs (OWASP API Security Top 10: API3:2019).

- **Rate Limiting:** Implement rate limiting to protect APIs from abuse and Denial of Service (DoS) attacks (OWASP API Security Top 10: API4:2019).

- **Input Validation:** Validate all inputs to APIs to prevent injection attacks (OWASP API Security Top 10: API5:2019).

- **Security Misconfiguration:** Ensure APIs are configured securely to prevent common vulnerabilities (OWASP API Security Top 10: API6:2019).

- **Encryption:** Encrypt sensitive data transmitted through APIs (OWASP API Security Top 10: API7:2019).

- **Error Handling:** Implement proper error handling to avoid exposing sensitive information (OWASP API Security Top 10: API8:2019).

- **API Gateway:** Use an API gateway to enforce security policies (OWASP API Security Top 10: API9:2019).

- **Logging and Monitoring:** Log and monitor API activities to detect and respond to security incidents (OWASP API Security Top 10: API10:2019).

## OWASP ASVS (Application Security Verification Standard)

> **https://owasp.org/www-project-application-security-verification-standard/**

### A framework for testing the security of web applications and web services.

### Secure Coding Requirements

- **Authentication Verification:** Ensure robust authentication mechanisms are in place (OWASP ASVS V1).

- **Session Management:** Implement secure session management practices (OWASP ASVS V2).

- **Access Control Verification:** Enforce proper access control measures (OWASP ASVS V4).

- **Input Validation:** Validate all inputs to prevent injection attacks (OWASP ASVS V5).

- **Cryptographic Controls:** Use strong cryptographic controls to protect data (OWASP ASVS V6).

- **Error Handling and Logging:** Implement proper error handling and logging mechanisms (OWASP ASVS V7).

- **Data Protection:** Ensure sensitive data is properly protected (OWASP ASVS V8).

- **API Security:** Apply security best practices for API development (OWASP ASVS V14).

### API Specific Requirements

- **API Authentication:** Ensure robust authentication mechanisms for APIs (OWASP ASVS V1).

- **API Session Management:** Implement secure session management for APIs (OWASP ASVS V2).

- **API Access Control:** Enforce proper access control measures for APIs (OWASP ASVS V4).

- **API Input Validation:** Validate all inputs to APIs to prevent injection attacks (OWASP ASVS V5).

- **API Cryptographic Controls:** Use strong cryptographic controls for API data (OWASP ASVS V6).

- **API Error Handling and Logging:** Implement proper error handling and logging for APIs (OWASP ASVS V7).

- **API Data Protection:** Ensure sensitive data transmitted through APIs is protected (OWASP ASVS V8).

## OWASP Cheat Sheet Series

> **https://cheatsheetseries.owasp.org/**

### Set of concise information on various application security topics.

### Authentication Cheat Sheet

- https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html

- Provides guidelines for implementing secure authentication mechanisms.

- Secure Coding Requirements

	- **Password Storage:** Use strong, one-way hashing algorithms with a salt for storing passwords (Authentication Cheat Sheet: Password Storage).

	- **Multi-Factor Authentication:** Implement multi-factor authentication to enhance security (Authentication Cheat Sheet: Multi-Factor Authentication).

	- **Session Management:** Securely manage user sessions, including session timeouts and regeneration of session IDs (Authentication Cheat Sheet: Session Management).

	- **Account Lockout:** Implement account lockout mechanisms to prevent brute force attacks (Authentication Cheat Sheet: Account Lockout).

	- **Password Complexity:** Enforce password complexity requirements to ensure strong passwords (Authentication Cheat Sheet: Password Complexity).

- API Specific Requirements

	- **API Authentication:** Use secure token-based authentication mechanisms, such as OAuth, for APIs (Authentication Cheat Sheet: API Authentication).

	- **API Session Management:** Securely manage API sessions, including session timeouts and token invalidation (Authentication Cheat Sheet: Session Management).

### Access Control Cheat Sheet

- https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html

- Provides guidelines for implementing secure access control mechanisms.

- Secure Coding Requirements

	- **Role-Based Access Control (RBAC):** Implement RBAC to restrict access to resources based on user roles (Access Control Cheat Sheet: Role-Based Access Control).

	- **Least Privilege:** Apply the principle of least privilege to limit user access rights (Access Control Cheat Sheet: Least Privilege).

	- **Access Control Lists (ACLs):** Use ACLs to define and enforce access policies (Access Control Cheat Sheet: Access Control Lists).

	- **Segregation of Duties:** Ensure that critical tasks require multiple users to prevent fraud and abuse (Access Control Cheat Sheet: Segregation of Duties).

	- **Access Control Enforcement:** Consistently enforce access control checks on both the server and client sides (Access Control Cheat Sheet: Access Control Enforcement).

- API Specific Requirements

	- **API Role-Based Access Control:** Implement RBAC for APIs to restrict access based on user roles (Access Control Cheat Sheet: Role-Based Access Control).

	- **API Access Control Enforcement:** Enforce access control checks in APIs to prevent unauthorized access (Access Control Cheat Sheet: Access Control Enforcement).

### Input Validation Cheat Sheet

- https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html

- Provides guidelines for validating inputs to prevent common vulnerabilities.

- Secure Coding Requirements

	- **Whitelist Input Validation:** Use whitelist validation to allow only known good inputs (Input Validation Cheat Sheet: Whitelist Input Validation).

	- **Input Sanitization:** Sanitize inputs to remove or neutralize potentially harmful data (Input Validation Cheat Sheet: Input Sanitization).

	- **Regular Expressions:** Use regular expressions carefully to validate input formats (Input Validation Cheat Sheet: Regular Expressions).

	- **Encoding:** Encode data before processing or displaying it to prevent injection attacks (Input Validation Cheat Sheet: Encoding).

	- **Input Length Checks:** Validate input lengths to prevent buffer overflow and other attacks (Input Validation Cheat Sheet: Input Length Checks).

- API Specific Requirements

	- **API Input Validation:** Validate all inputs to APIs to prevent injection attacks (Input Validation Cheat Sheet: Whitelist Input Validation).

	- **API Input Sanitization:** Sanitize API inputs to remove harmful data (Input Validation Cheat Sheet: Input Sanitization).

	- **API Input Length Checks:** Validate input lengths in APIs to prevent buffer overflow (Input Validation Cheat Sheet: Input Length Checks).

### Cryptographic Storage Cheat Sheet

- https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html

- Provides guidelines for securely storing sensitive data.

- Secure Coding Requirements

	- **Encryption Algorithms:** Use strong encryption algorithms, such as AES, for data encryption (Cryptographic Storage Cheat Sheet: Encryption Algorithms).

	- **Key Management:** Implement secure key management practices, including key rotation and storage (Cryptographic Storage Cheat Sheet: Key Management).

	- **Hashing:** Use strong hashing algorithms with salts for storing passwords and sensitive data (Cryptographic Storage Cheat Sheet: Hashing).

	- **Data at Rest:** Encrypt sensitive data at rest to protect it from unauthorized access (Cryptographic Storage Cheat Sheet: Data at Rest).

	- **Data in Transit:** Encrypt data in transit using protocols such as TLS (Cryptographic Storage Cheat Sheet: Data in Transit).

- API Specific Requirements

	- **API Data Encryption:** Ensure data transmitted through APIs is encrypted using strong algorithms (Cryptographic Storage Cheat Sheet: Data in Transit).

	- **API Key Management:** Implement secure key management practices for API encryption keys (Cryptographic Storage Cheat Sheet: Key Management).

	- **API Hashing:** Use strong hashing algorithms for sensitive data in APIs (Cryptographic Storage Cheat Sheet: Hashing).

### Error Handling Cheat Sheet

- https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html

- Provides guidelines for securely handling errors to avoid information leakage.

- Secure Coding Requirements

	- **Generic Error Messages:** Display generic error messages to users to avoid revealing sensitive information (Error Handling Cheat Sheet: Generic Error Messages).

	- **Detailed Logging:** Log detailed error information for debugging and auditing purposes (Error Handling Cheat Sheet: Detailed Logging).

	- **Exception Handling:** Use structured exception handling to manage errors gracefully (Error Handling Cheat Sheet: Exception Handling).

	- **Fail-Safe Defaults:** Ensure that the system fails safely in case of an error (Error Handling Cheat Sheet: Fail-Safe Defaults).

- API Specific Requirements

	- **API Error Messages:** Ensure API error responses do not reveal sensitive information (Error Handling Cheat Sheet: Generic Error Messages).

	- **API Error Logging:** Log detailed error information for API requests (Error Handling Cheat Sheet: Detailed Logging).

	- **API Exception Handling:** Use structured exception handling in APIs to manage errors gracefully (Error Handling Cheat Sheet: Exception Handling).

### Logging Cheat Sheet

- https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html

- Provides guidelines for securely logging system and application activities.

- Secure Coding Requirements

	- **Log Sensitive Data:** Avoid logging sensitive data such as passwords and credit card numbers (Logging Cheat Sheet: Log Sensitive Data).

	- **Log Retention:** Define and implement log retention policies to comply with legal and operational requirements (Logging Cheat Sheet: Log Retention).

	- **Log Integrity:** Protect logs from tampering by implementing integrity controls (Logging Cheat Sheet: Log Integrity).

	- **Log Access Controls:** Restrict access to logs to authorized personnel only (Logging Cheat Sheet: Log Access Controls).

	- **Log Analysis:** Regularly analyze logs to detect and respond to security incidents (Logging Cheat Sheet: Log Analysis).

- API Specific Requirements

	- **API Logging:** Ensure APIs log critical activities and events without exposing sensitive data (Logging Cheat Sheet: Log Sensitive Data).

	- **API Log Integrity:** Implement integrity controls for API logs to prevent tampering (Logging Cheat Sheet: Log Integrity).

	- **API Log Access Controls:** Restrict access to API logs to authorized personnel (Logging Cheat Sheet: Log Access Controls).

	- **API Log Analysis:** Regularly analyze API logs to detect and respond to security incidents (Logging Cheat Sheet: Log Analysis).

### REST Security Cheat Sheet

- https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html

- Provides guidelines for securing RESTful web services.

- Secure Coding Requirements

	- **HTTPS:** Use HTTPS to protect data in transit (REST Security Cheat Sheet: HTTPS).

	- **Authentication:** Implement token-based authentication mechanisms such as OAuth (REST Security Cheat Sheet: Authentication).

	- **Authorization:** Use role-based access control (RBAC) for authorization (REST Security Cheat Sheet: Authorization).

	- **Input Validation:** Validate all inputs to REST endpoints to prevent injection attacks (REST Security Cheat Sheet: Input Validation).

	- **Rate Limiting:** Implement rate limiting to prevent abuse of REST APIs (REST Security Cheat Sheet: Rate Limiting).

	- **Error Handling:** Ensure error responses do not expose sensitive information (REST Security Cheat Sheet: Error Handling).

- API Specific Requirements

	- **HTTPS:** Ensure REST APIs use HTTPS to protect data in transit (REST Security Cheat Sheet: HTTPS).

	- **API Authentication:** Implement secure token-based authentication for REST APIs (REST Security Cheat Sheet: Authentication).

	- **API Authorization:** Use RBAC to control access to REST APIs (REST Security Cheat Sheet: Authorization).

	- **API Input Validation:** Validate inputs to REST APIs to prevent injection attacks (REST Security Cheat Sheet: Input Validation).

	- **API Rate Limiting:** Implement rate limiting for REST APIs (REST Security Cheat Sheet: Rate Limiting).

	- **API Error Handling:** Ensure error responses from REST APIs do not expose sensitive information (REST Security Cheat Sheet: Error Handling).

### SQL Injection Prevention Cheat Sheet

- https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html

- Provides guidelines for preventing SQL injection attacks.

- Secure Coding Requirements

	- **Parameterized Queries:** Use parameterized queries to prevent SQL injection (SQL Injection Prevention Cheat Sheet: Parameterized Queries).

	- **Stored Procedures:** Use stored procedures to execute SQL statements (SQL Injection Prevention Cheat Sheet: Stored Procedures).

	- **ORMs:** Use Object-Relational Mapping (ORM) tools to manage database interactions (SQL Injection Prevention Cheat Sheet: ORMs).

	- **Input Validation:** Validate and sanitize user inputs before using them in SQL queries (SQL Injection Prevention Cheat Sheet: Input Validation).

	- **Least Privilege:** Apply the principle of least privilege to database accounts (SQL Injection Prevention Cheat Sheet: Least Privilege).

- API Specific Requirements

	- **API Parameterized Queries:** Ensure APIs use parameterized queries to interact with databases (SQL Injection Prevention Cheat Sheet: Parameterized Queries).

	- **API Input Validation:** Validate and sanitize inputs to APIs before using them in SQL queries (SQL Injection Prevention Cheat Sheet: Input Validation).

### Secure File Upload Cheat Sheet

- https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

- Provides guidelines for securely handling file uploads.

- Secure Coding Requirements

	- **File Validation:** Validate file types and content to prevent malicious uploads (Secure File Upload Cheat Sheet: File Validation).

	- **Storage Location:** Store uploaded files in a secure location outside the web root (Secure File Upload Cheat Sheet: Storage Location).

	- **File Size Limits:** Enforce file size limits to prevent Denial of Service (DoS) attacks (Secure File Upload Cheat Sheet: File Size Limits).

	- **Anti-Virus Scanning:** Scan uploaded files for malware (Secure File Upload Cheat Sheet: Anti-Virus Scanning).

	- **File Names:** Sanitize file names to prevent path traversal and other attacks (Secure File Upload Cheat Sheet: File Names).

- API Specific Requirements

	- **API File Validation:** Ensure APIs validate file types and content for uploads (Secure File Upload Cheat Sheet: File Validation).

	- **API Storage Location:** Store files uploaded via APIs in a secure location (Secure File Upload Cheat Sheet: Storage Location).

	- **API File Size Limits:** Enforce file size limits for uploads via APIs (Secure File Upload Cheat Sheet: File Size Limits).

	- **API Anti-Virus Scanning:** Scan files uploaded through APIs for malware (Secure File Upload Cheat Sheet: Anti-Virus Scanning).

	- **API File Names:** Sanitize file names for files uploaded via APIs (Secure File Upload Cheat Sheet: File Names).

### Transport Layer Protection Cheat Sheet

- https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html

- Provides guidelines for protecting data in transit.

- Secure Coding Requirements

	- **TLS Configuration:** Configure TLS securely to protect data in transit (Transport Layer Protection Cheat Sheet: TLS Configuration).

	- **Certificate Management:** Implement proper certificate management practices (Transport Layer Protection Cheat Sheet: Certificate Management).

	- **Forward Secrecy:** Prefer cipher suites that support forward secrecy (Transport Layer Protection Cheat Sheet: Forward Secrecy).

	- **HSTS:** Implement HTTP Strict Transport Security (HSTS) to enforce HTTPS (Transport Layer Protection Cheat Sheet: HSTS).

	- **Secure Cookies:** Use the secure flag for cookies to ensure they are only sent over HTTPS (Transport Layer Protection Cheat Sheet: Secure Cookies).

- API Specific Requirements

	- **API TLS Configuration:** Ensure APIs use secure TLS configurations (Transport Layer Protection Cheat Sheet: TLS Configuration).

	- **API Certificate Management:** Implement proper certificate management for API endpoints (Transport Layer Protection Cheat Sheet: Certificate Management).

	- **API Forward Secrecy:** Prefer forward secrecy for API communications (Transport Layer Protection Cheat Sheet: Forward Secrecy).

	- **API HSTS:** Implement HSTS for APIs to enforce HTTPS (Transport Layer Protection Cheat Sheet: HSTS).

	- **API Secure Cookies:** Ensure cookies used by APIs are flagged as secure (Transport Layer Protection Cheat Sheet: Secure Cookies).

### Cross-Site Scripting (XSS) Prevention Cheat Sheet

- https://cheatsheetseries.owasp.org/cheatsheets/XSS_Prevention_Cheat_Sheet.html

- Provides guidelines for preventing XSS attacks.

- Secure Coding Requirements

	- **Output Encoding:** Use output encoding to prevent XSS (XSS Prevention Cheat Sheet: Output Encoding).

	- **Input Validation:** Validate inputs to ensure they do not contain malicious content (XSS Prevention Cheat Sheet: Input Validation).

	- **Content Security Policy (CSP):** Implement CSP to mitigate XSS risks (XSS Prevention Cheat Sheet: Content Security Policy).

	- **Avoid Inline Scripts:** Avoid using inline scripts to prevent XSS (XSS Prevention Cheat Sheet: Avoid Inline Scripts).

	- **HTTPOnly and Secure Cookies:** Use HTTPOnly and secure flags for cookies to protect against XSS (XSS Prevention Cheat Sheet: HTTPOnly and Secure Cookies).

- API Specific Requirements

	- **API Output Encoding:** Ensure API responses are properly encoded to prevent XSS (XSS Prevention Cheat Sheet: Output Encoding).

	- **API Input Validation:** Validate inputs to APIs to prevent XSS (XSS Prevention Cheat Sheet: Input Validation).

	- **API Content Security Policy:** Implement CSP for APIs to mitigate XSS risks (XSS Prevention Cheat Sheet: Content Security Policy).

	- **API HTTPOnly and Secure Cookies:** Ensure cookies used by APIs are flagged as HTTPOnly and secure (XSS Prevention Cheat Sheet: HTTPOnly and Secure Cookies).

### Security Logging Cheat Sheet

- https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html

- Provides guidelines for securely logging system and application activities.

- Secure Coding Requirements

	- **Sensitive Data Logging:** Avoid logging sensitive data such as passwords and credit card numbers (Security Logging Cheat Sheet: Sensitive Data Logging).

	- **Log Integrity:** Protect logs from tampering by implementing integrity controls (Security Logging Cheat Sheet: Log Integrity).

	- **Log Access Controls:** Restrict access to logs to authorized personnel only (Security Logging Cheat Sheet: Log Access Controls).

	- **Log Retention:** Define and implement log retention policies to comply with legal and operational requirements (Security Logging Cheat Sheet: Log Retention).

	- **Log Analysis:** Regularly analyze logs to detect and respond to security incidents (Security Logging Cheat Sheet: Log Analysis).

- API Specific Requirements

	- **API Sensitive Data Logging:** Ensure APIs do not log sensitive data (Security Logging Cheat Sheet: Sensitive Data Logging).

	- **API Log Integrity:** Implement integrity controls for API logs (Security Logging Cheat Sheet: Log Integrity).

	- **API Log Access Controls:** Restrict access to API logs to authorized personnel (Security Logging Cheat Sheet: Log Access Controls).

	- **API Log Retention:** Define and implement log retention policies for API logs (Security Logging Cheat Sheet: Log Retention).

	- **API Log Analysis:** Regularly analyze API logs to detect and respond to security incidents (Security Logging Cheat Sheet: Log Analysis).

### CSRF Prevention Cheat Sheet

- https://cheatsheetseries.owasp.org/cheatsheets/CSRF_Prevention_Cheat_Sheet.html

- Provides guidelines for preventing Cross-Site Request Forgery (CSRF) attacks.

- Secure Coding Requirements

	- **CSRF Tokens:** Use unique CSRF tokens to protect against CSRF attacks (CSRF Prevention Cheat Sheet: CSRF Tokens).

	- **SameSite Cookies:** Use the SameSite attribute for cookies to mitigate CSRF risks (CSRF Prevention Cheat Sheet: SameSite Cookies).

	- **Double Submit Cookies:** Implement the double submit cookie pattern as an additional layer of protection (CSRF Prevention Cheat Sheet: Double Submit Cookies).

	- **Custom Request Headers:** Use custom request headers to verify the origin of requests (CSRF Prevention Cheat Sheet: Custom Request Headers).

	- **Secure Token Storage:** Securely store CSRF tokens to prevent disclosure (CSRF Prevention Cheat Sheet: Secure Token Storage).

- API Specific Requirements

	- **API CSRF Tokens:** Ensure APIs use unique CSRF tokens to protect against CSRF (CSRF Prevention Cheat Sheet: CSRF Tokens).

	- **API SameSite Cookies:** Use the SameSite attribute for cookies in APIs (CSRF Prevention Cheat Sheet: SameSite Cookies).

	- **API Custom Request Headers:** Use custom request headers to verify the origin of API requests (CSRF Prevention Cheat Sheet: Custom Request Headers).

	- **API Secure Token Storage:** Securely store CSRF tokens for API requests (CSRF Prevention Cheat Sheet: Secure Token Storage).

## OWASP Source Analysis Tools

> **https://owasp.org/www-community/Source_Code_Analysis_Tools**

### List of tools for static and dynamic code analysis.

### Secure Coding Requirements

- **Static Analysis:** Use static analysis tools to identify vulnerabilities in source code (OWASP Source Analysis Tools).

- **Dynamic Analysis:** Use dynamic analysis tools to detect runtime vulnerabilities (OWASP Source Analysis Tools).

- **Code Review:** Perform regular code reviews to ensure adherence to security best practices (OWASP Source Analysis Tools).

- **Automated Testing:** Implement automated security testing in the CI/CD pipeline (OWASP Source Analysis Tools).

### API Specific Requirements

- **API Static Analysis:** Use static analysis tools to identify vulnerabilities in API code (OWASP Source Analysis Tools).

- **API Dynamic Analysis:** Use dynamic analysis tools to detect runtime vulnerabilities in APIs (OWASP Source Analysis Tools).

- **API Code Review:** Perform regular code reviews for APIs to ensure adherence to security best practices (OWASP Source Analysis Tools).

## OWASP Top 10

> **https://owasp.org/www-project-top-ten/**

### Identifies top 10 security risks for web applications.

### Secure Coding Requirements

- **Injection:** Prevent injection attacks by validating inputs (OWASP Top 10: A1:2017).

- **Broken Authentication:** Implement strong authentication mechanisms to prevent unauthorized access (OWASP Top 10: A2:2017).

- **Sensitive Data Exposure:** Protect sensitive data with encryption and other controls (OWASP Top 10: A3:2017).

- **XML External Entities (XXE):** Validate XML inputs to prevent XXE attacks (OWASP Top 10: A4:2017).

- **Broken Access Control:** Enforce proper access controls to prevent unauthorized actions (OWASP Top 10: A5:2017).

- **Security Misconfiguration:** Ensure systems are securely configured to prevent vulnerabilities (OWASP Top 10: A6:2017).

- **Cross-Site Scripting (XSS):** Prevent XSS attacks by validating and sanitizing inputs (OWASP Top 10: A7:2017).

- **Insecure Deserialization:** Avoid insecure deserialization practices and validate serialized data (OWASP Top 10: A8:2017).

- **Using Components with Known Vulnerabilities:** Regularly update and patch software components (OWASP Top 10: A9:2017).

- **Insufficient Logging and Monitoring:** Implement logging and monitoring to detect and respond to security incidents (OWASP Top 10: A10:2017).

### API Specific Requirements

- **API Injection:** Prevent injection attacks in APIs by validating inputs (OWASP Top 10: A1:2017).

- **API Authentication:** Implement strong authentication mechanisms for APIs (OWASP Top 10: A2:2017).

- **API Data Protection:** Protect sensitive data transmitted through APIs with encryption (OWASP Top 10: A3:2017).

- **API Input Validation:** Validate API inputs to prevent XXE and other injection attacks (OWASP Top 10: A4:2017).

- **API Access Control:** Enforce proper access controls for APIs (OWASP Top 10: A5:2017).

- **API Security Configuration:** Ensure APIs are securely configured (OWASP Top 10: A6:2017).

- **API XSS Prevention:** Prevent XSS in API responses by sanitizing outputs (OWASP Top 10: A7:2017).

- **API Serialization:** Avoid insecure deserialization in APIs (OWASP Top 10: A8:2017).

- **API Component Management:** Regularly update and patch API components (OWASP Top 10: A9:2017).

- **API Logging and Monitoring:** Implement logging and monitoring for API activities (OWASP Top 10: A10:2017).

## RFC 5424 (The Syslog Protocol)

> **https://tools.ietf.org/html/rfc5424**

### Protocol for system logging.

### Secure Coding Requirements

- **Log Format:** Use the standardized syslog format for logging (RFC 5424 Section 6).

- **Log Transmission:** Ensure reliable transmission of logs, possibly using encryption to protect log data (RFC 5424 Section 5).

- **Log Storage:** Securely store logs to prevent tampering and unauthorized access (RFC 5424 Section 6.2).

- **Log Management:** Implement log management practices to maintain log integrity and availability (RFC 5424 Section 6.3).

### API Specific Requirements

- **API Log Integration:** Ensure APIs generate logs in the syslog format for consistency (RFC 5424 Section 6).

- **API Log Transmission:** Use secure transmission methods for API logs (RFC 5424 Section 5).

- **API Log Storage:** Securely store API logs to prevent tampering and unauthorized access (RFC 5424 Section 6.2).

## RFC 6749 (OAuth 2.0 Authorization Framework)

> **https://tools.ietf.org/html/rfc6749**

### Framework for token-based authorization.

### Secure Coding Requirements

- **Authorization Code Grant:** Implement the authorization code grant for obtaining access tokens securely, ensuring the client receives an authorization code that is exchanged for an access token (RFC 6749 Section 4.1).

- **Implicit Grant:** Use the implicit grant with caution, typically for public clients where access tokens are returned directly to the client without an authorization code (RFC 6749 Section 4.2).

- **Resource Owner Password Credentials Grant:** Only use this grant type for highly trusted clients, as it involves the sharing of user credentials (RFC 6749 Section 4.3).

- **Client Credentials Grant:** Use the client credentials grant for machine-to-machine authentication, where the client authenticates with the authorization server directly (RFC 6749 Section 4.4).

- **Access Token Security:** Protect access tokens using secure storage mechanisms and transmit them over secure channels (RFC 6749 Section 10.3).

- **Refresh Tokens:** Use refresh tokens to obtain new access tokens, reducing the exposure of long-lived access tokens (RFC 6749 Section 10.4).

- **Client Authentication:** Ensure clients are authenticated securely when requesting tokens, using mechanisms such as client secrets or public/private key pairs (RFC 6749 Section 2.3.1).

- **Scope Management:** Define and enforce scopes for access tokens to limit their privileges and reduce risk (RFC 6749 Section 3.3).

- **State Parameter:** Use the state parameter to prevent CSRF attacks during the authorization process (RFC 6749 Section 10.12).

- **Token Revocation:** Implement token revocation endpoints to invalidate access and refresh tokens when necessary (RFC 7009).

- **PKCE (Proof Key for Code Exchange):** Use PKCE with public clients to mitigate authorization code interception attacks (RFC 7636).

### API Specific Requirements

- **API Token Validation:** Ensure APIs validate access tokens properly, including checking signatures, expiration, and scope (RFC 6749 Section 7).

- **API Scope Enforcement:** Enforce scope restrictions on API access to ensure tokens are used appropriately (RFC 6749 Section 3.3).

- **API Token Revocation:** Implement token revocation endpoints for invalidating tokens when needed (RFC 7009).

- **API PKCE:** Support PKCE for public clients to enhance security during the authorization code exchange (RFC 7636).

- **API Error Handling:** Ensure APIs handle OAuth errors appropriately, returning standardized error responses (RFC 6749 Section 5.2).

- **API Logging:** Log authentication and authorization events for audit and monitoring purposes (OAuth 2.0 Best Current Practices).

## RFC 6811 (BGP Prefix Origin Validation)

> **https://tools.ietf.org/html/rfc6811**

### Mechanism to validate the origination of BGP announcements.

### Secure Coding Requirements

- **Origin Validation:** Implement origin validation to ensure BGP announcements are from legitimate sources (RFC 6811 Section 2).

- **Policy Configuration:** Configure policies to reject invalid BGP announcements (RFC 6811 Section 4).

- **Logging:** Log validation events and policy actions for auditing and troubleshooting (RFC 6811 Section 5).

### API Specific Requirements

- **Nothing API specific**

## RFC 7009 (OAuth 2.0 Token Revocation)

> **https://tools.ietf.org/html/rfc7009**

### Defines a mechanism for clients to revoke access and refresh tokens.

### Secure Coding Requirements

- **Revocation Endpoint:** Implement a token revocation endpoint to allow clients to invalidate tokens (RFC 7009 Section 2.1).

- **Token Types:** Support revocation of both access tokens and refresh tokens (RFC 7009 Section 2.1).

- **Client Authentication:** Require client authentication when requesting token revocation (RFC 7009 Section 2.3).

### API Specific Requirements

- **API Token Revocation:** Ensure APIs support token revocation to invalidate tokens as needed (RFC 7009 Section 2.1).

- **API Client Authentication:** Authenticate clients securely when they request token revocation (RFC 7009 Section 2.3).

## OAuth 2.0 Security Best Current Practice

> **https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics**

### Provides security recommendations and best practices for OAuth 2.0 implementations.

### Secure Coding Requirements

- **Redirect URI Validation:** Ensure strict validation of redirect URIs to prevent open redirect vulnerabilities (OAuth 2.0 Security BCP Section 3.1).

- **Authorization Code Reuse Prevention:** Prevent reuse of authorization codes to mitigate replay attacks (OAuth 2.0 Security BCP Section 3.2).

- **Access Token Binding:** Bind access tokens to client identifiers to prevent token misuse (OAuth 2.0 Security BCP Section 3.3).

- **Refresh Token Rotation:** Use refresh token rotation to detect and handle token theft (OAuth 2.0 Security BCP Section 3.4).

- **Confidential Client Registration:** Ensure confidential clients are registered with secrets or other credentials (OAuth 2.0 Security BCP Section 3.5).

### API Specific Requirements

- **API Redirect URI Validation:** Ensure APIs validate redirect URIs to prevent open redirect vulnerabilities (OAuth 2.0 Security BCP Section 3.1).

- **API Authorization Code Handling:** Ensure APIs prevent reuse of authorization codes (OAuth 2.0 Security BCP Section 3.2).

- **API Access Token Binding:** Bind access tokens to client identifiers for API access (OAuth 2.0 Security BCP Section 3.3).

- **API Refresh Token Handling:** Support refresh token rotation in APIs to detect token theft (OAuth 2.0 Security BCP Section 3.4).

## RFC 7525 (Recommendations for TLS and DTLS)

> **https://tools.ietf.org/html/rfc7525**

### Best practices for using TLS and DTLS securely.

### Secure Coding Requirements

- **Protocol Selection:** Use the latest versions of TLS (1.2 or higher) for secure communication (RFC 7525 Section 3.1).

- **Cipher Suites:** Configure secure cipher suites, avoiding weak or deprecated ones (RFC 7525 Section 4.2).

- **Certificate Management:** Implement proper certificate management practices, including validation and renewal (RFC 7525 Section 5.1).

- **Forward Secrecy:** Prefer cipher suites that support forward secrecy (RFC 7525 Section 4.2).

- **TLS Configuration:** Follow recommended practices for configuring TLS, including disabling renegotiation and compression (RFC 7525 Section 6).

### API Specific Requirements

- **API TLS Configuration:** Ensure APIs use TLS 1.2 or higher for secure communication (RFC 7525 Section 3.1).

- **API Cipher Suites:** Configure secure cipher suites for API communications (RFC 7525 Section 4.2).

- **API Certificate Management:** Implement proper certificate management for API endpoints (RFC 7525 Section 5.1).

## RFC 7636 (Proof Key for Code Exchange by OAuth Public Clients)

> **https://tools.ietf.org/html/rfc7636**

### Extends OAuth 2.0 to provide better security for public clients using the authorization code grant.

### Secure Coding Requirements

- **PKCE Support:** Implement PKCE to enhance the security of the authorization code flow (RFC 7636 Section 4).

- **Code Verifier and Code Challenge:** Generate a code verifier and a code challenge to use during the authorization process (RFC 7636 Section 4.1).

- **Code Challenge Methods:** Support the S256 transformation method for generating the code challenge (RFC 7636 Section 4.2).

### API Specific Requirements

- **API PKCE Validation:** Ensure APIs validate the PKCE parameters during the authorization code exchange (RFC 7636 Section 4.4).

- **API Error Handling:** Handle PKCE-related errors appropriately and return standardized error responses (RFC 7636 Section 4.6).

## RFC 8725 (JWT Best Current Practices)

> **https://tools.ietf.org/html/rfc8725**

### Best practices for securely using JSON Web Tokens (JWT).

### Secure Coding Requirements

- **Algorithm Selection:** Use secure algorithms for signing and encryption (RFC 8725 Section 3).

- **Token Expiration:** Set appropriate expiration times for JWTs to limit their validity (RFC 8725 Section 4.1).

- **Key Management:** Implement secure key management practices for signing and encryption keys (RFC 8725 Section 4.3).

- **Audience Restriction:** Restrict JWT audience to intended recipients only (RFC 8725 Section 4.2).

- **Token Validation:** Validate JWTs properly, including signature and claims verification (RFC 8725 Section 4.4).

### API Specific Requirements

- **API JWT Validation:** Ensure APIs validate JWTs, including signature and claims (RFC 8725 Section 4.4).

- **API Audience Restriction:** Enforce audience restrictions on JWTs used in API communications (RFC 8725 Section 4.2).

- **API Key Management:** Implement secure key management practices for API JWT keys (RFC 8725 Section 4.3).

## RFC 9110 (HTTP Semantics)

> **https://tools.ietf.org/html/rfc9110**

### Defines the semantics of HTTP.

### Secure Coding Requirements

- **HTTP Methods:** Implement proper use of HTTP methods (GET, POST, PUT, DELETE) according to their semantics (RFC 9110 Section 4).

- **Status Codes:** Use appropriate HTTP status codes to represent responses (RFC 9110 Section 9).

- **Content Negotiation:** Implement content negotiation to serve the appropriate representation of resources (RFC 9110 Section 5).

- **Caching:** Use caching headers correctly to control the caching behavior of responses (RFC 9110 Section 7).

- **Security Headers:** Implement security headers such as Content-Security-Policy and Strict-Transport-Security (RFC 9110 Section 10).

### API Specific Requirements

- **API HTTP Methods:** Ensure APIs use HTTP methods according to their semantics (RFC 9110 Section 4).

- **API Status Codes:** Use appropriate HTTP status codes in API responses (RFC 9110 Section 9).

- **API Content Negotiation:** Implement content negotiation for APIs to serve appropriate resource representations (RFC 9110 Section 5).

- **API Caching:** Use caching headers in API responses to control caching behavior (RFC 9110 Section 7).

- **API Security Headers:** Implement security headers in API responses (RFC 9110 Section 10).

## SANS CWE Top 25 Software Errors

> **https://cwe.mitre.org/top25/**

### Lists the top 25 most dangerous software weaknesses.

### Secure Coding Requirements

- **Input Validation:** Ensure proper validation of inputs to prevent common vulnerabilities such as SQL injection and buffer overflow (CWE-20, CWE-79).

- **Error Handling:** Implement proper error handling to prevent information leakage (CWE-209).

- **Access Controls:** Enforce strict access controls to prevent unauthorized access (CWE-284).

- **Resource Management:** Properly manage system resources to avoid issues such as memory leaks and resource exhaustion (CWE-400).

- **Authentication and Authorization:** Implement strong authentication and authorization mechanisms (CWE-287, CWE-306).

- **Logging and Monitoring:** Maintain logs and monitor activities to detect and respond to security incidents (CWE-778).

### API Specific Requirements

- **API Input Validation:** Ensure APIs validate inputs to prevent vulnerabilities (CWE-20, CWE-79).

- **API Error Handling:** Implement proper error handling in APIs to prevent information leakage (CWE-209).

- **API Access Controls:** Enforce strict access controls for APIs (CWE-284).

- **API Resource Management:** Properly manage resources in APIs to avoid issues such as resource exhaustion (CWE-400).

- **API Authentication and Authorization:** Implement strong authentication and authorization for APIs (CWE-287, CWE-306).

- **API Logging and Monitoring:** Maintain logs and monitor API activities to detect and respond to security incidents (CWE-778).

## SANS Secure Software Development and Code Analysis Tools - Whitepaper

> **https://www.sans.org/reading-room/whitepapers/securecode/secure-software-development-code-analysis-tools-36697**

### Guidelines and tools for secure software development and code analysis.

### Secure Coding Requirements

- **Secure Development Lifecycle:** Follow a secure development lifecycle (SDLC) to incorporate security at each stage of software development (SANS Whitepaper).

- **Static Code Analysis:** Use static code analysis tools to identify vulnerabilities early in the development process (SANS Whitepaper).

- **Dynamic Code Analysis:** Use dynamic code analysis tools to detect runtime vulnerabilities (SANS Whitepaper).

- **Manual Code Review:** Conduct manual code reviews to complement automated analysis (SANS Whitepaper).

- **Secure Coding Training:** Provide secure coding training for developers (SANS Whitepaper).

### API Specific Requirements

- **API Static Code Analysis:** Use static code analysis tools to identify vulnerabilities in API code (SANS Whitepaper).

- **API Dynamic Code Analysis:** Use dynamic code analysis tools to detect runtime vulnerabilities in APIs (SANS Whitepaper).

- **API Manual Code Review:** Conduct manual code reviews for APIs to complement automated analysis (SANS Whitepaper).
