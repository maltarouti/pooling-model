import asyncio
import random

import uvicorn
from fastapi import FastAPI
from fastapi import BackgroundTasks

app = FastAPI()
jobs = {}


@app.get("/create_new_job")
async def create_job(background_tasks: BackgroundTasks) -> dict:
    job_id = random.randint(1000000, 9000000)
    job = {
        "job_id": job_id,
        "job_status": 0,
        "status": "pending"
    }
    jobs[job_id] = job
    background_tasks.add_task(update_job_status, job_id)
    return job


@app.get("/check_status")
async def check_status(job_id: int) -> dict:
    job = jobs.get(job_id)
    if job is not None:
        return job
    else:
        return {
            "status": "failed",
            "payload": f"No job found with id: {job_id}"
        }


async def update_job_status(job_id: int):
    while jobs[job_id]["job_status"] != 100:
        jobs[job_id]["job_status"] += 5
        await asyncio.sleep(1)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
