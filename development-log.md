# Status Updates

### Distribution

(20/07/2020)

It's clear now that I've submitted my assignment that I need to provide a cleaner way for people to get in and use my program. At the 

### Implementation of list selection
(16/07/2020)

Since being able to choose an item from a numbered list forms the vast majority of the interaction between the user and the program, it is important that it is implemented with maximum flexibility. Today after several hours I have finally managed this task. The key features achieved are:

* The strings displayed as options to the user directly point to a data type or function.
* The list selection allows the option for a prompt to be displayed.
* Larger lists will be automatically broken into columns.
* Multiple groups of items can be displayed, with titles for each group, but each item overall is numbered individually.
* The function can accept multiple values as selections.

On a high level I have achieved this by creating a function that takes dict objects as vargs. The function checks for the items and titles keys, of which items is the only mandatory one. Items is in turn another dictionary with the display strings as keys pointing to the object essentially being chosen. I have also created a helper function to help create this object. The display string is then created and presented to the user. Once the input is validated, the function searches through the original keys, and returns the corresponding value(s).

A more detailed logical flow for this function is contained in the README file.


### Using of data properties
(14/07/2020)

A big part of ensuring the data integrity in my app is ensuring that the attributes of the 3 model classes (Players, Sections, and Rosters) cannot be arbitrarily modified, and that they all contain the right data type. For example the 'players' attribute of the section class must only contain Player objects.

To combat this, I've made use of the property decorator. This has proven to be an effective solution because it means that I can get all of the benefits of type safety, without having to refactor any code that was referencing those attributes. It also allows me to prevent collection attributes from being modified outside of the class.

Due to the low level nature of these classes, an incorrect reassignment of a variable will raise an exception, rather than simple causing the operation to fail.