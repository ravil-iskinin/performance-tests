import asyncio
import httpx


async def fetch_url(url: str):
    async with httpx.AsyncClient() as client:
        print("request")
        response = await client.get(url)
        print("response")
        return response.status_code, response.text[:50]


async def main():
    urls = [
        "https://echo.getpostman.com/delay/1",
        "https://echo.getpostman.com/delay/2",
        "https://echo.getpostman.com/delay/3"
    ]

    results = await asyncio.gather(*(fetch_url(url) for url in urls))
    for status, text in results:
        print(f"Статус ответа: {status}, начало текста: {text}")

if __name__ == "__main__":
    asyncio.run(main())
