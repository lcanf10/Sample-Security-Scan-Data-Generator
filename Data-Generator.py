import pandas as pd
from datetime import datetime, timedelta
import random
import os

# Generate a common pool of IP addresses
common_ip_pool = [f'192.168.{random.randint(1, 254)}.{random.randint(1, 254)}' for _ in range(50)]

def generate_ip_addresses_from_pool(num_records, pool):
    return random.sample(pool, min(num_records, len(pool)))

def generate_vulnerabilities(num_records):
    return [f'CVE-202{random.randint(0, 2)}-{random.randint(1000, 9999)}' for _ in range(num_records)]

def generate_dates(start_days_ago, end_days_ago, num_records):
    return [(datetime.now() - timedelta(days=random.randint(start_days_ago, end_days_ago))) for _ in range(num_records)]

def generate_acas_data(num_records=10):
    return pd.DataFrame({
        'host_ip': generate_ip_addresses_from_pool(num_records, common_ip_pool),
        'vulnerability': generate_vulnerabilities(num_records),
        'severity': [random.choice(['High', 'Critical', 'Medium', 'Low']) for _ in range(num_records)],
        'scan_date': generate_dates(1, 7, num_records)
    })

def generate_hbss_data(num_records=10):
    return pd.DataFrame({
        'host_ip': generate_ip_addresses_from_pool(num_records, common_ip_pool),
        'status': [random.choice(['Mitigated', 'Not Mitigated']) for _ in range(num_records)],
        'scan_date': generate_dates(1, 7, num_records)
    })

def generate_ad_data(num_records=10):
    return pd.DataFrame({
        'user_id': [f'user{i}' for i in range(1, num_records + 1)],
        'ip_address': generate_ip_addresses_from_pool(num_records, common_ip_pool),
        'last_logon': generate_dates(1, 60, num_records),
        'status': [random.choice(['Active', 'Inactive']) for _ in range(num_records)]
    })

def save_data(data, filename, valid_path):
    if not os.path.exists(valid_path):
        os.makedirs(valid_path)
    full_path = os.path.join(valid_path, filename)
    data.to_csv(full_path, index=False)
    print(f'{filename} saved successfully at {full_path}.')

valid_path = "/home/user/Desktop/"  # Adjust as needed

# Generate sample data
acas_data = generate_acas_data()
hbss_data = generate_hbss_data()
ad_data = generate_ad_data()

# Save sample data to CSV files
save_data(acas_data, 'acas_sample.csv', valid_path)
save_data(hbss_data, 'hbss_sample.csv', valid_path)
save_data(ad_data, 'ad_scan_sample.csv', valid_path)
