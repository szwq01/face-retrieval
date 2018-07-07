import random


def get_next_iteration_random(no, selected_photo, states, max_iteration_faces):
    photos = states.keys()
    if no == 0:
        for photo in photos:
            state = states[photo]
            state['selected'] = False
            state['shown'] = 0
    if no != 0:
        states[selected_photo]['selected'] = True
    filtered_photos = filter(
        lambda x: not states[x]['selected'], photos)
    samples = random.sample(list(filtered_photos), max_iteration_faces)
    for photo in samples:
        state = states[photo]
        state['shown'] += 1
    return samples


def get_next_iteration_similarity(no, selected_photo, states, max_iteration_faces, distance_path):
    print(distance_path)
    with open(distance_path,'r') as f:
        file_list = f.readline()
        
    photos = states.keys()
    if no == 0:
        for photo in photos:
            state = states[photo]
            state['selected'] = False
            state['shown'] = 0
    if no != 0:
        states[selected_photo]['selected'] = True
    filtered_photos = filter(
        lambda x: not states[x]['selected'], photos)
    samples = random.sample(list(filtered_photos), max_iteration_faces)
    for photo in samples:
        state = states[photo]
        state['shown'] += 1
    return samples


def get_next_iteration_(no, max_iteration_faces, selected_photo, states, distances):
    pass
