from collections import deque

food_portions = deque(map(int, input().split(', ')))
stamina = deque(map(int, input().split(', ')))

peaks = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70,
}

peaks_queue = deque(peak for peak in peaks)

climbed_peaks = 0
name_of_conquered_peaks = []

while (food_portions and stamina) and peaks_queue:

    curr_peak = peaks_queue.popleft()
    daily_food = food_portions.pop()
    daily_stamina = stamina.popleft()
    data = daily_food + daily_stamina

    if data >= peaks[curr_peak]:
        climbed_peaks += 1
        name_of_conquered_peaks.append(curr_peak)

    elif data < peaks[curr_peak]:
        peaks_queue.appendleft(curr_peak)


if len(peaks) == name_of_conquered_peaks:
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')
if name_of_conquered_peaks:
    print('Conquered peaks:')
    print(*name_of_conquered_peaks, sep='\n')
