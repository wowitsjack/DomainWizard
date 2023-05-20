# 🌐 Domain Search Wizard 🔮

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)]
![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)

Domain Search Wizard is a powerful, fun, and interactive command-line interface (CLI) tool that helps you find available domain names based on 'seed' input words that you vibe with. 💡🔍



## 🎩 Features

- User-friendly interactive wizard 🧙‍♂️
- Domain availability checks across multiple TLDs 🌐
- Optional domain list input 📝
- Permutation generation for terms, words, or phrases you like 🔄
- Beautiful progress updates with Rich 🎨
- Error handling for timed-out or failed checks ⏱️
- Result output to your chosen file 📂

## 🚀 Getting Started

Clone the repository and install the required Python packages.

\```bash
git clone https://github.com/username/DomainSearchWizard.git
cd DomainSearchWizard
pip install -r requirements.txt
\```

Run the script.

\```bash
python domain_search_wizard.py
\```

Follow the prompts in the interactive wizard. You can either provide a pre-made domain list, or enter industry buzzwords for domain permutation generation.

## ⚙️ How it Works

Domain Search Wizard uses several methods to check domain registration:

- **DNS Records**: Checks for `A`, `MX`, and `TXT` records.
- **SSL Certificates**: Checks for SSL certificates associated with the domain.
- **WHOIS Lookup**: Checks the WHOIS data for the domain.

If a domain check times out or fails, Domain Search Wizard will log a message and move on to the next domain.

## 💼 License

This project is licensed under the terms of the MIT license.

## 🤝 Contributing

We welcome contributions! Please see `CONTRIBUTING.md` for details on how to contribute.
