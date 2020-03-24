# XL Release Jenkins Console Text Search 

## Overview

This plugin allows XL Release to retrieve the /consoleText output from a Jenkins job and search for a specified text pattern

## Usage

The Jenkins server is selected from one of the shared configuration items. 

The project and build number must be specified. The build number can be provided using a release variable which is populated from a previous Jenkins build task. 

Specify your "Left Search" text, your "Right Search" text or both. The plugin will examine each line of the console output and attempt to find these strings. If successful, the plugin will return the data that is in between these strings, not including the provided search text. The search result will be saved in the provided output variable.

For example: 

Successfully assigned IP address to container: 127.0.0.1
Left search: "Successfully assigned IP address to container: "
Right search is empty
Result: 127.0.0.1

Security scanning succeeded with result PASS with scan ID 456100
Left search: "Security scanning succeeded with result "
Right search: " with scan ID"
Result: PASS

* If multiple lines match, the last result will be returned. 
* If only a left or right search parameter is specified, it will return everything to the right or left of the search, respectively.
* Tip: include any whitespace or quote marks you want stripped out. 

