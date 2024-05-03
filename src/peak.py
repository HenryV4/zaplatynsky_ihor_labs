def find_the_longest_peak(arr):
    el_pos = 1
    peak_start = None
    peak_end = None
    longest_peak_sequence = []
    longest_peak_length = 0
    while el_pos < len(arr) - 1:
        if arr[el_pos - 1] < arr[el_pos] > arr[el_pos + 1]:
            peak_start = el_pos - 1
            peak_end = el_pos + 1

            left = peak_start - 1
            while left >= 0 and arr[left] < arr[peak_start]:
                peak_start = left
                left -= 1

            right = peak_end + 1
            while right < len(arr) and arr[right] < arr[peak_end]:
                peak_end = right
                right += 1

            peak_sequence = arr[peak_start : peak_end + 1]

            if len(peak_sequence) > longest_peak_length:
                longest_peak_length = len(peak_sequence)
                longest_peak_sequence = peak_sequence

        el_pos += 1

    return longest_peak_sequence


arr = [4, 5, 3, 5, 6, 7, 4, 3, 10, 1, 6, 8, 10, 3, 3, 5, 7, 4, 3, 8, 3]
print(find_the_longest_peak(arr))
