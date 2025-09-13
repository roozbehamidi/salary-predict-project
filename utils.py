
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

country_list =['United Kingdom of Great Britain and Northern Ireland' 'Israel'
 'Netherlands' 'United States of America' 'Czech Republic' 'Austria'
 'Italy' 'Canada' 'Germany' 'Ireland' 'Poland' 'Madagascar' 'Norway'
 'Taiwan' 'France' 'Brazil' 'Uruguay' 'Sweden' 'Spain' 'Turkey' 'Romania'
 'Singapore' 'India' 'Belgium' 'Bulgaria' 'Greece' 'Portugal'
 'Russian Federation' 'Saudi Arabia' 'Mexico' 'Kenya' 'Switzerland'
 'Latvia' 'South Africa' 'Thailand' 'China' 'Montenegro' 'Finland'
 'Slovakia' 'Japan' 'Denmark' 'Australia' 'Viet Nam' 'Argentina' 'Hungary'
 'Tunisia' 'Bangladesh' 'Ukraine' 'Maldives' 'Hong Kong (S.A.R.)' 'Egypt'
 'Serbia' 'Pakistan' 'Nepal' 'Croatia' 'Indonesia'
 'Bosnia and Herzegovina' 'Armenia' 'Lithuania'
 'Iran, Islamic Republic of...' 'Belarus' 'Costa Rica' 'Mauritius'
 'Estonia' 'Kazakhstan' 'Morocco' 'Philippines' 'Chile' 'New Zealand'
 'Slovenia' 'Ecuador' 'Cyprus' 'Peru' 'Colombia' 'Afghanistan' 'Nicaragua'
 'Andorra' 'Republic of Korea' 'Lebanon' 'South Korea' 'Malaysia'
 'Sri Lanka' 'Guatemala' 'Jordan' 'Azerbaijan' 'United Arab Emirates'
 'Qatar' 'Nigeria' 'Uzbekistan' 'Ethiopia' 'Luxembourg'
 'The former Yugoslav Republic of Macedonia' 'Syrian Arab Republic'
 'Cambodia' 'Fiji' 'Albania' 'Mongolia' 'Republic of Moldova' 'Tajikistan'
 'Timor-Leste' 'Ghana' 'United Republic of Tanzania' 'Algeria' 'Cameroon'
 'Kosovo' 'Georgia' 'Turkmenistan' 'Botswana' 'Myanmar' 'Palestine'
 'Senegal' 'Dominican Republic' 'Rwanda' 'Malta'
 'Venezuela, Bolivarian Republic of...' 'Cuba' 'Kuwait' 'El Salvador'
 'Bolivia' 'Isle of Man' 'Honduras' 'Mali' 'Panama'
 "Lao People's Democratic Republic" 'Iceland' 'Bahrain' 'Paraguay'
 'Uganda' 'Democratic Republic of the Congo' 'Benin' "Côte d'Ivoire"
 'Barbados' 'Kyrgyzstan' 'Nomadic' 'Iraq' 'Congo, Republic of the...'
 'Libyan Arab Jamahiriya' 'Mozambique' 'Angola' 'Oman' 'Yemen' 'Sudan'
 'Zambia' 'Somalia' 'Guinea' 'Zimbabwe' 'Cape Verde' 'Trinidad and Tobago'
 'Bhutan' 'Togo' 'Suriname' 'Jamaica' 'Haiti' 'Malawi' 'Guyana' 'Palau'
 'Monaco' 'Saint Lucia' 'Seychelles']

edlevel_list =['Master’s degree', 'Bachelor’s degree', 'Less than a Bachelors','Post grad']