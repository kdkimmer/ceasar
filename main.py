#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from caesar import encrypt
import cgi

# html boilerplate for the top of every page
page_header = """
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
        </style>
        <title>Caesar</title> 
    </head>
<body>
    <h1>
        <a href="/">Caesar</a>
    </h1>
    """

input_form = """
    	<form action= /rotate method="post">
    			<div>
        		<label for="rot">Rotate by how many (must be an int):</label>
                <input type="number" name="rot"value="{0}">
                <p class="error"></p>
                </div>
            	<textarea type="text" name="input_text_area">{1}</textarea>
            	<br>
            	<input type="submit" value="Encrypt it" name="submit-button">
    </form>
    """
    
# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	
    	self.response.write(page_header + input_form.format('0','') + page_footer)


class RotateHandler(webapp2.RequestHandler):

   	def post(self):
    		rotate = self.request.get("rot")
    		rot = int(rotate)
    		user_text = self.request.get("input_text_area")
    		rotate_text = encrypt(user_text, rot)
    		escape_text = cgi.escape(rotate_text)
    		
        	rotate_answer = page_header + input_form.format(rot, escape_text) + page_footer
    		self.response.write(rotate_answer)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/rotate', RotateHandler)
], debug=True)
