""" 
All the routes of consumer service 
"""
import falcon

from src.Middleware.AuthMiddleware import AuthMiddleware
from src.Middleware.ResponseMiddleware import ResponseMiddleware
from src.Handler.EventHandler import EventHandler


def get_app():
    """All consumer view endpoints would be defined here"""
    app = falcon.App(middleware=[AuthMiddleware(), ResponseMiddleware()])
    #Subscribe api
    # app.add_route('/auditsrv/{version}/subscribe', Books())
   
    #add message api POST and GET ALL
    app.add_route("/auditsrv/{version}/message", EventHandler())
    
    #GET message by id message api ALL
    app.add_route("/auditsrv/{version}/message/{user_id:int}", EventHandler(), suffix="user")
    
    # app.add_route('/auditsrv/{version}/message/{user_id:int}/{event_type:str}', )
    
    return app