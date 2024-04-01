import pandas as pd

m_camp_path = './input_data/marketing_campaign.csv'
m_camp_df = pd.read_csv(m_camp_path)

sbscrbs_path = './input_data/subscribers.csv'
sbscrbs_df = pd.read_csv(sbscrbs_path)

users_path = './input_data/users.csv'
users_df = pd.read_csv(users_path)

print(m_camp_df)
print(sbscrbs_df)
print(users_df)
