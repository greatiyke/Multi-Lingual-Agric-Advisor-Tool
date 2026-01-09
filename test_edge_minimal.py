import asyncio
import edge_tts

async def main():
    voice = "en-NG-EzinneNeural"
    text = "Hello"
    output = "minimal.mp3"
    print(f"Generating {output}...")
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output)
    print("Done.")

if __name__ == "__main__":
    asyncio.run(main())
