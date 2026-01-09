import argparse
import asyncio
import edge_tts
import sys

async def generate(text, voice, output_file):
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)
        return True
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True)
    parser.add_argument("--voice", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    # On Windows, Proactor is default for 3.8+
    try:
        asyncio.run(generate(args.text, args.voice, args.output))
    except Exception as e:
        print(f"Asyncio Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
