from collections import Counter
from multiprocessing import Pool

def map_function(segment):
    letter_counts = Counter(filter(str.isalpha, segment.lower()))
    return letter_counts

def reduce_function(counts_list):
    combined_counts = Counter()
    for counts in counts_list:
        combined_counts.update(counts)
    return combined_counts

if __name__ == "__main__": 
    text_data = "Example text data for map-reduce. Count the frequency of each letter, ignoring case."
    
    num_processes = 4
    segment_size = len(text_data) // num_processes
    segments = [text_data[i:i + segment_size] for i in range(0, len(text_data), segment_size)]
    
    with Pool(processes=num_processes) as pool:
        mapped_counts = pool.map(map_function, segments)

    final_counts = reduce_function(mapped_counts)

    for letter, count in sorted(final_counts.items()):
        print(f"{letter}: {count}")