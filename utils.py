
# -----------------------------
# تابع تبدیل آدرس به one-hot
# -----------------------------
def encode_country(value, columns):
    # فقط ستون‌های آدرس را پیدا کن و مرتب کن
    address_cols = sorted([c for c in columns if c in country_list])
    encoded = {col: 0 for col in address_cols}
    if value in encoded:
        encoded[value] = 1
    return encoded


def encode_edlevel(value, columns):
    # فقط ستون‌های آدرس را پیدا کن و مرتب کن
    address_cols = sorted([c for c in columns if c in edlevel_list])
    encoded = {col: 0 for col in address_cols}
    if value in encoded:
        encoded[value] = 1
    return encoded

columns=["YearsCodePro"]

country_list =['United Kingdom of Great Britain and Northern Ireland', 'Israel',
       'Netherlands', 'United States of America', 'Czech Republic',
       'Austria', 'Italy', 'Canada', 'Germany', 'Poland', 'Norway',
       'France', 'Brazil', 'Sweden', 'Spain', 'Turkey', 'India',
       'Belgium', 'Mexico', 'Switzerland', 'South Africa', 'Finland',
       'Denmark', 'Australia', 'Greece', 'Portugal',
       'Iran, Islamic Republic of...', 'Russian Federation', 'Pakistan',
       'New Zealand']


edlevel_list =['Master’s degree', 'Bachelor’s degree', 'Less than a Bachelors','Post grad']
