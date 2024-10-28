import argparse
import subprocess
import os

def processOneVideo(video_path: str):
    command = [
        "ffmpeg",
        "-v",
        "error",  # Show only errors
        "-i",
        video_path,  # Input file
        "-f",
        "null",
        "-",  # Null output
    ]

    # Run the command and capture stderr (error log)
    result = subprocess.run(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    # Decode error log to a string and return it
    error_log = result.stderr.decode("utf-8")
    return error_log


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Detect Corrupt Video",
        description="ffmpeg cli wrapper to easily check video corruption.",
        add_help=True,
    )

    parser.add_argument(
        "-d", "--directory", help="Checks video files inside given directory."
    )
    parser.add_argument("-r", "--recurse", help="Recurse through subdirectories.")
    parser.add_argument("-f", "--file", help="Singular video file to check.")

    args = parser.parse_args()

    if args.file is not None:
        print(processOneVideo(args.file))
