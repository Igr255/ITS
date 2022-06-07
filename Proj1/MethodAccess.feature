Feature: Methods with different accessibility
	
	Background: 
		Given producent created a method
	
	Scenario: Viewing published method as producent
		Given created method is set to 'Published'
		And user is logged in as producent
		When user is on "Methods" page
		Then user can see the method being colored in green

	Scenario: Viewing private method as producent
		Given created method is set to 'Private'
		And user is logged in as producent
		When user is on "Methods" page
		Then user can see the method being colored in red

	Scenario: Viewing submitted method as producent
		Given created method is set to 'Submit for publication'
		And user is logged in as producent
		When user is on "Methods" page
		Then user can see the method being colored in yellow

	Scenario: Viewing published method as consument
		Given created method is set to 'Published'
		And user is logged in as consument
		When user is on "Methods" page
		Then user can see the method being colored in green

	Scenario: Viewing private method as consument
		Given created method is set to 'Private'
		And user is logged in as consument
		When user is on "Methods" page
		Then user cannot see the method

	Scenario: Viewing submitted method as consument
		Given created method is set to 'Submit for publication'
		And user is logged in as consument
		When user is on "Methods" page
		Then user cannot see the method

