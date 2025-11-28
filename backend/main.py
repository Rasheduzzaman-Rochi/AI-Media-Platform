from fastapi import FastAPI
from routers import f1_sentiment, f2_recommend, f3_translate, f4_safety, f5_insights, f6_summary

app = FastAPI()

# Connect the routers (Features)
app.include_router(f1_sentiment.router)
app.include_router(f2_recommend.router)
app.include_router(f3_translate.router)
app.include_router(f4_safety.router)
app.include_router(f5_insights.router)
app.include_router(f6_summary.router)

@app.get("/")
def read_root():
    return {"message": "AI Media Platform Backend is Running!"}