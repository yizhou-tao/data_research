#!/usr/bin/python
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()

# 固定选项集
investor_types = ['Individual', 'Joint', 'Trust', 'Entity']
#investment_profiles = ['Family Office', 'Registered Investment Advisor', 'Limited Partner']
lead_sources = ['Referral', 'Conference', 'Advertising', 'Website', 'Partner']
languages = ['English', 'Spanish', 'French', 'German', 'Chinese']
risk_bands = ['low', 'med', 'high']
liquidity_prefs = ['Short-term', 'Medium-term', 'Long-term']
investment_exp = ['Beginner', 'Intermediate', 'Advanced', 'Expert']
institution_types = ['Bank', 'Fund', 'Family Office', 'Corporation', 'Endowment']
tax_reporting_types = ['Simple', 'Complex', 'International']
fatca_classes = ['FATCA Compliant', 'Non-Compliant', 'Exempt']
crs_classes = ['CRS Reportable', 'Non-Reportable']
investment_vehicles = ['Stocks', 'Bonds', 'REITs', 'Private Equity', 'VC']
client_classes = ['Standard', 'Premium', 'VIP']
life_events = ['Marriage', 'Divorce', 'Retirement', 'Inheritance', 'None']
behavior_profiles = ['reactive', 'long-term', 'short-term', 'contrarian']
asset_types = ['Equities', 'Fixed Income', 'Real Estate', 'Private Equity', 'VC']
us_regions = [
    "Silicon Valley, CA", "New York Metro, NY", "Boston, MA", "Austin, TX", "Miami, FL",
    "Chicago, IL", "Seattle, WA", "Denver, CO", "Atlanta, GA", "Research Triangle, NC"
]

def generate_valid_us_phone():
    return f"1{random.randint(200, 999)}{random.randint(200, 999)}{random.randint(1000, 9999)}"

# 风险等级与逻辑映射
risk_band_options = {
    'low': {'score_range': (1, 3), 'goals': ['Preservation', 'Balanced'], 'liquidity': ['Long-term', 'Medium-term']},
    'med': {'score_range': (4, 6), 'goals': ['Income', 'Balanced'], 'liquidity': ['Medium-term']},
    'high': {'score_range': (7, 10), 'goals': ['Growth', 'Balanced'], 'liquidity': ['Short-term']}
}

# 生成数据
rows = []
for i in range(1, 10000):
    risk_band = np.random.choice(risk_bands)
    risk_score = random.randint(*risk_band_options[risk_band]['score_range'])
    goal = np.random.choice(risk_band_options[risk_band]['goals'])
    liquidity = np.random.choice(risk_band_options[risk_band]['liquidity'])

    is_institutional = np.random.choice([True, False], p=[0.3, 0.7])
    investor_type = np.random.choice(['Entity', 'Trust'] if is_institutional else ['Individual', 'Joint'])
    investment_profile = investor_type

    is_accredited = True if risk_score > 0 else False
    institution_name = fake.company() if is_institutional else None
    institution_type = np.random.choice(institution_types) if is_institutional else None

    dob = fake.date_of_birth(minimum_age=25, maximum_age=80)
    created = fake.date_time_between(start_date='-5y', end_date='now')
    updated = fake.date_time_between(start_date=created, end_date='now')
    qualified = fake.date_time_between(start_date=created, end_date='now') if is_accredited else None
    activated = fake.date_time_between(start_date=created, end_date='now')
    invested = fake.date_time_between(start_date=activated, end_date='now') if np.random.random() > 0.2 else None

    row = {
        'id': 10000 + i,
        ####### key features for users investment###########
        'irr_target': round(np.random.uniform(20, 60), 2)/100,
        'risk_tolerance_type_id': np.random.choice([1, 2, 3, 4], p=[0.6, 0.2, 0.15, 0.05]),
        'liquidity_preference': np.random.choice(liquidity_prefs),
        'investor_type': np.random.choice(investor_types),
        'investment_profile': np.random.choice(investor_types),
        'preferred_regions': ', '.join(random.sample(us_regions, np.random.randint(1, 2))),
        'preferred_asset_types': ', '.join(random.sample(asset_types, np.random.randint(1, 3))),
        'portfolio_construction_goals': goal,
        'behavioral_profile': np.random.choice(behavior_profiles),
        #########################################################
        'ticket_size_range': np.random.choice([5000, 25000, 100000, 500000, 1000000]),
        'date_of_birth': dob.strftime('%Y-%m-%d'),
        'email': fake.email(),
        'created_at': created.strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': updated.strftime('%Y-%m-%d %H:%M:%S'),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'phone': generate_valid_us_phone(),
        'country_code': "U.S.",
        'investment_stage_type_id': np.random.choice([1, 2, 3, 4]),
        'time_zone': np.random.choice([
            'America/New_York', 'America/Chicago', 'America/Denver',
            'America/Los_Angeles', 'America/Phoenix', 'America/Anchorage', 'America/Honolulu'
        ]),
        'investing_as_us_entity': np.random.choice([True, False], p=[0.7, 0.3]),
        'qualified_at': qualified.strftime('%Y-%m-%d %H:%M:%S') if qualified else None,
        'activated_at': activated.strftime('%Y-%m-%d %H:%M:%S'),
        'invested_at': invested.strftime('%Y-%m-%d %H:%M:%S') if invested else None,
        'lead_source': np.random.choice(lead_sources),
        'preferred_language': np.random.choice(languages),
        'years_of_investment_experience': min(20, int(np.random.exponential(scale=5))),
        'is_accredited_investor': is_accredited,
        'referral_source': fake.name() if np.random.random() > 0.7 else None,
        'risk_score': risk_score,
        'investment_experience': np.random.choice(investment_exp),
        'is_institutional_investor': is_institutional,
        'institution_name': institution_name,
        'institution_type': institution_type,
        'assets_under_management': round(np.random.uniform(100000, 10000000), 2),
        'requires_special_reporting': np.random.choice([True, False], p=[0.2, 0.8]),
        'tax_reporting_type': np.random.choice(tax_reporting_types),
        'is_subject_to_fatca': True,
        'fatca_classification': np.random.choice(fatca_classes),
        'is_subject_to_crs': True,
        'crs_classification': np.random.choice(crs_classes),
        'preferred_investment_vehicles': ', '.join(np.random.choice(investment_vehicles, size=np.random.randint(1, 4), replace=False)),
        'interested_in_private_placements': np.random.choice([True, False]),
        'interested_in_secondary_market': np.random.choice([True, False]),
        'has_offshore_accounts': np.random.choice([True, False]),
        'offshore_account_jurisdictions': fake.country() if np.random.random() > 0.7 else None,
        'is_professional_investor': np.random.choice([True, False]),
        'professional_investor_classification': np.random.choice(['Category I', 'Category II']),
        'professional_investor_expiry_date': (datetime.now() + timedelta(days=np.random.randint(100, 1000))).strftime('%Y-%m-%d'),
        'is_interested_in_impact_investing': np.random.choice([True, False]),
        'client_classification': np.random.choice(client_classes),
        'is_employee_of_financial_institution': np.random.choice([True, False]),
        'ml_risk_tolerance_type_id': np.random.choice([1, 2, 3, 4]),
        'life_events': np.random.choice(life_events),
        'risk_tolerance_band': risk_band
    }

    rows.append(row)

# 输出 CSV
df = pd.DataFrame(rows)
df.to_csv("fixed_investor_data_10000_rows.csv", index=False)
