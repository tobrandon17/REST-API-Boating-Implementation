# REST-API-Boating-Implementation

URL: https://elevated-cargo-166306.appspot.com/

## 1)	/boat
	a.	GET
		i.	Gets all of the boats
	b.	POST
		i.	Creating a new boat

## 2)	/slips
	a.	GET
		i.	Gets all of the slips
	b.	POST
		i.	Creating a new slip

## 3)	/boats/{boatId}
	a.	GET
		i.	Get a specific boat based on id
	b.	PATCH
		i.	Modify the information of a boat
	c.	DELETE
		i.	Deleting a boat
	d.	PUT
		i.	Replacing a boat

## 4)	/slips/{slipId}
	a.	GET
		i.	Get a specific slip based on id
	b.	PATCH
		i.	Modify the information of a slip
	c.	DELETE
		i.	Deleting a slip
	d.	PUT
		i.	Replacing a slip’s data

## 5)	 /slips/{slipId}/boats/{boatId}
	a.	PUT
		i.	Docking a specific boat into a slip
	b.	GET
		i.	Get the specific boat that is located at the designated slip
	c.	PATCH
		i.	Updates the boats information when it departs from the slip

