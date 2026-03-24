from fastapi import FastAPI 
from VDIIM import load_and_process_data 

app = FastAPI() 

df, daily_df = load_and_process_data() 

@app.get("/") 
def home(): 
    return {"message": "Nifty Volatility API is running"} 

@app.get("/test") 
def test(): 
    return {"status": "working"} 

@app.get("/volatility") 
def get_volatility(limit: int = 100): 
    data = df[["close", "rolling_vol_15", "vol_spike"]].reset_index().tail(limit)
    return data.to_dict(orient="records")

@app.get("/daily-summary")
def daily_summary(limit: int = 50):
    data = daily_df.reset_index().tail(limit)
    return data.to_dict(orient="records")

@app.get("/high-vol-days")
def high_vol_days(limit: int = 20):
    data = daily_df[daily_df["regime"] == "High Vol"].reset_index().tail(limit)
    return data.to_dict(orient = "records")