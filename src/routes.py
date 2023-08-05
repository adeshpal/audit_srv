""" 
All the routes of consumer service 
"""
import falcon

from src.Middleware.AuthMiddleware import AuthMiddleware
from src.Middleware.ResponseMiddleware import ResponseMiddleware
from src.Handler.EventHandler import EventHandler
from src.Handler.UserHandler import UserHandler
from src.Handler.AuthenticationHandler import AuthHandler

def get_app():
    """All consumer view endpoints would be defined here"""
    app = falcon.App(middleware=[AuthMiddleware(), ResponseMiddleware()])
    
    #JWT api
    app.add_route('/authentication/{version}/jwt/{user_id:int}/{service_name}', AuthHandler())
    
    #add message api POST and GET ALL
    app.add_route("/auditsrv/{version}/message", EventHandler())
    
    #GET message by id message api ALL
    app.add_route("/auditsrv/{version}/message/{user_id:int}", EventHandler(), suffix="user")

    app.add_route("/auditsrv/{version}/user", UserHandler(), suffix="create")
    app.add_route("/auditsrv/{version}/user/admin", UserHandler(), suffix="admin")
    
    return app
