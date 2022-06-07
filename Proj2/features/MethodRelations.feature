Feature: Method relations
	
	Background: 
		Given producent is logged in

	Scenario: Adding a test case relation to a method
		Given two different test cases are created
		And method is created
		And method contains 0 relations with test cases
		When producent edits method
		And adds a test case relation
		Then on the method page there is 1 test case relation visible

	Scenario: Removing a test case relation from a method
		Given method contains 1 relations with test cases
		When producent edits method
		And producent removes a test case relation
		Then on the method page there is 0 test case relations visible

	Scenario: Adding multiple test case relations to a method
		Given method contains 0 relation with test cases
		When producent edits method
		And adds two relations to a test case
		Then on the method page there are 2 test cases relation visible