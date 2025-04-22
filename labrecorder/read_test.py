import pyxdf
import pprint

def print_channel_info(stream):
    try:
        channels = stream['info']['desc'][0]['channels'][0]['channel']
        print(f"\nChannel details:")
        for i, ch in enumerate(channels):
            label = ch.get('label', ['Unnamed'])[0]
            unit = ch.get('unit', [''])[0]
            print(f"  Channel {i + 1}: {label} ({unit})")
    except (KeyError, IndexError, TypeError):
        print("  No detailed channel info available.")

def read_xdf_file(filepath):
    print(f"Reading file: {filepath}")
    streams, fileheader = pyxdf.load_xdf(filepath)

    print("\n=== File Header ===")
    pprint.pprint(fileheader)

    for idx, stream in enumerate(streams):
        print(f"\n=== Stream {idx + 1} ===")
        print(f"Name: {stream['info']['name'][0]}")
        print(f"Type: {stream['info']['type'][0]}")
        print(f"Channel count: {stream['info']['channel_count'][0]}")
        print(f"Nominal sampling rate: {stream['info']['nominal_srate'][0]}")
        print(f"Number of samples: {len(stream['time_series'])}")
        print_channel_info(stream)

        print("\nFirst 5 samples:")
        for ts, sample in zip(stream['time_stamps'][:5], stream['time_series'][:5]):
            print(f"Time: {ts}, Sample: {sample}")

if __name__ == "__main__":
    filepath = "C:\\Users\\IEMCI-2023000236\\Documents\\artur\\labrecorder\\sub-P001_ses-S001_task-Default_run-001_eeg.xdf"  # Change this to your actual file path
    read_xdf_file(filepath)
