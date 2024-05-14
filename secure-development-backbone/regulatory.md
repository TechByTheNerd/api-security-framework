# Regulatory

Below is a table of contents for help navigating this page:

- [Regulatory](#regulatory)
  - [CCPA (California Consumer Privacy Act)](#ccpa-california-consumer-privacy-act)
    - [Enhances privacy rights and consumer protection for residents of California.](#enhances-privacy-rights-and-consumer-protection-for-residents-of-california)
    - [Secure Coding Requirements](#secure-coding-requirements)
    - [API Specific Requirements](#api-specific-requirements)
  - [CPRA (California Privacy Rights Act)](#cpra-california-privacy-rights-act)
    - [Amends and enhances CCPA with additional privacy protections.](#amends-and-enhances-ccpa-with-additional-privacy-protections)
    - [Secure Coding Requirements](#secure-coding-requirements-1)
    - [API Specific Requirements](#api-specific-requirements-1)
  - [FDA 21 CFR Part 11](#fda-21-cfr-part-11)
    - [Establishes criteria for acceptance of electronic records and signatures by the FDA.](#establishes-criteria-for-acceptance-of-electronic-records-and-signatures-by-the-fda)
    - [Secure Coding Requirements](#secure-coding-requirements-2)
    - [API Specific Requirements](#api-specific-requirements-2)
  - [FISMA (Federal Information Security Management Act)](#fisma-federal-information-security-management-act)
    - [Requires federal agencies and contractors to implement information security programs.](#requires-federal-agencies-and-contractors-to-implement-information-security-programs)
    - [Secure Coding Requirements](#secure-coding-requirements-3)
    - [API Specific Requirements](#api-specific-requirements-3)
  - [FedRAMP (Federal Risk and Authorization Management Program)](#fedramp-federal-risk-and-authorization-management-program)
    - [Provides a standardized approach to security assessment, authorization, and continuous monitoring for cloud products and services used by the federal government.](#provides-a-standardized-approach-to-security-assessment-authorization-and-continuous-monitoring-for-cloud-products-and-services-used-by-the-federal-government)
    - [Secure Coding Requirements](#secure-coding-requirements-4)
    - [API Specific Requirements](#api-specific-requirements-4)
  - [GDPR (General Data Protection Regulation)](#gdpr-general-data-protection-regulation)
    - [Protects personal data and privacy for individuals within the European Union.](#protects-personal-data-and-privacy-for-individuals-within-the-european-union)
    - [Secure Coding Requirements](#secure-coding-requirements-5)
    - [API Specific Requirements](#api-specific-requirements-5)
  - [GLBA (Gramm-Leach-Bliley Act)](#glba-gramm-leach-bliley-act)
    - [Protects consumers' personal financial information held by financial institutions.](#protects-consumers-personal-financial-information-held-by-financial-institutions)
    - [Secure Coding Requirements](#secure-coding-requirements-6)
    - [API Specific Requirements](#api-specific-requirements-6)
  - [HiTRUST (Health Information Trust Alliance Common Security Framework)](#hitrust-health-information-trust-alliance-common-security-framework)
    - [Provides a certifiable framework for managing regulatory compliance and risk in healthcare information security.](#provides-a-certifiable-framework-for-managing-regulatory-compliance-and-risk-in-healthcare-information-security)
    - [Secure Coding Requirements](#secure-coding-requirements-7)
    - [API Specific Requirements](#api-specific-requirements-7)
  - [HIPAA (Health Insurance Portability and Accountability Act)](#hipaa-health-insurance-portability-and-accountability-act)
    - [Protects patient health information and ensures data privacy and security.](#protects-patient-health-information-and-ensures-data-privacy-and-security)
    - [Secure Coding Requirements](#secure-coding-requirements-8)
    - [API Specific Requirements](#api-specific-requirements-8)
  - [NAIC (National Association of Insurance Commissioners) Insurance Data Security Model Law](#naic-national-association-of-insurance-commissioners-insurance-data-security-model-law)
    - [Establishes standards for data security and for the investigation and notification of data breaches applicable to insurance providers.](#establishes-standards-for-data-security-and-for-the-investigation-and-notification-of-data-breaches-applicable-to-insurance-providers)
    - [Secure Coding Requirements](#secure-coding-requirements-9)
    - [API Specific Requirements](#api-specific-requirements-9)
  - [NIST CSF (Cybersecurity Framework)](#nist-csf-cybersecurity-framework)
    - [Provides a policy framework for cybersecurity management.](#provides-a-policy-framework-for-cybersecurity-management)
    - [Secure Coding Requirements](#secure-coding-requirements-10)
    - [API Specific Requirements](#api-specific-requirements-10)
  - [NYS DFS Cybersecurity Regulation (23 NYCRR 500)](#nys-dfs-cybersecurity-regulation-23-nycrr-500)
    - [Establishes cybersecurity requirements for financial services companies.](#establishes-cybersecurity-requirements-for-financial-services-companies)
    - [Secure Coding Requirements](#secure-coding-requirements-11)
    - [API Specific Requirements](#api-specific-requirements-11)
  - [PCI-DSS (Payment Card Industry Data Security Standard)](#pci-dss-payment-card-industry-data-security-standard)
    - [Ensures secure handling of cardholder information by merchants and service providers.](#ensures-secure-handling-of-cardholder-information-by-merchants-and-service-providers)
    - [Secure Coding Requirements](#secure-coding-requirements-12)
    - [API Specific Requirements](#api-specific-requirements-12)
  - [SOX (Sarbanes-Oxley Act)](#sox-sarbanes-oxley-act)
    - [No specific IT requirements. Ensures financial transparency and accountability, requiring stringent financial reporting and controls.](#no-specific-it-requirements-ensures-financial-transparency-and-accountability-requiring-stringent-financial-reporting-and-controls)
    - [Secure Coding Requirements](#secure-coding-requirements-13)
    - [API Specific Requirements](#api-specific-requirements-13)


---

## CCPA (California Consumer Privacy Act)

> **https://oag.ca.gov/privacy/ccpa**

### Enhances privacy rights and consumer protection for residents of California.

### Secure Coding Requirements

- **Data Minimization:** Collect and retain only as much personal data as needed for processing purposes (CCPA §1798.100(b)).

- **Data Security:** Implement and maintain reasonable security procedures and practices to protect personal data from unauthorized access, destruction, use, modification, or disclosure (CCPA §1798.150(a)(1)).

- **Access Controls:** Ensure that only authorized personnel can access personal data (CCPA §1798.140(w)(1)(B)).

- **Encryption:** Encrypt personal data both at rest and in transit to protect against unauthorized access (CCPA §1798.81.5).

- **Data Breach Notification:** Establish procedures for promptly notifying affected individuals in the event of a data breach (CCPA §1798.82).

- **Consumer Rights:** Implement mechanisms to facilitate consumer rights requests, such as access, deletion, and opt-out (CCPA §1798.105-1798.120).

### API Specific Requirements

- **Data Access APIs:** Ensure APIs that provide access to personal data are secured with proper authentication and authorization mechanisms (CCPA §1798.140(w)(1)(B)).

- **Data Deletion APIs:** Implement APIs that support consumer requests for data deletion, ensuring secure and complete removal of personal data (CCPA §1798.105(c)).

- **Data Portability APIs:** Provide APIs that allow consumers to receive their personal data in a readily usable format (CCPA §1798.100(d)).

## CPRA (California Privacy Rights Act)

> **https://www.caprivacy.org/**

### Amends and enhances CCPA with additional privacy protections.

### Secure Coding Requirements

- **Data Minimization:** Ensure that the collection, usage, retention, and sharing of personal data is limited to what is necessary (CPRA §1798.100(c)).

- **Data Classification:** Classify personal data based on sensitivity and apply appropriate security measures (CPRA §1798.185(a)(15)).

- **Data Protection Impact Assessments:** Conduct assessments to identify and mitigate risks related to data processing activities (CPRA §1798.185(a)(15)).

- **Contractual Controls:** Ensure that contracts with service providers include obligations to protect personal data (CPRA §1798.140(v)).

- **Data Security:** Maintain reasonable security procedures and practices appropriate to the nature of the personal data to protect against unauthorized access and disclosure (CPRA §1798.185(a)(1)).

- **Access Controls:** Implement role-based access controls to restrict access to personal data (CPRA §1798.185(a)(7)).

### API Specific Requirements

- **Consumer Rights APIs:** Ensure APIs facilitate consumer rights requests, including access, correction, deletion, and opt-out of personal data (CPRA §1798.105-1798.125).

- **Data Transfer APIs:** Implement secure APIs for transferring personal data to consumers or other entities upon request (CPRA §1798.100(d)).

- **Data Deletion APIs:** Provide secure APIs to support consumer requests for data deletion, ensuring secure and complete removal of personal data (CPRA §1798.105(c)).

- **Data Correction APIs:** Create APIs to allow consumers to request corrections to their personal data (CPRA §1798.106(a)).

## FDA 21 CFR Part 11

> **https://www.fda.gov/regulatory-information/search-fda-guidance-documents/**21-cfr-part-11-electronic-records-electronic-signatures-scope-and-application

### Establishes criteria for acceptance of electronic records and signatures by the FDA.

### Secure Coding Requirements

- **Electronic Signatures:** Implement controls to ensure the uniqueness of electronic signatures to prevent unauthorized use (21 CFR §11.200(a)).

- **Audit Trails:** Maintain audit trails that document who accessed the system and what operations were performed (21 CFR §11.10(e)).

- **Data Integrity:** Ensure the integrity of electronic records through the use of validated systems (21 CFR §11.10(a)).

- **Access Controls:** Restrict system access to authorized individuals (21 CFR §11.10(d)).

- **Record Retention:** Ensure electronic records are retained for the required period and are retrievable (21 CFR §11.10(c)).

- **Encryption:** Encrypt electronic records to protect against unauthorized access (21 CFR §11.30).

- **Validation:** Validate systems to ensure accuracy, reliability, consistent intended performance, and the ability to discern invalid or altered records (21 CFR §11.10(a)).

### API Specific Requirements

- **Signature Verification APIs:** Implement APIs to verify the authenticity of electronic signatures (21 CFR §11.200(a)).

- **Audit Trail APIs:** Provide APIs for querying and managing audit trails to track access and changes to electronic records (21 CFR §11.10(e)).

- **Data Integrity APIs:** Ensure APIs enforce data integrity checks and validations (21 CFR §11.10(a)).

- **Access Control APIs:** Implement APIs to manage and enforce access controls for electronic records (21 CFR §11.10(d)).

## FISMA (Federal Information Security Management Act)

> **https://www.nist.gov/programs-projects/**federal-information-security-management-act-fisma-implementation-project

### Requires federal agencies and contractors to implement information security programs.

### Secure Coding Requirements

- **Risk Management Framework:** Implement a risk management framework to categorize, select, implement, assess, authorize, and monitor security controls (FISMA §3544(a)(1)(B)).

- **Security Controls:** Apply security controls from NIST SP 800-53 to ensure adequate protection of information systems (FISMA §3544(a)(1)(A)).

- **Continuous Monitoring:** Implement continuous monitoring of information systems to detect and respond to security incidents (FISMA §3544(b)(7)(C)).

- **Incident Response:** Establish incident response procedures and conduct regular testing (FISMA §3544(b)(7)(D)).

- **Access Controls:** Ensure only authorized individuals have access to information systems (FISMA §3544(a)(1)(A)(ii)(I)).

- **Audit Trails:** Maintain audit logs to monitor and record system activity (FISMA §3544(a)(1)(A)(ii)(III)).

- **Data Encryption:** Encrypt sensitive data to protect it during transmission and storage (FISMA §3544(a)(1)(A)(ii)(II)).

### API Specific Requirements

- **Access Control APIs:** Implement APIs to manage and enforce role-based access controls (FISMA §3544(a)(1)(A)(ii)(I)).

- **Audit Trail APIs:** Provide APIs to log, monitor, and analyze access and activity logs (FISMA §3544(a)(1)(A)(ii)(III)).

- **Data Encryption APIs:** Ensure APIs facilitate data encryption during transmission and storage (FISMA §3544(a)(1)(A)(ii)(II)).

- **Incident Response APIs:** Create APIs to support incident detection, reporting, and response activities (FISMA §3544(b)(7)(D)).

## FedRAMP (Federal Risk and Authorization Management Program)

> **https://www.fedramp.gov/**

### Provides a standardized approach to security assessment, authorization, and continuous monitoring for cloud products and services used by the federal government.

### Secure Coding Requirements

- **Security Controls:** Implement security controls from NIST SP 800-53 tailored for cloud environments (FedRAMP Moderate Baseline).

- **Continuous Monitoring:** Conduct continuous monitoring to ensure ongoing assessment and authorization of cloud systems (FedRAMP Continuous Monitoring Requirements).

- **Configuration Management:** Apply secure configuration management practices to ensure cloud systems are maintained in a secure state (FedRAMP Configuration Management).

- **Incident Response:** Develop and test incident response plans for cloud systems (FedRAMP Incident Response Requirements).

- **Encryption:** Encrypt data at rest and in transit to protect sensitive information (FedRAMP Encryption Requirements).

- **Access Controls:** Implement role-based access controls to limit access to authorized personnel (FedRAMP Access Control Requirements).

### API Specific Requirements

- **Access Control APIs:** Provide APIs to manage and enforce role-based access controls for cloud resources (FedRAMP Access Control Requirements).

- **Audit Trail APIs:** Implement APIs to log and monitor access and activity within the cloud environment (FedRAMP Audit Logging Requirements).

- **Data Encryption APIs:** Ensure APIs support encryption of data at rest and in transit (FedRAMP Encryption Requirements).

- **Configuration Management APIs:** Develop APIs to automate and enforce secure configuration management practices (FedRAMP Configuration Management).

## GDPR (General Data Protection Regulation)

> **https://gdpr.eu/**

### Protects personal data and privacy for individuals within the European Union.

### Secure Coding Requirements

- **Data Minimization:** Only collect and process data that is necessary for the intended purpose (GDPR Article 5(1)(c)).

- **Data Security:** Implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk (GDPR Article 32(1)).

- **Data Protection by Design:** Integrate data protection into the development and operation of information systems (GDPR Article 25(1)).

- **Access Controls:** Ensure that access to personal data is limited to authorized personnel (GDPR Article 5(1)(f)).

- **Encryption:** Encrypt personal data to protect it against unauthorized access (GDPR Article 32(1)(a)).

- **Data Breach Notification:** Establish procedures to detect, report, and investigate personal data breaches (GDPR Article 33).

- **Data Subject Rights:** Implement mechanisms to facilitate data subject rights, such as access, rectification, erasure, and data portability (GDPR Articles 15-20).

### API Specific Requirements

- **Data Access APIs:** Ensure APIs that provide access to personal data are secured with proper authentication and authorization mechanisms (GDPR Article 5(1)(f)).

- **Data Deletion APIs:** Implement APIs that support data subject requests for data deletion (GDPR Article 17).

- **Data Portability APIs:** Provide APIs that allow data subjects to receive their personal data in a structured, commonly used, and machine-readable format (GDPR Article 20).

- **Data Protection APIs:** Develop APIs to enforce data protection by design and by default principles (GDPR Article 25(1)).

## GLBA (Gramm-Leach-Bliley Act)

> **https://www.ftc.gov/tips-advice/business-center/privacy-and-security/**gramm-leach-bliley-act

### Protects consumers' personal financial information held by financial institutions.

### Secure Coding Requirements

- **Data Security:** Implement administrative, technical, and physical safeguards to protect the security, confidentiality, and integrity of customer information (GLBA Safeguards Rule §314.4(b)).

- **Access Controls:** Limit access to customer information to those who need it to perform their job duties (GLBA Safeguards Rule §314.4(c)).

- **Encryption:** Encrypt customer information to protect it during transmission and storage (GLBA Safeguards Rule §314.4(b)(2)).

- **Risk Assessments:** Conduct regular risk assessments to identify potential threats to customer information (GLBA Safeguards Rule §314.4(b)).

- **Audit Trails:** Maintain logs to monitor and record access to customer information (GLBA Safeguards Rule §314.4(b)(3)).

- **Incident Response:** Develop and implement an incident response plan to respond to security incidents (GLBA Safeguards Rule §314.4(e)).

### API Specific Requirements

- **Access Control APIs:** Implement APIs to manage and enforce access controls for customer information (GLBA Safeguards Rule §314.4(c)).

- **Encryption APIs:** Ensure APIs facilitate encryption of customer information during transmission and storage (GLBA Safeguards Rule §314.4(b)(2)).

- **Audit Trail APIs:** Provide APIs to log and monitor access to customer information (GLBA Safeguards Rule §314.4(b)(3)).

- **Incident Response APIs:** Develop APIs to support incident detection, reporting, and response activities (GLBA Safeguards Rule §314.4(e)).

## HiTRUST (Health Information Trust Alliance Common Security Framework)

> **https://hitrustalliance.net/**

### Provides a certifiable framework for managing regulatory compliance and risk in healthcare information security.

### Secure Coding Requirements

- **Data Protection:** Implement controls to protect the confidentiality, integrity, and availability of healthcare data (HiTRUST CSF 01.b).

- **Access Controls:** Ensure access to healthcare data is restricted to authorized personnel (HiTRUST CSF 07.1.1).

- **Encryption:** Encrypt healthcare data both at rest and in transit to protect against unauthorized access (HiTRUST CSF 10.1.1).

- **Audit Trails:** Maintain audit logs to monitor access and changes to healthcare data (HiTRUST CSF 10.10.1).

- **Incident Response:** Develop and test incident response plans for healthcare data breaches (HiTRUST CSF 12.1.1).

- **Risk Management:** Conduct regular risk assessments to identify and mitigate risks to healthcare data (HiTRUST CSF 02.r).

### API Specific Requirements

- **Access Control APIs:** Provide APIs to manage and enforce access controls for healthcare data (HiTRUST CSF 07.1.1).

- **Encryption APIs:** Ensure APIs support encryption of healthcare data both at rest and in transit (HiTRUST CSF 10.1.1).

- **Audit Trail APIs:** Implement APIs to log and monitor access and changes to healthcare data (HiTRUST CSF 10.10.1).

- **Incident Response APIs:** Develop APIs to support incident detection, reporting, and response activities for healthcare data (HiTRUST CSF 12.1.1).

## HIPAA (Health Insurance Portability and Accountability Act)

> **https://www.hhs.gov/hipaa/index.html**

### Protects patient health information and ensures data privacy and security.

### Secure Coding Requirements

- **Access Controls:** Implement technical policies and procedures to limit access to electronic protected health information (ePHI) to authorized persons (HIPAA 45 CFR 164.312(a)(1)).

- **Audit Controls:** Implement hardware, software, and/or procedural mechanisms to record and examine access and other activity in information systems that contain or use ePHI (HIPAA 45 CFR 164.312(b)).

- **Integrity Controls:** Implement policies and procedures to protect ePHI from improper alteration or destruction (HIPAA 45 CFR 164.312(c)(1)).

- **Transmission Security:** Implement technical security measures to guard against unauthorized access to ePHI transmitted over an electronic network (HIPAA 45 CFR 164.312(e)(1)).

- **Encryption:** Encrypt ePHI to protect it during transmission and storage (HIPAA 45 CFR 164.312(a)(2)(iv)).

- **Incident Response:** Establish procedures for responding to security incidents involving ePHI (HIPAA 45 CFR 164.308(a)(6)).

### API Specific Requirements

- **Access Control APIs:** Provide APIs to manage and enforce access controls for ePHI (HIPAA 45 CFR 164.312(a)(1)).

- **Audit Trail APIs:** Implement APIs to log and monitor access and activity related to ePHI (HIPAA 45 CFR 164.312(b)).

- **Encryption APIs:** Ensure APIs support encryption of ePHI during transmission and storage (HIPAA 45 CFR 164.312(a)(2)(iv)).

- **Transmission Security APIs:** Develop APIs to secure ePHI transmitted over electronic networks (HIPAA 45 CFR 164.312(e)(1)).

## NAIC (National Association of Insurance Commissioners) Insurance Data Security Model Law

> **https://www.naic.org/**

### Establishes standards for data security and for the investigation and notification of data breaches applicable to insurance providers.

### Secure Coding Requirements

- **Data Security Program:** Implement a comprehensive information security program based on an assessment of risks (NAIC Model Law §4).

- **Access Controls:** Implement access controls to limit access to personal information to authorized individuals (NAIC Model Law §4).

- **Encryption:** Encrypt non-public information both in transit and at rest (NAIC Model Law §4).

- **Audit Trails:** Maintain audit logs to record access and activity involving non-public information (NAIC Model Law §4).

- **Incident Response:** Develop and maintain a written incident response plan to promptly respond to data breaches (NAIC Model Law §4).

- **Third-Party Service Provider Security:** Ensure that third-party service providers implement appropriate security measures to protect personal information (NAIC Model Law §4).

### API Specific Requirements

- **Access Control APIs:** Provide APIs to manage and enforce access controls for personal information (NAIC Model Law §4).

- **Encryption APIs:** Ensure APIs facilitate encryption of personal information both in transit and at rest (NAIC Model Law §4).

- **Audit Trail APIs:** Implement APIs to log and monitor access and activity related to personal information (NAIC Model Law §4).

- **Incident Response APIs:** Develop APIs to support incident detection, reporting, and response activities for personal information (NAIC Model Law §4).

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

## NYS DFS Cybersecurity Regulation (23 NYCRR 500)

> **https://www.dfs.ny.gov/industry_guidance/cybersecurity**

### Establishes cybersecurity requirements for financial services companies.

### Secure Coding Requirements

- **Cybersecurity Program:** Implement a cybersecurity program to protect the confidentiality, integrity, and availability of information systems (23 NYCRR 500.02).

- **Cybersecurity Policies:** Develop and implement policies for the protection of information systems and non-public information (23 NYCRR 500.03).

- **Access Controls:** Limit access to information systems and non-public information to authorized individuals (23 NYCRR 500.07).

- **Encryption:** Encrypt non-public information both in transit and at rest (23 NYCRR 500.15).

- **Audit Trails:** Maintain systems that log and record access and activity involving non-public information (23 NYCRR 500.06).

- **Incident Response:** Develop and maintain a written incident response plan to promptly respond to data breaches (23 NYCRR 500.16).

- **Third-Party Service Provider Security:** Ensure third-party service providers implement appropriate security measures to protect non-public information (23 NYCRR 500.11).

### API Specific Requirements

- **Access Control APIs:** Provide APIs to manage and enforce access controls for non-public information (23 NYCRR 500.07).

- **Encryption APIs:** Ensure APIs facilitate encryption of non-public information both in transit and at rest (23 NYCRR 500.15).

- **Audit Trail APIs:** Implement APIs to log and monitor access and activity related to non-public information (23 NYCRR 500.06).

- **Incident Response APIs:** Develop APIs to support incident detection, reporting, and response activities for non-public information (23 NYCRR 500.16).

## PCI-DSS (Payment Card Industry Data Security Standard)

> **https://www.pcisecuritystandards.org/**

### Ensures secure handling of cardholder information by merchants and service providers.

### Secure Coding Requirements

- **Network Security:** Install and maintain a firewall configuration to protect cardholder data (PCI-DSS Requirement 1).

- **Protect Cardholder Data:** Protect stored cardholder data through encryption and other means (PCI-DSS Requirement 3).

- **Encryption:** Encrypt transmission of cardholder data across open, public networks (PCI-DSS Requirement 4).

- **Access Controls:** Restrict access to cardholder data by business need to know (PCI-DSS Requirement 7).

- **Authentication:** Assign a unique ID to each person with computer access to cardholder data (PCI-DSS Requirement 8).

- **Audit Trails:** Track and monitor all access to network resources and cardholder data (PCI-DSS Requirement 10).

- **Regular Testing:** Regularly test security systems and processes (PCI-DSS Requirement 11).

- **Security Policies:** Maintain a policy that addresses information security for employees and contractors (PCI-DSS Requirement 12).

### API Specific Requirements

- **Access Control APIs:** Implement APIs to manage and enforce access controls for cardholder data (PCI-DSS Requirement 7).

- **Encryption APIs:** Ensure APIs facilitate encryption of cardholder data during transmission (PCI-DSS Requirement 4).

- **Audit Trail APIs:** Implement APIs to log and monitor access and activity related to cardholder data (PCI-DSS Requirement 10).

- **Authentication APIs:** Provide APIs to enforce unique ID assignment and authentication (PCI-DSS Requirement 8).

## SOX (Sarbanes-Oxley Act)

> **https://www.sec.gov/spotlight/sarbanes-oxley.htm**

### No specific IT requirements. Ensures financial transparency and accountability, requiring stringent financial reporting and controls.

### Secure Coding Requirements

- **No cybersecurity requirements**

### API Specific Requirements

- **Nothing API specific**

