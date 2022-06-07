Feature: Methods with different accessibility

	Background:
		Given user is logged in as producent
		And administrator created a method

	Scenario: Viewing published method as producent
		Given created method is set to 'Published'
		When producent is on "Methods" page
		Then producent can see the method being colored in green

	Scenario: Viewing private method as producent
		Given created method is set to 'Private'
		When producent is on "Methods" page
		Then producent can see the method being colored in red

	Scenario: Viewing submitted method as producent
		Given created method is set to 'Submit for publication'
		When producent is on "Methods" page
		Then producent can see the method being colored in yellow