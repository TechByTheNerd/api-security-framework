# API Specific Standards


## Regulations

### CCPA (California Consumer Privacy Act)

> https://www.oag.ca.gov/privacy/ccpa

#### Notice at Collection

- **API data collection disclosure** — Businesses MUST disclose the categories of personal information collected via APIs and the specific purposes for which the information is used, at or before the point of collection. (CCPA, Section 1798.100(b))

#### Data Access and Management

- **API consumer rights facilitation** — Businesses MUST provide mechanisms through APIs that allow consumers to request access to or deletion of their personal information, ensuring transparency and control over personal data. (CCPA, Section 1798.105(c))

#### Opt-out of Personal Information Sale

- **API opt-out functionality** — Businesses MUST implement API endpoints that enable consumers to opt-out of the sale of their personal information, making the process easily accessible and user-friendly. (CCPA, Section 1798.120(a))

#### Right to Non-Discrimination

- **API non-discriminatory practices** — Businesses MUST ensure that their APIs do not discriminate against consumers who exercise their rights under the CCPA, particularly in terms of functionality and response times. (CCPA, Section 1798.125(a)(1))

#### Action Items

Below are the action items for this standard, organized by responsible party:

##### Policymakers and Organizational Rules

- Define and document the categories of personal information collected via APIs and the specific purposes for which the information is used.
- Establish policies to ensure transparency and control over personal data.
- Develop policies to ensure non-discriminatory practices in API functionality and response times.

##### Infrastructure and Automation Implementers

- Implement mechanisms through APIs that allow consumers to request access to or deletion of their personal information.
- Implement API endpoints that enable consumers to opt-out of the sale of their personal information.

##### Software Architects and Developers

- Design APIs to disclose the categories of personal information collected and the specific purposes for which the information is used.
- Develop APIs that provide mechanisms for consumers to request access to or deletion of their personal information.
- Develop APIs that enable consumers to opt-out of the sale of their personal information.
- Ensure that APIs do not discriminate against consumers who exercise their rights under the CCPA, particularly in terms of functionality and response times.

---

### CPRA (California Privacy Rights Act)

> https://en.wikipedia.org/wiki/California_Privacy_Rights_Act

#### Expanded Consumer Rights

- **API access and correction** — Businesses MUST create API endpoints that allow consumers to request access to and correct their personal information easily. This supports transparency and accuracy in data handling. (CPRA, Article 2, Section 1798.106(a)(1)(A))

#### Sensitive Personal Information

- **API controls for sensitive information** — Businesses MUST implement API mechanisms that allow consumers to limit the use and disclosure of sensitive personal information, enhancing privacy protections. (CPRA, Article 2, Section 1798.121)

#### Automated Decision-Making

- **Transparency in API-based decisions** — Businesses MUST provide consumers with access to information via APIs about the logic involved in automated decision-making processes that have a significant effect on them. (CPRA, Article 3, Section 1798.141(a))

#### Risk Assessment

- **API risk assessment reporting** — Businesses MUST conduct regular risk assessments of their APIs that handle personal data and report these assessments as required by the CPRA. (CPRA, Article 4, Section 1798.185(a)(15)(B))

#### Right to Opt-Out of Automated Decision-Making

- **API opt-out mechanisms** — Businesses MUST enable an API-based method for consumers to opt-out of automated decision-making technology used by businesses. (CPRA, Article 3, Section 1798.141(b))

#### Action Items

Below are the action items for this standard, organized by responsible party:

##### Policymakers and Organizational Rules

- Define and document the categories of sensitive personal information handled via APIs and the specific purposes for which the information is used.
- Establish policies to ensure transparency and control over sensitive personal data, including automated decision-making processes.
- Develop policies for regular risk assessments of APIs that handle personal data.

##### Infrastructure and Automation Implementers

- Implement API endpoints that allow consumers to request access to and correct their personal information.
- Implement API mechanisms that allow consumers to limit the use and disclosure of sensitive personal information.
- Implement API-based methods for consumers to opt-out of automated decision-making technology.
- Implement mechanisms for conducting regular risk assessments of APIs that handle personal data.

##### Software Architects and Developers

- Design APIs to disclose the categories of sensitive personal information collected and the specific purposes for which the information is used.
- Develop APIs that provide mechanisms for consumers to request access to and correct their personal information.
- Develop APIs that allow consumers to limit the use and disclosure of sensitive personal information.
- Develop APIs that provide consumers with access to information about the logic involved in automated decision-making processes.
- Develop APIs that enable an API-based method for consumers to opt-out of automated decision-making technology.
- Ensure that APIs are designed and developed in a way that minimizes risks to personal data.

---

### GDPR (General Data Protection Regulation)

> https://gdpr.eu/

#### Consent Management

- **API endpoints for consent management** — Businesses MUST provide APIs that allow individuals to manage consent settings for the processing of their personal data dynamically. This includes granting, withdrawing, or modifying consent. (GDPR, Article 7, Recital 42)

#### Data Subject Access Rights

- **APIs for data access requests** — Organizations MUST provide APIs that enable individuals to access their personal data and utilize their rights under GDPR such as data portability and the right to erasure ("Right to be Forgotten"). (GDPR, Articles 15, 17, and 20)

#### Data Portability

- **APIs to facilitate data portability** — Organizations MUST ensure APIs offer capabilities for data subjects to receive their personal data in a structured, commonly used, and machine-readable format, and to transmit that data to another controller without hindrance. (GDPR, Article 20)

#### Data Protection by Design and by Default

- **API security by design** — Organizations MUST integrate comprehensive security features into their APIs at the design phase, ensuring data protection measures are embedded within the development lifecycle. (GDPR, Article 25)

#### Data Breach Notification

- **API for breach notification** — Organizations MUST implement APIs to facilitate rapid breach notification to supervisory authorities and affected individuals when personal data breaches occur, particularly when the breach poses a high risk to the rights and freedoms of natural persons. (GDPR, Articles 33 and 34)

#### Action Items

Below are the action items for this standard, organized by responsible party:

##### Policymakers and Organizational Rules

- Define and document the categories of personal data handled via APIs and the specific purposes for which the information is used.
- Establish policies to ensure transparency and control over personal data, including consent management and data subject access rights.
- Develop policies for data protection by design and by default, and data breach notification.

##### Infrastructure and Automation Implementers

- Implement API endpoints that allow individuals to manage consent settings for the processing of their personal data dynamically.
- Implement APIs that enable individuals to access their personal data and utilize their rights under GDPR such as data portability and the right to erasure ("Right to be Forgotten").
- Implement APIs that offer capabilities for data subjects to receive their personal data in a structured, commonly used, and machine-readable format, and to transmit that data to another controller without hindrance.
- Implement APIs to facilitate rapid breach notification to supervisory authorities and affected individuals when personal data breaches occur.

##### Software Architects and Developers

- Design APIs with comprehensive security features integrated at the design phase, ensuring data protection measures are embedded within the development lifecycle.
- Develop APIs that allow individuals to manage consent settings for the processing of their personal data dynamically.
- Develop APIs that enable individuals to access their personal data and utilize their rights under GDPR such as data portability and the right to erasure ("Right to be Forgotten").
- Develop APIs that offer capabilities for data subjects to receive their personal data in a structured, commonly used, and machine-readable format, and to transmit that data to another controller without hindrance.
- Develop APIs to facilitate rapid breach notification to supervisory authorities and affected individuals when personal data breaches occur.

---

### FISMA (Federal Information Security Modernization Act)

> https://www.cisa.gov/topics/cyber-threats-and-advisories/federal-information-security-modernization-act

#### Inventory of Information Systems

- **API asset management** — Federal agencies MUST maintain an accurate inventory of information systems, including APIs, as part of their system inventory. APIs should be categorized based on their security impact. (FISMA, 44 U.S.C. § 3554, Requirement for agency program)

#### Security Controls Implementation

- **Security controls for APIs** — Agencies SHALL implement specific security controls for APIs to protect against unauthorized access, data leaks, and attacks. This includes ensuring that APIs are integrated into the agency’s overall security architecture. (NIST SP 800-53, Security and Privacy Controls for Federal Information Systems and Organizations)

#### Risk Assessment

- **API-specific risk assessments** — Agencies MUST conduct risk assessments that explicitly consider vulnerabilities and threats specific to APIs, such as improper authentication, data exposure, and attack surface expansion. (NIST SP 800-30, Guide for Conducting Risk Assessments)

#### Security Authorization

- **API security authorization** — Information systems that include APIs MUST undergo a security authorization process where APIs are evaluated to ensure they meet security requirements before deployment. (FISMA, 44 U.S.C. § 3554, Authorization of information systems)

#### Continuous Monitoring

- **Monitoring API transactions** — Agencies SHALL implement a strategy for continuous monitoring that includes specific measures for monitoring API traffic and usage to detect security incidents and anomalies in real-time. (NIST SP 800-137, Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations)

#### Incident Response

- **API-focused incident response** — Agencies MUST develop and maintain an incident response capability that specifically includes procedures for responding to security incidents involving APIs. (NIST SP 800-61, Computer Security Incident Handling Guide)

#### Action Items

Below are the action items for this standard, organized by responsible party:

##### Policymakers and Organizational Rules

- Define and document an accurate inventory of information systems, including APIs, as part of their system inventory.
- Establish policies to ensure that APIs are integrated into the agency’s overall security architecture.
- Develop policies for conducting API-specific risk assessments.
- Develop policies for API security authorization process.
- Develop policies for continuous monitoring of API traffic and usage to detect security incidents and anomalies in real-time.
- Develop policies for API-focused incident response.

##### Infrastructure and Automation Implementers

- Implement mechanisms to maintain an accurate inventory of APIs.
- Implement specific security controls for APIs to protect against unauthorized access, data leaks, and attacks.
- Implement mechanisms for conducting API-specific risk assessments.
- Implement mechanisms for API security authorization process.
- Implement a strategy for continuous monitoring of API traffic and usage to detect security incidents and anomalies in real-time.
- Implement mechanisms for API-focused incident response.

##### Software Architects and Developers

- Design APIs with comprehensive security features integrated at the design phase, ensuring data protection measures are embedded within the development lifecycle.
- Develop APIs that are integrated into the agency’s overall security architecture.
- Develop APIs with mechanisms for conducting API-specific risk assessments.
- Develop APIs that undergo a security authorization process before deployment.
- Develop APIs with mechanisms for continuous monitoring of API traffic and usage to detect security incidents and anomalies in real-time.
- Develop APIs with mechanisms for API-focused incident response.

---

### HIPAA (Health Insurance Portability and Accountability Act)

> https://www.hhs.gov/hipaa/index.html

#### Privacy Rule Compliance

- **API access to PHI** — Covered entities MUST ensure the privacy of protected health information (PHI) and provide APIs that allow patients appropriate access to their medical records. (Privacy Rule, 45 CFR Part 160 and Subparts A and E of Part 164)

#### Security Rule Compliance

- **API security measures** — Entities SHALL implement technical safeguards to ensure the confidentiality, integrity, and security of electronic protected health information (ePHI) accessible or transmittable via APIs. (Security Rule, 45 CFR Part 160 and Subparts A and C of Part 164)

#### Breach Notification Rule

- **APIs for timely breach notification** — Entities MUST notify affected individuals, the Secretary of HHS, and, in certain circumstances, the media of breaches of unsecured PHI in a timely manner, typically no later than 60 days after discovery, which can be facilitated through API functionalities. (Breach Notification Rule, 45 CFR §§ 164.400-414)

#### Minimum Necessary Use

- **API data minimization** — When using or disclosing PHI or when requesting PHI from another covered entity, entities MUST design APIs to limit information to the minimum necessary to accomplish the intended purpose. (Minimum Necessary Requirement, 45 CFR § 164.502(b), 164.514(d))

#### Business Associate Agreements

- **API terms in agreements** — Covered entities MUST ensure that business associates who handle PHI via APIs agree to the same stringent conditions for the use and disclosure of PHI through formal agreements that include API specifications. (45 CFR § 164.504(e))

#### Risk Analysis and Management

- **API risk assessment** — Entities MUST conduct an accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability of ePHI handled by APIs. (Security Management Process, 45 CFR § 164.308(a)(1)(ii)(A))

#### Training and Awareness

- **API-specific training** — Entities MUST provide training programs to all employees concerning the entity’s privacy policies and procedures related to API use. (Security Awareness and Training, 45 CFR § 164.308(a)(5))

#### Patient Rights

- **API support for patient rights** — Entities SHALL ensure that APIs facilitate patients' rights to request privacy protections, access PHI, amend their PHI, and receive an accounting of disclosures. (Patient Rights, 45 CFR § 164.524, § 164.526, § 164.528)

#### Complaints Management

- **APIs for complaints** — Entities MUST provide a process via APIs for individuals to make complaints concerning the covered entity’s privacy policies and procedures. (Privacy Rule, 45 CFR § 164.530(d))

#### Data Encryption

- **API encryption protocols** — Entities SHOULD implement encryption for ePHI transmitted via APIs whenever deemed appropriate based on the risk assessment. (Technical Safeguards, 45 CFR § 164.312(a)(2)(iv))

#### Audit Controls

- **API auditing mechanisms** — Entities SHALL implement hardware, software, and procedural mechanisms to record and examine activity in information systems that contain or use ePHI via APIs. (Audit Controls, 45 CFR § 164.312(b))

#### Action Items

Below are the action items for this standard, organized by responsible party:

##### Policymakers and Organizational Rules

- Define and document the categories of protected health information (PHI) and electronic protected health information (ePHI) handled via APIs.
- Establish policies to ensure the privacy of PHI and provide patients appropriate access to their medical records.
- Develop policies for technical safeguards to ensure the confidentiality, integrity, and security of ePHI.
- Develop policies for timely breach notification.
- Develop policies for data minimization in API design.
- Develop policies for business associate agreements that include API specifications.
- Develop policies for conducting an accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability of ePHI handled by APIs.
- Develop policies for API-specific training programs.
- Develop policies for facilitating patients' rights to request privacy protections, access PHI, amend their PHI, and receive an accounting of disclosures.
- Develop policies for handling complaints concerning the entity’s privacy policies and procedures related to API use.
- Develop policies for implementing encryption for ePHI transmitted via APIs based on the risk assessment.
- Develop policies for implementing audit controls to record and examine activity in information systems that contain or use ePHI via APIs.

##### Infrastructure and Automation Implementers

- Implement APIs that allow patients appropriate access to their medical records.
- Implement technical safeguards to ensure the confidentiality, integrity, and security of ePHI accessible or transmittable via APIs.
- Implement APIs for timely breach notification.
- Implement APIs that limit information to the minimum necessary to accomplish the intended purpose.
- Implement APIs that handle PHI in accordance with business associate agreements.
- Implement mechanisms for conducting an accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability of ePHI handled by APIs.
- Implement API-specific training programs.
- Implement APIs that facilitate patients' rights to request privacy protections, access PHI, amend their PHI, and receive an accounting of disclosures.
- Implement APIs for handling complaints concerning the entity’s privacy policies and procedures.
- Implement encryption for ePHI transmitted via APIs based on the risk assessment.
- Implement audit controls to record and examine activity in information systems that contain or use ePHI via APIs.

##### Software Architects and Developers

- Design APIs that allow patients appropriate access to their medical records.
- Develop APIs with technical safeguards to ensure the confidentiality, integrity, and security of ePHI.
- Develop APIs for timely breach notification.
- Develop APIs that limit information to the minimum necessary to accomplish the intended purpose.
- Develop APIs that handle PHI in accordance with business associate agreements.
- Develop APIs with mechanisms for conducting an accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability of ePHI.
- Develop APIs that facilitate patients' rights to request privacy protections, access PHI, amend their PHI, and receive an accounting of disclosures.
- Develop APIs for handling complaints concerning the entity’s privacy policies and procedures.
- Develop APIs with encryption for ePHI transmitted based on the risk assessment.
- Develop APIs with audit controls to record and examine activity in information systems that contain or use ePHI.

---

### ISO 22301 Security and Resilience / Business Continuity

> https://www.iso.org/standard/75106.html

### Business Continuity Management

- **Policy Establishment** — Organizations MUST establish a business continuity policy that specifies the approach to managing business continuity in relation to APIs. [ISO 22301:2019, Clause 5]
- **Business Impact Analysis** — Organizations SHOULD conduct a business impact analysis to determine the importance, recovery priorities, and objectives for APIs. [ISO 22301:2019, Clause 8.2]
- **Risk Assessment** — Organizations MUST assess risks related to API disruptions, including the potential impacts on business operations and data integrity. [ISO 22301:2019, Clause 8.3]
- **Business Continuity Strategies** — Organizations SHOULD develop strategies that address the identified risks and impacts of API disruptions, including alternative solutions and recovery options. [ISO 22301:2019, Clause 8.4]
- **Incident Response** — Organizations MUST establish incident response plans that specifically include procedures for responding to API-related incidents, ensuring minimal service interruption. [ISO 22301:2019, Clause 8.4]
- **Recovery Plans** — Organizations MUST implement recovery plans that focus on restoring APIs to an operational state after a disruption. [ISO 22301:2019, Clause 8.5]
- **Training and Awareness** — Organizations MUST conduct regular training and awareness activities to ensure personnel are familiar with their roles and responsibilities regarding API continuity. [ISO 22301:2019, Clause 7.3]
- **Exercises and Testing** — Organizations SHOULD regularly test and exercise their API recovery procedures to ensure they are effective and that personnel are prepared. [ISO 22301:2019, Clause 9.1]
- **Continuous Improvement** — Organizations MUST review and continually improve their API business continuity management system based on operational feedback and changing conditions. [ISO 22301:2019, Clause 10.2]

### ISO/IEC 27001 Information Security, Cybersecurity and Privacy Protection

> https://www.iso.org/standard/27001

### Information Security Management System (ISMS)

- **ISMS Establishment** — Organizations MUST establish, implement, maintain, and continually improve an information security management system focused on API management and security. [ISO/IEC 27001:2013, Clause 4.1]
- **Leadership Commitment** — Top management SHOULD demonstrate leadership and commitment with respect to the ISMS, ensuring that the policies and objectives specifically address the security of APIs. [ISO/IEC 27001:2013, Clause 5.1]
- **Policy Development** — Organizations MUST develop information security policies that clearly define expectations for API security, including access controls, data handling, and incident response. [ISO/IEC 27001:2013, Clause 5.2]
- **Organizational Roles and Responsibilities** — Organizations MUST assign roles and responsibilities for API security management, ensuring that each role involved in API development and maintenance understands their security obligations. [ISO/IEC 27001:2013, Clause 5.3]
- **Risk Assessment** — Organizations MUST conduct risk assessments that specifically include API assets, considering both internal and external threats to API security. [ISO/IEC 27001:2013, Clause 6.1.2]
- **Risk Mitigation** — Organizations MUST treat risks identified in the API ecosystem, opting for mitigation, avoidance, acceptance, or transfer strategies based on the severity and potential impact of the risk. [ISO/IEC 27001:2013, Clause 6.1.3]
- **Security Objectives** — Organizations MUST establish specific, measurable security objectives for APIs, ensuring alignment with the broader ISMS goals. [ISO/IEC 27001:2013, Clause 6.2]
- **Resource Management** — Organizations MUST determine and provide the resources needed to maintain API security, including technological, human, and financial resources. [ISO/IEC 27001:2013, Clause 7.1]
- **Competence** — Organizations MUST ensure that all persons involved in API management and security have the necessary competence, offering training and awareness sessions as needed. [ISO/IEC 27001:2013, Clause 7.2]
- **Awareness** — Organizations MUST conduct awareness programs to raise and maintain awareness about API security policies and the importance of information security. [ISO/IEC 27001:2013, Clause 7.3]
- **Communication** — Organizations MUST establish internal and external communication protocols related to the security of APIs, including the types of information to be communicated and who should receive it. [ISO/IEC 27001:2013, Clause 7.4]
- **Documented Information** — Organizations MUST maintain documented information required by the ISMS and by this ISO standard, ensuring that documents related to API security are current and accessible. [ISO/IEC 27001:2013, Clause 7.5]
- **Operational Planning and Control** — Organizations MUST plan, implement, and control the processes needed to meet API security requirements, ensuring that these processes are evaluated and adjusted in light of operational feedback. [ISO/IEC 27001:2013, Clause 8]
- **Performance Evaluation** — Organizations MUST monitor, measure, analyze, and evaluate the security performance of APIs, adapting security practices based on this evaluation. [ISO/IEC 27001:2013, Clause 9]
- **Internal Audit** — Organizations MUST conduct internal audits at planned intervals to ensure the ISMS is effectively managing API security according to organizational and ISO standards. [ISO/IEC 27001:2013, Clause 9.2]
- **Management Review** — Top management MUST review the organization’s API security practices and ISMS at planned intervals to ensure its continuing suitability, adequacy, and effectiveness. [ISO/IEC 27001:2013, Clause 9.3]
- **Improvement** — Organizations MUST continually improve the effectiveness of the ISMS through the API security lifecycle, using the results of audits, reviews, and corrected non-conformities. [ISO/IEC 27001:2013, Clause 10]

### ISO/IEC 27017 Security Techniques for Cloud Services

> https://www.iso.org/standard/43757.html

### Cloud Service Customer Policies

- **Cloud API Security Policies** — Organizations SHOULD define and maintain policies for the security of APIs used within cloud services, addressing authentication, access control, and encryption. [ISO/IEC 27017, Clause 5.1.1]
- **API Access Control** — Organizations MUST implement robust access control measures for APIs, ensuring that access is restricted based on roles and responsibilities. [ISO/IEC 27017, Clause 6.9]

### User Identity and Authentication Management

- **API Authentication** — Cloud service providers MUST establish strong identity and authentication management systems for APIs, requiring secure authentication mechanisms like OAuth, OpenID Connect, or equivalent. [ISO/IEC 27017, Clause 6.6]

### Asset Management

- **Cloud API Asset Management** — Organizations SHOULD maintain an inventory of cloud API assets and define responsibilities for managing these assets, including their security configurations and associated data. [ISO/IEC 27017, Clause 8.1]

### Network Security

- **API Network Security** — Cloud service providers MUST implement network security controls to protect API communication channels, using secure transmission protocols and encryption to safeguard data in transit. [ISO/IEC 27017, Clause 10.1]
- **API Security Monitoring** — Organizations MUST monitor network traffic for APIs to detect potential security threats and unauthorized access attempts. [ISO/IEC 27017, Clause 10.2]

### Incident Response

- **API Incident Response** — Cloud service providers MUST develop and implement an incident response plan that specifically includes APIs, detailing procedures for responding to security incidents affecting APIs. [ISO/IEC 27017, Clause 12.1]

### Segregation in Virtual Computing Environments

- **API Segregation** — Cloud service providers MUST implement segregation controls in virtual computing environments to protect API data and functionality from unauthorized access and interference. [ISO/IEC 27017, Clause 7.2]

### Cryptographic Controls

- **API Data Encryption** — Use of cryptographic controls SHOULD be applied to protect API data in transit and at rest, focusing on strong key management practices. [ISO/IEC 27017, Clause 9.2]

### Compliance

- **API Compliance Audit** — Organizations MUST regularly review compliance with legal, regulatory, and contractual requirements related to APIs within the cloud environment. [ISO/IEC 27017, Clause 17.1]

## ISO/IEC 27018 Security Techniques for PII in Public Cloud

> https://www.iso.org/standard/76559.html

### Consent for PII Processing

- **API Consent Management** — Cloud service providers MUST obtain explicit consent from data subjects before processing PII through APIs in public clouds, ensuring transparency and user control. [ISO/IEC 27018, Clause 5.2.1]

### PII Protection

- **API PII Security Measures** — Organizations MUST implement technical and organizational measures to protect PII accessed or processed through APIs against unauthorized or unlawful processing and against accidental loss, destruction, or damage. [ISO/IEC 27018, Clause 5.3.1]

### Data Minimization

- **API Data Minimization** — Cloud service providers SHOULD ensure that APIs collect and process only the minimum necessary PII required for the completion of their duties, reflecting data minimization principles. [ISO/IEC 27018, Clause 5.4.1]

### Transparency

- **API Transparency in PII Processing** — Organizations MUST provide clear information about the processing of PII through APIs, including types of data processed, processing purposes, and the rights of data subjects. [ISO/IEC 27018, Clause 5.5.1]

### PII Disclosure

- **API Data Disclosure Control** — Cloud service providers MUST ensure that APIs do not disclose PII to third parties without the explicit consent of the data subject, unless required by law. [ISO/IEC 27018, Clause 5.6.1]

### Data Subject Rights

- **API Data Subject Rights** — Organizations MUST ensure that APIs provide mechanisms for data subjects to exercise their rights regarding their PII, such as access, correction, and deletion through appropriate API functionalities. [ISO/IEC 27018, Clause 5.7.1]

### PII Breach Notification

- **API Breach Notification** — In the event of a PII breach involving APIs, cloud service providers MUST notify relevant stakeholders, including data subjects and regulatory bodies, in a timely manner. [ISO/IEC 27018, Clause 5.8.1]

### Data Retention and Deletion

- **API Data Retention Policies** — Organizations MUST define and implement API-specific policies for the retention and deletion of PII, ensuring that data is not kept longer than necessary and is deleted securely. [ISO/IEC 27018, Clause 5.9.1]

### Accountability

- **API Accountability Measures** — Cloud service providers SHOULD implement governance measures that demonstrate compliance with privacy policies and legal requirements related to API management of PII. [ISO/IEC 27018, Clause 5.10.1]

### Data Encryption

- **API Data Encryption** — PII transmitted over public networks via APIs MUST be encrypted, and encryption should also be considered for PII stored by APIs within cloud services. [ISO/IEC 27018, Clause 5.11.1]

### International Data Transfers

- **API International Data Transfer Compliance** — Organizations MUST ensure that international transfers of PII via APIs comply with applicable legal and regulatory requirements, providing appropriate safeguards. [ISO/IEC 27018, Clause 5.12.1]

## ISO/IEC 27032 Guidelines for Internet Security

> https://www.iso.org/standard/76070.html

### Collaboration Mechanisms

- **API Security Collaboration** — Organizations SHOULD implement collaboration mechanisms to enable effective communication and cooperation among stakeholders in API ecosystems. [ISO/IEC 27032, Clause 6.2.1]

### Security Measures

- **API Security Implementation** — Organizations MUST implement appropriate security measures to protect APIs against identified risks, ensuring the confidentiality, integrity, and availability of data transmitted via APIs. [ISO/IEC 27032, Clause 6.3.1]

### Incident Management

- **API Incident Response** — Organizations MUST develop and maintain an incident management process specifically for API-related security incidents to detect, report, and respond effectively. [ISO/IEC 27032, Clause 6.4.1]

### User Awareness and Training

- **API Security Training** — Organizations MUST provide ongoing awareness and training programs about API security risks and safe online behaviors for developers and users of APIs. [ISO/IEC 27032, Clause 6.5.1]

### Cybersecurity Policies

- **API-Specific Security Policies** — Organizations MUST develop and enforce cybersecurity policies that address API-specific risks and comply with legal and regulatory requirements. [ISO/IEC 27032, Clause 6.6.1]

### Information Sharing

- **API Information Sharing** — Organizations SHOULD engage in information sharing platforms to exchange knowledge about threats, vulnerabilities, and incidents specifically related to APIs with other entities. [ISO/IEC 27032, Clause 6.7.1]

### Monitoring and Analysis

- **API Monitoring Systems** — Organizations MUST implement monitoring systems specifically for APIs to detect unusual activities and potential threats on the internet. [ISO/IEC 27032, Clause 6.8.1]

### Authentication and Access Control

- **API Access Control** — Organizations MUST use robust authentication methods and enforce strict access control measures to restrict unauthorized access to APIs. [ISO/IEC 27032, Clause 6.9.1]

### Encryption and Data Protection

- **API Encryption Technologies** — Organizations SHOULD employ encryption technologies to secure sensitive data transmitted over the internet via APIs. [ISO/IEC 27032, Clause 6.10.1]

### Emergency and Continuity Planning

- **API Continuity Planning** — Organizations MUST develop and test emergency response and business continuity plans that address potential internet security incidents affecting APIs. [ISO/IEC 27032, Clause 6.11.1]

### Cyber Resilience

- **API Cyber Resilience** — Organizations SHOULD build cyber resilience capabilities to withstand and recover from internet security breaches that impact APIs. [ISO/IEC 27032, Clause 6.12.1]

## ISO/IEC 27035 Information Security Incident Management

> https://www.iso.org/standard/78974.html

### Incident Management Policy

- **API-Specific Incident Policies** — Organizations MUST establish and maintain an information security incident management policy that includes specific provisions and procedures for handling incidents involving APIs. [ISO/IEC 27035, Clause 5.1.1]

### Planning and Preparation

- **API Incident Response Preparedness** — Organizations SHALL prepare for API-related incidents by setting up appropriate communication tools, securing forensic tools specific to APIs, and establishing secure storage for API incident data. [ISO/IEC 27035, Clause 5.2.1]

### Reporting Security Events

- **API Incident Reporting** — Organizations MUST establish mechanisms for personnel to report API-related security events promptly to the Incident Response Team. [ISO/IEC 27035, Clause 5.3.1]

### Assessment of Events

- **API Security Event Assessment** — Organizations SHALL assess reported API security events to determine if they qualify as security incidents specific to API operations. [ISO/IEC 27035, Clause 5.4.1]

### Response to Incidents

- **API-Specific Incident Response** — Organizations MUST respond to confirmed API security incidents according to predefined procedures that are tailored to the unique aspects of API security. [ISO/IEC 27035, Clause 5.5.1]

### Learning from Incidents

- **API Incident Learning** — Organizations SHALL conduct post-incident reviews to learn from API security incidents and find opportunities for improvement in API-specific security measures. [ISO/IEC 27035, Clause 5.6.1]

### Quantitative and Qualitative Incident Assessment

- **API Incident Impact Assessment** — Organizations SHALL assess API-related incidents quantitatively and qualitatively to understand the impact and apply appropriate resources for API-specific scenarios. [ISO/IEC 27035, Clause 5.7.1]

### Incident Classification

- **API Incident Categorization** — Organizations MUST classify API-related incidents according to predefined categories to prioritize response and resource allocation specific to API impacts. [ISO/IEC 27035, Clause 5.8.1]

### Incident Response Testing

- **API Incident Response Drills** — Organizations SHALL test their API incident response capabilities periodically to ensure preparedness and effectiveness specific to API-related security issues. [ISO/IEC 27035, Clause 5.9.1]

### Communication

- **API Incident Communication** — During and after API-related incidents, organizations MUST manage communication with internal and external stakeholders, including regulatory authorities if required, tailored to the specific nature of API incidents. [ISO/IEC 27035, Clause 5.10.1]

### Documentation

- **API Incident Documentation** — Organizations MUST document all detected API incidents, their handling process, and outcomes to support continuous improvement and compliance requirements specific to APIs. [ISO/IEC 27035, Clause 5.11.1]

### Continual Improvement

- **API Security Process Improvement** — Organizations SHALL continually improve incident response and management processes based on the learnings and outcomes of API-related incidents. [ISO/IEC 27035, Clause 5.12.1]

## ISO/IEC 27701 Security Techniques for Privacy Information Management

> https://www.iso.org/standard/71670.html

### Privacy Information Management System (PIMS)

- **API PIMS Integration** — Organizations MUST establish, implement, maintain, and continuously improve a Privacy Information Management System (PIMS) integrated with or as an extension of their ISMS, specifically addressing API data handling practices. [ISO/IEC 27701, Clause 5.3]

### Data Processing Roles

- **API Data Roles** — Organizations MUST clearly define and document roles and responsibilities related to API data processing activities to ensure compliance with privacy regulations. [ISO/IEC 27701, Clause 5.5]

### Privacy Risk Assessment

- **API Privacy Risk** — Organizations MUST conduct regular privacy risk assessments focused on API operations to identify, analyze, and evaluate risks associated with the processing of personal information via APIs. [ISO/IEC 27701, Clause 5.6]

### Privacy Controls

- **API-Specific Privacy Controls** — Organizations MUST implement appropriate privacy controls for APIs to mitigate identified risks and protect personal information in accordance with applicable privacy laws and regulations. [ISO/IEC 27701, Clause 5.8]

### Third-Party Management

- **API Third-Party Data Handling** — Organizations MUST ensure that third-party service providers handling API transactions comply with relevant privacy requirements and contractual obligations. [ISO/IEC 27701, Clause 5.10]

### Data Subject Rights

- **API Data Subject Access** — Organizations MUST establish processes to respect and facilitate the exercise of data subject rights regarding personal data handled by APIs, such as access, rectification, erasure, and data portability. [ISO/IEC 27701, Clause 5.12]

### Privacy Impact Assessments

- **API Privacy Assessments** — Organizations SHOULD conduct Privacy Impact Assessments (PIAs) for new and significantly altered APIs that handle personal information. [ISO/IEC 27701, Clause 5.15]

### Consent Management

- **API Consent Handling** — Organizations MUST implement mechanisms to obtain, manage, and document consent from individuals for the processing of their personal information via APIs, where required by law. [ISO/IEC 27701, Clause 5.18]

### Documentation and Record-Keeping

- **API Privacy Documentation** — Organizations MUST maintain comprehensive documentation and records of their PIMS and API privacy practices to demonstrate compliance with applicable privacy laws. [ISO/IEC 27701, Clause 5.19]

### Training and Awareness

- **API Privacy Training** — Organizations MUST provide regular privacy training and awareness programs focused on API-specific privacy issues to ensure that employees understand their privacy obligations related to API management. [ISO/IEC 27701, Clause 5.22]

### Breach Notification

- **API Breach Procedures** — Organizations MUST establish and follow procedures for managing data breaches involving APIs, including mechanisms for assessing the severity of breaches and notifying affected data subjects and regulatory authorities in accordance with legal requirements. [ISO/IEC 27701, Clause 5.23]

### Privacy by Design and Default

- **API Privacy by Design** — Organizations MUST apply the principles of privacy by design and default at all stages of API product or service development to ensure privacy is embedded within their API processes. [ISO/IEC 27701, Clause 5.25]

### International Data Transfers

- **API Data Transfer Controls** — Organizations MUST implement measures to ensure that international transfers of personal information via APIs comply with applicable legal and regulatory requirements, providing appropriate safeguards. [ISO/IEC 27701, Clause 5.28]

### Continuous Improvement

- **API Privacy Improvement** — Organizations MUST regularly review and update their PIMS to adapt to changes in API technologies, legal requirements, and privacy practices. [ISO/IEC 27701, Clause 5.30]

### Privacy Culture

- **API Privacy Culture** — Organizations SHOULD foster a culture of privacy and security within the organization to enhance compliance and alignment with privacy policies and API operations. [ISO/IEC 27701, Clause 5.32]

## ISO/IEC 29100 Information Technology Privacy Framework

> https://www.iso.org/standard/85938.html

### Privacy Principles Adoption

- **API-Specific Privacy Principles** — Organizations MUST adopt and adhere to the privacy principles outlined in ISO/IEC 29100 that are specifically applicable to APIs, ensuring the protection of personal data processed through APIs. [ISO/IEC 29100, Clause 5.1]

### Data Minimization

- **API Data Minimization** — Organizations SHALL ensure that only the minimum necessary personal data is collected, used, and retained through APIs. [ISO/IEC 29100, Clause 5.2]

### Consent Management

- **API Consent** — Organizations MUST obtain clear and explicit consent from individuals for the collection, use, and disclosure of their personal data via APIs, except where other lawful bases exist. [ISO/IEC 29100, Clause 5.3]

### Transparency

- **API Transparency** — Organizations MUST provide clear, concise, and accessible information about their API data processing activities and privacy practices. [ISO/IEC 29100, Clause 5.4]

### Accountability

- **API Accountability** — Organizations SHALL implement governance measures that demonstrate compliance with privacy policies and procedures in API operations. [ISO/IEC 29100, Clause 5.5]

### Privacy by Design and by Default

- **Privacy-Integrated API Design** — Organizations MUST integrate privacy into the design and operation of IT systems, networked infrastructure, and business practices that involve APIs. [ISO/IEC 29100, Clause 5.6]

### Access and Correction Rights

- **API Access and Correction** — Individuals ALWAYS have the right to access their personal data processed via APIs and request corrections or deletions where applicable. [ISO/IEC 29100, Clause 5.7]

### Privacy Impact Assessments

- **API-Specific PIAs** — Organizations SHALL conduct Privacy Impact Assessments (PIAs) when implementing new technologies or API data processing activities that might impact individual privacy. [ISO/IEC 29100, Clause 5.8]

### Third-Party Data Sharing

- **API Data Sharing** — Organizations MUST ensure that third parties processing personal data via APIs on their behalf adhere to the same privacy requirements as the primary organization. [ISO/IEC 29100, Clause 5.9]

### Breach Notification

- **API Breach Notification** — Organizations MUST notify relevant stakeholders, including affected individuals and regulators, of breaches involving personal data processed via APIs in a timely manner. [ISO/IEC 29100, Clause 5.10]

### Data Quality

- **API Data Quality** — Organizations SHALL maintain accurate, complete, and relevant personal data for the purposes for which it is processed via APIs. [ISO/IEC 29100, Clause 5.11]

### Security of Processing

- **API Security Measures** — Organizations MUST implement appropriate technical and organizational measures to ensure the security of personal data processed through APIs. [ISO/IEC 29100, Clause 5.12]

### Privacy Training

- **API Privacy Training** — Organizations MUST provide training on privacy policies and procedures to employees who have access to personal data processed via APIs. [ISO/IEC 29100, Clause 5.13]

## NIST CSF (Cyber Security Framework)

> https://www.nist.gov/cyberframework

### Identify Function

- **API-specific asset identification** — Organizations MUST catalog and manage data, personnel, devices, systems, and facilities that support API operations, treating APIs as unique assets within the IT environment. (Identify Function, NIST CSF)

### Protect Function

- **API access control** — Organizations MUST implement access control mechanisms to ensure only authorized individuals can interact with APIs. (Protect Function: Access Control, NIST CSF)
- **API encryption requirements** — Organizations SHOULD encrypt data transmitted through APIs to protect the integrity and confidentiality of data. (Protect Function: Data Security, NIST CSF)

### Detect Function

- **API anomaly detection** — Organizations MUST implement continuous monitoring mechanisms to detect unauthorized API access or anomalies in API usage. (Detect Function, NIST CSF)

### Respond Function

- **API-specific incident response** — Organizations MUST develop and implement an incident response plan that includes specific procedures for API-related incidents to manage and mitigate security events affecting API infrastructure. (Respond Function, NIST CSF)

### Recover Function

- **API resilience and recovery** — Organizations MUST establish plans to maintain resilience and quickly restore API functionality following a cybersecurity event. (Recover Function, NIST CSF)

## NIST Digital Identity Guidelines (SP 800-63*)

> https://pages.nist.gov/800-63-3/

### Identity Proofing

- **API client identity validation** — Organizations MUST conduct identity proofing to establish the validity of identities interacting with APIs, ensuring the uniqueness and validity of an individual’s identity for API transactions. This requirement is detailed in the context of enrollment and identity proofing. (SP 800-63A, Section 4: Enrollment and Identity Proofing)

### Authentication

- **API authentication mechanisms** — Organizations SHALL implement strong authentication mechanisms for API access, which may include multi-factor authentication to secure API endpoints. This involves the management of authenticators and session management in API interactions. (SP 800-63B, Section 4: Authentication and Lifecycle Management)

### Credential Management

- **Secure API credential management** — Organizations SHALL manage API credentials securely, ensuring that credentials are stored and transmitted securely to prevent unauthorized access. This includes considerations for cryptographic module use. (SP 800-63B, Section 5: Authenticator and Verifier Requirements)
- **API credential revocation** — Organizations SHALL provide a mechanism to revoke API credentials when they are compromised or no longer needed. This is part of lifecycle management of authenticators. (SP 800-63B, Section 6: Lifecycle Management)

### Federated Identity

- **Federated API access** — Organizations MAY use federated identity systems for APIs to enable the portability of identity information across different systems, reducing the need for multiple credentials. This covers the use of assertions in federated identity systems. (SP 800-63C, Section 5: Assertions)

### Privacy Considerations

- **API privacy protections** — Organizations MUST implement privacy-enhancing technologies to protect personal information accessed or transmitted through APIs, adhering to privacy laws and guidelines. This includes managing PII confidentiality in federated systems. (SP 800-63C, Section 6: Privacy Considerations)

## NIST SP 800-34 (Contingency Planning Guide for Federal Information Systems)

> https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final

### Contingency Policy

- **API-Specific Contingency Policies** — Organizations MUST develop a formal, documented contingency policy that addresses API-specific scenarios, including the purpose, scope, roles, responsibilities, management commitment, and coordination among organizational entities involved in API management. [NIST SP 800-34, Sec. 5.1]

### Contingency Planning

- **API Contingency Planning** — Organizations SHALL develop a comprehensive contingency plan for APIs that includes identification of critical API components, emergency response, backup procedures, and recovery steps. [NIST SP 800-34, Sec. 5.2]

### Training and Testing

- **API Contingency Training and Testing** — Organizations SHALL train personnel in their roles and responsibilities concerning API contingency plans and conduct tests and exercises to validate the effectiveness of the plan specifically for API operations. [NIST SP 800-34, Sec. 5.3]

### Data Backup

- **API Data Backup** — Organizations MUST regularly backup API data to ensure that it can be effectively recovered in the event of a disruption, detailing what data to backup, backup frequency, and storage location. [NIST SP 800-34, Sec. 5.4]

### Disaster Recovery

- **API Disaster Recovery** — Organizations SHALL establish a disaster recovery capability specific to APIs, outlining procedures for restoring API functionality and data after a disaster. [NIST SP 800-34, Sec. 5.5]

### Cyber Incident Response

- **API Cyber Incident Response** — Organizations MUST include API-specific procedures in the cyber incident response plan that outline steps to address attacks or failures affecting API operations. [NIST SP 800-34, Sec. 5.6]

### Alternative Processing Sites

- **API Alternative Processing** — Organizations MUST identify alternative processing sites that can support API operations in the event of a primary site failure, including details on the capabilities of alternative sites and the process for switching operations to these sites. [NIST SP 800-34, Sec. 5.7]

### Reconstitution Procedures

- **API Reconstitution** — Organizations SHALL develop procedures to restore API systems to normal operations after resolving an incident, including detailed steps for reconstitution. [NIST SP 800-34, Sec. 5.8]

## NIST SP 800-40 (Enterprise Patch Management)

> https://csrc.nist.gov/pubs/sp/800/40/r4/final

### Patch Management Policy

- **API Patch Management Policy** — Organizations MUST develop a formal, documented patch management policy that addresses the scope, roles, responsibilities, and management commitment to patching operations specific to APIs. [NIST SP 800-40, Sec. 3.1]

### Patch Management Process

- **API Vulnerability Identification** — Organizations MUST regularly identify vulnerabilities in APIs that require patching. [NIST SP 800-40, Sec. 3.2]
- **API Patch Assessment** — Before deployment, organizations SHALL assess patches for APIs to determine their applicability and potential impact on API stability and security. [NIST SP 800-40, Sec. 3.3]
- **API Patch Acquisition and Testing** — Organizations MUST acquire patches from reputable sources and test them in a non-production environment specific to API configurations. [NIST SP 800-40, Sec. 3.4]
- **API Patch Deployment** — Organizations MUST deploy patches to API environments in a timely manner, following successful testing and evaluation. [NIST SP 800-40, Sec. 3.5]
- **API Patch Verification and Reporting** — After deployment, organizations SHALL verify that patches have been applied correctly to APIs and generate reports for compliance and auditing purposes. [NIST SP 800-40, Sec. 3.6]

### Training and Awareness

- **API Patch Management Training** — Organizations MUST train IT staff and users about the importance of patch management for APIs and the specific procedures involved in the API patch management process. [NIST SP 800-40, Sec. 3.7]

### Patch Prioritization

- **API Patch Prioritization** — Organizations SHALL prioritize patches based on the severity of the vulnerabilities they address and the criticality of the affected API systems. [NIST SP 800-40, Sec. 3.8]

### Configuration Management Integration

- **API Configuration Management** — Organizations MUST integrate patch management processes with API configuration management to ensure consistency and prevent configuration drift. [NIST SP 800-40, Sec. 3.9]

### Automated Patch Management Tools

- **API Automated Patch Management** — Organizations SHOULD implement automated tools to streamline the patch management process for APIs, including detection, deployment, and verification. [NIST SP 800-40, Sec. 3.10]

### Continuous Improvement

- **API Patch Process Improvement** — Organizations MUST regularly review and refine their patch management processes to adapt to new vulnerabilities and changes in the API technology landscape. [NIST SP 800-40, Sec. 3.11]

## NIST SP 800-41 (Guidelines of Firewalls and Firewall Policy)

> https://csrc.nist.gov/pubs/sp/800/41/r1/final

### Firewall Policy Development

- **API Firewall Policy** — Organizations MUST develop a comprehensive firewall policy that outlines the management of firewall configurations, responsibilities, and procedures specific to API traffic. [NIST SP 800-41, Sec. 3.1]

### Firewall Configuration

- **API Traffic Configuration** — Organizations SHALL configure firewalls to effectively control API traffic in accordance with security policies, including specific rules for API endpoints. [NIST SP 800-41, Sec. 3.2]

### Network Architecture Design

- **API Protection Architecture** — Organizations MUST design network architectures that include firewall placement to specifically protect API endpoints and segregate them from other network traffic. [NIST SP 800-41, Sec. 3.3]

### Firewall Management

- **API-Specific Access Control** — Organizations MUST implement management practices to maintain firewall operations and security with a focus on controlling access to API endpoints. [NIST SP 800-41, Sec. 3.4]

### Firewall Monitoring and Logging

- **API Traffic Monitoring** — Organizations SHALL monitor and log firewall activity related to API traffic to detect and respond to security incidents impacting API services. [NIST SP 800-41, Sec. 3.5]
- **Real-Time API Alerts** — Organizations MUST configure firewalls to generate real-time alerts for suspicious API activities. [NIST SP 800-41, Sec. 3.5]

### Firewall Testing and Audits

- **API Firewall Audits** — Organizations MUST conduct regular testing and audits of firewall configurations and policies to ensure they effectively protect API endpoints against known and emerging threats. [NIST SP 800-41, Sec. 3.6]

### Firewall Maintenance

- **API Firewall Maintenance** — Organizations MUST implement procedures for regular updates and patches to firewall systems that specifically address vulnerabilities affecting API security. [NIST SP 800-41, Sec. 3.7]

### Firewall Training

- **API Security Training** — Organizations MUST provide training for personnel responsible for firewall management, including security practices and response procedures specific to API protection. [NIST SP 800-41, Sec. 3.8]

### Incident Response

- **API Incident Response Integration** — Organizations SHALL develop and implement an incident response plan that includes procedures for addressing security incidents affecting firewall operations related to APIs. [NIST SP 800-41, Sec. 3.9]

## NIST SP 800-53 (Security and Privacy Controls)

> https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final

### Access Control

- **API Authentication and Authorization** — Organizations MUST implement controls to manage access to API endpoints, ensuring that authentication and authorization mechanisms are robust and tailored to API-specific security requirements. [NIST SP 800-53, AC-2]

### Audit and Accountability

- **API Audit Logging** — Organizations SHALL create, protect, and retain audit logs specifically for API interactions to enable monitoring, analysis, investigation, and reporting of unauthorized or unexpected API activities. [NIST SP 800-53, AU-2]

### Configuration Management

- **API Configuration Settings** — Organizations SHALL establish and enforce security configuration settings for APIs and associated software and infrastructure, ensuring configurations are secure and consistent. [NIST SP 800-53, CM-2]

### Incident Response

- **API Incident Handling** — Organizations MUST develop an incident response capability for APIs that includes preparation, detection, analysis, containment, recovery, and user response activities, specifically focusing on API vulnerabilities. [NIST SP 800-53, IR-4]

### Identity and Authentication

- **API Identity Management** — Organizations SHALL manage and authenticate identities to ensure that authorized API users and processes are properly identified to information systems. [NIST SP 800-53, IA-2]

### System and Communications Protection

- **API Protection** — Organizations MUST implement controls to protect API communications across networks, ensuring integrity and confidentiality of API data in transit. [NIST SP 800-53, SC-7]

### System and Information Integrity

- **API Integrity Monitoring** — Organizations MUST identify, report, and correct information and API system flaws in a timely manner; provide protection from malicious code at appropriate locations within API infrastructure; and monitor security alerts and advisories that may affect APIs. [NIST SP 800-53, SI-1]

### Privacy Control Catalog

- **API Data Privacy** — Organizations SHALL integrate a catalog of privacy controls to specifically address privacy risks associated with APIs, incorporating protections for personally identifiable information (PII) processed through APIs. [NIST SP 800-53, Appendix J]

## NIST SP 800-61 (Computer Security Incident Handling Guide)

> https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

### Incident Response Policy

- **API Incident Response Policy** — Organizations MUST develop and maintain an incident response policy that specifically includes API-related incidents, detailing roles, responsibilities, and procedures. [NIST SP 800-61, Sec. 2.3]

### Incident Response Plan

- **API Incident Handling Procedures** — Organizations SHALL create a formal, documented incident response plan that includes specific guidelines for handling API security incidents. [NIST SP 800-61, Sec. 2.4]

### Incident Response Team

- **API-focused IRT** — Organizations MUST establish an incident response team (IRT) responsible for executing the incident response plan for API-related issues, ensuring members are trained in API-specific security concerns. [NIST SP 800-61, Sec. 2.4.2]

### Preparation

- **API Security Tools** — Organizations MUST prepare for API incident handling by setting up appropriate API security tools and establishing secure storage for incident data. [NIST SP 800-61, Sec. 3.2.1]

### Detection and Analysis

- **API Monitoring** — Organizations SHALL implement mechanisms for detecting and analyzing incidents specifically in the API environment, including monitoring for signs of API misuse or compromise. [NIST SP 800-61, Sec. 3.2.3]

### Containment, Eradication, and Recovery

- **API-specific Containment Strategies** — Organizations MUST develop strategies for containing API-related incidents to prevent further API system damage, followed by eradication and recovery procedures tailored to API architectures. [NIST SP 800-61, Sec. 3.3.8]

### Post-Incident Activity

- **API Incident Review** — Organizations SHALL conduct a post-incident review focused on API incidents to identify lessons learned and to develop strategies for improving API security and incident response capabilities. [NIST SP 800-61, Sec. 3.4.3]

### Continuous Improvement

- **API Incident Response Improvement** — Organizations MUST regularly update and test the API incident response plan to adapt to new threats and incorporate new security technologies and API updates. [NIST SP 800-61, Sec. 3.4.4]

## NIST SP 800-92 (Guide to Computer Security Log Management)

> https://csrc.nist.gov/pubs/sp/800/92/final

### Log Management Policy

- **API Log Management** — Organizations MUST develop and implement a log management policy that includes specific provisions for API logs, detailing the scope, roles, responsibilities, and management commitment to API log management. [NIST SP 800-92, Sec. 2.1]

### Log Generation

- **API-specific Logging** — Organizations SHALL configure API systems to generate logs for all security-relevant events related to API usage, ensuring logs capture sufficient detail to reconstruct API-related events. [NIST SP 800-92, Sec. 2.2]

### Log Collection

- **Secure API Log Collection** — Organizations MUST establish mechanisms to securely collect logs from API systems, ensuring data integrity and confidentiality during transmission. [NIST SP 800-92, Sec. 3.2]

### Log Aggregation

- **API Log Aggregation** — Organizations SHOULD implement log aggregation solutions that specifically include API logs to centralize the management and facilitate more effective analysis. [NIST SP 800-92, Sec. 3.4]

### Log Analysis

- **API Log Analysis** — Organizations SHALL perform regular analysis of API logs to identify indications of unauthorized or malicious API activity and to support the investigation of security incidents involving APIs. [NIST SP 800-92, Sec. 4.1]

### Log Storage

- **Secure API Log Storage** — Organizations MUST ensure secure and efficient storage of API log data to protect it from unauthorized access or modification, adhering to organizational and regulatory requirements for log retention. [NIST SP 800-92, Sec. 5.1]

### Log Monitoring

- **Real-time API Monitoring** — Organizations SHOULD implement real-time monitoring capabilities to analyze API logs and alert on anomalies or potential security incidents involving APIs. [NIST SP 800-92, Sec. 4.3]

### Incident Response Integration

- **Logs in API Incident Response** — Organizations SHALL integrate log management into their API incident response framework, utilizing API log data to detect, analyze, and respond to incidents. [NIST SP 800-92, Sec. 6.2]

### Audit and Accountability

- **API Log Auditing** — Organizations MUST regularly audit API log management processes and API log data to ensure compliance with policies and effectiveness of controls. [NIST SP 800-92, Sec. 6.3]

### Training and Awareness

- **API Log Management Training** — Organizations SHOULD provide training on API log management to relevant personnel to ensure they understand the importance, capabilities, and best practices for managing API logs. [NIST SP 800-92, Sec. 6.4]

## NIST SP 800-94 (Guide to Intrusion Detection and Preventions Systems (IDPS))

> https://csrc.nist.gov/pubs/sp/800/94/final

### IDPS Selection

- **API-aware IDPS** — Organizations MUST carefully select IDPS technologies that are capable of monitoring and protecting API traffic, aligning with their specific API security needs and network architecture. [NIST SP 800-94, Sec. 2.2]

### IDPS Deployment

- **API Traffic Monitoring** — Organizations SHALL deploy IDPS solutions strategically within their network to specifically monitor API traffic to and from all critical API components. [NIST SP 800-94, Sec. 3.1]

### Configuration and Customization

- **API-specific Configuration** — Organizations MUST configure and customize the IDPS to effectively identify and respond to threats specific to the API environment, including setting rules and signatures for common API attacks. [NIST SP 800-94, Sec. 3.4]

### Integration with Other Security Tools

- **API Security Integration** — Organizations SHOULD integrate IDPS with other API management and security tools (e.g., API gateways) for comprehensive API protection. [NIST SP 800-94, Sec. 3.6]

### Regular Updates

- **Update IDPS for API Threats** — Organizations MUST keep the IDPS software and signatures up to date to address new API-specific vulnerabilities and attack methods. [NIST SP 800-94, Sec. 4.3]

### Monitoring and Analysis

- **API Alerts Monitoring** — Organizations SHALL continuously monitor IDPS alerts related to API traffic and analyze detections for signs of potential API security incidents. [NIST SP 800-94, Sec. 4.4]

### IDPS Maintenance

- **Maintain IDPS for APIs** — Organizations MUST perform regular maintenance on the IDPS to ensure it continues to operate effectively and securely, particularly in monitoring and protecting APIs. [NIST SP 800-94, Sec. 4.5]

### Training and Awareness

- **API Security Training for IDPS** — Organizations MUST provide training for staff responsible for managing and responding to the IDPS to ensure they understand how to use the system effectively for API security. [NIST SP 800-94, Sec. 5.1]

### Documentation and Reporting

- **API-specific Documentation** — Organizations SHALL maintain documentation of IDPS configurations, incidents detected involving APIs, and responses to those incidents to support continuous improvement and compliance. [NIST SP 800-94, Sec. 5.3]

### Performance Evaluation

- **API-focused IDPS Performance Evaluation** — Organizations SHOULD periodically evaluate the performance of the IDPS to ensure it meets API security objectives and modify configurations as the API threat landscape evolves. [NIST SP 800-94, Sec. 5.5]

## NIST SP 800-128: Guide for Security-Focused Configuration Management of Information Systems

> https://csrc.nist.gov/pubs/sp/800/128/upd1/final

### Security Configuration Baselines

- **API-specific Baselines** — Organizations MUST establish and maintain security configuration baselines specifically for their APIs to ensure that all API components are configured securely. [NIST SP 800-128, Sec. 3.1.2]

### Configuration Change Control

- **API Change Management** — Organizations MUST implement a formal change control process for APIs that includes security impact analysis for all configuration changes to API systems. [NIST SP 800-128, Sec. 3.3.4]

### Configuration Monitoring

- **API Configuration Monitoring** — Organizations SHALL continuously monitor API configurations to detect unauthorized changes and ensure compliance with security baselines. [NIST SP 800-128, Sec. 3.4.1]
- Automated Configuration Tools
- 
## **API Automation** — Organizations SHOULD use automated tools to apply, manage, and verify API configuration settings consistently across the organization. [NIST SP 800-128, Sec. 3.4.2]

### Security Patches

- **API Patch Management** — Organizations MUST apply security patches to API systems in a timely manner to mitigate vulnerabilities specific to APIs. [NIST SP 800-128, Sec. 3.5.2]

### Configuration Documentation

- **API Configuration Documentation** — Organizations MUST maintain up-to-date documentation that includes detailed information on the configuration of API systems, including software, network settings, and security controls. [NIST SP 800-128, Sec. 3.6.1]

### Accountability and Traceability

- **API Access Controls** — Organizations SHALL restrict access to configuration management tools and resources to authorized personnel only, particularly those managing APIs. [NIST SP 800-128, Sec. 3.7.3]

### Configuration Audits

- **API System Audits** — Organizations MUST perform regular audits to ensure that API systems comply with established security configuration baselines and that unauthorized changes are detected and remediated. [NIST SP 800-128, Sec. 3.8.2]

### Training and Awareness

- **API Configuration Training** — Organizations MUST provide training to personnel responsible for API configuration management to ensure they understand their roles, the technology, and the security implications of configuration changes. [NIST SP 800-128, Sec. 4.1.4]

## NIST SP 800-137 (ISCM for Federal Information Systems and Organizations)

> https://csrc.nist.gov/publications/detail/sp/800-137/final

### ISCM Strategy

- **API Security Status Monitoring** — Organizations MUST develop a comprehensive ISCM strategy that includes specific measures for continuously monitoring the security status of APIs. [NIST SP 800-137, Sec. 5.1]

### Define Metrics

- **API Monitoring Metrics** — Organizations SHALL define metrics specifically to measure the effectiveness of security controls applied to APIs and the overall security posture of API services. [NIST SP 800-137, Sec. 5.1.1]

### ISCM Program

- **API-specific Integration** — The ISCM program SHOULD be integrated with API management platforms to ensure continuous awareness of information security, vulnerabilities, and threats affecting APIs. [NIST SP 800-137, Sec. 5.2]

### Security Status Monitoring

- **API System Monitoring** — Organizations MUST continuously monitor the security status of API systems, using automated tools to support real-time risk management. [NIST SP 800-137, Sec. 5.3]
- **Regular Assessments** — Organizations MUST conduct regular assessments of security controls applied to APIs to ensure they are functioning effectively. [NIST SP 800-137, Sec. 5.3.1]

### Response Capabilities

- **API Response Strategies** — Organizations MUST develop and implement response capabilities specifically to address findings from continuous monitoring of API systems. [NIST SP 800-137, Sec. 5.4]

### Reporting

- **API Security Reporting** — Organizations MUST regularly report the security status of APIs to appropriate organizational officials to support risk management decisions. [NIST SP 800-137, Sec. 5.5]
- **Real-Time Dashboards** — Organizations SHOULD develop real-time dashboards that provide current security statuses and trends over time specifically for API operations. [NIST SP 800-137, Sec. 5.5.1]

### ISCM Training

- **API Security Training** — Organizations MUST provide training for personnel involved in the ISCM process to ensure they understand their roles and the technologies used, especially in relation to APIs. [NIST SP 800-137, Sec. 5.6]

### Documentation and Policies

- **API Monitoring Policies** — Organizations MUST maintain documentation of the ISCM program, including policies and results of continuous monitoring activities related to APIs. [NIST SP 800-137, Sec. 5.7]
- **Documentation Updates** — Organizations SHALL regularly review and update ISCM documentation to reflect changes in API technologies, threats, and organizational priorities. [NIST SP 800-137, Sec. 5.7.1]

### Review and Update

- **API ISCM Updates** — Organizations MUST periodically review and update the ISCM strategy and program to adapt to changes in the API threat environment and technological advancements. [NIST SP 800-137, Sec. 5.8]

## NIST SP 800-150 (Guide to Cyber Threat Intelligence Sharing)

> https://csrc.nist.gov/pubs/sp/800/150/final

### Develop a Sharing Strategy

- **API Threat Intelligence Sharing** — Organizations MUST develop a cyber threat intelligence sharing strategy that includes specific measures for sharing intelligence related to API vulnerabilities and threats. [NIST SP 800-150, Sec. 4.1]

### Define Objectives

- **API-specific Sharing Objectives** — Organizations SHALL define clear objectives for sharing and receiving threat intelligence specific to API security. [NIST SP 800-150, Sec. 4.1.1]

### Establish Sharing Mechanisms

- **API-centric Sharing Tools** — Organizations SHOULD utilize automated sharing tools like TAXII (Trusted Automated eXchange of Intelligence Information) to facilitate timely and secure sharing of API-specific cyber threat intelligence. [NIST SP 800-150, Sec. 4.2]

### Select Trusted Partners

- **API Security Partners** — Organizations MUST carefully select trusted partners that specialize in or are relevant to API security to engage in threat intelligence sharing. [NIST SP 800-150, Sec. 4.3]

### Assess Trustworthiness

- **API Partner Trustworthiness** — Organizations SHALL assess the trustworthiness of potential sharing partners to ensure the confidentiality and integrity of API-related shared information. [NIST SP 800-150, Sec. 4.3.1]

### Develop Sharing Agreements

- **API-focused Agreements** — Organizations MUST develop formal agreements that outline the terms and conditions of the intelligence sharing relationship, specifically addressing API security considerations. [NIST SP 800-150, Sec. 4.4]

### Integrate Intelligence into Security Operations

- **Operationalize API Intelligence** — Organizations MUST integrate shared cyber threat intelligence into their API security operations to enhance situational awareness and response capabilities. [NIST SP 800-150, Sec. 4.5]

### Evaluate Effectiveness

- **API Intelligence Effectiveness** — Organizations SHALL regularly evaluate the effectiveness of their threat intelligence sharing activities, focusing on API security improvements. [NIST SP 800-150, Sec. 4.6]

### Provide Training

- **API Intelligence Training** — Organizations MUST provide training for all personnel involved in threat intelligence sharing, with a focus on API security practices. [NIST SP 800-150, Sec. 4.7]
- **Training Programs** — Training SHOULD cover legal and regulatory compliance, operational practices, and security measures related to API threat intelligence sharing. [NIST SP 800-150, Sec. 4.7.1]

## PCI-DSS (Payment Card Industry - Data Security Standard)

> https://www.pcisecuritystandards.org/standards/

### Build and Maintain a Secure Network and Systems

- **Secure API Gateways** — Organizations MUST install and maintain secure configurations of API gateways to protect cardholder data accessed or processed through APIs. [PCI-DSS, Req. 1]

### Protect Cardholder Data

- **Encrypt API Transmissions** — Organizations MUST encrypt transmission of cardholder data across open, public networks when accessed via APIs. [PCI-DSS, Req. 4]

### Maintain a Vulnerability Management Program

- **Secure API Coding** — Organizations MUST develop and maintain secure systems and applications, including APIs, by applying security patches and following secure development practices. [PCI-DSS, Req. 6]

### Implement Strong Access Control Measures

- **API Access Control** — Access to cardholder data via APIs MUST be restricted to authorized users based on business need-to-know. [PCI-DSS, Req. 7]
- **API Authentication** — Organizations MUST assign a unique ID to each person with API access to ensure that actions on critical data and systems are traceable. [PCI-DSS, Req. 8]

### Regularly Monitor and Test Networks

- **API Monitoring** — Organizations MUST track and monitor all access to network resources and cardholder data via APIs to ensure that security controls are functioning correctly. [PCI-DSS, Req. 10]
- **Monitor API Traffic** — Organizations SHOULD conduct regular testing of security systems and processes to identify vulnerabilities in APIs and ensure the effectiveness of protective measures. [PCI-DSS, Req. 11]

### Maintain an Information Security Policy

- **API Security Policy** — Organizations MUST establish, publish, maintain, and disseminate a security policy that addresses information security for employee and contractor access to APIs. [PCI-DSS, Req. 12]

## Best Practices

### MITRE ATT&CK Framework

> https://attack.mitre.org/

### Understand Adversary Behaviors

- **API Attack Vectors** — Organizations SHOULD use the MITRE ATT&CK framework to identify and understand specific adversary tactics and techniques that target APIs. [MITRE ATT&CK, Techniques]

### Integrate with Security Operations

- **API Threat Detection** — Security teams SHOULD integrate API-specific attack scenarios into their security operations to enhance threat detection, analysis, and response capabilities for APIs. [MITRE ATT&CK, Integration]

### Use in Red Teaming

- **Simulate API Attacks** — Organizations SHOULD use the MITRE ATT&CK framework to guide red team exercises focused on APIs, simulating known adversary behaviors to test API security controls. [MITRE ATT&CK, Red Teaming]

### Gap Analysis

- **API Security Controls Assessment** — Security teams SHOULD conduct gap analyses using the ATT&CK framework to identify and prioritize areas in their API defenses that require strengthening. [MITRE ATT&CK, Gap Analysis]

### Enhance Threat Intelligence

- **API Threat Correlation** — Organizations SHOULD use the ATT&CK framework to enhance their threat intelligence capabilities by correlating external threat information with framework tactics and techniques that specifically apply to API security. [MITRE ATT&CK, Threat Intelligence]

## OWASP API Security Top 10

> https://owasp.org/www-project-api-security/

### API1: Broken Object Level Authorization

- **Strict Access Controls** — Ensure that authorization checks are in place for each endpoint, especially when accessing objects directly through their identifiers to prevent unauthorized access. [OWASP API Security Top 10, API1]

### API2: Broken User Authentication

- **Robust Authentication Mechanisms** — Implement strong authentication mechanisms that are resistant to attacks and ensure that they are applied consistently across all API endpoints. [OWASP API Security Top 10, API2]

### API3: Excessive Data Exposure

- **Minimize Data Exposure** — Review all API responses to ensure they do not expose sensitive data unnecessarily and apply data minimization principles. [OWASP API Security Top 10, API3]

### API4: Lack of Resources & Rate Limiting

- **Implement Rate Limiting** — Use rate limiting to protect APIs against denial-of-service attacks, automated scraping, and brute-force attacks. [OWASP API Security Top 10, API4]

### API5: Broken Function Level Authorization

- **Function Level Checks** — Ensure that function level permissions are enforced before performing any actions or business logic decisions. [OWASP API Security Top 10, API5]

### API6: Mass Assignment

- **Proper Property Assignment** — Use allowlists to prevent mass assignment vulnerabilities by explicitly defining which properties users are allowed to modify. [OWASP API Security Top 10, API6]

### API7: Security Misconfiguration

- **Secure Configuration Settings** — Ensure that all security settings are defined, implemented, and maintained as APIs are developed and deployed. Avoid defaults. [OWASP API Security Top 10, API7]

### API8: Injection

- **Prevent Injections** — Use secure coding techniques to sanitize inputs and prevent injection attacks such as SQL, NoSQL, and command injection attacks. [OWASP API Security Top 10, API8]

### API9: Improper Assets Management

- **Secure API Documentation** — Ensure that old APIs are properly retired, documentation is updated, and that only current and secure APIs are exposed. [OWASP API Security Top 10, API9]

### API10: Insufficient Logging & Monitoring

- **Enhanced Logging and Monitoring** — Implement detailed logging and monitoring to detect attacks and anomalies in real time or near-real time to enable quick response to security incidents. [OWASP API Security Top 10, API10]

## OWASP Top 10

> https://owasp.org/Top10/

### A1: Injection

- **Prevent Injections** — Use secure coding techniques to validate input, parameterize queries, and ensure APIs are not vulnerable to SQL, NoSQL, and other injection attacks. [OWASP Top 10, A1]

### A2: Broken Authentication

- **Secure API Authentication** — Implement robust authentication mechanisms for APIs to prevent unauthorized access. [OWASP Top 10, A2]

### A3: Sensitive Data Exposure

- **Protect Sensitive Data** — Encrypt sensitive data in transit and at rest, and minimize exposure of sensitive data in API responses. [OWASP Top 10, A3]

### A4: XML External Entities (XXE)

- **Prevent XXE** — Disable XML external entity processing in APIs that parse XML input, and use less complex data formats like JSON. [OWASP Top 10, A4]

### A5: Broken Access Control

- **Strict Access Controls** — Ensure that APIs enforce strict access controls to prevent unauthorized actions by authenticated users. [OWASP Top 10, A5]

### A6: Security Misconfiguration

- **Avoid Misconfigurations** — Secure API configuration settings, and regularly review and update configurations to avoid security weaknesses. [OWASP Top 10, A6]

### A7: Cross-Site Scripting (XSS)

- **Prevent XSS** — Encode and sanitize user-generated content to prevent XSS attacks in APIs that serve HTML or JavaScript content. [OWASP Top 10, A7]

### A8: Insecure Deserialization

- **Secure Deserialization** — Avoid exposing APIs to deserialization attacks by implementing integrity checks and limiting serialized objects. [OWASP Top 10, A8]

### A9: Using Components with Known Vulnerabilities

- **Manage Dependencies** — Ensure that APIs do not use outdated libraries or components that contain known vulnerabilities. [OWASP Top 10, A9]

### A10: Insufficient Logging & Monitoring

- **Enhance Monitoring** — Implement comprehensive logging and monitoring to detect and respond to potential security incidents affecting APIs. [OWASP Top 10, A10]

## RFC 5424 (The Syslog Protocol)

> https://datatracker.ietf.org/doc/html/rfc5424

### No API specific requirements


## RFC 6811 (BGP Prefix Origin Validation)

> https://datatracker.ietf.org/doc/html/rfc6811

### No API specific requirements


## RFC 6749 (OAuth 2.0 Authorization Framework)

> https://datatracker.ietf.org/doc/html/rfc6749

### Client Registration

- **Registration Requirements** — Clients MUST register with the authorization server to obtain credentials such as client ID and client secret. This process involves providing the authorization server with details about the application and its redirection URIs. (Section 2)

### Authorization Grant

- **Grant Types** — Clients MUST obtain an authorization grant from the resource owner as a prerequisite to getting an access token. Different grant types like authorization code, implicit, resource owner credentials, or client credentials SHOULD be used according to the application needs. (Section 1.3)
- **Authorization Code Grant** — Clients SHOULD implement the authorization code grant type for web and native applications where the client can manage the confidentiality of its credentials. (Section 4.1)
- **Implicit Grant** — SHOULD be used for clients implemented in a browser using a scripting language, such as JavaScript. (Section 4.2)
- **Resource Owner Password Credentials Grant** — SHOULD be used only when there is a high degree of trust between the resource owner and the client, such as the device operating system or a highly privileged application. (Section 4.3)
- **Client Credentials Grant** — SHOULD be used for confidential clients acting on their own behalf (the client is also the resource owner) without external users. (Section 4.4)

### Access Tokens

- **Token Issuance and Handling** — The authorization server issues access tokens to the client after successfully authenticating the client and obtaining authorization. MUST ensure secure transmission and storage of access tokens and should set appropriate scopes and expiration times. (Section 1.4, 5.1)
- **Scope Management** — APIs SHOULD validate the scope of access tokens to ensure clients are authorized for the requested actions. (Section 3.3)

### Redirection URI

- **Secure Redirection** — MUST require the registration of redirection URIs to prevent redirection attacks where the authorization response can be intercepted by attackers. Clients MUST use HTTPS URIs to prevent interception during authorization. (Section 3.1.2)

### Secure Storage of Credentials

- **Credential Security** — Client credentials MUST be stored securely using appropriate security measures to prevent unauthorized access and leakage. (General Best Practices)

### Token Revocation

- **Revocation Support** — MUST support mechanisms to revoke access tokens and refresh tokens when needed, to manage the lifecycle of the tokens effectively. (Section 2.1, General Best Practices)

### Refresh Tokens

- **Secure Handling of Refresh Tokens** — If refresh tokens are used, they MUST be stored and handled securely, particularly in client applications. Implementations SHOULD enable the refresh token rotation and expiration to limit the impact of token leakage. (Section 1.5)

## RFC 8725 (JWT Best Current Practices)

> https://datatracker.ietf.org/doc/html/rfc8725

### JWT Creation and Validation

- **Secure Key Management** — Organizations MUST use strong, cryptographically secure keys for signing JWTs. Key rotation and secure storage practices are crucial to prevent compromise. (Section 3)
- **Algorithm Selection** — MUST use secure algorithms for JWT signing and encryption. Avoid algorithms known to be vulnerable such as "none" or weak symmetric keys. MUST reject tokens signed with insecure algorithms. (Section 3.1)

### JWT Structure

- **Implicit Trust of JWTs** — Organizations SHOULD NOT implicitly trust JWTs. Validate all JWTs before use, including signature validation and claims verification. (Section 3.2)
- **Claims Handling** — MUST carefully manage the claims included in JWTs to ensure they contain only necessary information, and SHOULD limit personal information and sensitive data. (Section 3.3)

### JWT Expiry and State Management

- **Short Expiry Times** — Use short expiration times for JWTs to reduce the risk of misuse or replay. (Section 3.4)
- **Stateful vs. Stateless** — Consider the trade-offs between using stateful JWTs (which require server-side state management) and stateless JWTs (which are fully self-contained). (Section 3.5)

### JWT Revocation and Lifecycle

- **Token Revocation Mechanism** — SHOULD implement mechanisms to revoke JWTs when necessary, particularly in situations where tokens need to be invalidated prior to their expiration. (Section 3.6)
- **Refresh Tokens** — If refresh tokens are used, these SHOULD also be secured and managed with caution, implementing refresh token rotation and strict usage guidelines. (Section 3.7)

### Secure Transmission and Storage

- **Secure Transmission** — MUST ensure JWTs are transmitted securely to protect them from interception. Use HTTPS and consider additional security measures like token binding. (Section 4)
- **Secure Storage** — Securely store JWTs on the client side to prevent unauthorized access. Use cookie storage with the HttpOnly, Secure, and SameSite attributes where appropriate. (Section 4.1)

### Audience Restriction

- **Audience Check** — MUST ensure JWTs contain the "aud" (Audience) claim and validate it to restrict the token's use to intended recipients. This prevents tokens from being misused on other services. (Section 5)

### Issuer Authentication

- **Issuer Verification** — MUST validate the "iss" (Issuer) claim in JWTs to ensure tokens are received from legitimate and expected issuers. (Section 5.1)

### Privacy Considerations

- **Privacy by Design** — Organizations SHOULD design JWT usage with privacy in mind, ensuring minimal data exposure and alignment with data protection regulations. (Section 6)

## RFC 7525 (Recommendations for TLS and DTLS)

> https://datatracker.ietf.org/doc/html/rfc7525

### Secure Protocols and Versions

- **Adopt Strong Protocols** — Organizations MUST use secure versions of TLS and DTLS to protect communications. Avoid deprecated protocols like SSL and earlier versions of TLS (prior to 1.2). (Section 3)

### Cipher Suite Selection

- **Use Strong Cipher Suites** — Organizations SHOULD use strong cipher suites that provide adequate security. Prefer cipher suites that offer forward secrecy and use strong encryption algorithms such as AES and ChaCha20. Avoid weak cipher suites that use weak encryption algorithms like RC4 or those with known vulnerabilities. (Section 4.1)

### Certificate and Key Management

- **Use Strong Keys** — Organizations MUST use RSA keys with at least 2048 bits or ECC keys with appropriate curve sizes for their TLS certificates. (Section 6)
- **Proper Certificate Validation** — Organizations MUST properly validate certificates to ensure they are issued by a trusted Certificate Authority (CA) and are still valid. (Section 6.2)

### Secure Configuration

- **Disable Compression** — Organizations MUST disable compression mechanisms in TLS to prevent attacks such as CRIME. (Section 9)
- **Configure Secure Extensions** — Properly configure extensions like SNI, ALPN, and renegotiation securely. (Section 9.3)

### Enforce Strong Authentication

- **Client Authentication** — Organizations SHOULD require strong authentication mechanisms in TLS and DTLS connections, particularly when APIs involve sensitive or critical operations. Implement mutual TLS (mTLS) where appropriate to require both client and server to authenticate themselves. (Section 10)

### Secure Renegotiation

- **Secure Renegotiation** — Organizations SHOULD securely configure renegotiation settings to avoid attacks. Use the secure renegotiation extension if renegotiation is necessary. (Section 11)

### Implementation Best Practices

- **Patch and Update Software** — Organizations MUST regularly patch and update software implementations of TLS and DTLS to defend against known vulnerabilities. (Section 12)
- **Use Reliable Libraries** — Use well-maintained and widely trusted cryptographic libraries to implement TLS and DTLS. (Section 12.1)

### Configuration Testing

- **Use Scanning Tools** — Organizations SHOULD regularly test TLS and DTLS configurations for weaknesses using tools like SSL Labs' SSL Test to check for misconfigurations and vulnerabilities. (Section 13)

### Regular Monitoring

- Organizations MUST monitor TLS and DTLS connections for anomalies that could indicate security breaches or misconfigurations. (Section 14)

### Training and Awareness

- Organizations SHOULD provide training on TLS and DTLS security to relevant personnel to ensure they understand the security measures and can implement them correctly. (Section 15)

## RFC 9110 (HTTP Semantics)

> https://datatracker.ietf.org/doc/html/rfc9110

### HTTP Methods Usage

- **Understand HTTP Methods** — Organizations SHOULD familiarize themselves with the standardized HTTP methods (GET, POST, PUT, DELETE, etc.) and their appropriate uses to ensure correct application behavior and compliance with HTTP standards. This is especially important in API design to ensure that each method is used according to its defined semantics, which can affect both the functionality and security of the API. (Section 4)

### Status Code Handling

- **Proper Status Codes Usage** — Organizations MUST use appropriate HTTP status codes to accurately describe the outcome of HTTP requests. Correct use of status codes improves the robustness and reliability of API interactions by clearly communicating outcomes and errors to client applications. (Section 15)

### Header Field Implementation

- **Header Fields Implementation** — Organizations SHOULD correctly implement and utilize HTTP header fields to control caching, negotiate content, manage connections, and set cookies securely. For APIs, this includes
- **Content Negotiation** — Use the Accept, Accept-Language, Accept-Encoding, and Content-Type headers to properly handle content negotiation between clients and servers. (Section 8.4)
- **Caching Mechanisms** — Correctly implement caching headers like Cache-Control and ETag to optimize network resources and improve client response times, which is vital for high-performance APIs. (Section 13)

### Secure Data Transmission

- **Use HTTPS** — Organizations MUST ensure the secure transmission of data over HTTP by always using HTTPS instead of HTTP to encrypt data in transit. This protects against interception and modification, which are critical for API security. (Section 12)
- **TLS Implementation** — Use current best practices for TLS configurations to enhance the security of HTTPS connections, crucial for safeguarding data transmitted by APIs. (Section 12.3)

### Authentication and Authorization

- **Authentication and Authorization** — Organizations SHOULD implement robust mechanisms for authentication and authorization. For APIs, this involves
- **Authentication Headers** — Use WWW-Authenticate and Authorization headers securely to manage credentials and access control, ensuring that API clients can authenticate and are authorized to access the requested resources. (Section 11)
- **Cookies Management** — Securely manage cookies with attributes such as Secure, HttpOnly, and SameSite to mitigate risks associated with cross-site request forgery (CSRF) and cross-site scripting (XSS), which are pertinent to APIs handling sensitive data. (Section 8.8)

### HTTP/2 and HTTP/3 Adoption

- **HTTP/2 and HTTP/3 Adoption** — Organizations MAY adopt HTTP/2 and HTTP/3 to improve performance and efficiency of web communications. For APIs, the benefits include header compression and multiplexing which can enhance web application performance by reducing latency and improving throughput. (General Introduction)

### Interoperability and Compliance

- **Interoperability and Compliance** — Organizations SHOULD ensure that their web services and APIs are interoperable with various HTTP clients and servers and comply with the HTTP specifications outlined in RFC 9110 to ensure they function correctly across different platforms and devices. (General Introduction)

### Continuous Monitoring and Testing

- **Compliance Testing** — Organizations SHOULD continuously monitor and test their HTTP implementations, including APIs, to ensure they adhere to HTTP semantics and function correctly. This involves regular testing for compliance with HTTP standards, which is essential for the reliable operation of APIs. (Section 14)

### Training and Awareness

- **Training and Awareness** — Organizations SHOULD provide training on HTTP semantics to developers, system administrators, and security teams to ensure they understand and can implement these foundational web standards effectively, which is crucial for the development and maintenance of secure and functional APIs. (General Introduction)

## SANS CWE Top 25 Software Errors

> https://www.sans.org/top25-software-errors/

### Common Vulnerabilities

- **Injection Flaws** — APIs MUST use prepared statements and parameterized queries to prevent SQL injection and other injection flaws, which are prevalent in APIs that interact with databases. (CWE-89)
- **Sensitive Data Exposure** — APIs MUST ensure encryption of sensitive data both at rest and in transit, and avoid unnecessary storage of sensitive data. This is crucial for APIs that handle personal or sensitive information. (CWE-311)
- **Improper Authentication** — APIs MUST implement robust authentication mechanisms to prevent unauthorized access. This includes the use of strong authentication methods and secure session management. (CWE-287)
- **Insecure Deserialization** — APIs SHOULD avoid deserialization of data from untrusted sources or implement integrity checks and deserialization monitoring. This is particularly relevant for APIs that accept serialized objects from clients. (CWE-502)
- **Using Components with Known Vulnerabilities** — APIs MUST regularly update and patch software components to mitigate vulnerabilities that can be exploited through the API. (CWE-937)
- **Insufficient Logging & Monitoring** — APIs MUST enhance logging and monitoring capabilities to detect potential security breaches more quickly. This is essential for identifying and responding to attacks in real-time. (CWE-778)

## SANS Secure Software Development and Code Analysis Tools - Whitepaper

> https://www.sans.org/white-papers/389/

### Requirements Phase

- **Security Expert Involvement** — Include a security expert in the project team to guide security-related decisions and ensure API-specific risks are addressed.
- **Security Training** — Provide security awareness training focused on API security to the project team.
- **API-Specific Security Requirements** — Incorporate security requirements that are unique to API development in the documentation.

### Design Phase

- **API Attack Surface Analysis** — Conduct an attack surface analysis specifically for the APIs to identify potential vulnerabilities.
- **API Threat Modeling** — Perform threat modeling to pinpoint high-risk areas in the API architecture and determine necessary countermeasures.

### Construction Phase

- **Secure Coding Guidelines** — Apply secure coding guidelines that specifically address API vulnerabilities.
- **Use of Security Libraries** — Ensure the use of security libraries and frameworks that provide API security functionalities like authentication and data validation.
- **Static Analysis for APIs** — Integrate static analysis tools during API development to detect and remediate vulnerabilities early.

### Verification Phase

- **API Security Testing** — Implement dynamic analysis and penetration testing specifically designed for APIs to identify exploitable vulnerabilities.

### Maintenance Phase

- **API Security Monitoring** — Continuously monitor the API for security events and anomalies to detect and respond to threats promptly.

## CSA CCM (Cloud Security Alliance - Cloud Controls Matrix)

> https://cloudsecurityalliance.org/research/cloud-controls-matrix/

### API Security Architecture

- **Security Design Integration** — Design security into the API from the outset, ensuring all security controls specified by the CSA CCM for cloud services are considered.
- API Access Control
- **Identity and Access Management** — Ensure robust identity and access management controls are implemented for API access, including authentication, authorization, and auditing capabilities.
- Encryption and Key Management
- **Secure Data Transmission** — Use strong encryption for data in transit especially for APIs, ensuring keys are managed securely according to the CCM guidelines.
- API Monitoring and Compliance
- **Continuous Monitoring** — Implement continuous security monitoring practices that include APIs to detect and respond to incidents in real-time.
- **Compliance Audits** — Regularly perform audits for APIs to ensure compliance with cloud security best practices and the CSA CCM.

## OWASP Source Analysis Tools

> https://owasp.org/www-community/Source_Code_Analysis_Tools

### Source Code Analysis for APIs

- **Tool Selection** — Organizations SHOULD select source code analysis tools that support the languages and frameworks used in their API development to effectively identify security vulnerabilities.
- **Integration into CI/CD Pipeline** — Organizations MUST integrate source code analysis tools into the continuous integration/continuous deployment (CI/CD) pipeline to automate the detection of security issues during the API development lifecycle.
- **Configuration for API-specific Checks** — Organizations SHOULD configure tools to perform checks relevant to common API vulnerabilities, such as improper input validation, authentication issues, and insecure data handling.
- **Regular Updates and Customization** — Organizations MUST ensure that source code analysis tools are regularly updated to detect new and emerging API security threats and MUST customize the tools to address the specific security needs of their API architecture.

## OWASP Cheat Sheet Series

> https://cheatsheetseries.owasp.org/

### Authentication Cheat Sheet

- **API Authentication** — Ensure that API endpoints utilize standard authentication mechanisms (such as tokens or OAuth) instead of relying on cookies.
- **Stateless Authentication** — APIs should be stateless, using tokens (such as JWT) for managing sessions instead of server-side storage.
- **Secure Transmission** — Always transmit authentication tokens over HTTPS to protect them from interception.
- **Token Management** — Properly manage the creation, distribution, storage, and revocation of authentication tokens.

### Cross-Site Request Forgery (CSRF) Cheat Sheet

- **Use of Tokens** — For APIs particularly, use anti-CSRF tokens in state-changing operations (if not using headers such as Authorization which are less susceptible to CSRF).
- **SameSite Cookies** — If cookies are used in APIs, ensure they are set with the SameSite attribute to mitigate CSRF risks.

### SQL Injection Prevention Cheat Sheet

- **Parameterized Queries** — Use parameterized APIs to prevent SQL injection, ensuring that SQL code is separate from data.
- **Escaping Data** — Where parameterized queries are not possible, ensure proper escaping of data before including it in SQL queries.

### Content Security Policy (CSP) Cheat Sheet

- **Implement CSP** — Implement Content Security Policy headers to prevent XSS attacks via API responses that may include dynamically generated content.

### Cryptographic Storage Cheat Sheet

- **Secure Storage** — Ensure encryption of sensitive API data stored at rest using strong encryption algorithms.
- **API Encryption Key Management** — Manage encryption keys securely, rotating them periodically and storing them using secure storage mechanisms.

### Error Handling Cheat Sheet

- **Standardized Error Handling** — Implement standardized error responses in APIs to avoid disclosing sensitive information or system details.
- **Error Monitoring** — Monitor and log API errors comprehensively, ensuring that sensitive information is not exposed in error messages or logs.

### AJAX Security

- **Secure Data Handling** — Ensure that data sent to and received from the server is sanitized and validated to prevent common vulnerabilities.

### Abuse Case

- No API specific requirements

### Access Control

- **API Access Levels** — Define and enforce access levels within the API to control who can access what resources and operations.

### Attack Surface Analysis

- **Minimize Endpoints** — Reduce the number of API endpoints to the minimum necessary to decrease the attack surface.

### Authentication

- **Token-based Authentication** — Implement token-based authentication mechanisms such as JWT to secure API access.

### Authorization

- **Granular Permissions** — Use granular permissions to control API access based on the principle of least privilege.

### Authorization Testing Automation

- **Automated Testing** — Implement automated testing techniques to validate API authorization processes.

### Bean Validation

- **Input Validation** — Apply bean validation to API inputs to ensure they adhere to expected formats and value ranges.

### C-Based Toolchain Hardening

- No API specific requirements

### Authentication Cheat Sheet

- **API Authentication mechanisms** — Design APIs to use strong authentication mechanisms, including multi-factor authentication and OAuth2.

### Authorization Cheat Sheet

- **API authorization controls** — Implement granular access control for APIs, ensuring that permissions are appropriately restricted based on user roles.

### Bean Validation Cheat Sheet

- No API specific requirements

### ClickJacking Defense Cheat Sheet

- **API frame busting** — Implement measures to prevent APIs from being called via unauthorized iframes or frames.

### CORS Cheat Sheet

- **CORS configuration for APIs** — Configure Cross-Origin Resource Sharing (CORS) policies specifically for API endpoints to control cross-domain access.

### Cryptographic Storage Cheat Sheet

- **Secure API data storage** — Ensure encryption of sensitive API data stored at rest and implement proper key management practices.

### CSRF Prevention Cheat Sheet

- **API-specific CSRF prevention** — Use tokens specifically designed for APIs, such as double submit cookies or custom header tokens, to mitigate CSRF risks.

### DOM based XSS Prevention Cheat Sheet

- No API specific requirements

### Deserialization Cheat Sheet

- **API input deserialization security** — Securely implement input deserialization mechanisms in APIs to prevent attacks such as remote code execution or injection.

### Error Handling Cheat Sheet

- **API error handling** — Implement consistent and secure error handling policies for APIs to avoid leaking information about the API's internal workings or sensitive data.

### CI CD Security

- **Secure Pipeline** — Ensure that the CI/CD pipeline incorporates security checks and tests for API endpoints.

### Expression Language Injection Prevention Cheat Sheet

- **Expression Language Injection safeguards** — Secure API endpoints against Expression Language (EL) injection by validating and encoding inputs.

### Forgot Password Cheat Sheet

- **Secure API password reset** — Implement secure API endpoints for password reset functionality, ensuring robust authentication and notification mechanisms.

### HTML5 Security Cheat Sheet

- **HTML5 features in APIs** — When using HTML5 features in APIs that output to web clients, ensure security settings are configured to prevent XSS and other vulnerabilities.

### HTTP Strict Transport Security Cheat Sheet

- **API HSTS policies** — Enforce HTTP Strict Transport Security (HSTS) on API servers to ensure secure connections by redirecting HTTP traffic to HTTPS.

### HTTP Security Headers Cheat Sheet

- **Security Headers for APIs** — Configure security headers for API responses to enhance security, such as Content Security Policy (CSP) and X-Frame-Options.

### Input Validation Cheat Sheet

- **API input validation** — Implement comprehensive input validation for APIs to prevent SQL injection, XSS, and other injection attacks.

### Insecure Direct Object References Prevention Cheat Sheet

- **Prevent direct object references** — Secure APIs from Insecure Direct Object References (IDOR) by ensuring access controls and resource identifiers are managed securely.

### JSON Web Token Cheat Sheet

- **Secure JWT usage** — Implement robust validation and handling practices for JSON Web Tokens (JWT) used in API authentication and data exchange.

### LDAP Injection Prevention Cheat Sheet

- **API LDAP injection protection** — Protect API endpoints that interact with LDAP services from injection attacks by sanitizing inputs.

### Logging Cheat Sheet

- **Secure API logging practices** — Design API logging to avoid sensitive data exposure and ensure logs do not store sensitive authentication data.

### Machine Learning Security Cheat Sheet

- **Secure ML model APIs** — Ensure API endpoints interacting with machine learning models are secured against attacks such as adversarial input and model theft.

### Mass Assignment Prevention Cheat Sheet

- **Prevent mass assignment in APIs** — Implement whitelisting of allowed properties in API requests to prevent mass assignment vulnerabilities.

### Memory Leak Prevention Cheat Sheet

- **Manage memory in API services** — Ensure that APIs managing memory-intensive tasks are properly monitored and managed to prevent memory leaks that could lead to service disruption.

### .NET Security Cheat Sheet

- **Secure .NET APIs** — Apply .NET security best practices specifically in API development to manage authentication, authorization, and data validation.

### Node.js Security Cheat Sheet

- **Secure Node.js API endpoints** — Implement security controls for Node.js APIs, focusing on secure dependency management and proper error handling.

### OS Command Injection Prevention Cheat Sheet

- **Protect APIs from OS command injections** — Validate and sanitize all API inputs to prevent operating system command injections.

### OWASP Proactive Controls

- **C1: Define security requirements for APIs** — Establish clear security requirements for API development as part of the proactive controls.

### OWASP Top Ten Proactive Controls Cheat Sheet

- **C2: Leverage security frameworks for APIs** — Use security frameworks and libraries that support secure API development to prevent common vulnerabilities.

### Password Storage Cheat Sheet

- **Secure API password storage** — Use strong, up-to-date hashing algorithms for storing passwords accessed through APIs.

### PIN Security Cheat Sheet

- **Secure PIN handling in APIs** — Ensure that APIs dealing with Personal Identification Numbers (PIN) implement stringent security measures to protect PIN data during transmission and storage.

### Session Management Cheat Sheet

- **Manage API session securely** — Ensure secure session management practices for APIs, including secure token handling and session expiration mechanisms.

### Signal Sciences Cheat Sheet

- **Integrate Signal Sciences with APIs** — Leverage Signal Sciences for additional security monitoring and protection in API environments.

### Site Reliability Engineering (SRE) Cheat Sheet

- **SRE practices for API reliability** — Apply Site Reliability Engineering principles to manage and improve the reliability of APIs, focusing on performance and error rate monitoring.

### Social Engineering Defense Cheat Sheet

- **APIs against social engineering** — Educate API developers and users on social engineering tactics that could be used to gain unauthorized access or manipulate API interactions.

### SOAP Security Cheat Sheet

- **Secure SOAP services** — Apply security measures to protect SOAP-based web services and APIs, particularly focusing on WS-Security standards and message validation.

### South Korea Personal Information Protection Act (PIPA) Cheat Sheet

- No API specific requirements

### Spring Boot Cheat Sheet

- **Secure Spring Boot APIs** — Implement security configurations specific to Spring Boot when developing APIs, including security dependencies and property settings.

### Spring Security Architecture Cheat Sheet

- **Secure API with Spring Security** — Utilize Spring Security's capabilities to protect APIs, focusing on authentication mechanisms and security configurations.

### SQL Injection Prevention Cheat Sheet

- **Prevent SQL injection in API queries** — Ensure that APIs that interact with SQL databases use prepared statements or ORM frameworks that automatically handle parameterized queries.

### PHP Configuration Cheat Sheet

- No API specific requirements

### PHP Security Cheat Sheet

- **Secure PHP API configuration** — Configure PHP environments securely when exposing APIs, especially in regards to error handling and input validation.

### Pinning Cheat Sheet

- **Implement certificate pinning in API clients** — Utilize certificate pinning in mobile or desktop clients that consume APIs to enhance the security of communications.

### Play Framework Cheat Sheet

- **Secure Play Framework APIs** — Apply security settings and practices specific to Play Framework when developing APIs, such as data validation and session management.

### Protect FileUpload Against Malicious File Cheat Sheet

- **Validate uploaded files via APIs** — Ensure that APIs accepting file uploads implement robust validation and sanitization to prevent malicious file uploads.

### Protecting crown jewels Cheat Sheet

- **Secure API access to sensitive data** — Implement strict authentication and authorization controls for APIs that provide access to sensitive or critical data.

### Quartz Job Scheduler Cheat Sheet

- **Secure Quartz API interactions** — Ensure that job scheduling and execution through Quartz APIs are secured and that job data is properly validated.

### Query Parameterization Cheat Sheet

- **Parameterize SQL queries in APIs** — Use parameterized queries in APIs to prevent SQL injection vulnerabilities when interacting with databases.

### REST Assessment Cheat Sheet

- **Secure RESTful APIs** — Follow best practices for securing RESTful APIs, including proper authentication, authorization, and data validation strategies.

### REST Security Cheat Sheet

- **Apply REST API security best practices** — Implement comprehensive security measures for REST APIs, such as HTTPS enforcement, token-based authentication, and rate limiting.

### Testing for Stack Traces Cheat Sheet

- No API specific requirements

### Test WordPress Security Cheat Sheet

- No API specific requirements

### Threat Modeling Cheat Sheet

- **Threat modeling for API design** — Apply threat modeling techniques to identify potential security risks in API design and implementation, focusing on data flow and authentication.

### TLS Deployment Best Practices Cheat Sheet

- **Implement TLS for API security** — Follow best practices for deploying TLS in API communications to ensure data is encrypted and secure during transmission.

### Transport Layer Protection Cheat Sheet

- **Secure API transport layers** — Use robust encryption (TLS) for API data transmission, ensure proper certificate validation, and configure strong cipher suites.

### User Privacy Protection Cheat Sheet

- **Privacy protection in API responses** — Design APIs to minimize data exposure and implement features that enhance user privacy, such as data masking and opt-out mechanisms for data collection.

### Using the OWASP Top Ten to Perform Security Code Reviews Cheat Sheet

- **Code review for API security** — Use the OWASP Top Ten as a guide to review the security of API source code, focusing on areas like injection flaws and authentication.

### VBA Macro Security Cheat Sheet

- No API specific requirements

### Web Service Security Cheat Sheet

- **Secure web service APIs** — Implement security controls for web services exposed via APIs, such as authentication, encryption, and access control measures.

### Windows Logging Cheat Sheet

- No API specific requirements

### XML External Entity (XXE) Prevention Cheat Sheet

- **Prevent XXE in API parsing** — Implement measures to prevent XML External Entity attacks when APIs accept XML input, such as disabling external entities and DTDs in XML parsers.

### XML Security Cheat Sheet

- **Secure XML processing in APIs** — Ensure secure processing of XML data within APIs by using secure parsing and validation techniques to protect against XML-related vulnerabilities.

### XXE Prevention Cheat Sheet

- No API specific requirements

### SSRF Prevention Cheat Sheet

- **Mitigate SSRF risks in APIs** — Implement safeguards in APIs to prevent Server-Side Request Forgery by validating and sanitizing incoming requests and restricting URL access.