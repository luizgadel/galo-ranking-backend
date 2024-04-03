from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.config_db import origins
from src.route.routes import routes

"""
    @brief      Galo - Sistema de pontuação para Dominó
    
    @details    Main file. Instance the FastAPI and include main endpoints of application
    
    @author     Luiz Gadelha <>
    @since      Apr 1, 2024
"""

description = """
`@brief`      Galo - Sistema de pontuação para Dominó
`@author`     **Luiz Gadelha** \<> \n
`@since`      Mar 23, 2024

## Introduction
This application's main objective is to manage data from the Galo App. \n
Below we have all methods of user interaction with our system.
"""

tags_metadata = [
    {"name": "Player", "description": "Players operations"},
    {"name": "Match", "description": "Matches operations"}
]

app = FastAPI(
    title="Galo API",
    description=description,
    version="1.0.0",
    openapi_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

for route in routes:
    app.include_router(route.router)