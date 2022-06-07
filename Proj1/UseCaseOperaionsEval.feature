Feature: Basic CRUD operations over use cases
	
	Background: 
		Given producent account is logged in
		And a use case used for evaluation is created

	Scenario: Creating use case without filling required fields
		Given website is on "Add Use Case" page
		And required fileds are not filled
		When saves the created method
		Then error is thrown
		And use case is not created
		And use case is not visible on use cases page

	Scenario: Creating use case where all required fields are filled
		Given website is on "Add Use Case" page
		And all required fields are filled
		When saves the created use case
		Then use case is created and is visible on the use cases page

	Scenario: Editing use case domain
		Given webside is on existing use case page
		When producent edits the use case
		And changes use case domain to "Railway"
		And saves the changes
		Then on the use case page there is a "Railway" domain shown

	Scenario: Deleting use case
		Given webside is on existing use case page
		When producent clicks on "Actions" button
		And clicks on "Delete" button
		Then "Do you really want to delete this folder and all its contents?" poopup appears

	Scenario: Popup on use case delete
		Given producent tried to remove a use case
		And "Do you really want to delete this folder and all its contents?" popup appeared
		When producent clicks on "Delete" button
		Then use case disappears from use cases page

	Scenario: Adding an evaluation scenario to a use case
			Given webside is on existing use case page
			And use case has 0 evaluation scenarios
			When edits the use case
			And adds a pre-made use case as an evaluation scenario 
			And and saves the use case
			Then "Changes saved" information appears
			And on the use case page there is 1 evaluation scenario visible