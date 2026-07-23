"""
Extract evenly-spaced frames from a video for MLLM analysis.
Usage: python extract_frames.py <video_path> <output_folder> [num_frames]
"""

import cv2
import os
import sys
from pathlib import Path

def extract_frames(video_path, output_folder, num_frames=6):
    """Extract N evenly-spaced frames from a video."""
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        print(f"Error: Could not open {video_path}")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = total_frames / fps if fps > 0 else 0

    print(f"Video: {Path(video_path).name}")
    print(f"  Total frames: {total_frames}")
    print(f"  FPS: {fps:.2f}")
    print(f"  Duration: {duration:.2f}s")

    # Get frame indices at evenly-spaced intervals
    # Skip the very first and very last frame (often black or fade-in)
    step = (total_frames - 2) / (num_frames - 1)
    frame_indices = [int(1 + i * step) for i in range(num_frames)]

    video_stem = Path(video_path).stem

    for i, frame_idx in enumerate(frame_indices):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if ret:
            timestamp = frame_idx / fps if fps > 0 else 0
            output_path = os.path.join(
                output_folder,
                f"{video_stem}_frame{i+1:02d}_t{timestamp:.2f}s.jpg"
            )
            cv2.imwrite(output_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
            print(f"  Saved: frame {i+1}/{num_frames} at t={timestamp:.2f}s")

    cap.release()
    print(f"Extraction complete. {num_frames} frames saved to {output_folder}\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_frames.py <video_path> <output_folder> [num_frames]")
        sys.exit(1)

    video_path = sys.argv[1]
    output_folder = sys.argv[2]
    num_frames = int(sys.argv[3]) if len(sys.argv) > 3 else 6

    extract_frames(video_path, output_folder, num_frames)