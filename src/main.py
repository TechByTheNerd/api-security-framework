import threading
import queue
import openai
from decouple import config
from colorama import Fore, Style
import json
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
import time

# Get OpenAI API key from environment variables
openai_api_key = config('OPENAI_API_KEY')

# Check if OpenAI API key is missing or empty
if not openai_api_key or len(openai_api_key) < 8:
    raise ValueError("Missing OpenAI API key. Please set the OPENAI_API_KEY environment variable in the .env file.")

# Set OpenAI API key
openai.api_key = openai_api_key

class Agent(threading.Thread):
    def __init__(self, id, task_queue, result_queue, lock, progress, task_id):
        threading.Thread.__init__(self)
        self.id = id
        self.task_queue = task_queue
        self.result_queue = result_queue
        self.lock = lock
        self.progress = progress
        self.task_id = task_id

    def run(self):
        while True:
            try:
                task = self.task_queue.get(timeout=1)
                result = self.process_task(task)
                self.result_queue.put(result)
                self.task_queue.task_done()
                self.progress.update(self.task_id, advance=1)
            except queue.Empty:
                break

    def process_task(self, task):
        messages = [
            {"role": "system", "content": "You are an expert in API security and compliance, and also an expert in JSON."},
            {"role": "user", "content": f"Generate a hierarchical JSON object that contains detailed and comprehensive requirements and best practices for {task['standard']}, specifically related to API security. Each requirement should follow the RFC9119 format of 'MUST', 'SHOULD', 'MAY', etc. and include properties like: a citation link, the intended audience (developers, security engineers, etc.), and any other relevant metadata. The result of your research should be pure, properly formatted JSON including any special character escaping, without any markdown, markdown code blocks, or other formatting, since the results will go directly into a `output.json` file. That includes the entire hierarchy of the JSON output. The JSON object should be structured in a way that is easy to navigate and understand. The format of the output should be like this, for example: {{ ""standard"": ""OWASP API Security Top 10"", ""version"": ""2019"", ""primary_url"": ""https://owasp.org/www-project-api-security/"", ""scope"": [""All Industries"", ""API Developers"", ""Security Engineers""], ""requirements"": [ {{ ""API_Authentication"": {{ ""MUST"": {{ ""requirement_id"": ""API-1"", ""requirement_text"": ""Implement strong authentication mechanisms for all APIs."", ""requirement_abstract"": ""APIs must use strong authentication mechanisms such as OAuth 2.0 or API keys."", ""requirement_details_markdown_formatted"": ""APIs must use strong authentication mechanisms such as OAuth 2.0 or API keys. OAuth 2.0 is an open standard for access delegation, commonly used for authorization. API keys are unique identifiers used to authenticate requests to an API."", ""citation_link"": ""https://cheatsheetseries.owasp.org/cheatsheets/API_Security_Cheat_Sheet.html#authentication"", ""intended_audience"": [""Developers"", ""Architects"", ""IdP Providers""], ""severity"": ""Critical"" }} }} }} ] }}" }
        ]

        total_tokens_in_messages = sum([len(message['content']) for message in messages])

        # NOTE: The max_tokens parameter is set to 16385 (max for this model) to 
        # allow for large JSON responses. Else, you'll get something like a: 
        # "json.decoder.JSONDecodeError: Unterminated string starting at: 
        # line 101 column 26 (char 6709)"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=4096 #16385 - total_tokens_in_messages
        )

        try:
            raw_response = response['choices'][0]['message']['content'].strip()
            #print(Fore.YELLOW + f"[Agent-{self.id}] Generated JSON for {task['standard']} {raw_response}" + Style.RESET_ALL)
            parsed_data = json.loads(raw_response)
            output = {"standard": task["standard"], "data": parsed_data}
            print(Fore.YELLOW + f"[Agent-{self.id}] Processed task for {task['standard']}" + Style.RESET_ALL)

            with self.lock:
                with open(task['filename'], 'r+') as f:
                    content = f.read()
                    f.seek(0)  # move the cursor to the start of the file
                    if content == '[]':
                        # If the file only contains the opening and closing brackets, write the output object
                        f.seek(0)  # move the cursor to the start of the file
                        f.write('[\n')  # write the opening bracket
                        json.dump(output, f, indent=4)  # write the output object
                        f.write('\n]')  # write the closing bracket
                    else:
                        # If the file contains other objects, append a comma and then the output object
                        f.seek(0, 2)  # move the cursor to the end of the file
                        f.seek(f.tell() - 2, 0)  # move the cursor two characters before the end
                        f.write(',\n')  # append a comma
                        json.dump(output, f, indent=4)  # append the output object
                        f.write('\n]')  # append the closing bracket

            return output
        except json.decoder.JSONDecodeError as exception:
            print(Fore.RED + f"[Agent-{self.id}] Error processing task for {task['standard']}: {exception}" + Style.RESET_ALL)
            return {"standard": task["standard"], "data": None}

def process_standards(standards_list, output_file_name, description):

    print(Fore.CYAN + f"[*] Initializing task and result queues for {description}" + Style.RESET_ALL)
    task_queue = queue.Queue()
    result_queue = queue.Queue()

    with open(output_file_name, 'w') as f:
        f.write('[]')

    for standard in standards_list:
        print(f"    - {standard}")
        task_queue.put({"standard": standard, "filename": output_file_name})

    num_agents = 6
    lock = threading.Lock()
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), 
                  BarColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"), auto_refresh=True) as progress:
        task_id = progress.add_task(f"[cyan]Processing...", total=len(standards_list))
        agents = [Agent(i, task_queue, result_queue, lock, progress, task_id) for i in range(num_agents)]

        print(Fore.CYAN + f"[*] Creating and starting {num_agents} agents to process {len(standards_list)} standards..." + Style.RESET_ALL)
        for agent in agents:
            agent.start()

        print(Fore.CYAN + "[*] Waiting for all tasks to be processed" + Style.RESET_ALL)
        task_queue.join()

        results = []
        while not result_queue.empty():
            result = result_queue.get()
            results.append(result)

        with open(output_file_name, 'w') as f:
            json.dump(results, f, indent=4)

        print(Fore.GREEN + f"[+] Results written to {output_file_name}" + Style.RESET_ALL)

def main():
    
    standards_list = [
        "PCI-DSS",
        "GDPR",
        "CCPA",
        "CPRA",
        "FDA 21 CFR Part 11",
        "FISMA",
        "FedRAMP",
        "GLBA",
        "HiTRUST",
        "HIPAA",
        "NAIC Model Law",
        "NIST CSF",
        "NYS DFS Regulation",
        "SOX"
    ]

    print(Fore.CYAN + f"[*] Processing Regulatory Requirements" + Style.RESET_ALL)
    process_standards(standards_list, 'regulatory.json', 'Regulatory Requirements')
    print(Fore.GREEN + "[+] Done." + Style.RESET_ALL)

    standards_list = [
        "OWASP API Security Top 10",
        "OWASP Top 10",
        "MITRE ATT&CK Framework",
        "CIS Controls",
        "CSA Security Guidance",        
        "ISO 22301 Security and Resilience / Business Continuity",
        "ISO/IEC 27001 Information Security, Cybersecurity and Privacy Protection",
        "ISO/IEC 27017 Security Techniques for Cloud Services",
        "ISO/IEC 27018 Security Techniques for PII in Public Cloud",
        "ISO/IEC 27032 Guidelines for Internet Security",
        "ISO/IEC 27035 Information Security Incident Management",
        "ISO/IEC 27701 Security Techniques for Privacy Information Management",
        "ISO/IEC 29100 Information Technology Privacy Framework",
        "NIST CSF (Cyber Security Framework)",
        "NIST Digital Identity Guidelines (SP 800-63*)",
        "NIST SP 800-34 (Contingency Planning Guide for Federal Information Systems)",
        "NIST SP 800-40 (Enterprise Patch Management)",
        "NIST SP 800-41 (Guidelines of Firewalls and Firewall Policy)",
        "NIST SP 800-53 (Security and Privacy Controls)",
        "NIST SP 800-61 (Computer Security Incident Handling Guide)",
        "NIST SP 800-92 (Guide to Computer Security Log Management)",
        "NIST SP 800-94 (Guide to Intrusion Detection and Preventions Systems (IDPS))",
        "NIST SP 800-128: Guide for Security-Focused Configuration Management of Information Systems",
        "NIST SP 800-137 (ISCM for Federal Information Systems and Organizations)",
        "NIST SP 800-150 (Guide to Cyber Threat Intelligence Sharing)",
        "RFC 5424 (The Syslog Protocol)",
        "RFC 6811 (BGP Prefix Origin Validation)",
        "RFC 6749 (OAuth 2.0 Authorization Framework)",
        "RFC 8725 (JWT Best Current Practices)",
        "RFC 7525 (Recommendations for TLS and DTLS)",
        "RFC 9110 (HTTP Semantics)",
        "SANS CWE Top 25 Software Errors",
        "SANS Secure Software Development and Code Analysis Tools - Whitepaper",
        "CSA CCM (Cloud Security Alliance - Cloud Controls Matrix)",
        "OWASP Source Analysis Tools",
        "OWASP Cheat Sheet Series"
    ]

    print(Fore.CYAN + f"[*] Processing Best Practices" + Style.RESET_ALL)
    process_standards(standards_list, 'best-practices.json', 'Best Practices')

    print(Fore.GREEN + "[+] Done." + Style.RESET_ALL)

def fix_json_formatting(filename):
    # Do a final read and write of proper JSON formatting
    with open(filename, 'r') as f:
        data = json.load(f)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()