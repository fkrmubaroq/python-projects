import math
def filter_negative_number(numbers):
    filter_data = filter(lambda num: num <= 0, numbers)
    return list(filter_data)

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print("Filter Only negative number:  ",filter_negative_number(numbers))

def flatten_list(list_of_lists):
    result = []
    for item in list_of_lists:
        if isinstance(item, list):
            for sub_item in item:
                result.append(sub_item)
        else:
            result.append(item)

    return result

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Flatten List : ",flatten_list(list_of_lists))

list_comprehension = [ (x, *(x ** p for p in range(6))) for x in range(11) ]
print("List Comprehension : ", list_comprehension)

def flatten_countries(countries):
    result = []
    for item in countries:
        if isinstance(item[0], tuple):    
            data = list(i.upper() for i in item[0])
            mid = math.floor(len(data) / 2)
            data.insert(mid, data[mid - 1][:3].upper())
            result.append(data)
        
    return result

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print("Flatten Countries : ",flatten_countries(countries))

def list_to_dict(countries):
    result = [];
    for item in countries:
        if isinstance(item[0], tuple):
            country, city = item[0]
            result.append({
                "country":country,
                "city": city
            })
    return result


print("List to dics : ", list_to_dict(countries))


# concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
def concatenated_strins(str):
    result = [];
    for item in str:
        if isinstance(item[0], tuple):
            result.append(" ".join(item[0]))

    return result

print("Concatenated Strings : ",concatenated_strins(names))
