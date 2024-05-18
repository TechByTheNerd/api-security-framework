# Standards for API Security

This project is an attempt to automate some of the research and analysis around how to gather relevant standards for a technology, and get that data into a consumable format. In this case, the thesis question is:

> I have a list of regulatory requirements to which I need to adhere. Also, there are many public standards for best practices (e.g. ISO, RFC, frameworks, etc). What is a list of things that I need to do, to come into compliance with these standards.

The idea is, maybe GenerativeAI and these Large Language Models (LLMs) can help us solve this quicker. Better: what if could do this in a repeatable way?

## Mark I: Using regulat ChatGPT

I started with just using ChatGPT, but despite having very detailed prompts, ran into issues. See [this page for my prompts and the issues I had](gpt-prompts.md).

## Mark II: Using Python and "Agent Swarms"

The problem with regular ChatGPT is there is a lot of "context" involved, including:

1. What I'm asking for.
2. The format that I want it.
3. The actual data is processes and results it produces.

In the `src` folder of this repository is some OpenAI-compliant Python code for having multiple agents so the work of research and analysis, and then bring all of those results together.

To learn more, see the: [src/README.md](src/README.md) file.