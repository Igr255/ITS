Feature: Methods with different accessibility

	Background:
		Given producent created a method

	Scenario: Viewing published method as consument
		Given method created by producent is set to 'Published'
		And user is logged in as consument
		When consument is on "Methods" page
		Then consument can see the method being colored in green

	Scenario: Viewing private method as consument
		Given method created by producent is set to 'Private'
		And user is logged in as consument
		When consument is on "Methods" page
		Then consument cannot see the method

	Scenario: Viewing submitted method as consument
		Given method created by producent is set to 'Submit for publication'
		And user is logged in as consument
		When consument is on "Methods" page
		Then consument cannot see the method
