# GPT Prompts

If you use a Large Language Model (LLM) like ChatGPT to help you, this is by no-means a slam-dunk. It can hallucinate, it constantly wants to summarize things instead of being thorough, and you often need to re-remind it of details. So, it is a very helpful assistant that will save you hours of research and typing, BUT, you also can't really trust what it says. At the time of this writing, the following was used to help generate this material:

| GenAI Platform | Model |
| -------------- | ----- |
| OpenAI ChatGPT | 4o    |

You should ABSOLUTELY double-check everything it outputs because it could wrong or it could realistic-looking, but made up.

Below was the final set of prompts I used to generate the starting information for this project.

## Step 1: Get initial List of Regulatory Standards

Below is the prompt:

    For each of these standards:

    CCPA (California Consumer Privacy Act)
    CPRA (California Privacy Rights Act)
    FDA 21 CFR Part 11
    FISMA (Federal Information Security Management Act)
    FedRAMP (Federal Risk and Authorization Management Program)
    GDPR (General Data Protection Regulation)
    GLBA (Gramm-Leach-Bliley Act)
    HiTRUST (Health Information Trust Alliance Common Security Framework)
    HIPAA (Health Insurance Portability and Accountability Act)
    NAIC (National Association of Insurance Commissioners) Insurance Data Security Model Law
    NIST CSF (Cybersecurity Framework)
    NYS DFS Cybersecurity Regulation (23 NYCRR 500)
    PCI-DSS (Payment Card Industry Data Security Standard)
    SOX (Sarbanes-Oxley Act)

    Please create a text code block in this exact format (using a tab character for the indent), with no extra lines:

    ```text
    {Standard Name}
        Link
            {URL}
        Description
            {description goes here}
        Scope
            {definition of what kinds of organizations would be in-scope for this standard}
    ```

## Step 2: Get details about action items

Below is the prompt:

    I will be giving you a standard. For that standard, I need the full and complete answer in your response so that no follow-up queustions are needed. What we need is a look at the software security requirements (which might extend into infrastructure items). What we ultimately need to do is produce a checklist of who at my company needs to do what, in order to be in compliance with this standard. Again, this should not be a summary of items, or the top 5 items, or the most common items from the standard, but it should be 100% of all of the standard requirements that you can find, that you respond with.

    For this standard that I give you, please create a text code block in this exact format (using a tab character for the indent), with no extra lines:

    ```text
    {Category}
        {the requirement for infrastructure to implement, to be in compliance with this standard with RFC 2119 using that uppercase SHALL/MUST, SHOULD/MAY language} ({citation to the source: section name or number, chapter and section, page number, etc}, {link to specification if available}) {#hastags}
    ```

    At the end of each requirement, append a lowercase hashtag of: #infrastructure, #architecture, #development, #sdlc, to specify which party or parties would be responsible for this requirement.

    Please keep the categories somewhat broad, just for general organization

    Please do not include the curly braces in the output, those are just indicators to you what kind of data should be there. Also, do not put any extra lines in the code block.

    And what I mean here is that some of these security requirements are things that are done by sysadmins and network engineers (e.g. available cipher suites, patch management, etc), some things are a result of how a system is architected (e.g. acceptable JWT token algorithms and key sizes, password complexity, etc), and some of these requirements are coding things a developer might do (e.g. input validation and output encoding)

    Please double-check and make sure you are including 100% of what is needed in your initial response. Every actionable requirement in the standard MUST be included in the output.

    Let's start with: CCPA

After that, I would just use something like:

    Next one is: FDA 21 CFR Part 11

And sometimes I need to remind it about small formatting issues. For that, I would word it like:

    Next is: FedRAMP and please use uppercase for SHALL/MUST, etc as discussed from RFC 2119

## Step 3: Consolidate of Requirements

Once we have all of the standards, and then requirements for each standard, I used this prompt:

    I realize this is a big task, but I would like you to consolidate the data you provided. For example, output "Data Security Measures", and under that might be an item that is pretty much the same across 3 different standards. So, output that standard, include the citations for EACH standard as before, and also include additional #hashtags for the unique standard (e.g. #ccpa, #pci-dss, #naic, etc). The idea is to end up with perhaps a dozen unique categories, and under them are the consolidation of all of the requirements from all of the standards, but tagged in such a way that it's clear that this particular requirement is pretty much a duplicate from this other standard, and these other standards.

You of course can't trust the output, so I asked:

    Does this fully represent 100% of the standards and 100% of the requirements within each standard?

It responded with:

> *"This consolidation represents key requirements from each standard but may not capture every specific detail from each standard. For full compliance, each standard's complete text should be reviewed directly. Here's an updated attempt to ensure thorough coverage:"*

And then responded with a longer, more-thorough output. So I asked again:

    Does this fully represent 100% of the standards and 100% of the requirements within each standard?

It responded with:

> *"The previous output consolidates many key requirements across multiple standards, but it may not cover 100% of every requirement from each standard due to the complexity and extensive details in these regulatory documents. To ensure full coverage, it's crucial to reference the complete text of each standard directly. Here's an attempt to cover all actionable requirements more comprehensively:"*

And then responded with a longer, more-thorough output. Are you seeing why you can't trust what it outputs on face value? I was very clear that I wanted 100%. It responded with a realistic answer. However, when questioned, it confirmed that it was not in-fact 100% complete.

You would think that would be it, but I asked again:

    Does this fully represent 100% of the standards and 100% of the requirements within each standard? If it's not, please don't make me keep asking. Please just process 100% of this and output the results.

and this time it said:

> *"Here is a comprehensive attempt to ensure 100% of the requirements from the given standards:"*

And then responded with a bit more. This went on a couple of more times until it said it wanted to go standard by standard. I then said:

    But wait, I already have the details of each standard. The effort here is to look at "Incident Response" for example, as a category, and see what it common across all the standards, determine if "Oh wait, this is basically identical to this requirement!" (and then consolidating those two items, and marking the hashtags and citations at the end to specify that this one requirement covers those two, specific requirements. Are you able to do that?

and it responded with:

> *"I understand now. Let's consolidate the requirements by category, identify commonalities, and mark the hashtags and citations for each standard they apply to. Here’s a consolidated approach:"*



Does this mean it's complete and that we can trust it? No. However, for my purposes, this gives me a good enough base. Hopefully I will catch any missing or erroneous data when I go through all of this, or we will find it when Internal Audit comes around.