Feature: Basic CRUD operations on methods
	
	Background: 
		Given producent account is logged in

	Scenario: Creating method without filling required fields
		Given website is on "Add method" page
		And required fields are not filled
		When producent saves the method
		Then error is thrown
		And method is not created
		And method is not visible on methods page

	Scenario: Creating method with filled required fields
		Given website is on "Add method" page
		And required fields are filled
		When producent saves the method
		Then method is created
		And method is visible on methods page

	Scenario: Popup on method delete
		Given website is on existing method page
		When producent clicks on "Actions" button
		And producent clicks on "Delete" button
		Then "Do you really want to delete this folder and all its contents?" popup should appear

	Scenario: Popup on method delete
		Given producent tries to remove a method
		And "Do you really want to delete this folder and all its contents?" popup appeared
		When producent clicks on popup "Delete" button
		Then method disappears from methods page

	Scenario: Editing method data
		Given website is on existing method page
		When producent edits the method
		And producent edits methods data
		And saves the edited method
		Then "Changes saved" information appears
		And method gets updated
		And updated method is visible on methods page
