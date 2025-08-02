# Day 5 - Lists

#1
empty_list = []

#2
five_list = ["one", "two", "three", "four", "five"]

#3
print(len(five_list))

#4
print(five_list[0])
print(five_list[2])
print(five_list[-1])

#5
kilian = ["Kilian", 19, 1.92, "Good", "Germany"]

#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7
print(it_companies)

#8
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

#9
it_companies[0] = "Meta"
print(it_companies)

#11
it_companies.append("KIT")

#12
it_companies.insert(3, "3KIT")

#13
it_companies[0] = it_companies[0].upper()

#14
new_list = it_companies + ["#; "]
print(new_list)

#15
check_list = "Apple" in it_companies
print(check_list)

#16
it_companies.sort()
print(it_companies)

#17
it_companies.reverse()
print(it_companies)

#18
print(it_companies[0:3])

#19
print(it_companies[-3:])

#20
print(it_companies[3:6])

#21
del it_companies[0]
print(it_companies)

#22
del it_companies[4]

#23
it_companies.pop()
print(it_companies)

#24
del it_companies[:]
print(it_companies)

#25
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_end = front_end + back_end
print(full_end)

#27
full_stack = full_end.copy()
index = full_stack.index("Redux")
full_stack.insert(index+1, "Python")
full_stack.insert(index+2, "SQL")
print(full_stack)

# Level 2

#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#2
ages.sort()
print(ages[0])
print(ages[-1])
print(min(ages))
ages.append(ages[0])
ages.append(ages[-1])
ages.sort()
print(ages)
median_age = ages[5]
print(median_age)

all_ages = 0
for age in ages:
    all_ages += age
    print(all_ages)

average_age = all_ages / len(ages)
print(average_age)

print(max(ages)-min(ages))

value_one = abs(min(ages) - average_age)
value_two = abs(max(ages) - average_age)
print(f"Min - Average: {value_one} Max - Average: {value_two}")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

print(len(countries))
middle_index = len(countries) // 2
print(countries[middle_index])
countries_first = countries[:middle_index+1]
countries_second = countries[middle_index+1:]
print(len(countries_first))
print(len(countries_second))
