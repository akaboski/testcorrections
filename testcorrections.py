def count_unique_proteins(protein_list):
    return len(set([protein.split(".")[0] for protein in protein_list]))


def count_proteins(protein_list):
    family_dict = {}
    for protein in protein_list:
        family = protein.split(".")[0]
        if family in family_dict:
            family_dict[family] += 1
        else:
            family_dict[family] = 1
    return family_dict


def merge_protein_counts(dict1, dict2):
    dict3 = {}
    for family, count in dict1.items():
        if family in dict2:
            dict3[family] = (count, dict2[family])
        else:
            dict3[family] = (count, 0)
    for family, count in dict2.items():
        if family not in dict1:
            dict3[family] = (0, count)
    return dict3


def dates_to_iso8601(dates):
    MONTHS = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    dates_new = []
    for date in dates:
        month = MONTHS[date.split()[0]]
        day = date.split(",")[0][-2:].replace(" ", "0").strip()
        year = date.split()[2]
        dates_new.append(year + "-" + month + "-" + day)
    return dates_new


def sort_dates(dates):
    dates_isos = dates_to_iso8601(dates)
    dates_sorted = []
    for n in range(len(dates)):
        dates_sorted.append(dates_isos[n] + dates[n])
    dates_sorted.sort()
    return [date[10:] for date in dates_sorted]