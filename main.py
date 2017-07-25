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
# import logging
HOMEPAGE = """
<html>
<body background ="https://media.giphy.com/media/pruntGJyPxE52/giphy.gif">
  <head>
    <title>My First Webpage</title>
    <link rel="stylesheet" href="/resources/hello.css"/>
  <head>
  <body>
    <center>
    <h1>Hello, My Name is Anita Chu!</h1>
    <h2>About me</h2>
    <p> I am from Brooklyn, New York. I am going to <a href="http://www.baruch.cuny.edu/">Baruch College</a>.I have a pet rabbit named Fufu.</p></center>
    <a href="html_2.html">
    <img src="http://www.animatedimages.org/data/media/327/animated-rabbit-image-0422.gif">
    </a>
    <center>
    <h3>HOBBIES
      <div class="pictures">

      <div class="pictures"><li>Drawing</li>
      <img src="http://intuitivecreativity.typepad.com/.a/6a00d83451dc5b69e201bb087309e5970d-pi" id="Drawing"></div>
      <div class="pictures"><li>Reading Manga</li>
      <img src="https://lh4.googleusercontent.com/-9EUfAtchCjI/UAaqA9mq5yI/AAAAAAAAFY8/1p4C1Zxxjkw/s720/manga0052.jpg" id="Reading Manga"></div>
      <div class="pictures"><li>Gaming</li>
      <img src="https://crushthestreet.com/wp-content/uploads/2017/06/gamingincolor1.jpg" id="Gaming"></div>
     </center>
   </div>
    </h3>
    <center>
    <h4>Food That I Like
      <div class="pictures">

      <div class="pictures"><li>Sushi</li>
      <img src="https://media.tenor.com/images/3be04af037ef139044f7ff8dac40f92b/tenor.gif" id="Sushi"></div>
      <div class="pictures"><li>Chicken</li>
      <img src="https://images-gmi-pmc.edge-generalmills.com/549e441a-eed1-4e39-8ad3-6ae60ab3ad7f.jpg" id="Chicken"></div>
      <div class="pictures"><li>Spaghetti</li>
      <img src="https://cdn.instructables.com/FY0/BMNB/IB226AMH/FY0BMNBIB226AMH.MEDIUM.jpg" id="Spaghetti"></div>
     </center>
   </div>
    </h4>


  </body>
</html>
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
        # logging.error('Printing hello message')
        self.response.write(HOMEPAGE)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
