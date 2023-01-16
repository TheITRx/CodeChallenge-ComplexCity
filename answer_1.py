
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
            print(x['state'] + ',', x['city'])
            print('Interstates:', ', '.join(x['istates']))
        print('\n')


#answer_1()
print(sorted_list)
