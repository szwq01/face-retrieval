import random


def get_next_iteration_random(no, selected_photo, states, max_iteration_faces=16):
    photos = states.keys()
    if no == 0:
        for photo in photos:
            state = states[photo]
            state['selected'] = False
            state['shown'] = 0
    if no != 0:
        states[selected_photo]['selected'] = True
    print(states)
    filtered_photos = filter(
        lambda x: not states[x]['selected'], photos)
    samples = random.sample(list(filtered_photos), max_iteration_faces)
    for photo in samples:
        state = states[photo]
        state['shown'] += 1
    return samples


def get_next_iteration_most_similar(no, max_iteration_faces, selected_photo, states, distances):
    pass
