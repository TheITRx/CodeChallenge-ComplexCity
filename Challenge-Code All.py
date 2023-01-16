
objify = []

with open('input.txt','r') as input_file:
    for line in input_file:
        spl = line.split('|')
        objify.append(
            {
                'population': int(spl[0]),
                'city' : spl[1],
                'state' : spl[2],
                'istates': sorted(spl[3].replace('\n', '').split(';'))
            }
        )

# create a good well structured data
# output structure --> https://pastebin.com/K9TLFeqK
sorted_list = sorted(objify, key=lambda d: d['population'], reverse=True)

#region answer_1
sorted_list_by_population = {}

for item in sorted_list:
    if item['population'] in sorted_list_by_population:
        sorted_list_by_population[item['population']].append(item)
    else:
        sorted_list_by_population[item['population']] = [item]


sorted_list_by_state = {}

for k, v in sorted_list_by_population.items():
    sorted_list_by_state[k] = sorted(v, key=lambda x : (x['state'], x['city']))


def answer_1():
    for k, v in sorted_list_by_state.items():
        print(k)
        for x in v:
            print(x['city'] + ',', x['state'])
            print('Interstates:', ', '.join(x['istates']))
        print('\n')


#endregion answer_1


#region answer_2

istates_cities = {}

for item in sorted_list:
    for istate in item['istates']:
        if istate not in istates_cities:
            istates_cities[istate] = {
                'cities': list()
            }    
        istates_cities[istate]['cities'].append(item['city'])

istates_cities_sorted = {}
for state in sorted(list(istates_cities.keys()), key=lambda x: int(x[2:])):
    istates_cities_sorted[state] = istates_cities[state]

def answer_2():
    for k, v in istates_cities_sorted.items():
        print(k, len(v['cities']))



#endregion answer_2

#region answer_3
ans_3_data = sorted_list
reference_city = 'Chicago'
result_holder = {}


for item in sorted_list:
    if item['city'] == reference_city:
        reference_city = item
        break

for degree in range(1,99):
    if not ans_3_data:
        break

    index = 0
    for item in ans_3_data:
        if item['city'] == reference_city['city']:
            result_holder[0] = [item]
            ans_3_data.pop(index)
        else:
            degree_check = set(reference_city['istates']).intersection(
                set(item['istates']))

            if degree_check:
                if degree not in result_holder:
                    result_holder[degree] = [item]
                else:
                    result_holder[degree].append(item)
                ans_3_data.pop(index)
            else:
                index += 1
                continue

        index += 1
    
    if degree not in result_holder:
        result_holder[-1] = ans_3_data
        break

    joined_degree = []
    for this_degree in result_holder[degree]:
        joined_degree += this_degree['istates']

    reference_city['istates'] = joined_degree

result_holder_deg_sorted = {}


def answer_3():
    for degree, city in reversed(result_holder.items()):
        for item in city:
            print(degree, item['city'] + ', ' + item['state'])



#endregion answer_3

# call answers
#answer_1()
#answer_2()
answer_3()
