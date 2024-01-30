from fastapi import FastAPI


app = FastAPI()


@app.get("/swamp")
def read_root():
    return {
        "swamp_biome": [
            {
                "name": "Algae"
            },
            {
                "name": "Cattails"
            },
            {
                "name": "Cypress Trees"
            }
        ]
    }




## start the server
# uvicorn server:app --reload