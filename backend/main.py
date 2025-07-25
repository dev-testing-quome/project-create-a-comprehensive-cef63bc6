import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

from database import engine, Base
from routers import users, courses, auth # Replace with your actual router imports

app = FastAPI(title=\