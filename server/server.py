import web
import os

urls = (
'/images/(.*)', 'images' #this is where the image folder is located....
)


class images:
    def GET(self,name):
        ext = name.split(".")[-1] # Gather extension

        cType = {
            "png":"images/png",
            "jpg":"images/jpeg",
            "gif":"images/gif",
            "ico":"images/x-icon"            }

        if name in os.listdir('static/images'):  # Security
            web.header("Content-Type", cType[ext]) # Set the Header
            return open('images/%s'%name,"rb").read() # Notice 'rb' for reading images
        else:
            raise web.notfound()