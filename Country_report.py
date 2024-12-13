def city_country_reporter(city,country,population=''):
    if population:
        report=f"{city.title()},{country.title()} - population:{population}"
    else:
        report=f"{city.title()},{country.title()}"
    return report

