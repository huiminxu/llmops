

from flask import Flask,Blueprint
from internal.handler import AppHandler, app_handler
from injector import inject
from dataclasses import dataclass
@inject
@dataclass
class Router:
	"""路由"""
	app_handler: AppHandler
	def register_router(self,app:Flask):
		bp = Blueprint("llmops",__name__,url_prefix="")
		bp.add_url_rule("/ping",methods=["GET"],view_func=self.app_handler.ping)

		# 注册蓝图
		app.register_blueprint(bp)


