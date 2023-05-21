import subprocess
import whois
from datetime import datetime
from itertools import combinations
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.table import Table
import time

console = Console(record=True)  # updated console initialization to remove timestamps
tlds = [".org", ".com", ".io", ".net"]
request_interval = 1  # Set your preferred interval (in seconds) between each whois request here

def generate_word_combinations(words):
    return [''.join(map(str.capitalize, comb)) for comb in combinations(words, 2)]

def generate_domain_file(words):
    filename = "generated_domains_" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".txt"
    with open(filename, "w") as file:
        for word_combination in generate_word_combinations(words):
            file.write(word_combination + "\n")
    return filename

def is_domain_likely_registered(domain):
    try:
        w = whois.whois(domain)
        return bool(w.domain_name)
    except Exception as e:
        return None

def check_domain_tlds(domain):
    for tld in tlds:
        full_domain = domain + tld
        if is_domain_likely_registered(full_domain):
            time.sleep(request_interval)  # prevent rate limiting
            return None
        time.sleep(request_interval)  # prevent rate limiting
    return domain

def read_file_and_check_domain(filename):
    console.print(Panel(f'📚 Opening domain file: {filename}', title="Domain File", expand=False))
    with open(filename, "r") as file:
        lines = file.readlines()
        domains = [line.strip() for line in lines]
        available_domains = []
        status_table = Table(show_header=False, show_edge=False)
        live_table = Live(status_table, console=console, refresh_per_second=4)
        with live_table:
            for i, domain in enumerate(domains):
                progress_percent = (i / len(domains)) * 100
                status_table.columns = []
                status_table.add_column("Current Status", justify="center", no_wrap=True)
                status_table.rows = []
                status_table.add_row(Text(f'🔎 Checking: {domain}', style='bold cyan'))
                status_table.add_row(Text(f'📊 Progress: {progress_percent:.2f}%', style='bold magenta'))
                live_table.update(Panel(status_table, expand=False))
                available_domain = check_domain_tlds(domain)
                if available_domain:
                    available_domains.append(available_domain)
                    panel_text = f"🎉🔥🚀🌍 Available Domain: {available_domain}! 🎉"
                    console.print(Panel(Text(panel_text, style="bold green"), title="Domain Status", expand=False))
    return available_domains

def run_domain_search():
    console.print(Panel("[bold]🎩🔮 Welcome to the Domain Wizard! 🔮🎩", expand=False))
    console.print(Panel('📝 Do you have a pre-made domain list? (y/n): ', title="File Provided", expand=False))
    file_provided = input().lower()
    if file_provided == 'y':
        console.print(Panel('🔤 Please enter your domain list file name: ', title="Filename", expand=False))
        filename = input()
    else:
        console.print(Panel('🔤 Please enter your industry seed input keywords (eg. fire space strike glitch), separated by spaces: ', title="Keywords", expand=False))
        words = input().split(' ')
        console.print(Panel(f'🌀 Generating domain combinations...', title="Generating", expand=False))
        filename = generate_domain_file(words)
    results = read_file_and_check_domain(filename)
    console.print(Panel('🎉🎉🎉 All done! 💃🕺💥', title="Completion", expand=False))

run_domain_search()
