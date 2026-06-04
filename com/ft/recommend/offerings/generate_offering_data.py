import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

def long_tail_distribution(low, high, size, scale=1.5):
    return np.round(np.random.pareto(scale, size=size) * (high - low) / 5 + low, 2)

deal_types = ['real_estate', 'equity', 'debt']
risk_levels = ['low', 'medium', 'high']
liquidity_options = ['short', 'medium', 'long']
asset_classes = ['multi_family', 'self_storage', 'mixed_use', 'office']
security_types = ['common_equity', 'preferred_equity', 'mezzanine_debt', 'senior_debt']
investment_structures = ['LLC', 'LP', 'REIT']
jurisdictions = ['Delaware', 'Texas', 'California']
regions = ['Northeast', 'Southeast', 'Midwest', 'West Coast', 'Southwest']
distribution_freqs = ['monthly', 'quarterly', 'annually']
exit_strategies = ['sale', 'refinance', 'IPO']
tenant_scores = ['Excellent', 'Good', 'Fair', 'Poor']
accreditation_levels = ['accredited_only', 'open_to_all']

data = []

for i in range(10):
    irr = float(np.clip(np.random.normal(0.12, 0.03), 0.06, 0.25))
    risk = 'high' if irr > 0.15 else 'medium' if irr > 0.10 else 'low'
    holding = 'short' if irr > 0.14 else 'medium' if irr > 0.10 else 'long'
    asset_value = long_tail_distribution(5e6, 30e6, 1)[0]
    gross_income = round(asset_value * np.random.uniform(0.08, 0.12), 2)
    expense_ratio = round(np.random.uniform(0.3, 0.5), 2)
    cash_flow = round(gross_income * (1 - expense_ratio), 2)
    vacancy_rate = round(np.random.uniform(0.05, 0.15), 2)
    cash_flow_with_vacancy = round(cash_flow * (1 - vacancy_rate), 2)
    leverage = round(np.random.uniform(0.5, 0.75), 2)
    loan_amount = round(asset_value * leverage, 2)
    loan_to_value = round(loan_amount / asset_value, 2)
    capitalization_rate = round(cash_flow / asset_value, 4)
    price_per_unit = round(asset_value / 1000, 2)
    total_units = 1000
    income_per_unit = cash_flow / total_units
    cash_on_cash = round(income_per_unit / (price_per_unit * 0.3), 2)
    dscr = round(cash_flow / (loan_amount * 0.06), 2)
    noi = cash_flow
    discount_rate = round(np.random.uniform(0.07, 0.12), 2)
    growth_rate = round(np.random.uniform(0.01, 0.04), 2)
    annual_debt = round(loan_amount * 0.06, 2)
    target_multiple = round(np.random.uniform(1.6, 2.2), 2)
    average_return = round(np.random.uniform(0.08, 0.15), 2)
    break_even = round((annual_debt / gross_income), 2)
    net_op_income = noi
    volatility = round(np.random.uniform(0.1, 0.3), 2)
    sensitivity = round(np.random.uniform(0.1, 0.6), 2)
    tenant_score = random.randint(600, 850)

    row = {
        "id": 1000 + i,
        "deal_type": random.choice(deal_types),
        "required_risk_tolerance": risk,
        "liquidity_horizon": holding,
        "asset_class": random.choice(asset_classes),
        "expected_irr": round(irr * 100, 2),
        "name": " Opportunity",
        "property_class_id": random.randint(1, 5),
        "investment_strategy_type_id": random.randint(1, 4),
        "description": "",
        "target_amount": round(asset_value * 0.6, 2),
        "minimum_investment": random.choice([25000, 50000, 100000]),
        "start_date": (datetime.today() - timedelta(days=random.randint(30, 90))).date(),
        "end_date": (datetime.today() + timedelta(days=random.randint(30, 120))).date(),
        "company_id": random.randint(1, 20),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "status": random.choice(["active", "closed", "upcoming"]),
        "offering_type_id": random.randint(1, 3),
        "security_type": random.choice(security_types),
        "price_per_unit": price_per_unit,
        "total_units": total_units,
        "use_of_proceeds": "acquisition and value-add improvements",
        "investment_structure": random.choice(investment_structures),
        "risk_factors": "market volatility, liquidity risk, tenant default",
        "jurisdiction": random.choice(jurisdictions),
        "region": random.choice(regions),
        "allows_international_investors": random.choice([0, 1]),
        "investor_accreditation_requirement": random.choice(accreditation_levels),
        "target_irr": round(irr * 100, 2),
        "target_multiple": target_multiple,
        "target_holding_period": random.choice([3, 5, 7]),
        "distribution_frequency": random.choice(distribution_freqs),
        "exit_strategy": random.choice(exit_strategies),
        "term": random.choice([3, 5, 7, 10]),
        "asset_value": asset_value,
        "gross_income": gross_income,
        "cash_flow": cash_flow,
        "cash_flow_with_vacancy": cash_flow_with_vacancy,
        "leverage_ratio": leverage,
        "capitalization_rate": capitalization_rate,
        "gross_return_multiple": target_multiple,
        "occupancy_rate": round(1 - vacancy_rate, 2),
        "cash_on_cash_returns": cash_on_cash,
        "vacancy_rate": vacancy_rate,
        "break_even_occupancy": break_even,
        "expense_ratio": expense_ratio,
        "average_annual_return": average_return,
        "net_operating_income": net_op_income,
        "discount_rate": discount_rate,
        "growth_rate": growth_rate,
        "annual_debt_service": annual_debt,
        "sensitivity_factor": sensitivity,
        "volatility_factor": volatility,
        "dscr": dscr,
        "dcf": round(cash_flow / discount_rate, 2),
        "dyr": round(cash_flow / asset_value, 4),
        "tenant_credit_score": tenant_score,
        "tenant_creditworthiness": random.choice(tenant_scores),
        "economic_market_risk": round(np.random.uniform(0.1, 0.4), 2),
        "loan_amount": loan_amount,
        "loan_to_value": loan_to_value
    }

    data.append(row)

# 保存为 CSV
df = pd.DataFrame(data)
df.to_csv("synthetic_deals.csv", index=False)
