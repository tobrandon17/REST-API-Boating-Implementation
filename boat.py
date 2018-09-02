# Brandon To
# REST Planning and Implementation

from google.appengine.ext import ndb

import webapp2
import json

class Boat(ndb.Model):
	id = ndb.StringProperty()
	name = ndb.StringProperty(required=True)
	type = ndb.StringProperty()
	length = ndb.IntegerProperty()
	at_sea = ndb.BooleanProperty()

	
class Slip(ndb.Model):
	id = ndb.StringProperty()
	number = ndb.IntegerProperty(required=True)
	current_boat = ndb.StringProperty()
	arrival_date = ndb.StringProperty()

"""
# I put the demo as reference	
class FishHandler(webapp2.RequestHandler):
	def post(self):
		parent_key = ndb.Key(Fish, "parent_fish")
		fish_data = json.loads(self.request.body)
		new_fish = Fish(name=fish_data['name'], parent=parent_key)
		new_fish.put()
		fish_dict = new_fish.to_dict()
		fish_dict['self'] = '/fish/' + new_fish.key.urlsafe()
		self.response.write(json.dumps(fish_dict))
	
	def get(self, id=None):
		if id:
			f = ndb.Key(urlsafe=id).get()
			f.ph_max = 100
			f.put()
			f_d = f.to_dict()
			f_d['self'] = "/fish/" + id
			self.response.write(json.dumps(f_d))
"""			
	
class BoatHandler(webapp2.RequestHandler):
# Keeping track of the order
#	def get(self, id=None):
#	def post(self):
#	def delete(self, id=None):
#	def patch(self, id=None):
#	def put(self, id=None):

# Gets all of the boats 
	def get(self, id=None):
		query = Boat.query()
		allEntities = query.fetch()
		query_json = ndb_json.dumps(allEntities)
		query_dict = ndb_json.loads(query_json)
		
		for i in range(0, Boat.query().count()):
			query_dict[i]['id'] = allEntities[i].key.urlsafe()
			
		output = json.dumps(query_dict)
		self.response.write(output)
		self.response.headers['Content-Type'] = 'application/json'

# Creating a new boat
	def post(self):
		boat_data = json.loads(self.request.body)
		if 'name' in boat_data:
			if boat_data['name']:
				new_boat = Boat(name=boat_data['name'], at_sea=True)
				if 'type' in boat_data:
					new_boat.type = boat_data['type']
				else:
					new_boat.type = None
				if 'length' in boat_data:
					new_boat.length = boat_data['length']
				else:
					new_boat.length = None
				new_boat.put()
				new_boat.id = new_boat.key.urlsafe()
				new_boat.put()
				boat_dict = new_boat.to_dict()
				boat_dict['self'] = "/boats/" + new_boat.id
				self.response.write(json.dumps(boat_dict))
			else:
				self.response.set_status(400)
				return
		else:
			self.response.set_status(400)
	
# Deleting a boat		
	def delete(self, id=None):
		if id:
			boat = ndb.Key(urlsafe=id).get()
			if boat:
				if not boat.at_sea:
					query = Slip.query(Slip.current_boat == id)
					slip = query.get()
					slip.current_boat = None
					slip.arrival_date = None
					slip.put()
				boat.key.delete()
			else:
				self.response.set_status(404)
				return
		else:
			self.response.set_status(404)

# Replacing a boat			
	def patch(self, id=None):
		if id:
			boat = ndb.Key(urlsafe=id).get()
			if boat:
				boat_data = json.loads(self.request.body)
				if 'name' in boat_data:
					if boat_data['name']:
						boat.name = boat_data['name']
					else:
						self.response.set_status(400)
						return
				if  'type' in boat_data:
					boat.type = boat_data['type']
				if 'length' in boat_data:
					boat.length = boat_data['length']
				boat.put()
			else:
				self.response.set_status(404)
				return
		else:
			self.response.set_status(404)

# Deleting a boat			
	def put(self, id=None):
		if id:
			boat_data = json.loads(self.request.body)
			if 'name' in boat_data:
				if boat_data['name']:
					boat = ndb.Key(urlsafe=id).get()
					if boat:
						if 'name' in boat_data:
							boat.name = boat_data['name']
						else:
							self.response.set_status(400)
							return
						if 'type' in boat_data:
							boat.type = boat_data['type']
						else:
							boat.type = None
						if 'length' in boat_data:
							boat.length = boat_data['length']
						else:
							boat.length = None
						boat.put()
					else:
						self.response.set_status(404)
						return
				else:
					self.response.set_status(400)
					return
			else:
				self.response.set_status(400)
				return
		else:
			self.response.set_status(404)	
	
class SlipHandler(webapp2.RequestHandler):	

# Get a specific slip based on id
	def get(self, id=None):
		query = Slip.query()
		allEntities = query.fetch()
		query_json = ndb_json.dumps(query)
		query_dict = ndb_json.loads(query_json)
		
		for i in range(0, Slip.query().count()):
			query_dict[i]['id'] = allEntities[i].key.urlsafe()
			
		output = json.dumps(query_dict)
		self.response.write(output)
		self.response.headers['Content-Type'] = 'application/json'
"""
# I did not finish due to time constraints
# Creating a new slip
	def post(self):

# Deleting a slip	
	def delete(self, id=None):

# Modifying the information of a slip	
	def patch(self, id=None):

# Replacing a slip's data	
	def put(self, id=None):
"""	

class MainPage(webapp2.RequestHandler):


    def get(self):
			self.response.write("REST Planning and Implementation")


allowed_methods = webapp2.WSGIApplication.allowed_methods
new_allowed_methods = allowed_methods.union(('PATCH',))
webapp2.WSGIApplication.allowed_methods = new_allowed_methods
app = webapp2.WSGIApplication([
    ('/', MainPage),
	('/boats', BoatHandler),
	('/boats/(.*)', BoatHandler),
	('/slips', SlipHandler),
	('/slips/(.*)', SlipHandler),
], debug=True)
