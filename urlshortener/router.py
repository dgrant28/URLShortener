
import secrets
import string
from fastapi import APIRouter
from urlshortener.models import CreateUrlShortener, CreateUrlShortenerResponse
from urlshortener.database import MockDBOperations
from starlette.responses import RedirectResponse


# Create the router
urlshortener = APIRouter()

# Create database
mock_db_operations = MockDBOperations()

# Create the short url
# This function is used to generate the short url
# Returns the CreatedUrlShortenerResponse


@urlshortener.post("/create", response_model=CreateUrlShortenerResponse)
async def create(shortener: CreateUrlShortener):
    # Generate a random string of 7 characters
    short_url_length = 7
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                  for i in range(short_url_length))

    # Convert to string
    short_url = str(res)
    # Add the url to database
    status = await mock_db_operations.add_data_to_db(url=shortener.url, short_url=short_url)
    # If the url is added to the database, return the short url
    if status:
        return CreateUrlShortenerResponse(short_url=short_url, url=shortener.url)
    else:
        # If the url is not the added to the database, return the error message
        return CreateUrlShortenerResponse(short_url="", url="")

# Get urls from the database


@urlshortener.get("/list", response_model=list[CreateUrlShortenerResponse])
async def list():
    # Get the data from the database
    data = await mock_db_operations.fetch_all_data()
    # Create a list of CreateUrlShortenerResponse
    arr = []
    # Loop through the data
    for key, value in data.items():
        # Add the data to the list
        arr.append(CreateUrlShortenerResponse(short_url=key, url=value))
        # Return the list
        return arr

# Delete the url from the database


@urlshortener.delete("/delete/{short_url}")
async def delete_short_url(short_url: str):
    # Delete the url from the database
    status = await mock_db_operations.delete_data_from_db(short_url=short_url)
    # If the url is deleted from the database, return the status
    if status:
        return {"message": "Successfully deleted"}
    else:
        # If the url is not dleted from the database, return the error message
        return {"message": "Failed to delete"}

# Redirect the user to the original url


@urlshortener.get("/test/{short_url}")
async def test(short_url: str):
    # Get the url from the database
    data = await mock_db_operations.fetch_all_data()
    # Check if the url exists in the database
    if short_url in data:
        # Check if the url exists in the database
        url = data[short_url]
        # return the redirect response
        response = RedirectResponse(url=url)
        return response
    else:
        # return the error message
        return {"message": "Failed to fetch"}
