# Sample-Security-Scan-Data-Generator

Overview

This Python script generates simulated security scan data for network assessments, including ACAS scans, HBSS scans, and Active Directory (AD) scans. Designed to help cybersecurity professionals and enthusiasts, it offers a practical tool for generating realistic datasets. These datasets can be used for testing, training, or demonstration purposes in various security and IT infrastructure contexts. The script creates overlap in IP addresses across scans to reflect real-world network scenarios, enhancing the authenticity of the data for analytical exercises.
Features

    ACAS Scan Data Generation: Simulates vulnerability scan results with varied severities and CVEs.
    HBSS Scan Data Generation: Generates host-based security system scan outcomes, including mitigation statuses.
    AD Scan Data Generation: Creates user activity logs within an Active Directory environment, complete with IP addresses and login timestamps.
    Realistic Data Simulation: Ensures IP address overlap across datasets to mimic actual network environments.

Requirements

    Python 3.6+
    pandas

Installation

First, ensure Python 3.6 or newer is installed on your machine. Python can be downloaded from the official website: https://www.python.org/downloads/.

Then, install the required Python packages using the following command:

bash

pip install pandas

Usage

To use the script:

    Modify Output Directory: Open the script in a text editor and adjust the valid_path variable to your desired output directory for the CSV files.

    Run the Script: Execute the script from your terminal or command prompt:

bash

python /path/to/generate_sample_scans.py

Replace /path/to/ with the actual directory path where the script is saved.

    Check the Output: Upon successful execution, the script generates three CSV files:
        acas_sample.csv: Contains ACAS scan data.
        hbss_sample.csv: Contains HBSS scan data.
        ad_scan_sample.csv: Contains AD scan data.

Each file will be saved in the directory specified by the valid_path variable.
Customization

You can customize the script to generate different amounts of data or to simulate different scenarios by adjusting the num_records parameter within each function. Additionally, you can modify the IP address generation logic if you need a specific subnet or range.
Contributing

Contributions are welcome! If you have suggestions for improving this script or have developed features that could benefit others, please feel free to share. Fork this repository, commit your changes, and open a pull request.

This tool was developed to support the cybersecurity community, offering a free resource for training, testing, and research purposes. I hope it serves your needs effectively.
