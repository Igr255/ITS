Feature: Method relations
	
	Background: 
		Given producent created a method
		And two different tools
		And two different test cases
	
	Scenario: Adding a tool relation to a method
		Given method contains 0 relations with tools
		When producent edits method
		And adds a tool relation
		Then on the method page there is 1 tool relation visible

	Scenario: Removing a tool relation from a method
		Given method contains 1 relation with a tool
		When producent edits method
		And removes a tool relation
		Then on the method page there is 0 tool relations visible

	Scenario: Adding multiple tool relations to a method
		Given method contains 1 relation with tools
		When producent edits method
		And adds a second relation to a tool
		Then on the method page there are 2 tool relations visible

	Scenario: Adding a test case relation to a method
		Given method contains 0 relations with test cases
		When producent edits method
		And adds a test case realtion
		Then on the method page there is 1 test case relation visible

	Scenario: Removing a test case relation from a method
		Given method contains 1 relations with test cases
		When producent edits method
		And removes a test case relation
		Then on the method page there is 0 test case relations visible

	Scenario: Adding multiple test case realtions to a method
		Given method contains 1 relation with test cases
		When producent edits method
		And adds a second relation to a test case
		Then on the method page there is 2 test case relation visible

	Scenario: Adding test case and tool relations
		Given method contains 0 relations with test cases
		And contains 0 relations with tools
		When producent edits method
		And adds a tool realtion
		And adds a test case relation
		Then on the method page there is 1 tool
		And 1 test case relations
