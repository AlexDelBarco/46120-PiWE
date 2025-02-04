### 1

def greet(name):
    print(f"Hello, {name}")


### 2

def goldilocks(num):
    if num <= 140:
        print('Too small!')
    if num >= 150:
        print('Too large!')
    if num > 140 and num < 150:
        print('Just right. :)')


### 3

def fibonacci_stop(num):
    if num < 1:
        return []

    fib_sequence = [1, 1]
    while True:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        if next_value > num:
            break
        fib_sequence.append(next_value)

    return fib_sequence if num > 1 else [1]

### 4

def clean_pitch(pitch_angles, statuses):
    cleaned_angles = []

    for i in range(len(pitch_angles)):
        pitch = pitch_angles[i]
        status = statuses[i]

        if (pitch < 0 or pitch > 90) and status > 0:
            cleaned_angles.append(-999)
        else:
            cleaned_angles.append(pitch)

    return cleaned_angles

#Example
pitch_angles = [45, 92, 85, 130, 70]
statuses = [0, 1, 0, 2, 0]


### 5


print('end')